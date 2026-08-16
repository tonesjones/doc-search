---
title: "Configure Red Hat OpenShift storage"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configure-red-hat-openshift-storage.html"
content_id: "~NQf8kq~cwOCzUDLZNLg_g"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:45.084298+00:00"
---

# Configure Red Hat OpenShift storage

If you are deploying the Storage Service in Red Hat OpenShift, set the following storage
values with the values you set when you created the storage and the secret to access the
storage:

- For OpenShift, the storage bucket type is `s3`.
- Storage bucket name.
- Storage bucket region.
- The secret name.

In the `scan-services` Helm subchart, configure the following keys:

1. Configure the storage bucket type. For OpenShift, use
   `"s3"`.

   ```
   storage-service:
     storageType: "s3"
   ```

   :
2. Configure the bucket name, region, and thename of the secret. For
   example:

   ```
   storage-service:
     s3:
       bucket: "S3Bucket1"
       region: "region1"
       secret:
         name: "mySecret"
   ```
