---
title: "Enabling logging for metrics"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enabling-logging-for-metrics.html"
content_id: "LJ60dUgrMW_OSfuiDeHN7w"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:24.503968+00:00"
---

# Enabling logging for metrics

To enable error- and latency-related logging of Coverity Connect metrics, perform the
following procedure:

1. Add `connect.enable.logging.metrics=true` to the
   `cim.properties` file. This property is set to
   `false` by default.
2. Restart the Connect server.
