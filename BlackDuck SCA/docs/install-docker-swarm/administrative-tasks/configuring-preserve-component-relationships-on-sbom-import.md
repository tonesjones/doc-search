---
title: "Configuring Preserve Component Relationships on SBOM Import"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-preserve-component-relationships-on-sbom-import.html"
content_id: "oRe6UOIG98jb0vtX8H_jQw"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:25.692095+00:00"
content_hash: "2ad10622c7b057f0f45efa67eb6c6be982117d3c048f67b4c8d1e124ec5b0b80"
---

# Configuring Preserve Component Relationships on SBOM Import

Preserving component relationships on SBOM import is disabled by default. To enable this feature, you must configure the following setting:

```
blackduck.scan.sbom.preserve.relationships=true
```

Once this configuration is set, Black Duck SCA will automatically preserve relationship data from imported SBOM reports.
