---
title: "Using PostgreSQL read replicas and Pgpool to balance database loads"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-postgresql-read-replicas-and-pgpool-to-balance-database-loads.html"
content_id: "6eF3bNGOdjZzQLzN2Ay~yA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:08.025237+00:00"
---

# Using PostgreSQL read replicas and Pgpool to balance database loads

This section describes how to create and configure PostgreSQL read replica databases to
improve database read and write performance. A PostgreSQL read replica database is a
read-only copy of the primary PostgreSQL database. Data written to the primary database
is also immediately written to the all replicas of that primary database. A read replica
database is an exact copy of the primary database instance.

Using database read replicas improves read and write performance by routing read traffic
to the read replica databases. Writes are always sent to the primary database while
reads are to one or more replicas. Even during write-intensive periods, for example
during commits, balancing reads across the read replicas improves performance for both
reads and writes.

Using read replica databases offloads UI activity and REST API calls from the primary
database instance to the read replica instances. This increases throughput to the
primary database, especially in environments with large numbers of read requests.

For more information about PostgreSQL database read replicas, see the Google Cloud
document, [About replication in Cloud SQL](https://cloud.google.com/sql/docs/postgres/replication).
