---
title: "Azure ARM64"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/azure-arm64.html"
content_id: "05Hu6YLDq77UmvkI_hut_g"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:02.774559+00:00"
---

# Azure ARM64

To support ARM64 hardware in Microsoft Azure, you need to set the following Azure node
pool properties:

- The node pool `instance_type` for the default node pool must be
  `Standard_D2ps_v5`.
- The node pool `instance_type` for the job service node pool must be
  `Standard_D8pds_v5`.

Note: Refer to <https://learn.microsoft.com/en-us/azure/aks/create-node-pools>.

Ingress controller: No Helm chart changes are needed to deploy the ingress
controller.

Helm chart: No changes are needed to deploy the Helm chart.
