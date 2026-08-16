---
title: "Configure Storage Service access to the storage blob"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configure-storage-service-access-to-the-storage-blob.html"
content_id: "uxlI5J4bdEhWch7sT4QHxw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:46.669708+00:00"
---

# Configure Storage Service access to the storage blob

In addition to creating a storage blob, you need to configure Scan Service access the
storage blob.

Note: This procedure assumes that you have created an Azure blob
storage container as described in Create an Azure blob storage container.

For secure access between the Storage Service and the Azure storage blob, you need to set
up either:

- Azure shared key secret as described in Using an Azure shared key client secret for RBAC.
- Azure Entra ID (formerly known as Azure Active Directory, Azure AD, or AAD)
  client secret as described in Using an Azure Entra ID client secret for RBAC.

Important: We do not recommended using a shared key secret
for storage blob access. We recommend that you use an Azure AD client secret because it
is much more secure.

Important: Azure Entra ID is formerly known as Azure
Active Directory, Azure AD or AAD.

For information on these Azure configurations, see:

- For information on shared key for blob, see the Microsoft document [Authorize with Shared Key](https://learn.microsoft.com/en-us/rest/api/storageservices/authorize-with-shared-key?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json).
- For an overview of Azure Entra ID client secret management, see [An Overview of Client Secret Management in
  Azure AD](https://o365reports.com/2023/07/20/an-overview-of-client-secret-management-in-azure-ad/#:~:text=%E2%80%93%20Stephane%20Nappo-,What%20is%20Client%20Secret%20in%20Azure%20AD%3F,tokens%20for%20Azure%20app%20access.) .

The following sections outline setting up either a shared key secret or an Azure Entra ID
client secret for blob access control.
