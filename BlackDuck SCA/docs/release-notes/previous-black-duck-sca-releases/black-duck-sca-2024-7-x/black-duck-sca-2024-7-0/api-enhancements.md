---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "ZB2SdeEXje_KbzRXxYt5sQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:08.885406+00:00"
---

# API enhancements

For more information on API requests, please refer to the REST API Developers Guide
available in Black Duck.

## Removal of deprecated matched components API request

The following deprecated API request has been removed in the 2024.7.0 release:

- `/api/projects/{projectId}/versions/{projectVersionId}/matched-components`

## New vulnerable-bom-components version

A new version (V8) of the following API request has been added:

- `/api/projects/<project-id>/versions/<version-id>/vulnerable-bom-components`

The latest version of this API request features improved performance and the following
fix to enhance the quality of the output:

- The `vulnerabilityName` field has been removed from the
  `/api/projects/<project-id>/versions/<version-id>/vulnerable-bom-components`
  API request in the new lightweight version as `vulnerabilityName` and
  `vulnerabilityId` fields possessed same value and
  `vulnerabilityId` is more commonly used.
