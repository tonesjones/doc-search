---
title: "Microsoft Azure PostgreSQL database extensions fail"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/microsoft-azure-postgresql-database-extensions-fail.html"
content_id: "MxR8sA4eKG4i8xfe4FpOig"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:42.769677+00:00"
---

# Microsoft Azure PostgreSQL database extensions fail

If the Microsoft Azure PostgreSQL database environment has been recently migrated
from Single Server to Flexible Server, or if the Flexible Server was newly
provisioned, extensions that previously worked will now fail until explicitly
allowed.

Note: See also Azure command line considerations.

You can fix this issue using either the Azure portal or the Azure CLI.

**To fix the issue using the Azure portal**:

1. In Azure Portal, go to Flexible Server > Server parameters.
2. Search for `azure.extensions`.
3. Add `btree_gist` to the comma-separated list of server
   extensions.
4. Click Save.

**To fix the issue using the Azure CLI**, use the following command to add the
`btree_gist` extension, specifying the resource group and the
PostgreSQL server name:

```
az postgres flexible-server parameter set \
  --resource-group <rg> \
  --server-name <server> \
  --name azure.extensions \
  --value btree_gist
```
