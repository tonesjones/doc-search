---
title: "Using a role-based AWS service account for Storage Service and Cache Service"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-a-role-based-aws-service-account-for-storage-service-and-cache-service.html"
content_id: "sqqimAGx4FxvJ6HLtrdCpw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:16.733513+00:00"
---

# Using a role-based AWS service account for Storage Service and Cache Service

If you are deploying Scan Service in Amazon AWS, to provide Scan Services access keys for
both Storage Service and Cache Service, you can either:

- create a role-based AWS service account using IAM policy as described in this
  section, or
- create an AWS service account secret as described in Create an AWS storage service secret.

To create a Kubernetes role based service account (SA), in the AWS environment:

1. Create an IAM policy to access the storage bucket and cache bucket. For
   example:

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action" : [
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
2. Create a service account. For example:

   ```
   eksctl create iamserviceaccount  \
       --name <name_of_the_service_account>  \
       --namespace <namespace_in_which_chart_will_deploy>  \
       --cluster <cluster_name>  \
       --region <cluster_region>  \
       --role-name "<name_of_the_role_you_want_to_create>"  \
       --attach-policy-arn <arn of the existing policy>  \
       --approve
   ```

   Note:

   If you create the service account using this command, you do not need to
   manually configure (annotate) the service account.

   For additional `eksctl` information, refer to [create service account using eksctl](https://eksctl.io/usage/iamserviceaccounts/).

   For additional information on IAM and service accounts, refer to [aws reference 1](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) and [aws reference 2](https://aws.amazon.com/blogs/opensource/introducing-fine-grained-iam-roles-service-accounts/).
3. Override the following Helm keys with the service account name:

   - `cache-service.aws.serviceAccount` Refer to cache-service.aws Helm keys.
   - `storage-service.s3.serviceAccount` Refer to storage-service.s3 Helm keys.
4. Deploy the chart.

   Note:

   If you configure both a secret and a role-based service account, the
   role-based service account takes precedence over secret credentials.
