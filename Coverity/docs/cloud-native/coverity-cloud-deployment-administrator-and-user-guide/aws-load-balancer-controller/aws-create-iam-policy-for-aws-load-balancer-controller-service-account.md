---
title: "AWS: Create IAM policy for AWS Load Balancer Controller Service Account"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/aws-create-iam-policy-for-aws-load-balancer-controller-service-account.html"
content_id: "mDlo905XDjAk5XOuTrwo4g"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:19.509168+00:00"
---

# AWS: Create IAM policy for AWS Load Balancer Controller Service Account

For information on the AWS ALB Load Balancer Controller, see:

- <https://github.com/aws/eks-charts/tree/master/stable/aws-load-balancer-controller>
- <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html>

To create IAM policy for the AWS Load Balancer Controller Service Account:

1. Create an IAM OIDC (OpenID Connect) provider:

   ```
   eksctl utils associate-iam-oidc-provider \
     --region <aws-region> \
     --cluster <your-cluster-name> \
     --approve
   ```
2. Download the IAM policy for the AWS Load Balancer Controller:

   ```
   curl -o iam-policy.json \
     https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/main/docs/install/iam_policy.json
   ```
3. Create an IAM policy called AWSLoadBalancerControllerIAMPolicy, using the
   `iam_policy.json` file you just downloaded:

   ```
   aws iam create-policy \
     --policy-name AWSLoadBalancerControllerIAMPolicy \
     --policy-document file://iam-policy.json
   ```
4. Take note of the policy ARN that is returned.
5. Create an IAM role and ServiceAccount for the Load Balancer controller, use the
   ARN from above.

   ```
   eksctl create iamserviceaccount \
     --cluster=<cluster-name> \
     --namespace=kube-system \
     --name=aws-load-balancer-controller \
     --attach-policy-arn=arn:aws:iam::<AWS_ACCOUNT_ID>:policy/AWSLoadBalancerControllerIAMPolicy \
     --approve
   ```
