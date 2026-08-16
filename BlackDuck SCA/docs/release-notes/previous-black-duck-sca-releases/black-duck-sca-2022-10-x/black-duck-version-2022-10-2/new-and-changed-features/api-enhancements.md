---
title: "API Enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "uRqDsQyQ2VmWXg6WJnv5Bg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:18.450311+00:00"
---

# API Enhancements

For more information on API requests, please refer to the REST API Developers Guide available
in Black Duck.

## Enhanced project endpoints

The following endpoints have been updated to include OSS component pURL coordinates:

- `api/projects/<projectId>/versions/<projectVersionId>/components`
- `api/projects/<projectId>/versions/<projectVersionId>/vulnerable-bom-components`
- `api/projects/<projectId>/versions/<projectVersionId>/components?filter=licensePolicy`
