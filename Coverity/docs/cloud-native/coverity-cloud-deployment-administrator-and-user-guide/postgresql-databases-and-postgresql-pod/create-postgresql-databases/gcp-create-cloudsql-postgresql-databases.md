---
title: "GCP: Create CloudSQL PostgreSQL databases"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/gcp-create-cloudsql-postgresql-databases.html"
content_id: "QsAF5CSbyyQTEdzGBa2Jqw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:59.757529+00:00"
---

# GCP: Create CloudSQL PostgreSQL databases

The following guidance uses the Google Cloud console to create CloudSQL PostgreSQL
databases.

Important: Keep all database names handy; you will need
them when you configure the Helm keys.

## GCP: creating the primary PostgreSQL database

Create the primary PostgreSQL database instance as described in the Google Cloud
documentation: [Create instances](https://cloud.google.com/sql/docs/postgres/create-instance).

## GCP: creating read-only replica PostgreSQL databases

Optionally, if you are deploying read-only replica PostgreSQL databases:

1. Create one or more GCP read replica database instance(s) of the primary
   database instance as described in the GCP documentation: [Create read replicas](https://cloud.google.com/sql/docs/postgres/replication/create-replica).

   Important: In GCP, the database replicas must
   use private IP addresses. Make sure that the primary and replica databases
   use the same type of IP and that both are in the same network. After
   deploying, the primary database cloudsql instance uses a private IP address.
   Use the same configuration for the replica(s). By default, after creating a
   replica, it has a public IP address. You must change it to match the primary
   database configuration.
2. Continue with confguring the read-only replica PostgreSQL databases as described
   in Using PostgreSQL read replicas and Pgpool to balance database loads.
