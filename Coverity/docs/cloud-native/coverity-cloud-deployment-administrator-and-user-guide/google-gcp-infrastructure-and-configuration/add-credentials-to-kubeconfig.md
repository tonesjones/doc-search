---
title: "Add credentials to kubeconfig"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/add-credentials-to-kubeconfig.html"
content_id: "CxCqaLMbneYR7qZsVmhIHg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:26.547422+00:00"
---

# Add credentials to kubeconfig

Add credentials to kubeconfig:

```
gcloud container clusters get-credentials ${CNC_CLUSTER_NAME} \
    --project $CNC_PROJECT_ID \
    --zone $CNC_ZONE
```
