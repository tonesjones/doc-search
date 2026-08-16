---
title: "PostgreSQL database tuning: embedded database"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/postgresql-database-tuning-embedded-database.html"
content_id: "H5kSUNCXQuFsyXr6_LsG0w"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:12.017445+00:00"
---

# PostgreSQL database tuning: embedded database

When you run the 2026.6.0 Coverity Platform installer, you select a database
performance level for a Production or Demo system. The selected level applies changes to
both the PostgreSQL database configuration that is embedded with Coverity Connect and
the JVM. These changes balance the memory utilization so that approximately 75% of RAM
is allocated to the JVM and the remaining 25% is allocated to PostgreSQL and the
operating system cache. The allocation of memory in this fashion is to avoid disk
swapping by either the application or the database. This new memory allocation strategy
biases memory towards the JVM to allow the application to scale under heavier loads
without impacting database performance.

You can see the settings stored for your environment and installation by executing the
`cov-admin-db tune --read` command.
