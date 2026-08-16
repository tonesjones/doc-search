---
title: "Installing chart releases for your deployment"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/installing-chart-releases-for-your-deployment.html"
content_id: "lStCOYwukiHgYBdi04vapQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:34.600655+00:00"
---

# Installing chart releases for your deployment

Running a Helm install command installs a chart if none exists, or upgrades an existing
chart. The sections that follow describe how to use Helm install commands to install
chart releases that support various Coverity deployments. These chart releases are the
result of creating Helm override in YAML file(s) to support the deployment. The chart
release contains customized Helm key overrides for your deployment.

Important: Before running Helm install, you must scale
down any running Coverity Connect Web applications running in the cluster. For
example:

```
kubectl scale deployment/${RELEASE}-cim-webapp -n ${NS} --replicas=0
```
