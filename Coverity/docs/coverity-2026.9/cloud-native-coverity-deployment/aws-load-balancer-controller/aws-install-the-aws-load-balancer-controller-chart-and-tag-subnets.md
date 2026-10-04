---
title: "AWS: Install the aws-load-balancer-controller chart and tag subnets"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/aws-install-the-aws-load-balancer-controller-chart-and-tag-subnets.html"
content_id: "o3q0pwrOjDdByvlcscetHw"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:34.903925+00:00"
---

# AWS: Install the aws-load-balancer-controller chart and tag subnets

1. Install the AWS Load Balancer Controller chart as described in <https://artifacthub.io/packages/helm/aws/aws-load-balancer-controller/#installing-the-chart>.
2. Add the following tag to public subnets:

   `kubernetes.io/role/elb =
   1`

   For information on tagging subnets in Amazon AWS EKS, refer to:
   <https://repost.aws/knowledge-center/eks-vpc-subnet-discovery>
