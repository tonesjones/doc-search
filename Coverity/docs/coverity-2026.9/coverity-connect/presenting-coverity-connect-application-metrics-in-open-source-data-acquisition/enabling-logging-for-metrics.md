---
title: "Enabling logging for metrics"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/enabling-logging-for-metrics.html"
content_id: "LJ60dUgrMW_OSfuiDeHN7w"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:20.353821+00:00"
---

# Enabling logging for metrics

To enable error- and latency-related logging of Coverity Connect metrics, perform the
following procedure:

1. Add `connect.enable.logging.metrics=true` to the
   `cim.properties` file. This property is set to
   `false` by default.
2. Restart the Connect server.
