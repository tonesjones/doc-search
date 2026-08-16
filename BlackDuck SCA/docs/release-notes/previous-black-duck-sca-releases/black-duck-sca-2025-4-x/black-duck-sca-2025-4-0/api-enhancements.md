---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "2Mt6FfO5u6ik2BbYTH1PdA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:40.272258+00:00"
---

# API enhancements

For more information on API requests, please refer to the REST API Developers Guide
available in Black Duck.

## Deprecation of v4, v5 data-retention endpoint

Black Duck is deprecating v4 and v5 of the `GET
/settings/data-retention` endpoint and introducing v6 as the latest
version. Customers are encouraged to transition to v6 to take advantage of the
improved functionality, performance, and security enhancements.

Users should update their integrations accordingly, as v4 and v5 will be fully
removed in a future release.

## Updated `matched-files` API endpoints

A new `strict` parameter has been added to the following API endpoints
below.

- `GET
  /api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/matched-files`
- `GET
  /api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/versions/{componentVersionId}/matched-files`

Default value is `strict=true`. When true, the response returns
matched files for a component with given component ID, component version ID, and
null origin ID. If set to `strict=false`, the response returns
matched files for a component with given component ID, component version ID, and
arbitrary origin ID.

## Deprecation of ReversingLabs public endpoints

The following API endpoints have been deprecated and will be removed in a future
release:

- `/projects/{projectId}/versions/{projectVersionId}/rl-issue-count`
- `/projects/{projectId}/versions/{projectVersionId}/rl-issues/categories`
- `/projects/{projectId}/versions/{projectVersionId}/rl-issues/{categoryId}`
- `/projects/{projectId}/versions/{projectVersionId}/rl-issues/{categoryId}/issues/{ruleId}`
- `/projects/{projectId}/versions/{projectVersionId}/rl-issues/{categoryId}/issues/{ruleId}/files`
- `/projects/{projectId}/versions/{projectVersionId}/rl-files/{fileId}/issues`
- `/projects/{projectId}/versions/{projectVersionId}/rl-rules/{ruleId}`
