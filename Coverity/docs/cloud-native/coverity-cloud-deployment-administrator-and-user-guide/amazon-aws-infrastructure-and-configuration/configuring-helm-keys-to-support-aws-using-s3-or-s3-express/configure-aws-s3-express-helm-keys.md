---
title: "Configure AWS S3 Express Helm keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configure-aws-s3-express-helm-keys.html"
content_id: "1ZPuGvSVIF3uNvvaXRBaUA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:20.659297+00:00"
---

# Configure AWS S3 Express Helm keys

Note: If you are using S3 (not S3 Express), skip this section and see
Configure AWS S3 Helm keys.

Note: With an AWS S3 Express storage bucket configured, you can NOT
upload a `coverity-all-platforms-<version>.tar.gz` file from
the Connect UI. See Uploading Coverity Tools artifacts to the Connect UI.

This procedure assumes that you have created the AWS S3 Express buckets and either IAM
policies or secrets:

- To create AWS S3 Express buckets, see AWS: Create an S3 Express bucket and your Amazon AWS
  documentation.

  Note: For bucket and region naming, see <https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html>.
- To create an AWS S3 Express bucket IAM policies, see AWS: Create S3 Express bucket IAM policies.
- To create a storage service secret, see Create an AWS storage service secret.

Configure the Helm keys for AWS S3 Express as follows:

1. In the `scan-services` Helm subchart, enable S3 Express, set the
   value `"s3Express"` in the following storage type Helm key:

   ```
   storage-service.storageType: "s3Express"
   ```
2. In the `scan-services` Helm subchart, configure the following
   storage service Helm keys. For the storage service keys, use the values you set
   when you created the storage bucket and the AWS storage service secret.

   Note: Configure the following Helm keys only if you have
   created an AWS S3 Express storage bucket and configured the
   `storage-service.storageType: "s3Express"` Helm key. Do NOT
   use them for either AWS S3 or other storage platforms.

   Configure the following S3 Express Helm keys for storage service:

   ```
   storage-service:
     s3Express:
       bucket: ""
       region: ""
       secret:
         name: ""
       serviceAccount: ""
   ```

   where:

   - `bucket: ""` - Enter the unique name of the Amazon S3 Express
     storage bucket.
   - `region: ""` - Enter the Amazon S3 Express bucket region.
     S3 Express storage is available in the following regions:

     - ap-northeast-1
     - eu-north-1
     - us-east-1
     - us-west-2
   - `secret.name: ""` - Enter the secret that contains the keys
     aws_secret_key and aws_access_key. See Create an AWS storage service secret.
   - `serviceAccount: ""` - Enter the name of the AWS service
     account IAM policy (IRSA) used to access the AWS S3 Express storage bucket
     and cache bucket. See AWS: Create S3 Express bucket IAM policies.
     AWS credentials (aws_secret_key and aws_access_key) provided in the service
     account secret will not be used.

   For storage service Helm key descriptions, see the Helm key reference, storage-service.s3Express Helm keys.
3. Configure the following S3 Express Helm keys for the cache
   service:

   ```
   cache-service:
     aws:
       region: ""
       secret: ""
       serviceAccount: ""
       s3Express:
         enabled: false
         ttlDays: ""
   ```

   where:

   - `region: ""` - Enter the Amazon S3 Express bucket region.
     S3 Express storage is available in the following regions:

     - ap-northeast-1
     - eu-north-1
     - us-east-1
     - us-west-2
   - `secret: ""` - Enter the secret that contains the keys
     aws_secret_key and aws_access_key. See Create an AWS storage service secret.
   - `serviceAccount: ""` - Enter the name of the AWS service
     account IAM policy (IRSA) used to access the AWS S3 Express storage bucket
     and cache bucket. See AWS: Create S3 Express bucket IAM policies.
     AWS credentials (aws_secret_key and aws_access_key) provided in the service
     account secret will not be used.
   - `s3Express.enabled: false` - To enable S3 Express caching,
     change the value to `true`. This key must be set to
     `true` when S3Express is configured:
     `storage-service.storageType: "s3Express"`.
   - `s3Express.ttlDays: 90` - You can keep or change the cache
     time to live in days. This specifies the number of days to retain cached
     objects.

   For cache Helm key descriptions, see the Helm key reference, cache-service.aws Helm keys.
