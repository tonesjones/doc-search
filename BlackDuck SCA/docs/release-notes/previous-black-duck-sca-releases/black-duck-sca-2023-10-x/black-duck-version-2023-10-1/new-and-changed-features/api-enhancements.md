---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "dQKmw~gX43IEV3lOUD8AHg"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:31.337763+00:00"
content_hash: "672e50c5e03ab32612ebc136fc636a9f1cfb8351fea424a73b51c9a952ab91fc"
---

# API enhancements

For more information on API requests, please refer to the REST API Developers Guide available in Black Duck.

## Updated response for matched-file API requests

The following API requests now have a `uri` field include in their responses:

- `/api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/versions/{componentVersionId}/origins/{originId}/matched-files`
- `/api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/matched-files`
- `/api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/versions/{componentVersionId}/matched-files`
