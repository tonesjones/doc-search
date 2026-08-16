---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "E_9UgWjaWPIEJ_o3CVA4yg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:56.448914+00:00"
---

# API enhancements

## Updated scan endpoints BDIO header information

The following API endpoints have been updated to use project and version names from
the BDIO header instead of from HTTP headers:

- /api/scan/data
- /api/intelligent-persistence-scans
- /api/intelligent-persistence-scans/{scanId}
- /api/developer-scans
- /api/developer-scans/{scanId}
