---
title: "Create a cache bucket"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-cache-bucket.html"
content_id: "RQyR2bfvPCSjFDbdH6l3nw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:31.777683+00:00"
---

# Create a cache bucket

Create a cache bucket for the Cache Service. Refer to:

- For requirements when creating a cache storage container, see: Create and configure a cache storage bucket
- For information on creating a cache bucket in GCP, see <https://cloud.google.com/storage/docs/creating-buckets#storage-create-bucket-cli>

For example:

```
gsutil mb -p "${CNC_PROJECT_ID}" \
    --pap enforced -l US gs://${CNC_CACHE_BUCKET}
```
