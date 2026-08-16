---
title: "Changing the limit on active connections to the database pool"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/changing-the-limit-on-active-connections-to-the-database-pool.html"
content_id: "AStp5bO1jO70Z0Qm8hCRQg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:59.481555+00:00"
---

# Changing the limit on active connections to the database pool

You can add this property to cim.properties.

db.maxActiveConnections
:   Specifies the maximum number of active connections allowed to the database pool.
    The default is `50`.

    Example:
    `db.maxActiveConnections=75`
