---
title: "Making metrics available"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/making-metrics-available.html"
content_id: "J5Rn9OkfgHswapkeBkBgcQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:23.883610+00:00"
---

# Making metrics available

To make Connect metrics available to open-source data acquisition and monitoring
software:

1. Add `connect.enable.metrics=true` to the
   `cim.properties` file. Setting this property to
   `true` exposes Connect metrics at the
   `/metrics` endpoint.
2. Restart the Connect server.
