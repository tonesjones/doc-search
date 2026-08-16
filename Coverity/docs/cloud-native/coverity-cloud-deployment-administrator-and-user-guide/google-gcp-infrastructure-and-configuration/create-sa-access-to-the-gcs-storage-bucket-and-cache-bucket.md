---
title: "Create SA access to the GCS storage bucket and cache bucket"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-sa-access-to-the-gcs-storage-bucket-and-cache-bucket.html"
content_id: "RqCGvWWCPLWp5icSP1Ngyw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:33.702133+00:00"
---

# Create SA access to the GCS storage bucket and cache bucket

Create SA access to the storage bucket and cache bucket. For example:

```
gsutil iam ch serviceAccount:${CNC_STORAGE_SA}@${CNC_PROJECT_ID}.iam.gserviceaccount.com:roles/storage.objectAdmin gs://${CNC_BUCKET}
gsutil iam ch serviceAccount:${CNC_STORAGE_SA}@${CNC_PROJECT_ID}.iam.gserviceaccount.com:roles/storage.legacyBucketReader gs://${CNC_BUCKET}
gsutil iam ch serviceAccount:${CNC_STORAGE_SA}@${CNC_PROJECT_ID}.iam.gserviceaccount.com:roles/storage.objectAdmin gs://${CNC_CACHE_BUCKET}
gsutil iam ch serviceAccount:${CNC_STORAGE_SA}@${CNC_PROJECT_ID}.iam.gserviceaccount.com:roles/storage.legacyBucketReader gs://${CNC_CACHE_BUCKET}
```
