---
title: "Option B: AWS Load Balancer Controller"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/option-b-aws-load-balancer-controller.html"
content_id: "2fPaBx3aRL5LpuYR99zHFQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:43.627678+00:00"
---

# Option B: AWS Load Balancer Controller

The AWS Load Balancer Controller (AWS LBC) provisions an AWS Application Load Balancer
(ALB) directly from Gateway API resources. No separate proxy pod is deployed — the ALB
is fully managed by AWS. This is the native AWS approach and integrates with IAM, target
groups, and AWS WAF.

**Prerequisites**

- EKS cluster running any [supported EKS Kubernetes version](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html) (AWS LBC
  baseline is Kubernetes 1.22+)
- **AWS Load Balancer Controller v3.0+** — Gateway API went GA in v3.0.0 (January
  2025). Earlier versions (v2.14.0+ for L7, v2.13.3+ for L4) required preview feature
  gates. See the [version compatibility table](https://blackducksoftware-my.sharepoint.com/shared?listurl=https%3A%2F%2Fblackducksoftware%2Dmy%2Esharepoint%2Ecom%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments&id=%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments%2FMicrosoft%20Teams%20Chat%20Files%2Fingress%2Dto%2Dgateway%2Dapi%2Dmigration%2Dguide%207%2Emd&parent=%2Fpersonal%2Fdmahakud%5Fblackduck%5Fcom%2FDocuments%2FMicrosoft%20Teams%20Chat%20Files&shareLink=1&ga=1#kubernetes-version-compatibility).
- `kubectl` configured for the cluster
- Helm 3.x and `eksctl` installed
- AWS CLI configured with appropriate credentials

1. Export Cluster
   Information

   ```
   export CLUSTER_NAME=<your-cluster-name>
   export AWS_REGION=<your-region>   # e.g. us-east-2

   export VPC_ID=$(aws eks describe-cluster \
     --name $CLUSTER_NAME \
     --region $AWS_REGION \
     --query 'cluster.resourcesVpcConfig.vpcId' \
     --output text)

   export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
   ```
2. Create IAM Policy and Service Account (IRSA)

   Download the IAM
   policy:

   ```
   curl -o iam-policy.json \
     https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/main/docs/install/iam_policy.json
   ```

   Create
   the policy (skip if it already exists — use the existing
   ARN):

   ```
   aws iam create-policy \
     --policy-name AWSLoadBalancerControllerIAMPolicy \
     --policy-document file://iam-policy.json \
     --region $AWS_REGION

   export POLICY_ARN=arn:aws:iam::${AWS_ACCOUNT_ID}:policy/AWSLoadBalancerControllerIAMPolicy
   ```

   Create
   the Kubernetes service account with the IAM role
   attached:

   ```
   eksctl create iamserviceaccount \
     --cluster=$CLUSTER_NAME \
     --namespace=kube-system \
     --name=aws-load-balancer-controller \
     --attach-policy-arn=$POLICY_ARN \
     --override-existing-serviceaccounts \
     --region $AWS_REGION \
     --approve
   ```
3. Install Gateway API CRDs

   AWS LBC v3.2+ requires Gateway API CRDs v1.5.0. Only the
   standard CRDs are needed — the experimental bundle contains NGF-specific
   resources (`SnippetsFilter`, `SnippetsPolicy`,
   `ClientSettingsPolicy`) that are not used by AWS
   LBC:

   ```
   kubectl apply --server-side \
     -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.5.0/standard-install.yaml
   ```

   Verify:

   ```
   kubectl get crd | grep gateway
   ```
4. Install AWS Load Balancer
   Controller

   ```
   helm repo add eks https://aws.github.io/eks-charts
   helm repo update

   helm upgrade -i aws-load-balancer-controller eks/aws-load-balancer-controller \
     -n kube-system \
     --set clusterName=$CLUSTER_NAME \
     --set serviceAccount.create=false \
     --set serviceAccount.name=aws-load-balancer-controller \
     --set region=$AWS_REGION \
     --set vpcId=$VPC_ID
   ```

   > Gateway API support is GA in AWS LBC v3.0.0+ and enabled by default. If you
   > are pinned to v2.14.0–v2.x for any reason, also set `--set
   > featureGates.ALBGatewayAPI=true` (and `--set
   > featureGates.NLBGatewayAPI=true` for L4). These flags are
   > removed in v3.0+.

   Verify:

   ```
   kubectl rollout status deployment aws-load-balancer-controller -n kube-system
   kubectl logs -n kube-system deployment/aws-load-balancer-controller | grep -i gateway
   ```
5. Create
   GatewayClass

   ```
   kubectl apply -f - <<EOF
   apiVersion: gateway.networking.k8s.io/v1
   kind: GatewayClass
   metadata:
     name: amazon-alb
   spec:
     controllerName: gateway.k8s.aws/alb
   EOF
   ```

   > `GatewayClass` graduated to `v1` in Gateway API
   > v1.0. Use `v1beta1` only if pinning to an older CRD
   > release.

   Verify
   acceptance:

   ```
   kubectl get gatewayclass amazon-alb
   # Expected: ACCEPTED = True
   ```
6. Create LoadBalancerConfiguration

   The `LoadBalancerConfiguration`
   resource controls ALB settings. By default the ALB is internal; set
   `scheme: internet-facing` for public
   access:

   ```
   export APP_NAMESPACE=<your-release-namespace>

   kubectl apply -f - <<EOF
   apiVersion: gateway.k8s.aws/v1beta1
   kind: LoadBalancerConfiguration
   metadata:
     name: ${CLUSTER_NAME}-lb-config
     namespace: $APP_NAMESPACE
   spec:
     scheme: internet-facing
   EOF
   ```

   The controller auto-selects public subnets tagged
   `kubernetes.io/role/elb=1`. To specify subnets explicitly,
   add `loadBalancerSubnets` entries with your subnet IDs.
7. Create the TLS
   secret:

   ```
   kubectl create secret tls coverity-tls \
     --cert=path/to/tls.crt \
     --key=path/to/tls.key \
     -n $APP_NAMESPACE
   ```
8. Configure the cnc Helm chart

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
       gatewayClassName: "amazon-alb"
       name: "<release-name>-cim-gateway"         # default — auto-derived from Helm release name
       lbConfigName: "<cluster-name>-lb-config"
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
       healthCheck:
         requestPath: "/login/login.htm"
         commitServerRequestPath: "/login/login.htm"
   ```

   Deploy:

   ```
   helm upgrade --install <release-name> charts/cnc/ -f values.yaml -n $APP_NAMESPACE
   ```

   **What the chart creates automatically on AWS:**

   | Resource | Purpose |
   | --- | --- |
   | `Gateway` | HTTP (80) and HTTPS (443) listeners |
   | `HTTPRoute` `<release-name>-cim` | Routes HTTPS traffic to CIM on port 8080 |
   | `HTTPRoute` `<release-name>-http-redirect` | Redirects HTTP → HTTPS (301) |
   | `HTTPRoute` `<release-name>-commit-server` | Routes `/ccd` to commit-server (when `cimweb.replicas > 1`) |
   | `TargetGroupConfiguration` `<release-name>-cim-tg-config` | Health check path + target group settings for CIM |
   | `TargetGroupConfiguration` `<release-name>-commit-server-tg-config` | Health check settings for commit-server (when `cimweb.replicas > 1`) |
9. Retrieve the ALB DNS Name

   The ALB DNS hostname appears directly on the Gateway
   resource once provisioning completes (typically 2–5
   minutes):

   ```
   kubectl get gateway <release-name>-cim-gateway -n $APP_NAMESPACE

   export ALB_DNS=$(kubectl get gateway <release-name>-cim-gateway -n $APP_NAMESPACE \
     -o jsonpath='{.status.addresses[0].value}')
   echo "ALB DNS: $ALB_DNS"
   ```
10. Update DNS

    In Route 53, create a **CNAME record** pointing
    `coverity.example.com` to `$ALB_DNS`. For
    zone-apex domains, use an Alias record instead.
11. Verify

    ```
    # Gateway must show PROGRAMMED = True and have an ADDRESS
    kubectl get gateway <release-name>-cim-gateway -n $APP_NAMESPACE

    # HTTPRoutes must show Accepted: True, ResolvedRefs: True
    kubectl get httproute -n $APP_NAMESPACE

    # TargetGroupConfigurations must be present
    kubectl get targetgroupconfiguration -n $APP_NAMESPACE

    # Test HTTP redirect (expect 301)
    curl -I http://$ALB_DNS -H "Host: coverity.example.com"

    # Test HTTPS (expect 200 or login redirect)
    curl -sk -o /dev/null -w "%{http_code}\n" https://coverity.example.com/login/login.htm
    ```
