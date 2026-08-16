---
title: "AWS: Create an S3 storage bucket"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/aws-create-an-s3-storage-bucket.html"
content_id: "o6wwZhll8qRh7s6QB67iHQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:14.744306+00:00"
---

# AWS: Create an S3 storage bucket

Note: If you are using S3 Express (not S3), skip this section and see
Configure AWS S3 Express Helm keys.

You can create either an S3 storage bucket or an S3 Express storage bucket. This section
outlines the S3 storage bucket. To create an Amazon S3 storage bucket:

1. See the following for information on sizing the bucket and to create the
   bucket:

   - Scan Service storage bucket sizing
   - <https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html>

   Important:

   Do NOT set a retention policy or lifecycle policy for the storage-service
   bucket. Setting either policy might cause the idir and tools files to be
   deleted from the bucket as per the policy. You would then lose this
   data.

After you create the S3 storage bucket, you will additionally need to:

1. Ceate either an AWS storage bucket IAM policy or a storage service secret. See .
   - For AWS storage bucket IAM policy: Specifying AWS S3 storage bucket and cache bucket IAM policy
   - For storage service secret: Create an AWS storage service secret.
2. Configure the `s3` Helm keys as described in Configure AWS S3 Helm keys.
