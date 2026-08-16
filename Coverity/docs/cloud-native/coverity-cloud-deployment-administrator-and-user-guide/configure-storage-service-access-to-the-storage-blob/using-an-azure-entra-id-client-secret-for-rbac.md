---
title: "Using an Azure Entra ID client secret for RBAC"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-an-azure-entra-id-client-secret-for-rbac.html"
content_id: "m7OlbrzM_gnakV3AXJyBqQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:47.969996+00:00"
---

# Using an Azure Entra ID client secret for RBAC

When the storage service requests access to the storage blob which is protected by Entra
ID, the client secret is used to authenticate the storage service application. Using the
Azure `az` CLI, create the Azure Entra ID (formerly Azure AD) client
secret. The secret must include the following:

- `azure_endpoint: <URL>` where <URL> is either:
  - Storage service storage account blob URL:
    `https://<storageAccount>.blob.core.windows.net`
  - A custom domain URL: `https://<customDomain>`

    Important: If you are using a custom domain,
    see also Storage service custom domains.
- `azure_tenant_id: <your-tenant-id>`
- `azure_client_id: <your-client-id>`
- `azure_client_secret: <your-client-secret>`

The following example uses the Azure `az` CLI to create an Azure Entra ID
client secret

```
az ad sp create-for-rbac
  --role="Contributor"
  --scopes="/subscriptions/00000000-0000-0000-0000-000000000000" 

export STORAGE_ACCOUNT=<storageAccountName> 
export USER_ASSIGNED_CLIENT_ID=<output-from-above-command> 
export RESOURCE_GROUP=<resourceGroupName> 
export SUBSCRIPTION=00000000-0000-0000-0000-000000000000 

az role assignment create \
  --role "Storage Blob Data Owner" \
  --assignee "${USER_ASSIGNED_CLIENT_ID}" \
  --scope "/subscriptions/${SUBSCRIPTION}/resourceGroups/${RESOURCE_GROUP}/providers/Microsoft.Storage/storageAccounts/${STORAGE_ACCOUNT}"
            
az role assignment create \
  --role "Storage Account Contributor" \
  --assignee "${USER_ASSIGNED_CLIENT_ID}" \
  --scope "/subscriptions/${SUBSCRIPTION}/resourceGroups/${RESOURCE_GROUP}/providers/Microsoft.Storage/storageAccounts/${STORAGE_ACCOUNT}"
```

Create the Azure Entra ID client secret using either the storage service storage account
URL or a custom domain URL:

```
azure_endpoint: <URL>
azure_tenant_id: <your-tenant-id>
azure_client_id: <your-client-id>
azure_client_secret: <your-client-secret>
```

For further information, see:

- For `az ad sp create-for-rbac`, see [az ad sp create-for-rbac](https://learn.microsoft.com/en-us/cli/azure/ad/sp?view=azure-cli-latest#az-ad-sp-create-for-rbac) .
- For `az role assignment create`, see [az role assignment create](https://learn.microsoft.com/en-us/cli/azure/role/assignment?view=azure-cli-latest#az-role-assignment-create).

Configure the storage-service.azure Helm keys to deploy the Azure Entra ID client secret.
For example:

```
storage-service:
  azure:
    storageAccountName: "my-sa"
    container: "my-container"
    authMode: "aadClientSecret"
    secret:
      name: "azure-aad-secret"
```

For further Helm key information, see storage-service.azure Helm keys.
