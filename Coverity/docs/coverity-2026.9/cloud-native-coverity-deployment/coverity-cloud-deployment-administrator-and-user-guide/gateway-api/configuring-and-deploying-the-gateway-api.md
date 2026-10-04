---
title: "Configuring and deploying the gateway API"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/configuring-and-deploying-the-gateway-api.html"
content_id: "Cp_azQmDoAJGmm_t37ksPw"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:27.299124+00:00"
---

# Configuring and deploying the gateway API

Before enabling the ingress gateway API in the `cnc` Helm chart:

1. Install the Gateway API CRDs on your cluster:

   ```
   kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.1.0/standard-install.yaml
   kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.1.0/experimental-install.yaml
   ```
2. Install the NGINX gateway fabric with snippets support enabled:

   ```
   helm install ngf oci://ghcr.io/nginx/charts/nginx-gateway-fabric \
     --create-namespace \
     -n nginx-gateway \
     --set nginxGateway.snippets.enable=true \
     --set nginx.service.externalTrafficPolicy=Local
   ```

   `snippets.enable=true` is required for IP allowlisting features
   (`allowedSourceRanges` /
   `gatewayAllowedSourceRanges`). It is not required for basic
   routing.
3. Verify that the NGINX gateway fabric is running and a
   `GatewayClass` named `nginx` exists:

   ```
   kubectl get pods -n nginx-gateway
   kubectl get gatewayclass nginx
   ```
