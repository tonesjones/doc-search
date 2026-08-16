---
title: "Azure Kubernetes Service (AKS)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/azure-kubernetes-service-aks-.html"
content_id: "0V7Ckx0P4Ql5aNq1vBjvcg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:44.921769+00:00"
---

# Azure Kubernetes Service (AKS)

Two options are available on AKS: NGINX Gateway Fabric and the Azure Application Load
Balancer (ALB) Controller (Application Gateway for Containers). Choose based on your
organizational requirements and existing Azure infrastructure.

| Dimension | Option A: NGINX Gateway Fabric | Option B: Azure ALB Controller |
| --- | --- | --- |
| Gateway implementation | NGF controller pod in cluster | Azure-managed Application Gateway for Containers |
| Load balancer type | Azure Standard Load Balancer | Azure Application Gateway for Containers (AGfC) |
| L7 features | NGF-native (SnippetsFilter, ClientSettingsPolicy) | Azure-native (WAF, AGfC routing) |
| IP allowlisting | `SnippetsPolicy` / `SnippetsFilter` | Azure Application Gateway WAF / NSG rules |
| GatewayClass | `nginx` | `azure-alb-external` (or `azure-alb-internal`) |
| Managed service | No (NGF runs in your cluster) | Yes (AGfC is a fully managed Azure service) |

**Option A: NGINX Gateway Fabric on AKS**

**Prerequisites**

- AKS cluster running **Kubernetes 1.31+** (required by NGF 2.5.x / 2.6.0 — see the
  [version compatibility table](https://blackducksoftware-my.sharepoint.com/shared?listurl=https%3A%2F%2Fblackducksoftware%2Dmy%2Esharepoint%2Ecom%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments&id=%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments%2FMicrosoft%20Teams%20Chat%20Files%2Fingress%2Dto%2Dgateway%2Dapi%2Dmigration%2Dguide%207%2Emd&parent=%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments%2FMicrosoft%20Teams%20Chat%20Files&shareLink=1&ga=1#kubernetes-version-compatibility))
- `kubectl` configured for the cluster
- Helm 3.x installed
- Azure CLI installed

1. Install Gateway API
   CRDs

   ```
   kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.5.0/standard-install.yaml
   kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.5.0/experimental-install.yaml
   ```
2. Install NGINX Gateway
   Fabric

   ```
   helm install ngf oci://ghcr.io/nginx/charts/nginx-gateway-fabric \
     --create-namespace \
     -n nginx-gateway \
     --set nginxGateway.snippets.enable=true \
     --set nginx.service.externalTrafficPolicy=Local
   ```
3. Create a TLS
   Secret

   ```
   kubectl create secret tls coverity-tls \
     --cert=path/to/tls.crt \
     --key=path/to/tls.key \
     -n <release-namespace>
   ```
4. Configure the CNC Helm Chart

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
5. Retrieve the External
   IP

   ```
   kubectl get svc -n nginx-gateway
   # EXTERNAL-IP is the Azure Standard Load Balancer public IP
   ```
6. Update DNS

   Update your DNS record for `coverity.example.com` to
   point to the public IP retrieved above. If using Azure DNS, create an A record
   in your DNS zone.
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
