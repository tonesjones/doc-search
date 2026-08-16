---
title: "Database size guidelines"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/database-size-guidelines.html"
content_id: "hoYF702xTwcRA361DiAowg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:52.215238+00:00"
---

# Database size guidelines

The amount of RAM available limits the size of the Coverity Connect database. It is
recommended that the amount of RAM be at least 25% of the database size.

In the minimum hardware configuration, there is a minimum of 32GB of RAM. If the JVM heap
setting is 75% of system memory, or 24GB, then the database size can reach approximately
96GB before there are any performance problems. You should periodically check the size
of the Coverity Connect database and consider provisioning more resources for the server
if the database size increases to more than four times the amount of available RAM.

The database size can be found in Coverity Connect by navigating to Help > About... > Database Size.
