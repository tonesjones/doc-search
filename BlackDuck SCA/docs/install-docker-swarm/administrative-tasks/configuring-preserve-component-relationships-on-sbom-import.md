---
title: "Configuring Preserve Component Relationships on SBOM Import"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-preserve-component-relationships-on-sbom-import.html"
content_id: "W~_JkUkUhJGIpBgZHu7q6g"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:13.879985+00:00"
---

# Configuring Preserve Component Relationships on SBOM Import

Preserving component relationships on SBOM import is disabled by default. To
enable this feature, you must configure the following setting:

```
blackduck.scan.sbom.preserve.relationships=true
```

Once this configuration is set, Black Duck SCA will automatically
preserve relationship data from imported SBOM reports.
