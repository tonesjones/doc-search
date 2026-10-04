---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "nrkAZsIGrIGk4coaJM2Piw"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:28.874861+00:00"
content_hash: "cf406dd0a30469851a06d87c01623e7feceefc93c28f9370755fbe0d1f28dc6f"
---

# API enhancements

For more information on API requests, please refer to the REST API Developers Guide available in Black Duck.

## New bulk LTS vulnerability remediation API endpoints

The following new API endpoints have been added to support bulk vulnerability remediation on LTS project versions. These endpoints follow RESTful standards and address limitations in the previous implementation at `/api/lts-projects/{projectId}/lts-project-versions/{versionId}/remediation`. They are designed to provide consistent functionality both Active and LTS projects, including integration with the LTS Affected Projects search functionality.

These new endpoints are temporary and will be replaced in a future release when the LTS vulnerability remediation APIs are fully reworked.

The new endpoints are:

- For bulk LTS vulnerability remediation:

  - `PUT /api/vulnerabilities/{vulnerabilityId}/lts-remediation`
- For single LTS vulnerability remediation:

  - `GET /api/lts-projects/{projectId}/lts-project-versions/{projectVersionId}/components/{componentId}/versions/{componentVersionId}/vulnerabilities/{vulnerabilityId}/remediation`
  - `PUT /api/lts-projects/{projectId}/lts-project-versions/{projectVersionId}/components/{componentId}/versions/{componentVersionId}/vulnerabilities/{vulnerabilityId}/remediation`
  - `GET /api/lts-projects/{projectId}/lts-project-versions/{projectVersionId}/components/{componentId}/versions/{componentVersionId}/origins/{originId}/vulnerabilities/{vulnerabilityId}/remediation`
  - `PUT /api/lts-projects/{projectId}/lts-project-versions/{projectVersionId}/components/{componentId}/versions/{componentVersionId}/origins/{originId}/vulnerabilities/{vulnerabilityId}/remediation`

## Deprecation of the component vulnerabilities API endpoint

The following API endpoint is now marked as deprecated:

- `GET /api/components/<component-id>/vulnerabilities`

To enhance accuracy, vulnerabilities are more effectively mapped to:

- Component versions:

  `GET /api/components/<component-id>/versions/<version-id>/vulnerabilities`
- Component origins:

  `GET /api/components/<component-id>/versions/<version-id>/origin/<origin-id>/vulnerabilities`

As a result, we recommend that customers transition their usage to the documented endpoints for component version vulnerabilities and component origin vulnerabilities. A future version will limit the amount of data returned from the deprecated endpoint, followed by a subsequent version that will fully remove the API. Users are encouraged to update their implementations accordingly to ensure continued access to vulnerability data.
