---
title: "Create a Redis instance"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-redis-instance.html"
content_id: "kLI9bnYnJF9EaJvZSZ5bOg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:35.649429+00:00"
---

# Create a Redis instance

1. Create a Redis instance. For example:

   ```
   gcloud redis instances create $CNC_REDIS_NAME \
       --size=$CNC_REDIS_SIZE \
       --region=$CNC_REGION \
       --transit-encryption-mode=SERVER_AUTHENTICATION \
       --enable-auth \
       --redis-config=maxmemory-policy=noeviction \
       -q
   ```
2. Get the Redis AUTH string. For example:

   ```
   REDIS_AUTH=$(gcloud redis instances get-auth-string $CNC_REDIS_NAME --region=$CNC_REGION)
   ```
3. Get the Redis TLS CA certificate from the memorystore metadata for the Redis
   instance. For example, to display the metadata from the Redis memorystore:

   ```
   gcloud redis instances describe $CNC_REDIS_NAME --region=$CNC_REGION
   ```
4. Add the Redis CA certificate to the truststore as described in the following
   section within this document:

   - for an overview and links to creating a truststore: Create a truststore ConfigMap for Connect communication over TLS
