---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "nLje3YqlmTzWqnoBj4DjxA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:51.400047+00:00"
---

# API enhancements

For more information on API requests, please refer to the REST API Developers Guide
available in Black Duck.

## Added sorting to LTS vulnerability view endpoint

The `GET
/api/lts-projects/{projectId}/lts-project-versions/{versionId}/vulnerabilities`
API endpoint now supports sorting on the following points:

- Vulnerability ID (default)
- Affected Components, the first component in the list
- Overall Score
- Remediation Status
