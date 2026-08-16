---
title: "Amazon Elastic Kubernetes Service (EKS)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/amazon-elastic-kubernetes-service-eks-.html"
content_id: "DW8V_oSNdKoeZ~qUx8xlKA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:41.597968+00:00"
---

# Amazon Elastic Kubernetes Service (EKS)

Two options are available on EKS: NGINX Gateway Fabric (NGF) and the AWS Load Balancer
Controller (AWS LBC), which provisions an AWS Application Load Balancer (ALB) natively.
Both implement the standard Kubernetes Gateway API and are compatible with the CNC
chart.

| Dimension | Option A: NGINX Gateway Fabric | Option B: AWS Load Balancer Controller |
| --- | --- | --- |
| Gateway implementation | NGF controller pod in cluster | AWS ALB (fully managed) |
| Load balancer type | AWS Network Load Balancer (NLB) | AWS Application Load Balancer (ALB) |
| L7 features | NGF-native (SnippetsFilter, ClientSettingsPolicy) | AWS-native (TargetGroupConfiguration, HealthCheck) |
| IP allowlisting | `SnippetsPolicy` / `SnippetsFilter` | AWS WAF / Security Groups |
| External IP location | `kubectl get svc -n nginx-gateway` (NLB DNS) | `kubectl get gateway` status addresses (ALB DNS) |
| GatewayClass | `nginx` | `amazon-alb` |
| IRSA required | No | Yes (IAM role for service account) |
