---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "tonABoEQE_uVrKGk7vWFZA"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:35.469726+00:00"
content_hash: "8593648464017b1217806ea60f80050a4cce2e84f3c03375f3d2cc6184dc8c54"
---

# API enhancements

- New API added that enables bulk confirm/un-confirm ignore/un-ignore of snippet matches.

  - ```
    PUT /api/projects/{projectId}/versions/{versionId}/bulk-snippet-bom-entries Media Type: application/vnd.blackducksoftware.bill-of-materials-6+json
    ```
- The following API endpoints have been updated to consider projects the user can access via project group membership. The query parameter has also changed from `name` to `entityName` for parity with the response content.
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
