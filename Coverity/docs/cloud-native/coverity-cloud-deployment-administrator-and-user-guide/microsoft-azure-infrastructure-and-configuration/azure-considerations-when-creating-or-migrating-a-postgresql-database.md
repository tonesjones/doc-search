---
title: "Azure considerations when creating or migrating a PostgreSQL database"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/azure-considerations-when-creating-or-migrating-a-postgresql-database.html"
content_id: "fJ~CrPrClz4S0R8Hz2YtaQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:42.800294+00:00"
---

# Azure considerations when creating or migrating a PostgreSQL database

This section outlines considerations when creating or migrating a PostgreSQL database in
Microsoft Azure. It contains the following subsections:

- Azure command line considerations
- PostgreSQL SSL considerations

## Azure command line considerations

This section outlines a few Azure commands that are important when you define the
PostgreSQL database. Refer to Microsoft Azure documentation for further
information.

Specify an administrator username and password:

```
az postgres flexible-server create 
  --resource-group "${RESOURCE_GROUP_NAME}" 
  --name "${PSQLSERVER_NAME}" 
  --admin-user <psqladmin> 
  --admin-password <myPassword> 
  --sku-name Standard_D2ds_v4 
  --tier GeneralPurpose 
  --yes
```

Create firewall rules:

```
az postgres flexible-server firewall-rule create 
  --resource-group "${RESOURCE_GROUP_NAME}" 
  --name "${PSQLSERVER_NAME}" 
  --start-ip-address 0.0.0.0
```

Set server properties:

```
az postgres flexible-server parameter set 
  --resource-group "${RESOURCE_GROUP_NAME}" 
  --server-name "${PSQLSERVER_NAME}" 
  --name require_secure_transport --value off
```

Enable the Azure `uuid-ossp` extension in server properties:

```
az postgres flexible-server parameter set 
  --resource-group "${RESOURCE_GROUP_NAME}" 
  --server-name "${PSQLSERVER_NAME}" 
  --name azure.extensions --value UUID-OSSP
```

Important:

If the Microsoft Azure PostgreSQL database environment has been recently
migrated from Single Server to Flexible Server, or if the Flexible
Server was newly provisioned, extensions that previously worked will now
fail until explicitly allowed.

Note: See also Microsoft Azure PostgreSQL database extensions fail.

You can fix this issue using either the Azure portal or the Azure
CLI.

**To fix the issue using the Azure portal**:

1. In Azure Portal, go to Flexible Server > Server parameters.
2. Search for `azure.extensions`.
3. Add `btree_gist` to the comma-separated list of
   server extensions.
4. Click Save.

**To fix the issue using the Azure CLI**, use the following command to
add the `btree_gist` extension, specifying the resource
group and the PostgreSQL server name:

```
az postgres flexible-server parameter set \
  --resource-group <rg> \
  --server-name <server> \
  --name azure.extensions \
  --value btree_gist
```

## Azure PostgreSQL SSL considerations

Get SSL certificates for the Azure PostgreSQL instance. For information on Azure
PostgreSQL SSL, refer to <https://docs.microsoft.com/en-us/azure/postgresql/flexible-server/how-to-connect-tls-ssl>.

You can allow non SSL connections.

Optionally, you can force your server to accept only SSL connections as follows:

1. Create a secret for the PostgreSQL server certificate.
2. Set the `cim.postgres.sslmode` Helm key override as described in
   Select the PostgreSQL sslmode and find the PostgreSQL root certificate for TLS.
