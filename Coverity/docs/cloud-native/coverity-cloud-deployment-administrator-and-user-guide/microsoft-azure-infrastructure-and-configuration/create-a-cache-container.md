---
title: "Create a cache container"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-cache-container.html"
content_id: "zJNQtMhq85yta15QxYqkvA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:48.615499+00:00"
---

# Create a cache container

Create a cache container in Microsoft Azure. Refer to:

- For requirements when creating a cache storage container, see: Create and configure a cache storage bucket
- For a cache overview, see <https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-overview>
- For Azure cache container info, see <https://learn.microsoft.com/en-us/cli/azure/storage/container?view=azure-cli-latest>

For example:

```
az storage container create --name "${CNC_CACHE_CONTAINER}" \
    --account-key "$AZURE_CONTAINER_ACCESS_KEY" \
    --account-name $CNC_STORAGE_ACCOUNT_NAME \
    --fail-on-exist \
    --public-access off \
    --resource-group "${CNC_RESOURCE_GROUP}"
```
