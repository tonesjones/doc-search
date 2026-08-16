---
title: "Create a service account (SA)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-service-account-sa-.html"
content_id: "pZXlw7HWeSl8ew0Lur0jjQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:33.056571+00:00"
---

# Create a service account (SA)

Create a service account (SA) to access the storage bucket: For example:

```
gcloud iam service-accounts create "${CNC_STORAGE_SA}" \
   --project "${CNC_PROJECT_ID}" \
   --display-name "service account for ${CNC_PREFIX} environment"
```
