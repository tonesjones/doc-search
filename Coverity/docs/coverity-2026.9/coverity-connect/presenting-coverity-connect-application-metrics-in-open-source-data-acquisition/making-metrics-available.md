---
title: "Making metrics available"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/making-metrics-available.html"
content_id: "J5Rn9OkfgHswapkeBkBgcQ"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:20.313464+00:00"
---

# Making metrics available

To make Connect metrics available to open-source data acquisition and monitoring
software:

1. Add `connect.enable.metrics=true` to the
   `cim.properties` file. Setting this property to
   `true` exposes Connect metrics at the
   `/metrics` endpoint.
2. Restart the Connect server.
