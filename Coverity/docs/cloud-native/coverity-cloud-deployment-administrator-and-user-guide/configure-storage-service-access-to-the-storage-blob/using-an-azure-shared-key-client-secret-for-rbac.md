---
title: "Using an Azure shared key client secret for RBAC"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-an-azure-shared-key-client-secret-for-rbac.html"
content_id: "VKrjUHbyEhZw57N8qkTNqQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:47.327015+00:00"
---

# Using an Azure shared key client secret for RBAC

Important: We do not recommended using a shared key secret
for storage blob access. We recommend that you use an Azure Entra ID client secret
because it is much more secure.

This section outlines how to set up a Microsoft Azure shared key secret for secure blob
access by the Storage Account.

- For information on shared key for blob, see the Microsoft document [Authorize with Shared Key](https://learn.microsoft.com/en-us/rest/api/storageservices/authorize-with-shared-key?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json).

To set up a shared key secret:

1. Create the Azure sharedKey secret. The shared key secret must include the name of
   the Azure storage account key:

   `azure_account_key:
   <your-azure-storage-account-key>`

   To find (view) your storage
   account access key, see [Manage storage account access
   keys](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json&tabs=azure-portal).
2. Enter the name of the shared key secret in the Helm chart. For example:

   ```
   storage-service:
     azure:
       container: "my-container" 
       storageAccountName: "mystorageaccount" 
       authMode: "sharedKey" 
       secret: 
         name: "azure-sharedkey-secret"
   ```

   This Helm example defines the authMode as sharedKey and specifies the secret name
   azure-sharedkey-secret.

   For further Helm key information, see storage-service.azure Helm keys.
