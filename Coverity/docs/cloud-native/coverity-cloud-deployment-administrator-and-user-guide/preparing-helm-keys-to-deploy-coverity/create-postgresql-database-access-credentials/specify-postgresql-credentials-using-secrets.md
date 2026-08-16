---
title: "Specify PostgreSQL credentials using secrets"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/specify-postgresql-credentials-using-secrets.html"
content_id: "D_xgGZQIArVPOqazHsc6bg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:32.565761+00:00"
---

# Specify PostgreSQL credentials using secrets

If you created secret(s) to provide PostgreSQL credentials as described in Creating secret(s) for PostgreSQL access, this section describes how to specify
the secret(s) in the Helm values.yaml file.

`global.postgres` Helm key values can be used by all services or
overridden by each service. You override values for a service if you have created a
PostgreSQL database for that service and created PostgreSQL secrets to access that
database. Overriding the `global.postgres.existingSecret` Helm key value
for a particular service provides that service access to its own PostgreSQL database.
Global `postgres` values can be overridden by each of the following
services to access their own databases:

- `cim.postgres.existingSecret`
- `scan-service.postgres.existingSecret`
- `storage-service.postgres.existingSecret`

If you created a single secret to support all services, you need to configure the
following Helm key:

- `global.postgres.existingSecret`: See global.postgres Helm keys.

If you created separate secrets for each service (cim, scan-service, storage-service),
you need to configure the following Helm keys as needed:

- For Coverity Connect: `cim.postgres.existingSecret`: See cim.postgres Helm keys - create Connect cim PostgreSQL access job.
- For Scan Service: `scan-service.postgres.existingSecret`: See
  scan-service.postgres Helm keys - configure access to a Scan Service PostgreSQL database.
- For Storage Service: `storage-service.postgres.existingSecret`:
  See storage-service.postgres Helm keys - configure access to a Storage Service PostgreSQL database.
