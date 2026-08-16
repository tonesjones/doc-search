---
title: "Create a storage bucket for Scan Service"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-storage-bucket-for-scan-service.html"
content_id: "kj0GdlosrWhbo1UNq9n0nw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:56.878236+00:00"
---

# Create a storage bucket for Scan Service

If you are deploying Scan Service in the cloud, before you deploy the Helm chart, you
must create a storage bucket in your infrastructure. Scan Service uses this storage
bucket to store scan outputs such as intermediate directories, error logs, debug logs,
etc.

For storage bucket sizing, see Scan Service storage bucket sizing.

Create a storage bucket as defined in the cloud provider documentation:

- For Amazon: [Amazon S3](https://aws.amazon.com/s3/)
- For Microsoft Azure: [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction#blob-storage-resources+)
- For Google GCS: [Google Cloud Storage](https://cloud.google.com/storage/docs/creating-buckets)
- For OpenShift: refer to the Red Hat OpenShift documentation to create an
  S3-compatible storage bucket.

Important:

Do NOT set a retention policy or lifecycle policy for the storage-service bucket.
Setting either policy might cause the idir and tools files to be deleted from the
bucket as per the policy. You would then lose this data.

When you create the storage bucket, retain the following information. You will need it
when you create Helm overrides and set up the Helm chart release.

- For Amazon S3: When you create the storage bucket, retain the s3 bucket name. When
  you create the S3 secret, retain the S3 secret key and S3 access key.
- For Microsoft Azure storage blob: When you create the storage bucket, retain the
  Azure container and storage account names. When you create the Azure secret, retain
  the Azure account key.
- For Google GCS: When you create the storage bucket, retain the GCS bucket name. When
  you create the GCS secret, retain the GCP Service account.
- For Red Hat OpenShift: When you create the storage bucket, retain the storage bucket
  name.
