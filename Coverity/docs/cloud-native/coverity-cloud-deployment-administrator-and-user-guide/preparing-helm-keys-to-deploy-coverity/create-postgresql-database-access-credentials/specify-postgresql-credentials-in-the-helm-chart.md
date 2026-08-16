---
title: "Specify PostgreSQL credentials in the Helm chart"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/specify-postgresql-credentials-in-the-helm-chart.html"
content_id: "lF3jF580SYW1oHZGTQ9IyA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:33.207497+00:00"
---

# Specify PostgreSQL credentials in the Helm chart

If you did not create a PostgreSQL secret that contains the following credentials, you
need to provide values in postgres Helm keys for the following credentials:

- host
- port The default as defined in `global postgres.port` is 5432
- user
- password

You can set these as global Helm keys to provide PostgreSQL database access for all of
the services:

```
global.postgres:
  host: "hostname"
  port: portnum  #The default port is 5432.
  password: "password"
  user: "username"
```

For port support, see Ports.

For example:

```
global.postgres:
  host: "cnc-postgres"
  password: "postgres"
  user: "coverity"
```

The `global.postgres` Helm key values can be used by all services or
overridden by each service. You override values for a service if you have created a
PostgreSQL database for that service and configured credentials to access that database.
Overriding `postgres` Helm key values for a particular service provides
that service access to its own PostgreSQL database. Global `postgres`
values can be overridden by each of the following services to access their own
databases:

- Coverity Connect: `cim.postgres`: See cim.postgres Helm keys - create Connect cim PostgreSQL access job.
- Scan Service: `scan-service.postgres`: See scan-service.postgres Helm keys - configure access to a Scan Service PostgreSQL database.
- Storage Service: `storage-service.postgres`: See storage-service.postgres Helm keys - configure access to a Storage Service PostgreSQL database.

Alternatively, you might provide these override values In the `helm
install` command.
