---
title: "Configure AWS S3 Helm keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configure-aws-s3-helm-keys.html"
content_id: "kp2b9qWnDk4~T12IlkSZug"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:20.002237+00:00"
---

# Configure AWS S3 Helm keys

Note: If you are using S3 Express (not S3), skip this section and see
Configure AWS S3 Express Helm keys.

If you are deploying the Amazon AWS S3 storage bucket, set the following storage values
with the values you set when you created the storage bucket and the secret to access the
storage bucket:

If you are using an AWS S3 storage bucket, set up S3 as follows:

1. Create the AWS S3 storage bucket and either IAM policy or secret:
   - To create an AWS S3 storage bucket, see AWS: Create an S3 storage bucket and your Amazon AWS
     documentation.

     Note: For bucket and region naming, see <https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html>.
   - To create an AWS S3 storage bucket IAM policy, see Specifying AWS S3 storage bucket and cache bucket IAM policy.
   - To create a storage service secret, see Create an AWS storage service secret.
2. In the `scan-services` Helm subchart, enable S3, enter the value
   `"s3"` in the following storage type Helm key:

   ```
   storage-service.storageType: "s3"
   ```
3. In the `scan-services` Helm subchart, configure the following
   `storage-service:s3:` Helm keys. Use the values you set when
   you created the storage bucket and the AWS storage service secret.

   Note: Configure the following Helm keys only if you have
   created an AWS S3 storage bucket and configured the
   `storage-service.storageType: "s3"` Helm key. Do NOT use them
   for either AWS S3 Express or other storage platforms.

   Configure the following S3 Helm keys, for example, with sample entries:

   ```
   storage-service:
     s3:
       bucket: "my-bucket"
       region: "us-east-1"
       secret:
         name: "my-s3-secret"
       serviceAccount: "my-sa"
   ```

   where:

   - `bucket: ""` - Enter the unique name of the Amazon S3 storage
     bucket.
   - `region: ""` - Enter the Amazon S3 bucket region.
   - `secret.name: ""` - Enter the secret that contains the keys
     aws_secret_key and aws_access_key. See Create an AWS storage service secret.
   - `serviceAccount: ""` - Enter the name of the AWS service
     account IAM policy (IRSA) used to access the AWS S3 storage bucket and cache
     bucket. See Specifying AWS S3 storage bucket and cache bucket IAM policy. If you provide
     this key, AWS credentials (aws_secret_key and aws_access_key) provided in
     the service account secret will not be used.
4. In the `scan-services` Helm subchart, configure the following
   `cache-service:aws:` Helm keys. Use the values you set when
   you created the storage bucket and the AWS secret.

   ```
   cache-service:
     aws:
       region: ""
       secret: ""
       serviceAccount: ""
   ```

   where:

   - `region: ""` - Enter the Amazon S3 bucket region.
   - `secret: ""` - Enter the secret that contains the keys
     aws_secret_key and aws_access_key. See Create an AWS storage service secret.
   - `serviceAccount: ""` - Enter the name of the AWS service
     account IAM policy (IRSA) used to access the AWS S3 storage bucket and cache
     bucket. See Specifying AWS S3 storage bucket and cache bucket IAM policy. If you provide
     this key, AWS credentials (aws_secret_key and aws_access_key) provided in
     the service account secret will not be used.
