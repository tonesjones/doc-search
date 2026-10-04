---
title: "Upgrading the database"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/upgrading-the-database.html"
content_id: "yyXsXEa1iFefXOqoLBjMDA"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:15.830904+00:00"
---

# Upgrading the database

Use the `upgrade-schema` subcommand to upgrade your database schema: The
command modifies the existing schema and data to make it compatible with the current
version of Coverity Connect.

The upgrade-schema subcommand supports an external PostgreSQL database or the embedded
database. Because the `cov-admin-db restore` command and the installer
always upgrade the schema, you need to run `cov-admin-db
upgrade-schema` only when using an external database.
