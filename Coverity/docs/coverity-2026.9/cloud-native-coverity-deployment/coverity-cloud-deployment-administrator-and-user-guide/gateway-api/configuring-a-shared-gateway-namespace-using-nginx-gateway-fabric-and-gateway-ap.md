---
title: "Configuring a shared gateway namespace using NGINX Gateway Fabric and Gateway API"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/configuring-a-shared-gateway-namespace-using-nginx-gateway-fabric-and-gateway-api.html"
content_id: "HjLk23erJjk_sAvTIEFslw"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:27.532443+00:00"
---

# Configuring a shared gateway namespace using NGINX Gateway Fabric and Gateway API

Configure NGINX Gateway Fabric with the Gateway API to use shared namespaces across deployments.

- You have `kubectl` access to your Kubernetes cluster.
- You have Helm installed and configured.
- You have a valid TLS certificate and key for your domain.
- You know the hostname URL for your deployment.

1. Install Gateway API CRDs.

   Install both the standard and experimental Gateway API Custom Resource Definitions (CRDs):

   ```
   kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.1.0/standard-install.yaml
   kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.1.0/experimental-install.yaml
   ```

   The experimental CRDs are required for `SnippetsFilter` and
   `SnippetsPolicy` resources used by NGINX Gateway Fabric. Both sets are
   needed even if you do not use snippets immediately.
2. Install NGINX Gateway Fabric.

   The Helm chart creates the NGINX data-plane deployment and its LoadBalancer Service in
   one operation. The core flags are identical across clouds — only the Service annotations
   differ.

   **Do not create a separate LoadBalancer Service after this step.** The Helm chart
   provisions the Service directly via `nginx.service.*` flags. A second
   Service targeting the same pods would provision a second load balancer.

   **AWS**

   ```
   helm upgrade ngf \
     oci://ghcr.io/nginx/charts/nginx-gateway-fabric \
     -n nginx-gateway \
     --version 2.6.7 \
     --set nginxGateway.snippets.enable=true \
     --set nginx.service.type=LoadBalancer \
     --set nginx.service.externalTrafficPolicy=Cluster \
     --set nginx.service.annotations."service\.beta\.kubernetes\.io/aws-load-balancer-type"=external \
     --set nginx.service.annotations."service\.beta\.kubernetes\.io/aws-load-balancer-nlb-target-type"=ip \
     --set nginx.service.annotations."service\.beta\.kubernetes\.io/aws-load-balancer-scheme"=internet-facing
   ```

   `internet-facing` provisions a public NLB accessible from the internet.
   Change to `internal` to restrict access to your VPC only.

   **GCP / GKE**

   ```
   helm upgrade ngf \
     oci://ghcr.io/nginx/charts/nginx-gateway-fabric \
     -n nginx-gateway \
     --version 2.6.7 \
     --set nginxGateway.snippets.enable=true \
     --set nginx.service.type=LoadBalancer \
     --set nginx.service.externalTrafficPolicy=Cluster
   ```

   GKE provisions a public-IP external Network Load Balancer by default — no annotation
   required. To restrict to internal (VPC-only) access, add `--set
   nginx.service.annotations."networking\.gke\.io/load-balancer-type"=Internal`.

   **Azure**

   ```
   helm upgrade ngf \
     oci://ghcr.io/nginx/charts/nginx-gateway-fabric \
     -n nginx-gateway \
     --version 2.6.7 \
     --set nginxGateway.snippets.enable=true \
     --set nginx.service.type=LoadBalancer \
     --set nginx.service.externalTrafficPolicy=Cluster
   ```

   AKS provisions a public-IP external Standard Load Balancer by default — no annotation
   required. To restrict to internal (VNet-only) access, add `--set
   nginx.service.annotations."service\.beta\.kubernetes\.io/azure-load-balancer-internal"=true`.
3. Create the TLS secret.

   Create the TLS secret in the `nginx-gateway` namespace — the same
   namespace as the Gateway.

   ```
   kubectl create secret tls cov-test-tls-secret \
     --cert=<path-to-certificate> \
     --key=<path-to-key> \
     -n nginx-gateway
   ```

   Placing the secret in the Gateway's namespace avoids a cross-namespace TLS reference.
   If the secret must live in a different namespace, a `ReferenceGrant` in
   the secret's namespace is required to permit the Gateway to read it.
4. Create the Gateway resource.

   Create a file named `shared-gateway.yaml` with the following specification:

   ```
   apiVersion: gateway.networking.k8s.io/v1
   kind: Gateway
   metadata:
     name: nginx-gateway-fabric
     namespace: nginx-gateway
   spec:
     gatewayClassName: nginx
     listeners:
     - name: http
       port: 80
       protocol: HTTP
       hostname: "<your-host-url>"
       allowedRoutes:
         namespaces:
           from: All
     - name: https
       port: 443
       protocol: HTTPS
       hostname: "<your-host-url>"
       allowedRoutes:
         namespaces:
           from: All
       tls:
         mode: Terminate
         certificateRefs:
         - name: cov-test-tls-secret
   ```

   ```
   kubectl apply -f shared-gateway.yaml
   ```

   `allowedRoutes.namespaces.from: All` allows HTTPRoutes in any namespace
   to attach without a `ReferenceGrant`. The listener names
   `http` and `https` are referenced by the Helm chart — if
   you use different names here, set `cim.gateway.sectionName` accordingly
   in Step 5.
5. Update the Helm values.

   Update your deployment's `values.yaml`. The
   `gatewayClassName` is always `nginx` for NGINX Gateway
   Fabric regardless of cloud provider — the cloud differences were handled in Step 2
   through Service annotations.

   ```
   cim:
     gateway:
       create: false          # Gateway is externally managed — do not recreate it
       enabled: true          # Render HTTPRoute resources in the application namespace
       gatewayClassName: "nginx"
       name: "nginx-gateway-fabric"
       namespace: "nginx-gateway"

       hostnames:
         - "<your-hostname>"

       path: "/<your-path>"
       pathType: "PathPrefix"
       ccdPath: "/ccd"

       sectionName: ""        # Auto-derives to "https" when listeners.https.enabled=true
       backendWeight: null

       filters: []
       allowedSourceRanges: []
       gatewayAllowedSourceRanges: []

       clientSettings:
         body:
           maxSize: ""

       annotations: {}

       listeners:
         http:
           enabled: true
           port: 80
           redirect: true     # Renders an HTTP→HTTPS 301 redirect HTTPRoute

         https:
           enabled: true
           port: 443
   ```

   **Field reference**

   | Field | Notes |
   | --- | --- |
   | `create: false` | The chart will not render a `kind: Gateway` resource. The Gateway was created in Step 4 and is not owned by this Helm release. |
   | `enabled: true` | Enables HTTPRoute resource creation for CIM and commit-server. Independent of `create` — HTTPRoutes attach to the externally-managed Gateway. |
   | `sectionName:` | When empty and `listeners.https.enabled: true`, the chart auto-derives `sectionName: https`, matching the listener name in Step 4. Override only if your Gateway uses a different listener name. |
   | `redirect: true` | Renders a second HTTPRoute on the `http` listener that issues HTTP 301 → HTTPS redirects. Remove if redirects are handled at the load balancer. |
   | `healthCheck` | Not shown — these fields only apply when using a native cloud Gateway class (`gke-*`, `amazon-alb`, `azure-alb*`). They have no effect for NGINX Gateway Fabric. |
