---
title: "Configure Helm keys to support GCP using GCS"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configure-helm-keys-to-support-gcp-using-gcs.html"
content_id: "hvnUfwtiJtpuaQC1_TtZEg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:36.310518+00:00"
---

# Configure Helm keys to support GCP using GCS

If you are configuring Google Cloud Storage (GCS) on the Google Cloud Platform (GCP), you
must set the following keys.

Important: Unless otherwise noted, the Helm keys in this
section are in the `scan-services` subchart.

Important:

When overriding any `scan-services` Helm subchart key from outside the
`scan-services` subchart `values.yaml` file, you
must precede the key name with `scan-services` to identify the key as
a `scan-services` chart key:

```
scan-services:
  cache-service:
    #overrides
  scan-service:
    #overrides
  storage-service:
    #overrides
```

For information on subcharts and overrides, see scan-services Helm subchart and [Subcharts and Global Values](https://helm.sh/docs/chart_template_guide/subcharts_and_globals/).

1. In the `cnc` Helm chart, change the
   `scan-services.enabled:` Helm key to `true` to
   enable the `scan-services` Helm chart and feature.

   ```
   scan-services:
     enabled: "true"
   ```
2. Select the storage provider, for this instance, GCP:

   ```
   cache-service:
     storageProvider: "gcp"
   ```

   Note: Valid platform providers include: `"aws" |
   "azure" | "gcp" | "minio"`
3. Select the storage service. For GCP, the storage bucket type is
   `gcs`:

   ```
   storage-service:
     storageType: "gcs"
   ```

   Note: Valid storage types
   include: `"s3" | "s3Express" |"azure" | "gcs"`
4. Enter the name of the GCS storage bucket used by the cache service. For example,
   "cncGCSBucket".

   ```
   cache-service:
     bucketName: "cncGCSBucket"
   ```
5. Verify that the cache service is enabled. For cache service to be enabled, the
   following key must be `true`. This causes capture and analysis output
   to be cached:

   ```
   cache-service:
     enabled: true
   ```
6. If you are using GCP storage, you must set the following properties:

   ```
   cache-service:
     gcp:
       project: ""
       secret: ""
   ```

   - The name of the GCP project.
   - The name of the GCP credential secret. The name of the key within this
     secret must be `key.json`.
7. The following keys identify credentials used to access storage when on GCP. These
   keys are required with GCP. Do not use them with any other platform. Configure
   the following GCS access credentials:

   The following example from the `scan-services` chart sets up a
   single GCS bucket named GCSBucket1:

   ```
   storage-service:
     gcs:
       bucket: "GCSBucket1"
       secret:
         key: "<gcs_secret_key>"
         name: "<gcs_secret_name>"
     storageType: "gcs"
     version: "2026.6.0"
   ```

   - `bucket` is the name of the GCS storage bucket.
   - `secret.key` is the name of the GCS key inside the
     secret.
   - `secret.name` is the name of the secret that contains the GCS
     service account.
   - `storageType` and `version` are from steps
     above.
