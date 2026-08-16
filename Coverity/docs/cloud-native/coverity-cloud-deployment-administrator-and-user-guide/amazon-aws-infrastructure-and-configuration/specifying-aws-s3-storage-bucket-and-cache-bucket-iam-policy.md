---
title: "Specifying AWS S3 storage bucket and cache bucket IAM policy"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/specifying-aws-s3-storage-bucket-and-cache-bucket-iam-policy.html"
content_id: "O6dLhY4WsRjjgb045IK~jg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:16.075975+00:00"
---

# Specifying AWS S3 storage bucket and cache bucket IAM policy

Note: If you are using S3 Express, skip this section and see AWS: Create S3 Express bucket IAM policies.

If you will be installing Scan Service in the cluster, create the IAM role and
permissions that allow the Storage Service to access the storage bucket and cache bucket.

In AWS, the required action for the IAM storage bucket user or role is
`s3:GetBucketCORS` and `s3:PutBucketCORS`. Refer to Amazon
CORS (Cross-Origin-Resource Sharing) and IAM (Identity and Access Management)
documentation.

For example:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action" : [
        "s3:GetBucketCORS",
        "s3:PutBucketCORS",
        "s3:ListBucket"
    ],
      "Resource": ["arn:aws:s3:::${STORAGE_BUCKET_NAME}"]
    },
    {
      "Effect": "Allow",
      "Action" : [
        "s3:GetLifecycleConfiguration",
        "s3:PutLifecycleConfiguration",
        "s3:ListBucket"
    ],
      "Resource": ["arn:aws:s3:::${CACHE_BUCKET_NAME}"]
    },    
    {
      "Sid": "VisualEditor1",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:AbortMultipartUpload",
        "s3:DeleteObject",
        "s3:ListMultipartUploadParts"
        ],
      "Resource": [
        "arn:aws:s3:::${STORAGE_BUCKET_NAME}/*",
        "arn:aws:s3:::${CACHE_BUCKET_NAME}/*"
        ]
    }
  ]
}
```
