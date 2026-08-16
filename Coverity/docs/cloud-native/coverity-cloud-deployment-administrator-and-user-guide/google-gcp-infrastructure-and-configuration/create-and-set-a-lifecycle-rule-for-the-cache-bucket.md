---
title: "Create and set a lifecycle rule for the cache bucket"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-and-set-a-lifecycle-rule-for-the-cache-bucket.html"
content_id: "v8dGjYUZAkyX4pUBweZ5dw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:32.416555+00:00"
---

# Create and set a lifecycle rule for the cache bucket

1. Create a lifecycle rule for the cache bucket. For example:

   ```
   read -r -d '' LS_RULE <<EOF
   {
       "lifecycle": {
         "rule":
         [
           {
             "action": {"type": "Delete"},
             "condition": {"age": $CNC_LIFECYCLE_DELETE_DAYS}
           }
         ]
       }
   }
   EOF
   echo "${LS_RULE}" > gcp_bucket_lifecycle_config.json
   ```
2. Set the lifecycle rule. For example:

   ```
   gsutil lifecycle set gcp_bucket_lifecycle_config.json gs://${CNC_CACHE_BUCKET}
   ```
