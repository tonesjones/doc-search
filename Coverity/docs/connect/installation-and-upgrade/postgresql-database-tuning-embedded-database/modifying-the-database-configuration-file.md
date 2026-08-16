---
title: "Modifying the database configuration file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/modifying-the-database-configuration-file.html"
content_id: "D8nfx2uAgb29~3ZG53Sb1g"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:12.631296+00:00"
---

# Modifying the database configuration file

You can reconfigure the embedded PostgreSQL database using one of the following
methods:

- Run the `cov-admin-db tune` command. This is the recommended method
  for achieving optimal tuning of your database. For information on how to use this
  command, refer to the section "Tuning Coverity Connect for your environment" in the
  Coverity 2026.6.0 Command Reference.
- You can alternatively edit the postgresql.conf file manually.
  This file resides in the following location, if you chose the default location
  during the installation or upgrade:
  - <install_dir>/database/ (Unix systems)
  - <install_dir>\database\ (Windows systems)

You must stop and restart Coverity Connect after reconfiguring the database. Use
`cov-im-ctl stop` to stop Coverity Connect and `cov-im-ctl
start` to restart it.

Note: Incorrect configuration updates can prevent Coverity Connect from starting or cause
Coverity Connect to perform poorly. You can recover from such an error by restoring the
configuration file to its original state.
