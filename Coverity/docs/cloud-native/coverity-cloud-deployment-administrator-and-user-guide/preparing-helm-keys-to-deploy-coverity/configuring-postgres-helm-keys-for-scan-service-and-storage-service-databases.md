---
title: "Configuring postgres Helm keys for Scan Service and Storage Service databases"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-postgres-helm-keys-for-scan-service-and-storage-service-databases.html"
content_id: "h0iUneyAwsSYcHIchYy6tg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:46.047631+00:00"
---

# Configuring postgres Helm keys for Scan Service and Storage Service databases

## Configuring `scan-service.postgres` Helm keys for a Scan Service database

If you created a PostgreSQL database instance for use by the Scan Service, you need
to configure several `scan-service.postgres` Helm keys to create jobs
that that enable the Scan Service to access its' own PostgreSQL database, for
example, a database named "scan".

Note: The PostgreSQL database resources must already exist.

The `scan-service.postgres` Helm keys, when configured, override
broader chart-level postgres keys such as `postgres` Helm keys within
the `scan-services` chart, and `global.postgres`
keys.

For information on the `scan-service.postgres` Helm keys, refer to
scan-service.postgres Helm keys - configure access to a Scan Service PostgreSQL database.

## Configuring `storage-service.postgres` Helm keys for a Storage Service database

If you created a PostgreSQL database instance for use by the Storage Service, you
need to configure several `storage-service.postgres` Helm keys to
create jobs that that enable the Storage Service to access its' own PostgreSQL
database, for example, a database named "storage".

Note: The PostgreSQL database resources must already exist.

The `storage-service.postgres` Helm keys, when configured, override
broader chart-level postgres keys such as `postgres` Helm keys within
the `scan-services` chart, and `global.postgres`
keys.

For information on the `storage-service.postgres` Helm keys, refer to
storage-service.postgres Helm keys - configure access to a Storage Service PostgreSQL database.
