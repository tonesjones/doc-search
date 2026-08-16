---
title: "Option A: NGINX gateway fabric on EKS"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/option-a-nginx-gateway-fabric-on-eks.html"
content_id: "8pQ7CtsFcAUNFQvV77Z72Q"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:42.241002+00:00"
---

# Option A: NGINX gateway fabric on EKS

On EKS, NGINX Gateway Fabric is a straightforward Gateway API implementation that mirrors
the local (kind) and GKE NGF setup. NGF creates a LoadBalancer Service that EKS backs
with an AWS Network Load Balancer (NLB) by default. Choose Option B (AWS LBC) if you
prefer a fully managed ALB with native AWS IAM integration.

**Prerequisites**

- EKS cluster running **Kubernetes 1.31+** (required by NGF 2.5.x / 2.6.0 — see
  the [version compatibility table](https://blackducksoftware-my.sharepoint.com/shared?listurl=https%3A%2F%2Fblackducksoftware%2Dmy%2Esharepoint%2Ecom%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments&id=%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments%2FMicrosoft%20Teams%20Chat%20Files%2Fingress%2Dto%2Dgateway%2Dapi%2Dmigration%2Dguide%207%2Emd&parent=%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments%2FMicrosoft%20Teams%20Chat%20Files&shareLink=1&ga=1#kubernetes-version-compatibility))
- `kubectl` configured for the cluster
- Helm 3.x installed
- AWS Load Balancer Controller installed on the cluster (for NLB/ALB
  provisioning)

  > Install the AWS Load Balancer Controller if not already present: [AWS Load Balancer Controller Installation
  > Guide](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html)

1. Install Gateway API
   CRDs

   ```
   kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.5.0/standard-install.yaml
   kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.5.0/experimental-install.yaml
   ```

   Verify:

   ```
   kubectl get crd | grep gateway.networking.k8s.io
   ```
2. Install NGINX Gateway
   Fabric

   ```
   helm install ngf oci://ghcr.io/nginx/charts/nginx-gateway-fabric \
     --create-namespace \
     -n nginx-gateway \
     --set nginxGateway.snippets.enable=true \
     --set nginx.service.externalTrafficPolicy=Local \
     --set nginx.service.annotations."service\.beta\.kubernetes\.io/aws-load-balancer-type"=external \
     --set nginx.service.annotations."service\.beta\.kubernetes\.io/aws-load-balancer-nlb-target-type"=ip
   ```

   > The annotations above instruct the AWS Load Balancer Controller to provision
   > an **IP-mode NLB**, which is required for
   > `externalTrafficPolicy=Local` to preserve client source
   > IPs (used for IP allowlisting). Omit these annotations if you do not require
   > source IP preservation.

   Verify:

   ```
   kubectl get pods -n nginx-gateway
   kubectl get gatewayclass nginx
   kubectl get svc -n nginx-gateway   # wait for EXTERNAL-IP (NLB DNS hostname)
   ```

   On
   AWS, the NLB is assigned a DNS hostname (e.g.
   `abc123.elb.us-east-1.amazonaws.com`), not an IP address. Use
   a CNAME record in Route 53 (or an Alias record for zone apex domains) to map
   your hostname to the NLB DNS name.
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
5. Retrieve the NLB
   Hostname

   ```
   kubectl get svc -n nginx-gateway
   # Locate the EXTERNAL-IP column — this is the NLB DNS hostname
   ```
6. Update DNS

   In Route 53 (or your DNS provider), create a CNAME record pointing
   `coverity.example.com` to the NLB hostname. For zone apex
   records, use an Alias record.
7. Verify

   ```
   # Check Gateway is Programmed (allow 2–5 minutes for NLB provisioning)
   kubectl get gateway <release-name>-cim-gateway -n <release-namespace>

   # Check HTTPRoutes are Accepted
   kubectl get httproute -n <release-namespace>

   # Test HTTPS (expect 200)
   curl -sk -o /dev/null -w "%{http_code}\n" https://coverity.example.com/login/login.htm

   # Test HTTP redirect (expect 301)
   curl -sk -o /dev/null -w "%{http_code} → %{redirect_url}\n" http://coverity.example.com/
   ```
