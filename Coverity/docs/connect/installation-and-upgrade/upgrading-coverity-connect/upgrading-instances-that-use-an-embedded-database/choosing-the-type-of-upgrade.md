---
title: "Choosing the type of upgrade"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/choosing-the-type-of-upgrade.html"
content_id: "r2J6LZbIcTtFduDiub~NjQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:28.443235+00:00"
---

# Choosing the type of upgrade

This section helps you choose the type of upgrade. Note that each type of upgrade corresponds
to the Coverity Platform *installer options* as shown in the following table. This
chapter uses the terminology specified in the table to describe upgrade types:

Table 1. Installer options

| Type of upgrade | Installer option(s) |
| --- | --- |
| In-place upgrade | "In-place Upgrade" option |
| Backup-and-restore upgrade | "Backup-and-restore" option |
| Intermachine upgrade | “Upgrade Preparation” option followed by “Intermachine Upgrade” option |

Upgrade types are described in the following subsections.

**Intermachine upgrade**

Use the intermachine upgrade if you want the upgraded Coverity Connect instance to exist on a
new host machine. Otherwise, use the in-place upgrade or the Backup-and-restore
upgrade.

**In-place upgrade versus backup-and-restore upgrade**

An in-place upgrade is faster and uses less disk space than a backup-and-restore upgrade.
However, a backup-and-restore upgrade keeps the old instance intact, which is useful if
you want to create a staging environment.

An in-place upgrade transforms an existing Coverity Connect instance, including all of its
data, into a new Coverity Connect instance in the same directory location on the same
machine. Essentially, an in-place upgrade does the following:

- Optionally, backs-up the existing database
- For PostgreSQL major version changes, modifies the data storage format in-place
- If required by Coverity Connect, upgrades the database schema
- Updates non-database state (the configuration not stored in the database)

A backup-and-restore upgrade backs-up the entire, existing Coverity Connect instance. Then the
backup-and-restore upgrade restores the Coverity Connect instance, including the
database, to a new location (a different directory than where the existing instance is
installed) on the same machine without affecting the existing instance. Essentially, a
backup-and-restore upgrade does the following:

- Backs-up the existing database
- Installs a new Coverity Connect instance in the new location
- Restores the database to the new location
- If required by Coverity Connect, upgrades the database schema in the new
  installation
- Copies non-database state (the configuration not stored in the database) to the
  new installation
