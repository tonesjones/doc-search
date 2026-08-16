---
title: "Configuring Helm keys to support AWS using S3 or S3 Express"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-helm-keys-to-support-aws-using-s3-or-s3-express.html"
content_id: "ADzB_LQzVSVwdwTX50xA2g"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:19.349190+00:00"
---

# Configuring Helm keys to support AWS using S3 or S3 Express

If you are configuring S3 or S3Express storage on Amazon Web Services (AWS), you must set the
following Helm keys.

Also refer to the following:

- For `scan-services` subchart Helm key descriptions and default values, see
  scan-services Helm subchart: Helm keys.
- For AWS-specific infrastructure setup procedures, see Amazon AWS infrastructure and configuration.

Important: Unless otherwise noted, the Helm keys in this
section are in the `scan-services` subchart.

Important:

When overriding any `scan-services` Helm subchart key from outside the
`scan-services` subchart `values.yaml` file, you must
precede the key name with `scan-services` to identify the key as a
`scan-services` chart key:

```
scan-services:
  cache-service:
    #overrides
  scan-service:
    #overrides
  storage-service:
    #overrides
```

For information on subcharts and overrides, see scan-services Helm subchart
and [Subcharts and Global Values](https://helm.sh/docs/chart_template_guide/subcharts_and_globals/).

Note: Refer to this section as you create scan service components in order
to define the service account and storage resources for the Coverity cluster and allow access
to the resources.

Note: Some of the following examples use sample values for this
configuration.

1. In the `cnc` Helm chart, change the
   `scan-services.enabled:` Helm key to `true` to enable the
   `scan-services` Helm chart and feature.

   ```
   scan-services:
     enabled: "true"
   ```
2. In the `scan-services` subchart, Select the storage provider, for this
   instance, AWS:

   ```
   cache-service:
     storageProvider: "aws"
   ```

   Note: Valid platform providers include: `"aws" | "azure" |
   "gcp" | "minio"`
3. Select the storage type, for this instance, "s3" or
   "s3Express":

   ```
   storage-service:
     storageType: "s3"
   ```

   Note: Valid storage types include:
   `"s3" | "s3Express" | "azure" | "gcs"`
4. Enter the name of the AWS storage bucket used by the cache service. For example,
   "cncAWSBucket".

   ```
   cache-service:
     bucketName: "cncAWSBucket"
   ```
5. Verify that the cache service is enabled. For cache service to be enabled, the following
   key must be `true`. This causes capture and analysis output to be
   cached:

   ```
   cache-service:
     enabled: true
   ```
6. If you created S3 storage, configure the following Helm keys: (Bucket keys & Storage
   Access Keys)

   Important: For detailed information on configuring Helm
   keys for S3, see Configure AWS S3 Helm keys.

   1. For S3, you must configure the following `cache-service` keys:

      ```
      cache-service:
        aws:
          region: ""
          secret: ""
          serviceAccount: ""
      ```

      - The region of the S3 bucket.
      - The name of the secret that contains the keys: aws_access_key and
        aws_secret_key.
      - `serviceAccount:` The name of the AWS instance profile service
        account that contains IAM roles (IRSA) that enable EC2 instances to access AWS
        services. If you provide a serviceAccount value, the IRSA will be used and any AWS
        credentials (aws_secret_key and aws_access_key) provided in the secret will be
        ignored.
   2. For S3, you must configure the following `storage-service` keys that
      provide credentials used to access storage. Do not configure them for any other
      storage type.

      ```
      storage-service:
        s3:
          bucket: ""
          region: ""
          secret:
            name: ""
          serviceAccount: ""
      ```

      - `bucket:`The S3Express bucket name.
      - `region:`The S3Express bucket region.
      - `secret.name:`The name of the secret that contains the keys:
        aws_access_key and aws_secret_key.
      - `serviceAccount:` The name of the AWS instance profile service
        account that contains IAM roles (IRSA) that enable EC2 instances to access AWS
        services. If you provide a serviceAccount value, the IRSA will be used and any AWS
        credentials (aws_secret_key and aws_access_key) provided in the secret will be
        ignored.

   See also Configure AWS S3 Helm keys.
7. If you created S3Express storage, configure the following Helm keys: (Bucket keys,
   Express Enable keys, & Storage Access Keys)

   Important: For detailed information on configuring Helm
   keys for S3Express, see Configure AWS S3 Express Helm keys.

   1. Complete the following `cache-service` keys:

      ```
      cache-service:
        aws:
          region: ""
          secret: ""
          serviceAccount: ""
      ```

      - `region:`The region of the S3 bucket.
      - `secret:`The name of the secret that contains the keys:
        aws_access_key and aws_secret_key.
      - `serviceAccount:` The name of the AWS instance profile service
        account that contains IAM roles (IRSA) that enable EC2 instances to access AWS
        services. If you provide a serviceAccount value, the IRSA will be used and any AWS
        credentials (aws_secret_key and aws_access_key) provided in the secret will be
        ignored.
   2. For S3Express, setv the following `cache-service` keys:

      ```
      cache-service:
        aws:
          s3Express:
            enabled: false
            ttlDays: 90
      ```

      - `s3Express.enabled:` If the S3Express (Directory) bucket is
        configured, change `enabled:` to `true`. If the S3
        general purpose bucket is configured, do not enable S3Express.
      - `ttlDays:` indicates the number of days to keep cached objects. The
        cache service deletes old or expired objects from the bucket after this life is
        reached.
   3. For S3Express, set the following `storage-service` keys.

      ```
      storage-service:
        s3Express:
          bucket: ""
          region: ""
          secret:
            name: ""
          serviceAccount: ""
      ```

      - `bucket:` The S3Express bucket name.
      - `region:` The S3Express bucket region.
      - `secret.name:` The name of the secret that contains the keys:
        aws_access_key and aws_secret_key.
      - `serviceAccount:` The name of the AWS instance profile service
        account that contains IAM roles (IRSA) that enable EC2 instances to access AWS
        services. If you provide a serviceAccount value, the IRSA will be used and any AWS
        credentials (aws_secret_key and aws_access_key) provided in the secret will be
        ignored.
