---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "jM20mzFYGbMQTYrls7qPXQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:06.869765+00:00"
---

# API enhancements

- New API added that enables bulk confirm/un-confirm ignore/un-ignore of
  snippet matches.

  - ```
    PUT /api/projects/{projectId}/versions/{versionId}/bulk-snippet-bom-entries Media Type: application/vnd.blackducksoftware.bill-of-materials-6+json
    ```
- The following API endpoints have been updated to consider projects the user can
  access via project group membership. The query parameter has also changed from
  `name` to `entityName` for parity with the
  response content.
  - ```
    GET /api/users/{userId}/assignable-projects
    ```
  - ```
    GET /api/users/{userId}/assignable-project-groups/
    ```
  - ```
    GET /api/usergroups/{userGroupId}/assignable-projects
    ```
  - ```
    GET /api/usergroups/{userGroupId}/assignable-project-groups
    ```
