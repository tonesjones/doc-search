---
title: "API Enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "q4aV9iSoOcb3ZEXvnZdvuA"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:33.221344+00:00"
content_hash: "e379e40161681341ab3af64892b42ee148ad975fc5a8c14ff1636b7bc8b14c75"
---

# API Enhancements

For more information on API requests, please refer to the REST API Developers Guide available in Black Duck.

## Enhanced project endpoints

The following endpoints have been updated to include OSS component pURL coordinates:

- `api/projects/<projectId>/versions/<projectVersionId>/components`
- `api/projects/<projectId>/versions/<projectVersionId>/vulnerable-bom-components`
- `api/projects/<projectId>/versions/<projectVersionId>/components?filter=licensePolicy`
