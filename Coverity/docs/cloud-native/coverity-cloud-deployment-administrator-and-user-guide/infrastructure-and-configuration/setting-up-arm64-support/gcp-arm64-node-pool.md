---
title: "GCP ARM64 node pool"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/gcp-arm64-node-pool.html"
content_id: "~3pLeIa_T3x8zblm8199wA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:04.100753+00:00"
---

# GCP ARM64 node pool

To support ARM64 hardware in Google GCP, you need to set the following GCP node pool
parameter:

- The node pool `machine_type` for both node pools (the default node
  pool and the job service node pool) must be `t2a-standard-8`.

Note: Refer to <https://cloud.google.com/kubernetes-engine/docs/how-to/create-arm-clusters-nodes>.
