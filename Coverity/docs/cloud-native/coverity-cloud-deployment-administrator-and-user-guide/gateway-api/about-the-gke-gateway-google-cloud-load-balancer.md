---
title: "About the GKE gateway (Google cloud load balancer)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/about-the-gke-gateway-google-cloud-load-balancer-.html"
content_id: "8050Uv5V4xSKR82x90Ku2g"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:40.192618+00:00"
---

# About the GKE gateway (Google cloud load balancer)

The chart supports GKE's native Gateway implementation (backed by Google Cloud Load
Balancers) as an alternative to NGINX Gateway Fabric. Detection is automatic — set
`gatewayClassName` to any GKE Gateway class (they all start with
`gke-`).

**NEG annotation:** GKE Gateway API automatically provisions NEGs for Services
referenced as backends in HTTPRoutes — no `cloud.google.com/neg`
annotation is needed on the Service.

## GatewayClass options

| GatewayClass | Load Balancer type | Use case |
| --- | --- | --- |
| `gke-l7-global-external-managed` | Global External Application LB | Internet-facing, global anycast |
| `gke-l7-regional-external-managed` | Regional External Application LB | Internet-facing, single region |
| `gke-l7-rilb` | Regional Internal Application LB | Internal traffic within VPC |
| `gke-l7-gxlb` | Classic Global External HTTP(S) LB | Legacy — prefer `global-external-managed` |

## Example values

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
    # healthCheck.requestPath defaults to /login/login.htm — no change needed for standard installs
    # healthCheck:
    #   requestPath: "/login/login.htm"
```

The chart automatically:

- Creates a `HealthCheckPolicy` for CIM
  (`<release>-cim-healthcheck`) and commit-server
  (`<release>-commit-server-healthcheck` when
  `cimweb.replicas > 1`), both using
  `/login/login.htm` — GKE LB requires 2xx; both services
  redirect on their root paths
- Skips `SnippetsFilter`, `SnippetsPolicy`, and
  `ClientSettingsPolicy` (NGF-only CRDs not supported by GKE
  Gateway)

## NEG annotation

GKE Gateway API automatically provisions NEGs for Services referenced as backends in
HTTPRoutes — no `cloud.google.com/neg` annotation is needed on the
Service.

## Prerequisites for GKE Gateway

GKE Gateway is built into GKE — no separate NGF installation needed. Ensure that:

- GKE version ≥ 1.24 with Gateway API enabled on the cluster:

  ```
  # Enable during cluster creation
  gcloud container clusters create ... --gateway-api=standard

  # Or enable on an existing cluster
  gcloud container clusters update CLUSTER --gateway-api=standard --region=REGION
  ```
- Verify the GatewayClasses are available:

  ```
  kubectl get gatewayclass
  # Should show gke-l7-global-external-managed, gke-l7-rilb, etc.
  ```

## Getting the Gateway external IP

GKE Gateway publishes its IP directly in `gateway.status.addresses` —
there is no separate LoadBalancer Service to look up (unlike NGF which creates a
proxy pod + Service in your namespace).

```
# Get the IP
kubectl get gateway <release>-gateway -n <namespace>
# ADDRESS column shows the GKE LB IP

# Just the IP
kubectl get gateway <release>-gateway -n <namespace> \
  -o jsonpath='{.status.addresses[0].value}'
```

## HealthCheckPolicy

GKE Application Load Balancer uses HTTP health checks to determine backend health. By
default it checks `/` on port 8080 — CIM returns **302** on
`/` (redirect to login page), which GKE treats as unhealthy.

The chart automatically creates `HealthCheckPolicy` resources using
`/login/login.htm` (returns 200) for both the CIM service and the
commit-server service (when `cimweb.replicas > 1`).

```
# rendered automatically — no action needed
apiVersion: networking.gke.io/v1
kind: HealthCheckPolicy
metadata:
  name: <release>-cim-healthcheck       # CIM service
  # name: <release>-commit-server-healthcheck  (also created when cimweb.replicas > 1)
spec:
  targetRef:
    kind: Service
    name: <release>-cim   # or <release>-commit-server
  default:
    config:
      type: HTTP
      httpHealthCheck:
        requestPath: /login/login.htm
        port: 8080
```

If you use a custom context path (e.g. `/coverity`), override the
request paths:

```
cim:
  gateway:
    healthCheck:
      requestPath: "/coverity/login/login.htm"
      commitServerRequestPath: "/coverity/login/login.htm"
```

Verify both are attached:

```
kubectl get healthcheckpolicy -n <namespace>
kubectl describe healthcheckpolicy <release>-cim-healthcheck -n <namespace>
kubectl describe healthcheckpolicy <release>-commit-server-healthcheck -n <namespace>
# Look for: Reason: Attached, Status: True
```

## Migrating from NGF to GKE Gateway

If you previously used NGINX Gateway Fabric (`gatewayClassName:
nginx`), NGF creates a dedicated nginx proxy pod and LoadBalancer Service
**inside your namespace** (e.g. `<release>-gateway-nginx`
pod + Service). When you switch GatewayClass to `gke-*`, NGF stops
managing the Gateway but does **not** clean up the proxy pod/Service it
created.

After switching, delete the orphaned NGF resources manually:

```
# Find them
kubectl get pods,svc -n <namespace> | grep "gateway-nginx"

# Delete
kubectl delete pod <release>-gateway-nginx-<hash> -n <namespace>
kubectl delete svc <release>-gateway-nginx -n <namespace>
```

Important: Update DNS to point to the new GKE Gateway
IP, not the old NGF LoadBalancer IP. Run `kubectl get gateway
<release>-gateway -n <namespace>` to get the new IP.

## IP allowlisting on GKE Gateway

`allowedSourceRanges` and `gatewayAllowedSourceRanges`
are silently skipped on GKE Gateway (SnippetsFilter/SnippetsPolicy are NGF-only).
Use **Google Cloud Armor** instead:

1. Create a Cloud Armor security policy with IP allowlist rules in the GCP Console
   or via `gcloud`
2. Create a `BackendConfig` in the same namespace referencing the
   policy:

   ```
   apiVersion: cloud.google.com/v1
   kind: BackendConfig
   metadata:
     name: coverity-backend-config
   spec:
     securityPolicy:
       name: "coverity-ip-allowlist"   # Cloud Armor policy name
   ```
3. Annotate the CIM Service to reference the BackendConfig:

   ```
   # in your values.yaml
   cim:
     serviceAnnotations:
       beta.cloud.google.com/backend-config: '{"default": "coverity-backend-config"}'
   ```

## Limitations vs NGINX Gateway Fabric

| Feature | NGF | GKE Gateway |
| --- | --- | --- |
| IP allowlisting | `allowedSourceRanges` / `gatewayAllowedSourceRanges` | Google Cloud Armor (external) |
| Max body size | `clientSettings.body.maxSize` | BackendConfig / LB settings |
| Raw nginx directives | `filters[]` with SnippetsFilter | Not supported |
| Health check | Auto-configured via `HealthCheckPolicy` (chart-managed) | Auto-configured via `HealthCheckPolicy` (chart-managed) |
| Gateway IP location | ``` kubectl get               svc <release>-gateway-nginx ``` | ``` kubectl get               gateway <release>-gateway ``` |
| Proxy pod in namespace | Yes (NGF creates `<release>-gateway-nginx` pod) | No (GKE LB is fully managed) |
