---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "0W8FHaraQ8SD5QNva8leBg"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:30.466962+00:00"
content_hash: "9775c7805aaee80355b2c6b95d709c9227f60bf1b2c58f4fbf69280e0d560174"
---

# API enhancements

For more information on API requests, please refer to the REST API Developers Guide available in Black Duck.

## Removal of deprecated matched components API request

The following deprecated API request has been removed in the 2024.7.0 release:

- `/api/projects/{projectId}/versions/{projectVersionId}/matched-components`

## New vulnerable-bom-components version

A new version (V8) of the following API request has been added:

- `/api/projects/<project-id>/versions/<version-id>/vulnerable-bom-components`

The latest version of this API request features improved performance and the following fix to enhance the quality of the output:

- The `vulnerabilityName` field has been removed from the `/api/projects/<project-id>/versions/<version-id>/vulnerable-bom-components` API request in the new lightweight version as `vulnerabilityName` and `vulnerabilityId` fields possessed same value and `vulnerabilityId` is more commonly used.
