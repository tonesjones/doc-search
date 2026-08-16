---
title: "Optimizing an embedded database"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/optimizing-an-embedded-database.html"
content_id: "QIhiZ8sc94qQS3ZG6sAmrQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:12.828409+00:00"
---

# Optimizing an embedded database

Use the `cov-admin-db optimize` command to optimize database use of indexes and
statistics.

Important: `cov-admin-db optimize` is not
supported with an external database.

You can use this subcommand without putting Coverity Analysis in Maintenance mode.

To reclaim the maximum amount of space in an embedded database, you can back up and restore the
embedded database after optimizing. For information about this process, see
"Coverity Connect administration" in the Coverity Platform 2026.6.0 User and Administrator Guide.
