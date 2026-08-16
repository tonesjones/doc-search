---
title: "Create a storage account (SA)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-storage-account-sa-.html"
content_id: "bslmK3UccF1uzGSNNWOLjA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:44.737129+00:00"
---

# Create a storage account (SA)

Create a storage account:

1. Create the storage account. For example:

   ```
   az storage account create -n $CNC_STORAGE_ACCOUNT_NAME \
       -g "${CNC_RESOURCE_GROUP}" \
       -l "${CNC_LOCATION}" \
       --sku "$CNC_STORAGE_ACCOUNT_SKU" \
       --allow-shared-key-access true
   ```
2. Before attaching a secret storage key to a storage container, get the secret
   storage key using the following command:

   ```
   AZURE_BLOB_ACCESS_KEY=$(az storage account keys list -g \
       "${CNC_RESOURCE_GROUP}" \
       -n $CNC_STORAGE_ACCOUNT_NAME \
       --query [0].value -o tsv)
       export AZURE_BLOB_ACCESS_KEY
   ```

   Note: You will need the access key for the next step when you
   create the storage blob container.
