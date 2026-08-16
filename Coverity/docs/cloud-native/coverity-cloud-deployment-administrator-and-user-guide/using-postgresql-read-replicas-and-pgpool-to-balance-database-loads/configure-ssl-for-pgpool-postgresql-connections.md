---
title: "Configure SSL for Pgpool PostgreSQL connections"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configure-ssl-for-pgpool-postgresql-connections.html"
content_id: "OQiSEuaZbGeXASKCDdD_mw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:12.071733+00:00"
---

# Configure SSL for Pgpool PostgreSQL connections

SSL configuration secures PostgreSQL connections by enabling encryption and
certificate validation.

## SSL connection paths

There are two distinct SSL connection paths in the Pgpool architecture:

- **Backend connections (Pgpool → PostgreSQL)**: Connections from Pgpool to
  PostgreSQL database servers. SSL is enabled with certificate verification.
  Pgpool validates certificates against the configured Certificate Authority.
- **Frontend connections (Connect → Pgpool)**: Connections from Connect
  components to Pgpool. SSL is currently disabled for internal cluster
  communication.

## Cloud provider certificate requirements

PostgreSQL SSL requirements depending on the cloud provider and database
configurations.

- **AWS RDS and Azure Database for PostgreSQL**: A single CA certificate
  configuration is used for the primary database and all read replica
  instances.
- **GCP CloudSQL**: Each database instance may use a unique CA configuration.
  All CA certificates must be combined and provided through the trust-stores
  ConfigMap.

## SSL mode behavior with Pgpool

- **sslmode=disable**: SSL is disabled and certificates are not validated.
- **sslmode=verify-ca**: Pgpool validates PostgreSQL certificates against CA in
  trust-stores.
- **sslmode=verify-full**: Direct database connections use SSL with full
  hostname verification. Pgpool backend connections validate certificates against
  the Certificate Authority, which is the maximum level of verification supported
  by Pgpool.

Note: `verify-full` mode on GCP CloudSQL and
OpenShift has not been validated but is expected to work. If hostname verification
issues occur, use `verify-ca` for these environments.
