---
title: "Google Kubernetes Engine (GKE)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/google-kubernetes-engine-gke-.html"
content_id: "a5mqP01n96jHFAFM94OiVw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:40.938932+00:00"
---

# Google Kubernetes Engine (GKE)

Two options are available on GKE: NGINX Gateway Fabric (NGF) and the GKE-native Gateway
controller. Both implement the standard Kubernetes Gateway API and are compatible with
the CNC chart. Choose based on your operational requirements.

| Dimension | Option A: NGINX Gateway Fabric | Option B: GKE Native Controller |
| --- | --- | --- |
| Gateway implementation | NGF controller pod in cluster | Fully managed by Google |
| Load balancer type | GCP TCP/UDP Network Load Balancer | Google Cloud Application Load Balancer |
| L7 features | NGF-native (SnippetsFilter, ClientSettingsPolicy) | GKE-native (Cloud Armor, HealthCheckPolicy) |
| IP allowlisting | `SnippetsPolicy` / `SnippetsFilter` | Google Cloud Armor |
| External IP location | `kubectl get svc` (NGF proxy Service) | `kubectl get gateway` (directly on Gateway) |
| GatewayClass | `nginx` | `gke-l7-global-external-managed` (and others) |

## Option A: NGINX gateway fabric on GKE

**Prerequisites**

- GKE cluster running **Kubernetes 1.31+** (required by NGF 2.5.x / 2.6.0 — see
  the [version compatibility table](https://blackducksoftware-my.sharepoint.com/shared?listurl=https%3A%2F%2Fblackducksoftware%2Dmy%2Esharepoint%2Ecom%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments&id=%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments%2FMicrosoft%20Teams%20Chat%20Files%2Fingress%2Dto%2Dgateway%2Dapi%2Dmigration%2Dguide%207%2Emd&parent=%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments%2FMicrosoft%20Teams%20Chat%20Files&shareLink=1%2C1&ga=1#kubernetes-version-compatibility))
- `kubectl` access with cluster-admin privileges
- Helm 3.x installed

1. Install gateway API
   credentials

   ```
   kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.5.0/standard-install.yaml
   kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.5.0/experimental-install.yaml
   ```

   Verify:

   ```
   kubectl get crd | grep gateway.networking.k8s.io
   ```
2. Install NGINX gateway
   fabric

   ```
   helm install ngf oci://ghcr.io/nginx/charts/nginx-gateway-fabric \
     --create-namespace \
     -n nginx-gateway \
     --set nginxGateway.snippets.enable=true \
     --set nginx.service.externalTrafficPolicy=Local
   ```

   > `snippets.enable=true` is required for IP allowlisting
   > features (`allowedSourceRanges` /
   > `gatewayAllowedSourceRanges`). It is not required for
   > basic routing.

   Verify:

   ```
   kubectl get pods -n nginx-gateway
   kubectl get gatewayclass nginx
   ```
3. Create a TLS
   secret

   ```
   kubectl create secret tls coverity-tls \
     --cert=path/to/tls.crt \
     --key=path/to/tls.key \
     -n <release-namespace>
   ```
4. Configure the CNC Helm chart

   ```
   global:
     ingress:
       enabled: false

   cim:
     ingress:
       enabled: false

     gateway:
       create: true
       enabled: true
       gatewayClassName: "nginx"
       hostnames:
         - "coverity.example.com"
       listeners:
         http:
           enabled: true
           port: 80
           redirect: true
         https:
           enabled: true
           port: 443
           tlsSecretName: "coverity-tls"

       # Optional: IP allowlisting (requires snippets.enable=true)
       # gatewayAllowedSourceRanges:
       #   - "10.0.0.0/8"
       #   - "203.0.113.0/24"

       # Optional: increase body size for large scan uploads
       # clientSettings:
       #   body:
       #     maxSize: "500m"
   ```

   Deploy:

   ```
   helm upgrade --install <release-name> charts/cnc/ -f values.yaml -n <release-namespace>
   ```
5. Retrieve the external IP

   NGF creates a LoadBalancer Service in the
   `nginx-gateway` namespace. GKE provisions a Network Load
   Balancer for
   it:

   ```
   kubectl get svc -n nginx-gateway
   # Look for the EXTERNAL-IP column on the ngf Service
   ```
6. Update DNS

   Update your DNS record for `coverity.example.com` to
   point to the external IP retrieved above.
7. Verify

   ```
   # Check Gateway is Programmed
   kubectl get gateway <release-name>-cim-gateway -n <release-namespace>

   # Check HTTPRoutes are Accepted
   kubectl get httproute -n <release-namespace>

   # Test HTTPS (expect 200)
   curl -sk -o /dev/null -w "%{http_code}\n" https://coverity.example.com/login/login.htm

   # Test HTTP redirect (expect 301)
   curl -sk -o /dev/null -w "%{http_code} → %{redirect_url}\n" http://coverity.example.com/
   ```

## IP Allowlisting on GKE with NGF

Use `gatewayAllowedSourceRanges` for a gateway-level policy or
`allowedSourceRanges` for per-route control. Both require NGF
with snippets enabled. See [IP Allowlisting](https://blackducksoftware-my.sharepoint.com/shared?listurl=https%3A%2F%2Fblackducksoftware%2Dmy%2Esharepoint%2Ecom%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments&id=%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments%2FMicrosoft%20Teams%20Chat%20Files%2Fingress%2Dto%2Dgateway%2Dapi%2Dmigration%2Dguide%207%2Emd&parent=%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments%2FMicrosoft%20Teams%20Chat%20Files&shareLink=1%2C1&ga=1#ip-allowlisting) for full details.

As an alternative, you may also use **Google Cloud Armor** for IP restriction at
the load balancer level (upstream of NGF). See the GKE Native Gateway section below
for Cloud Armor configuration.

## Option B: GKE native gateway controller

The GKE native Gateway controller is built into GKE and backed by Google Cloud
Application Load Balancers. No separate controller installation is required.

**GatewayClass Options**

| GatewayClass | Load Balancer type | Use case |
| --- | --- | --- |
| `gke-l7-global-external-managed` | Global External Application LB | Internet-facing, global anycast |
| `gke-l7-regional-external-managed` | Regional External Application LB | Internet-facing, single region |
| `gke-l7-rilb` | Regional Internal Application LB | Internal traffic within VPC |
| `gke-l7-gxlb` | Classic Global External HTTP(S) LB | Legacy — prefer `gke-l7-global-external-managed` for new deployments |

**Prerequisites**

- GKE version 1.24 or later (1.27+ required for header rewrites and URL
  rewrites). See the [version compatibility table](https://blackducksoftware-my.sharepoint.com/shared?listurl=https%3A%2F%2Fblackducksoftware%2Dmy%2Esharepoint%2Ecom%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments&id=%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments%2FMicrosoft%20Teams%20Chat%20Files%2Fingress%2Dto%2Dgateway%2Dapi%2Dmigration%2Dguide%207%2Emd&parent=%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments%2FMicrosoft%20Teams%20Chat%20Files&shareLink=1%2C1&ga=1#kubernetes-version-compatibility).
- Gateway API enabled on the cluster:

  ```
  # Enable during cluster creation
  gcloud container clusters create <cluster-name> \
    --gateway-api=standard \
    --region=<region>

  # Or enable on an existing cluster
  gcloud container clusters update <cluster-name> \
    --gateway-api=standard \
    --region=<region>
  ```
- Verify the GatewayClasses are available:

  ```
  kubectl get gatewayclass
  # Expected output includes gke-l7-global-external-managed, gke-l7-rilb, etc.
  ```

1. Create a TLS
   secret

   ```
   kubectl create secret tls coverity-tls \
     --cert=path/to/tls.crt \
     --key=path/to/tls.key \
     -n <release-namespace>
   ```
2. Configure the CNC Helm chart

   ```
   global:
     ingress:
       enabled: false

   cim:
     ingress:
       enabled: false

     gateway:
       create: true
       enabled: true
       gatewayClassName: "gke-l7-global-external-managed"
       hostnames:
         - "coverity.example.com"
       listeners:
         http:
           enabled: true
           port: 80
           redirect: true
         https:
           enabled: true
           port: 443
           tlsSecretName: "coverity-tls"
       # Health check path defaults to /login/login.htm — override only if using a custom context path
       # healthCheck:
       #   requestPath: "/custom-path/login/login.htm"
       #   commitServerRequestPath: "/custom-path/login/login.htm"
   ```

   > The chart automatically creates `HealthCheckPolicy` resources
   > for both the CIM service and commit-server when a GKE GatewayClass is
   > detected. GKE Application LB requires HTTP 2xx responses for health checks;
   > both services return 302 on their root paths, so
   > `/login/login.htm` (which returns 200) is used.

   Deploy:

   ```
   helm upgrade --install <release-name> charts/cnc/ -f values.yaml -n <release-namespace>
   ```
3. Retrieve the external IP

   GKE publishes the external IP directly on the Gateway
   resource — there is no proxy
   Service:

   ```
   kubectl get gateway <release-name>-cim-gateway -n <release-namespace>
   # ADDRESS column shows the GKE load balancer IP
   ```
4. Update DNS

   Update your DNS record for `coverity.example.com` to
   point to the IP retrieved above.
5. Verify

   ```
   # Check Gateway status (look for Programmed: True)
   kubectl get gateway <release-name>-cim-gateway -n <release-namespace> -o wide

   # Check HTTPRoutes (look for Accepted: True, ResolvedRefs: True)
   kubectl get httproute -n <release-namespace>

   # Check HealthCheckPolicies are attached
   kubectl get healthcheckpolicy -n <release-namespace>

   # Test HTTPS (expect 200)
   curl -sk -o /dev/null -w "%{http_code}\n" https://coverity.example.com/login/login.htm

   # Test HTTP redirect (expect 301)
   curl -sk -o /dev/null -w "%{http_code} → %{redirect_url}\n" http://coverity.example.com/
   ```

## IP Allowlisting on GKE Native Gateway

The NGF-specific resources (`SnippetsFilter`,
`SnippetsPolicy`) are not supported by the GKE native Gateway
controller. Use **Google Cloud Armor** for IP allowlisting:

1. Create a Cloud Armor security policy in the GCP console or via
   `gcloud`:

   ```
   gcloud compute security-policies create coverity-ip-allowlist \
     --description="CNC IP allowlist"

   gcloud compute security-policies rules create 1000 \
     --security-policy coverity-ip-allowlist \
     --src-ip-ranges="10.0.0.0/8,203.0.113.0/24" \
     --action=allow

   gcloud compute security-policies rules create 2147483647 \
     --security-policy coverity-ip-allowlist \
     --src-ip-ranges="*" \
     --action=deny-403
   ```
2. Create a `BackendConfig` in the release namespace:

   ```
   apiVersion: cloud.google.com/v1
   kind: BackendConfig
   metadata:
     name: coverity-backend-config
     namespace: <release-namespace>
   spec:
     securityPolicy:
       name: "coverity-ip-allowlist"
   ```
3. Annotate the CIM service via chart values:

   ```
   cim:
     serviceAnnotations:
       beta.cloud.google.com/backend-config: '{"default": "coverity-backend-config"}'
   ```

## NEG provisioning

GKE Gateway API automatically provisions Network Endpoint Groups (NEGs) for any
Service referenced as a `backendRef` in an HTTPRoute. No
`cloud.google.com/neg` annotation is required on the Service.
(The annotation is only needed for the legacy Ingress path or when you also expose
the Service via a standalone NEG outside the Gateway controller.)
