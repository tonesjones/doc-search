---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "9LND_axcV1wSLIkg~9gwjg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:10.341459+00:00"
---

# Description

The `cov-admin-db` command contains subcommands to perform various Coverity
Connect PostgreSQL database maintenance operations as described in the following
table.

| Subcommand | Database support | Operation |
| --- | --- | --- |
| `backup` | embedded only | Backs up the database to an archive file or directory. See also Backing up and restoring an embedded database. |
| `check-integrity` | external and embedded  Command not supported in cloud deployments | Checks the integrity of your database by verifying tables, sequences, columns, constraints, and indexes.  See Checking database integrity.  Note: This command is not supported in cloud deployments. If Coverity Connect is deployed in the cloud, refer to the section Coverity tools in a Coverity cloud deployment in the Coverity 2026.6.0 Cloud Deployment Administrator and User Guide. |
| `optimize` | embedded only | Improves database use of indexes and statistics.  See Optimizing an embedded database. |
| `psql` | embedded only | Runs the `psql` command on the database, allowing you to issue queries interactively to PostgreSQL. |
| `reset-admin-password` | external and embedded  Command not supported in cloud deployments | Changes password for the admin account to that specified at the prompt.  Note: This command is not supported in cloud deployments. If Coverity Connect is deployed in the cloud, refer to the section Coverity tools in a Coverity cloud deployment in the . |
| `restore` | embedded only | Restores data to the embedded database, using the specified archive file or directory.  See Backing up and restoring an embedded database. |
| `scramble` | external and embedded  Command not supported in cloud deployments | Strips all sensitive information from your database backup so that Coverity support can troubleshoot it.  See Preparing the Connect database to send to Black Duck.  Note: The scramble command is not supported with Coverity cloud deployments. |
| `tune` | external and embedded | Allows you to tune PostgreSQL and Java JVM settings for the Coverity Connect database for optimal performance. Tune options allow you to read tune settings, display the server profile, display suggested settings, and to apply the suggested tune settings.  See Tuning Coverity Connect for your environment. |
| `upgrade-schema` | external and embedded  Command not supported in cloud deployments | Upgrades an archived schema from a previous version of Coverity Connect to make it compatible with the current version of Coverity Connect.  Note: This command is not supported in cloud deployments. If Coverity Connect is deployed in the cloud, refer to the Coverity 2026.6.0 Cloud Deployment Administrator and User Guide. |
