---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "5QNef13UjtPq5Y1IjPH3SQ"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:29.767025+00:00"
content_hash: "6e0e85725411d320134f4c70b8f013df9788c568bff53764b39a68432f3469f8"
---

# API enhancements

For more information on API requests, please refer to the REST API Developers Guide available in Black Duck.

## Added sorting to LTS vulnerability view endpoint

The `GET /api/lts-projects/{projectId}/lts-project-versions/{versionId}/vulnerabilities` API endpoint now supports sorting on the following points:

- Vulnerability ID (default)
- Affected Components, the first component in the list
- Overall Score
- Remediation Status
