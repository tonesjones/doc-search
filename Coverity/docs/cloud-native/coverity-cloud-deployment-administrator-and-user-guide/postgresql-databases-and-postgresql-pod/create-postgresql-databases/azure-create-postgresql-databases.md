---
title: "Azure: Create PostgreSQL databases"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/azure-create-postgresql-databases.html"
content_id: "CbT495CyOIKt9u8gTtTemA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:59.102498+00:00"
---

# Azure: Create PostgreSQL databases

The following guidance uses the Azure portal to create PostgreSQL databases.

Important: Keep all database names handy; you will need
them when you configure the Helm keys.

## Azure: creating the primary PostgreSQL database

Create the PostgreSQL primary database instance as described in the Azure
documentation: [Quickstart: Create an instance of Azure Database
for PostgreSQL - Flexible Server](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/quickstart-create-server?tabs=portal-create-flexible%2Cportal-get-connection%2Cportal-delete-resources).

## Azure: creating read-only replica PostgreSQL databases

Optionally, if you are deploying read-only replica PostgreSQL databases:

1. Create one or more PostgreSQL read replica database instance(s) of the
   primary database instance as described in the Azure documentation: [Create and manage read replicas in Azure
   Database for PostgreSQL](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/how-to-read-replicas-portal?tabs=portal)

   Note: Keep the replica database names handy. You will use
   them to set the `cim.pgpool` Helm keys.
2. Continue with confguring the read-only replica PostgreSQL databases as described
   in Using PostgreSQL read replicas and Pgpool to balance database loads.
