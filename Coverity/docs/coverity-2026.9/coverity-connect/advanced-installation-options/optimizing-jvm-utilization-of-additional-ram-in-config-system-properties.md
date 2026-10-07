---
title: "Optimizing JVM utilization of additional RAM in config/system.properties"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/optimizing-jvm-utilization-of-additional-ram-in-config/system.properties.html"
content_id: "_05MSrCS_uN6xRZExWmx0w"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:18.846600+00:00"
---

# Optimizing JVM utilization of additional RAM in config/system.properties

The application is started with the following JVM defaults.

For Production deployments (default):

`-Xms=512m`

`-Xmx=75% of the Total System Memory`
