---
title: "Create an Azure blob storage container"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-an-azure-blob-storage-container.html"
content_id: "hwWjvvaFoPxwkDEtRmoAeQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:46.026690+00:00"
---

# Create an Azure blob storage container

Create a storage container. Refer to:

- To information about Azure storage blobs, see [Azure Blob Storage documentation](https://learn.microsoft.com/en-us/azure/storage/blobs/)
- For Coverity cloud storage blob sizing, see Scan Service storage bucket sizing
- For Azure storage commands, see [az storage container](https://learn.microsoft.com/en-us/cli/azure/storage/container?view=azure-cli-latest)

For example:

```
az storage container create --name "${CNC_CONTAINER}" \
    --account-key "$AZURE_BLOB_ACCESS_KEY" \
    --account-name $CNC_STORAGE_ACCOUNT_NAME \
    --fail-on-exist \
    --public-access off \
    --resource-group "${CNC_RESOURCE_GROUP}"
```

Important:

Do NOT set a retention policy or lifecycle policy for the storage-service bucket.
Setting either policy might cause the idir and tools files to be deleted from the
bucket as per the policy. You would then lose this data.

Next, for secure access between the Storage Service and the Azure storage blob, set up an
Azure access secret and Helm keys as outlined in Configure Storage Service access to the storage blob.
