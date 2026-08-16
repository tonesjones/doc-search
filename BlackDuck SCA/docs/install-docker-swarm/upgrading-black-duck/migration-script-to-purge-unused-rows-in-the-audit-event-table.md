---
title: "Migration script to purge unused rows in the audit event table"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/migration-script-to-purge-unused-rows-in-the-audit-event-table.html"
content_id: "gtyOKW6vnV2XR4SuBpS6PQ"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:16.213912+00:00"
---

# Migration script to purge unused rows in the audit event table

Please note that this section is only applicable when upgrading from Black Duck versions
older than 2019.12.0.

During an upgrade, a migration script is run to purge rows that are no longer used in the
`audit_event` table because of changes to the reporting database.
This script might take a long time to run, depending on the size of the
`audit_event` table. For example, the migration script takes
approximately 20 minutes to run against a 350 GB `audit_event` table.

To determine the size of the audit event table, do one of the following tasks:

- From the bds_hub database, run the following command:

  `SELECT pg_size_pretty( pg_total_relation_size('st.audit_event')
  );`
- Log in to the Black Duck UI as system administrator and do the following
  steps:

  1. Click the expanding menu icon ( [image: image] ) and
     select **Administration**.
  2. On the Administration page, select **System Information**.

     The System Information page appears.
  3. Select **db** in the left column of the page.
  4. Find the *total_tbl*_size value for the *audit_event* tablename in the Table
     Sizes table.  
      [image: image]

Once the upgrade is complete, it is strongly recommended that you run the `VACUUM
FULL` command on the `audit_event` table to optimize
PostgreSQL performance.

- Depending on your system usage, running the `VACUUM FULL` command can reclaim
  a significant amount of disk space no longer in use by Black Duck.
- By running this command, querying performance will be improved.

Note: If you don't run the `VACUUM FULL` command, there may be a degradation of
performance.

Important: You must ensure you have enough space to run the `VACUUM
FULL` command, otherwise, it will fail by running out of disk space and
possibly corrupt the entire database. The `VACUUM FULL` command requires
twice the amount of disk space that is currently being used by the
`audit_event` table.

To run the `VACUUM FULL` command with containerized PostgreSQL database
deployments, do the following steps:

1. Get the size of the `audit_event` table and ensure that you have enough space
   to run the `VACUUM FULL` command.
2. Run the `docker ps` command to get the ID of the PostgreSQL container.
3. Run the following command to access the PostgreSQL container.

   ```
   docker exec -it <container_ID> psql bds_hub
   ```
4. Run the following `VACUUM FULL` command to reclaim space that is no longer
   used.

   ```
   VACUUM FULL ANALYZE st.audit_event;
   ```

If you have an external PostgreSQL database deployment, you must determine the size of your
audit_event table, execute the `VACUUM FULL` command, and when it's
finished, you restart the deployment.
