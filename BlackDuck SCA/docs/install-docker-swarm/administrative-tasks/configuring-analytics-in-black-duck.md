---
title: "Configuring analytics in Black Duck"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-analytics-in-black-duck.html"
content_id: "sf9FsHog4AMOMIqGX0TSBw"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:24.764533+00:00"
content_hash: "d28a0e295c63b5e38dfdd0ceb9a21eadd358533a06bcd64e2913ec02dca8d808"
---

# Configuring analytics in Black Duck

In Black Duck you can disable phone home globally for Black Duck Detect by turning off analytics in the `blackduck-config.env` file.

1. In the `blackduck-config.env` file, configure `ANALYTICS=false`.
2. Restart Black Duck.
