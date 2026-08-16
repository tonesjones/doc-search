---
title: "AWS ARM64"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/aws-arm64.html"
content_id: "TJMD2AN4UKD0laMf_8gNzw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:02.128079+00:00"
---

# AWS ARM64

To support ARM64 hardware in AWS, when you create node pools, you need to set the
following AWS node pool properties:

- The node pool `instance_type` for both node pools (the default node
  pool and the job service node pool must be `m6gd.2xlarge`.
- The node pool `ami_type` for both node pools (the default node pool
  and the job service node pool must be `AL2_ARM_64`.

Note: Refer to <https://docs.aws.amazon.com/eks/latest/APIReference/API_Nodegroup.html> and .<https://aws.amazon.com/ec2/instance-types/m6g/>

Ingress controller: No Helm chart changes are needed to deploy the ingress
controller.

Helm chart: No changes are needed to deploy the Helm chart.
