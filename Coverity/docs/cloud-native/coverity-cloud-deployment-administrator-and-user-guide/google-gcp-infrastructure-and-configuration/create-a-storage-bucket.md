---
title: "Create a storage bucket"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-storage-bucket.html"
content_id: "iGNaEqnKzhphg7xXgVH45g"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:31.129570+00:00"
---

# Create a storage bucket

Create a storage bucket for the Storage Service. Refer to:

- <https://cloud.google.com/storage/docs/creating-buckets#storage-create-bucket-cli>

For example:

```
gsutil mb -p "${CNC_PROJECT_ID}" \
    --pap enforced -l US gs://${CNC_BUCKET}
```

Important:

Do NOT set a retention policy or lifecycle policy for the storage-service bucket.
Setting either policy might cause the idir and tools files to be deleted from the
bucket as per the policy. You would then lose this data.
