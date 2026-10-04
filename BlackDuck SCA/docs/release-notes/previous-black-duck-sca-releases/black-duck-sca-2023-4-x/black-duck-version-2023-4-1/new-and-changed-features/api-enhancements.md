---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "lusjp9KLydWk~V1ullILlw"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:32.366722+00:00"
content_hash: "4c5c17e46f7007e16ecbd6d8b1ac9d48ab2b20d590d819c7ec36d7b000333951"
---

# API enhancements

## Updated scan endpoints BDIO header information

The following API endpoints have been updated to use project and version names from the BDIO header instead of from HTTP headers:

- /api/scan/data
- /api/intelligent-persistence-scans
- /api/intelligent-persistence-scans/{scanId}
- /api/developer-scans
- /api/developer-scans/{scanId}
