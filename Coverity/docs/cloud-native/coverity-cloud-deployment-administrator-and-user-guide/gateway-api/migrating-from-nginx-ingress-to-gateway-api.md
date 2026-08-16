---
title: "Migrating from NGINX ingress to gateway API"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/migrating-from-nginx-ingress-to-gateway-api.html"
content_id: "KMgsPfL_jsI8jFxKkWgJfA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:46.948953+00:00"
---

# Migrating from NGINX ingress to gateway API

1. Install Gateway API
   credentials:

   ```
   kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.1.0/standard-install.yaml

   kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.1.0/experimental-install.yaml
   ```
2. Install the NGINX gateway
   fabric:

   ```
   helm install ngf oci://ghcr.io/nginx/charts/nginx-gateway-fabric \
     --create-namespace \
     -n nginx-gateway \
     --set nginxGateway.snippets.enable=true \
     --set nginx.service.externalTrafficPolicy=Local
   ```
3. Update your Helm values:

   ```
   global:
     ingress:
       enabled: false      # disable global Ingress

   cim:
     ingress:
       enabled: false      # disable CIM Ingress

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
           tlsSecretName: "coverity-ingress"   # reuse existing TLS secret
   ```
4. Deploy and
   verify:

   ```
   helm upgrade <release> . -f values.yaml

   # Check Gateway is Programmed
   kubectl get gateway <release>-gateway -n <namespace>

   # Check HTTPRoutes are Accepted
   kubectl get httproute -n <namespace>

   # Test HTTPS
   curl -sk -o /dev/null -w "%{http_code}\n" https://coverity.example.com/login/login.htm
   # Expected: 200

   # Test HTTP redirect
   curl -sk -o /dev/null -w "%{http_code} → %{redirect_url}\n" http://coverity.example.com/
   # Expected: 301 → https://coverity.example.com/
   ```
5. Update DNS:
   1. Find the NGINX Gateway Fabric external IP:

      ```
      kubectl get svc -n nginx-gateway
      ```
   2. Update your DNS record for `coverity.example.com` to point
      to the new Gateway IP.
6. Once traffic has been validated on the Gateway IP, remove the old Ingress
   Controller:

   ```
   # Remove old Ingress resources
   kubectl delete ingress -n <namespace> --all

   # Uninstall NGINX Ingress Controller
   helm uninstall nginx-ingress -n ingress-nginx
   kubectl delete namespace ingress-nginx
   ```

**Rollback**

If you need to revert:

```
helm upgrade <release> . -f values.yaml \
  --set cim.ingress.enabled=true \
  --set global.ingress.enabled=true \
  --set cim.gateway.enabled=false \
  --set cim.gateway.create=false
```
