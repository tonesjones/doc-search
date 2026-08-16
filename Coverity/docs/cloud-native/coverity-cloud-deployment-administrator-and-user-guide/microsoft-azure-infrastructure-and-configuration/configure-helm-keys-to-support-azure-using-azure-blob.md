---
title: "Configure Helm keys to support Azure using Azure blob"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configure-helm-keys-to-support-azure-using-azure-blob.html"
content_id: "N7pd3umJvJAuu13qV48Rzw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:51.239270+00:00"
---

# Configure Helm keys to support Azure using Azure blob

If you are configuring Azure blob storage on the Azure platform, you must set the following
keys.

Important: Unless otherwise noted, the Helm keys in this
section are in the `scan-services` subchart.

Important:

When overriding any `scan-services` Helm subchart key from outside the
`scan-services` subchart `values.yaml` file, you must
precede the key name with `scan-services` to identify the key as a
`scan-services` chart key.

```
scan-services:
  cache-service:
    #overrides
  scan-service:
    #overrides
  storage-service:
    #overrides
```

For example, to enable the cache service from a command line or script, the syntax for the
Helm key:

```
cache-service.enabled: true
```

must be:

```
scan-services.cache-service.enabled: true
```

Alternatively, within a yaml file other than the subchart's `values.yaml`
file, the syntax is:

```
scan-services:
  cache-service:
    enabled: true
```

For further information on subcharts, see scan-services Helm subchart and
[Subcharts and Global Values](https://helm.sh/docs/chart_template_guide/subcharts_and_globals/).

1. In the `cnc` Helm chart, change the
   `scan-services.enabled:` Helm key to `true` to enable the
   `scan-services` Helm chart and feature.

   ```
   scan-services:
     enabled: "true"
   ```
2. Select the storage provider, for this instance, azure:

   ```
   cache-service:
     storageProvider: "azure"
   ```

   Note: Valid platform providers include: `"aws" | "azure" |
   "gcp" | "minio"`
3. Select the storage service, for this instance,
   azure:

   ```
   storage-service:
     storageType: "azure"
   ```

   Note: Valid storage types include:
   `"s3" | "s3Express" |"azure" | "gcs"`
4. Enter the name of the Azure storage blob used by the cache service. For example,
   "cncAzureBlob".

   ```
   cache-service:
     bucketName: "cncAzureBlob"
   ```
5. Verify that the cache service is enabled. For cache service to be enabled, the following
   key must be `true`. This causes capture and analysis output to be
   cached:

   ```
   cache-service:
     enabled: true
   ```
6. Enter the name of the secret that contains the Azure access credentials. These
   credentials are azure_endpoint, azure_tenant_id, azure_client_id, azure_client_secret,
   azure_subscription_id, azure_resource_group.

   ```
   cache-service:
     azure:
       secret: ""
   ```
7. Enter the following azure access credentials. They are required to access scan services
   storage in the Azure platform. These credentials are required for a deployment on Azure.
   Do not use them for any other platform.

   - For the `container:` key, enter the name of the blob storage
     container. This is required when using Azure storage,
   - The `storageAccountName:` key is required with both sharedKey and
     aadClientSecret authentication modes.
   - In the `secret.name:` key, enter the name of the secret that contains
     either the sharedKey or aadClientSecret keys.

     Note: The secret is either:

     - The sharedKey secret which must contain the `azure_account_key` for
       authentication.
     - The aadClientSecret secretwhich must contain the following keys: azure_endpoint,
       azure_tenant_id, azure_client_id, azure_client_secret. The client secret for the
       Azure application.
   - For authMode:, enter the authentication mode, either "sharedKey" or
     "aadClientSecret".

   ```
   storage-service:
     azure:
       container: ""
       storageAccountName: ""
       secret:
         name: ""
       authMode: "sharedKey"
   ```
