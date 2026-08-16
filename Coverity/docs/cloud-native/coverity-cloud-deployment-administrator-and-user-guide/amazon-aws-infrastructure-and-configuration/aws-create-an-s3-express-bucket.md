---
title: "AWS: Create an S3 Express bucket"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/aws-create-an-s3-express-bucket.html"
content_id: "DPWyIiqWpZZW_Iuna3DGBA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:13.411447+00:00"
---

# AWS: Create an S3 Express bucket

Note: If you are using S3 (not S3 Express), skip this section and see
AWS: Create an S3 storage bucket.

You can create either S3 or S3 Express storage buckets. This section outlines how to
create S3 Express storage buckets and cache buckets. To create an Amazon S3 Express
bucket:

1. See the following to determine the size of the bucket:

   - Scan Service storage bucket sizing
2. See your Amazon AWS documentation for information on creating a storage bucket
   and/or a cache bucket. For example, see:

   - <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-one-zone.html>

   Important:

   Do NOT set a retention policy or lifecycle policy for the storage-service
   bucket. Setting either policy might cause the idir and tools files to be
   deleted from the bucket as per the policy. You would then lose this
   data.
3. After you create the S3 Express storage bucket and/or cache bucket, create either an
   AWS storage bucket IAM policy for each bucket, or a storage service secret.
   - For AWS S3 Express storage bucket IAM policy: AWS: Create S3 Express bucket IAM policies
   - For storage service secret: Create an AWS storage service secret.
4. Configure `s3Express` Helm keys for the storage bucket and cache
   bucket as described in: .

   - Configure AWS S3 Express Helm keys
