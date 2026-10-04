---
title: "Option B: GKE native gateway controller"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/option-b-gke-native-gateway-controller.html"
content_id: "cr8lwlzM4022WD8KVcsgvQ"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:28.186660+00:00"
---

# Option B: GKE native gateway controller

The GKE native Gateway controller is built into GKE and backed by Google Cloud
Application Load Balancers. No separate controller installation is required.

## GatewayClass Options

| GatewayClass | Load Balancer type | Use case |
| --- | --- | --- |
| `gke-l7-global-external-managed` | Global External Application LB | Internet-facing, global anycast |
| `gke-l7-regional-external-managed` | Regional External Application LB | Internet-facing, single region |
| `gke-l7-rilb` | Regional Internal Application LB | Internal traffic within VPC |
| `gke-l7-gxlb` | Classic Global External HTTP(S) LB | Legacy — prefer `gke-l7-global-external-managed` for new deployments |

## Prerequisites

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

## Installation

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

   > The chart automatically creates `HealthCheckPolicy`
   > resources for both the CIM service and commit-server when a GKE
   > GatewayClass is detected. GKE Application LB requires HTTP 2xx responses
   > for health checks; both services return 302 on their root paths, so
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
