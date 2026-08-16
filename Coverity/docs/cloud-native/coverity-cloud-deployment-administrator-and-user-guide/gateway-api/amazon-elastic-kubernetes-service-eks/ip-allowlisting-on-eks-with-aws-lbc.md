---
title: "IP allowlisting on EKS with AWS LBC"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ip-allowlisting-on-eks-with-aws-lbc.html"
content_id: "89WvrYcJBB4AcPhCBKYacw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:44.271376+00:00"
---

# IP allowlisting on EKS with AWS LBC

`allowedSourceRanges` and `gatewayAllowedSourceRanges` are
NGF-only. The chart does not render `SnippetsFilter` or
`SnippetsPolicy` resources when `gatewayClassName` is
not `nginx`, so setting these values has no effect on AWS deployments.
Use **AWS WAF** or **Security Groups** instead:

- **AWS WAF:** Attach a WAF Web ACL to the ALB via the AWS Console or `aws
  wafv2`.
- **Security Groups:** Restrict inbound traffic to the ALB security group to
  trusted CIDR ranges.

**Troubleshooting (AWS LBC)**

| Symptom | Cause | Fix |
| --- | --- | --- |
| Gateway not getting an address | ALB still provisioning or IRSA misconfigured | Check `kubectl logs -n kube-system deployment/aws-load-balancer-controller` |
| `ACCEPTED = False` on GatewayClass | LBC older than v3.0 without preview feature gate | Upgrade to AWS LBC v3.0+ (Gateway API GA, no flag needed). On v2.14.0–v2.x, set `featureGates.ALBGatewayAPI=true`. |
| Targets unhealthy | Health check path returning non-2xx | Verify `healthCheck.requestPath: "/login/login.htm"` in Helm values |
| `LoadBalancerConfiguration` not found | Resource not created in release namespace | Ensure `lbConfigName` matches the `LoadBalancerConfiguration` name and namespace |
| ALB created as internal | Missing `scheme: internet-facing` | Update `LoadBalancerConfiguration` and reapply |
| Permission errors in controller logs | IAM policy not attached to IRSA role | Run `eksctl create iamserviceaccount` with `--override-existing-serviceaccounts` |
