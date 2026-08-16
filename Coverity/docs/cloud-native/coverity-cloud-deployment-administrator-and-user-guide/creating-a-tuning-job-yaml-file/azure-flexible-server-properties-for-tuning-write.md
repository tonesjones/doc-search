---
title: "Azure Flexible Server properties for tuning-write"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/azure-flexible-server-properties-for-tuning-write.html"
content_id: "NOwkugn5sHNlxy0dRZlsHA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:19.351100+00:00"
---

# Azure Flexible Server properties for tuning-write

If the PostgreSQL database is on Azure Flexible Server and if you are performing a
tuning-write, set `<POSTGRES-DISTRO>`, authentication, and
authorization as follows.

## POSTGRES-DISTRO

If the PostgreSQL database is on Azure Flexible Server, in the tuning yaml file, set
`<POSTGRES-DISTRO>` to `flexibleserver`.

## Authentication

Provide the following Azure environment variables:

- AZURE_SUBSCRIPTION_ID: Subscription ID.
- AZURE_TENANT_ID,: Tenant ID.
- AZURE_CLIENT_ID: Client ID.
- AZURE_CLIENT_SECRET: Client secret using.
- AZURE_RESOURCE_GROUP: Resource group.

## Authorization

Set the following required permissions for Microsoft Azure PostgreSQL Flexible Server
to proceed with the tuning write process.

Note: This authorization is not required with
tuning-suggest.

| Action | Required permission |
| --- | --- |
| Modify the database flexible server. | `Microsoft.DBforPostgreSQL/flexibleServers/configurations/read` |
| Update the server configuration. | `Microsoft.DBforPostgreSQL/flexibleServers/configurations/write` |
