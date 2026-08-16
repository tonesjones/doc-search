---
title: "Create a lifecycle rule for the cache container"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-lifecycle-rule-for-the-cache-container.html"
content_id: "hHq1s_Xm3P3zB7Sbdx8IBA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:49.259340+00:00"
---

# Create a lifecycle rule for the cache container

1. Create a lifecycle rule for the cache container. For example:

   ```
       read -r -d '' policy <<EOF
   {
     "rules": [
       {
         "enabled": true,
         "name": "cnc-lifecycle-rule",
         "type": "Lifecycle",
         "definition": {
           "actions": {
             "version": {
               "delete": {
                 "daysAfterCreationGreaterThan": $CNC_LIFECYCLE_DELETE_DAYS
               }
             },
             "baseBlob": {
               "delete": {
                 "daysAfterModificationGreaterThan": $CNC_LIFECYCLE_DELETE_DAYS
               }
             }
           },
           "filters": {
             "blobTypes": [
               "blockBlob"
             ],
   	      "prefixMatch": [
   			"${CNC_CACHE_CONTAINER}"
   	      ]
           }
         }
       }
     ]
   }
   EOF
   ```
2. Create the data policy rules for the storage account. For example:

   ```
   az storage account management-policy create 
       --account-name $STORAGE_ACCOUNT_NAME 
       --policy "$policy" 
       --resource-group $RESOURCE_GROUP
   ```
