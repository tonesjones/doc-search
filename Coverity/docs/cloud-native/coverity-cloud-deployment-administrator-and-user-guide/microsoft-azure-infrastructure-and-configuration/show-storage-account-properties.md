---
title: "Show storage account properties"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/show-storage-account-properties.html"
content_id: "zjH0GfxwNfSCON2i5KPvmQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:45.381490+00:00"
---

# Show storage account properties

Using the `az storage account show` command, show storage account
properties to use for the secret. For example:

```
az storage account show \
    --name $STORAGE_ACCOUNT_NAME \
    --resource-group $RESOURCE_GROUP \
    --query primaryEndpoints.blob
```
