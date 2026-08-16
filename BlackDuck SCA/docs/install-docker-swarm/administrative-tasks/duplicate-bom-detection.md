---
title: "Duplicate BOM Detection"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/duplicate-bom-detection.html"
content_id: "e2AilrnrUXpIqU_plop7Zg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:40.307604+00:00"
---

# Duplicate BOM Detection

To improve scan performance, the duplicate BOM detection feature is enabled by
default.

If the feature determines that a scan will produce a BOM identical to the existing one,
it skips the BOM computation. You can disable it by using the following setting:

```
SCAN_SERVICE_OPTS=-Dblackduck.scan.disableRedundantScans=true
```

You can change this setting in the `blackduck-config.env` file.

Note: In Black Duck 2021.4.0, this feature only impacts package manager (dependency) scans when
the set of dependencies discovered by Detect is identical to the set from the previous
scan. This capability will be extended in future releases.
