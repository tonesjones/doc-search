---
title: "Restoring an embedded database"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/restoring-an-embedded-database.html"
content_id: "kTMEYFA9~BwzoPEaczonOQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:21.159314+00:00"
---

# Restoring an embedded database

Once you have a process for regular backups, you should also implement a process for
periodically testing the backups by attempting to restore them to an instance of the
Coverity Connect server that is the same version the backup was created from. This
practice will verify the media reliability and information integrity in the event
restoring a backup is required.

Note: For information specific to restoring databases in *clustered deployments*, see
Managing multiple database instances

**To restore an embedded database in a stand-alone deployment:**

Note: Use caution when restoring a database with `cov-admin-db`, because it
deletes data in an existing database. For more information, see the
`cov-admin-db`
description in the Coverity 2026.6.0 Command Reference and the `pg_restore` documentation at
<http://www.postgresql.org/docs/8.4/static/app-pgrestore.html>.

1. Place the embedded database in maintenance mode using the
   `cov-im-ctl` command. For example:

   ```
   > cov-im-ctl maintenance
   ```
2. Use the `cov-admin-db` command to restore the database from an
   archive file. For example:

   ```
   > cov-admin-db restore daily_cim_database_backup
   ```
3. Start Coverity Connect using the `cov-im-ctl` command. For
   example:

   ```
   > cov-im-ctl start
   ```
