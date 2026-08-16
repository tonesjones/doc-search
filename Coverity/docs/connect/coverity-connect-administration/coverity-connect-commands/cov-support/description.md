---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "RZJbjDBb7d8L4V0WP2lSgg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:46.679285+00:00"
---

# Description

The `cov-support` command creates a compressed archive that contains
various property and log files related to Coverity Connect.
Black Duck Support migt request that you create this archive and submit it for analysis.

If the `--with-config` option is specified, then the following files in the
/config folder are included in the archive:

- cim.properties
- server.xml
- VERSION
- system.properties
- postgresql.conf
- web.properties

If the `--with-logs` option is specified, then log files in the
/logs, /postgressql, and
/.install4j directories are added to the archive.
