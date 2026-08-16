---
title: "Sizing a Coverity Connect (cim) pod for optimum performance"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sizing-a-coverity-connect-cim-pod-for-optimum-performance.html"
content_id: "JqMPGCkXs7OulMnz2KleZw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:48.897613+00:00"
---

# Sizing a Coverity Connect (cim) pod for optimum performance

Coverity Connect (cim) pod sizing and scaling are different but related considerations.
Sizing ensures that the pod resources meet the analysis processing and storage workload
requirements. Scaling defines pod resource requirements to support growth of the
analysis environment over time.

Important: In a deployment with multiple Coverity Connect
(cim) pods, the resource guidance applies equally to all pods deployed. Provide the full
resources for each pod that you deploy; do not split up calculated CPU and memory
resources between pods.

The following sections describe how to estimate Coverity Connect pod CPU and memory
resources using the following methods:

- Scaling CPU and memory using commits.
- Scaling CPU and memory using view loading.
