---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "4v7s6uqT7d8mHi8NBPAHRw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:31.451845+00:00"
---

# API enhancements

For more information on API requests, please refer to the REST API Developers Guide
available in Black Duck.

## Updated response for matched-file API requests

The following API requests now have a `uri` field include in their
responses:

- `/api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/versions/{componentVersionId}/origins/{originId}/matched-files`
- `/api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/matched-files`
- `/api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/versions/{componentVersionId}/matched-files`
