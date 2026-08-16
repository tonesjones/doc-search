---
title: "Using the command line to back up an embedded database"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-the-command-line-to-back-up-an-embedded-database.html"
content_id: "tRRCAOJ1sWtM8iJlt3BmhQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:20.494863+00:00"
---

# Using the command line to back up an embedded database

You can manually run (or create a script to automatically run) `cov-admin-db
backup` to backup your database. For more information, see the
`cov-admin-db` description
in the Coverity 2026.6.0 Command Reference.

To backup the database in a stand-alone deployment:

1. Verify that the Coverity Connect database is running. To check the status of your
   database, type the following command:

   ```
   > cov-im-ctl status
   ```
2. Back up your database by entering the `cov-admin-db` command.
   For example:

   ```
   > cov-admin-db backup daily_cim_database_backup
   ```
