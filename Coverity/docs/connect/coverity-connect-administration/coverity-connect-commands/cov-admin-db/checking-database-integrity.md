---
title: "Checking database integrity"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/checking-database-integrity.html"
content_id: "sf24avloAhv5oG~ArJCZog"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:12.213575+00:00"
---

# Checking database integrity

Use the `check-integrity` subcommand to check the integrity of your
database: the command verifies that tables, sequences, columns, constraints, and indexes
have the intended definitions.

Note: With an embedded database, this operation automatically runs before a `cov-admin-db
backup` command is executed and after a `cov-admin-db
restore` command is executed.

Important: If Coverity Connect is deployed in the cloud, refer
to the section Coverity tools in a Coverity cloud deployment in the Coverity 2026.6.0 Cloud Deployment Administrator and User Guide.

```
cov-admin-db check-integrity 
    [--install-dir <install_dir_name>] 
    [--debug]
```

Use the `--install-dir` option to specify another Coverity Connect
installation to check. The default location is
`install-dir-CC`. The subcommand is compatible
with all versions of Coverity Connect.
