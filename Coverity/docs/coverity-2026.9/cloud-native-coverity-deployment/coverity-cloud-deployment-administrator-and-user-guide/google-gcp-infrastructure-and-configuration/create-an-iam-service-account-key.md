---
title: "Create an IAM service account key"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/create-an-iam-service-account-key.html"
content_id: "_YwE7xeMAyiJP5gCDl2QTQ"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:23.888831+00:00"
---

# Create an IAM service account key

Create an IAM service account key. This key will be used by the Storage Service to access
the GCS bucket. For example:

```
gcloud iam service-accounts keys create key.json \
  --iam-account "${CNC_STORAGE_SA}@${CNC_PROJECT_ID}.iam.gserviceaccount.com"
```

Also refer to:

- <https://cloud.google.com/iam/docs/keys-create-delete>
- Create a GCS service account secret
