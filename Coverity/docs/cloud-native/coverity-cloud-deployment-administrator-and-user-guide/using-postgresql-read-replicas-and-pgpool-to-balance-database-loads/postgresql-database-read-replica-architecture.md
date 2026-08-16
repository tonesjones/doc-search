---
title: "PostgreSQL database read replica architecture"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/postgresql-database-read-replica-architecture.html"
content_id: "Ua~BC0yFmnkwiILIITTR9g"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:09.312554+00:00"
---

# PostgreSQL database read replica architecture

The following simplified drawing illustrates a single database instance handling multiple
reads and writes. As the number of clients increases, database performance decreases,
causing read lags for Coverity clients requesting scan data.

Figure 1. Single database architecture
[image: image]

With a single read-write database as illustrated above, having large numbers of clients
request database reads can affect performance and delay access to the data when there
are many users.

A Database read replica architecture as illustrated below distributes database read
requests among many read-only database replicas. The replicas are exact copies of the
primary read-write database. This helps resolve performance issues that can occur when
there are large numbers of database scan data read requests from large numbers of
Connect clients.

Figure 2. Database read replica architecture
[image: image]

The sample database read replica configuration shown above contains:

- two CIM pods.
- one commit server (CS) pod. The commit server pod which is deployed with Connect
  Web client HA (high availability), manages commits to the primary database
  instance.

  Important: You cannot deploy database read
  replicas without Coverity Connect (CIM) Web application HA deployed.
- one Pgpool pod that distributes data read requests among the primary and replica
  databases. Optionally, you can also configure replica Pgpool pods as a safeguard
  against a Pgpool pod failure; see the `cim.pgpool.replicas` Helm
  key.
- one primary PostgreSQL database instance.
- three read-only replica PostgreSQL database instances.

You might use these names:

- Connect (CIM) pods: CIM1, CIM2
- Commit Server pod: CommitSP
- Primary database: DBP
- Replica databases: DBReplica-1, DBReplica-2, through DBReplica-n
