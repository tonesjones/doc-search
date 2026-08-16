---
title: "Managing Connect PostgreSQL database size and integrity"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/managing-connect-postgresql-database-size-and-integrity.html"
content_id: "_AXSgvcCyAYKT1VE4NkvqA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:14.738847+00:00"
---

# Managing Connect PostgreSQL database size and integrity

This section provides guidance to manage the size and integrity of external Connect
PostgreSQL databases used with a Coverity cloud deployment.

In a Relational Database Management System (RDBMS), when data from the database pages is
deleted, the space is not reclaimed. This results in data fragmentation which causes SQL
query performance to degrade; the database optimiser, which determines the best way to
execute SQL commands, needs to traverse more pages. Performing database management
procedures identified in the following table helps maintain the database and improve
database access performance.

Table 1. PostgreSQL database management procedures

| Procedure | Link |
| --- | --- |
| Statically tune a database to increase performance. | In this document, see:   - Statically tuning an external Connect PostgreSQL database |
| Perform cross reference (Xref) deduplication to reduce database size and increase performance. | In the document:   - Coverity Platform 2026.6.0 User and Administrator Guide   see the chapter: Coverity Connect administration and subsection: Database cross-reference deduplication. |
| If Policy Manager is not used, in the `cim.properties` file:  1. Disable Policy Manager ETL data scheduling using the    following configuration:      ```    policymanager.etl.scheduled.disable=true    ``` 2. Rmove Policy Manager data using the following configuration::    policymanager.etl.truncate.enable      ```    policymanager.etl.truncate.enable=false    ```   If Policy Manager is used, during a database migration, disable and truncate ETL data to reduce database size and increase performance. | In the document:   - Coverity Platform 2026.6.0 User and Administrator Guide   see the chapter: Coverity policy manager administration and subsection: Truncating ETL data |
| Skeletonization and deletion:   1. Enable snapshot Skeletonization as a background job.    Skeletonization yet retains some necessary data of old    snapshots while removing mainly the source files and related    data. 2. Or delete the snapshots, streams, projects manually. On    delete, you won't be able to access the snapshot    anymore. 3. Skeletonization can be scheduled at a particular frequency,    whereas deletion is a manual action, and deletion progresses    in background when manually initiated. 4. In either skeletonization or deletion, the disk space would    not be reclaimed from DB, unless we run vacuum full during    maintenance mode. |  |
| While orphaned LOBs are cleaned up regularly, the cleanup does not reclaim the freed-up space. Use the vacuum command to help reclaim space: `vacuum full pg_largeobject,pg_largeobject_metadata;` Vacuuming locks tables until completion. We recommend performing a vacuum while Coverity is shut down or during non-peak hours when commits are not occurring. |  |
| You can check the database integrity using the `check-integrity.sh` script. | In this document, see:   - Checking database integrity: check-integrity.sh |
| To import streams from an archive file, export streams to an archive, or get information about an archive file, you can use the `cov-archive.sh` script. | In this document, see:   - Managing archives: cov-archive.sh |
| Migrate a database to a new cloud database instance. This is performed to migrate an existing Connect database instance to the cloud. | In this document, see:   - Migrating a PostgreSQL database instance to the cloud |
