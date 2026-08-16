---
title: "Create and configure a cache storage bucket"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-and-configure-a-cache-storage-bucket.html"
content_id: "7z5hTPoqiT9ZxmPxUh491Q"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:58.171352+00:00"
---

# Create and configure a cache storage bucket

The Cache Service stores data in an object storage bucket. This bucket is different from
the Scan Service bucket. Cache Service requires Redis and a cache storage bucket.

Note: Caching is optional, even if you are using Scan Service..

Adhere to the following requirements and recommendations when you create and configure a
cache storage bucket:

- Requirement: You must create the Cache storage bucket before you run the Helm
  install. The Cache Service does not attempt to create the storage bucket. If the
  bucket does not exist, the Cache Service will fail to start.
- Requirement: You must configure the cache storage bucket lifecycle policy that
  removes objects after a certain time as described in the documentation from the
  bucket provider (Amazon S3, Azure Blob Storage, Google GCS, Red Hat OpenShift,
  or MinIO). The minimum cache retention period is 8 days. Black Duck recommends 30 days. The Cache Service checks
  that this lifecycle rule is present and will not start if a lifecycle policy
  retention period is not set.
- Recommendation: The cache storage bucket should not be geographically
  distributed.
- Recommendation: The cache storage bucket should not enable versioning, retention,
  or other special features.

Important: For AWS ElastiCache and Redis configuration for
ElastiCache, see also Configuring AWS ElastiCache and Redis.

Retain the bucket name. When you set up the Helm chart, you will need to enter the cache
storage bucket name in the `cache-service.bucketName` Helm key. Refer
to:

- Scan Service caching
- cache-service Helm keys
