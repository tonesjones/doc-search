---
title: "AWS keys for Cache Service"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/aws-keys-for-cache-service.html"
content_id: "I3JI~Sv1YmYExlqHGvmrnw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:54.436236+00:00"
---

# AWS keys for Cache Service

If the `cache-service.​storageProvider` is `aws`, set the
`cache-service.aws:` Helm keys as needed. These keys include the
following:

```
cache-service:
  aws:
    region: ""
    secret: ""
    serviceAccount: ""
    s3Express:
      enabled: false
      ttlDays: 90
```

where:

- `region: ""` - Enter the Amazon S3 Express bucket region. S3
  Express storage is available in the following regions:

  - ap-northeast-1
  - eu-north-1
  - us-east-1
  - us-west-2
- `secret: ""` - Enter the secret that contains the keys aws_secret_key
  and aws_access_key. See Create an AWS storage service secret.
- `serviceAccount: ""` - Enter the name of the AWS service account IAM
  policy (IRSA) used to access the AWS S3 Express storage bucket and cache bucket. See
  AWS: Create S3 Express bucket IAM policies. AWS credentials
  (aws_secret_key and aws_access_key) provided in the service account secret will not
  be used.

The s3Express keys are for S3 Express bucket only. For information on setting the S3
Express Helm keys, see: Configure AWS S3 Express Helm keys.

For reference information on these keys, see cache-service.aws Helm keys.
