---
title: "Configuring analytics in Black Duck"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-analytics-in-black-duck.html"
content_id: "voxkBRYIIDonNK76V~COMg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:51.785730+00:00"
---

# Configuring analytics in Black Duck

In Black Duck you can disable phone home globally for Black Duck
Detect by turning off analytics in the `blackduck-config.env` file.

1. In the `blackduck-config.env` file, configure
   `ANALYTICS=false`.
2. Restart Black Duck.
