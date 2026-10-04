---
title: "Checking database integrity"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/checking-database-integrity.html"
content_id: "sf24avloAhv5oG~ArJCZog"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:15.664251+00:00"
---

# Checking database integrity

Use the `check-integrity` subcommand to check the integrity of your
database: the command verifies that tables, sequences, columns, constraints, and indexes
have the intended definitions.

Note: With an embedded database, this operation automatically runs before a `cov-admin-db
backup` command is executed and after a `cov-admin-db
restore` command is executed.

Important: This command is not supported in cloud deployments.
If Coverity Connect is deployed in the cloud, refer to Coverity tools in a Coverity cloud deployment.

```
cov-admin-db check-integrity 
    [--install-dir <install_dir_name>] 
    [--debug]
```

Use the `--install-dir` option to specify another Coverity Connect
installation to check. The default location is
`install-dir-CC`. The subcommand is compatible
with all versions of Coverity Connect.
