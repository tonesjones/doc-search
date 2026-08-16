---
title: "API Enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "IpuEgDQeg9d0miQjyMybPw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:10.272138+00:00"
---

# API Enhancements

For more information on API requests, please refer to the REST API Developers Guide
available in Black Duck SCA.

## Update: Report Creation Endpoints

The following report creation endpoints now have the project version ID in the
request payload changed from required to optional:

- `POST /api/versions/{projectVersionId}/reports`
- `POST /api/versions/{projectVersionId}/license-reports`
- `POST
  /api/projects/{projectId}/versions/{projectVersionId}/sbom-reports`
- `POST
  /api/lts-projects/{projectId}/lts-project-versions/{projectVersionId}/sbom-reports`

If the project version ID is provided in the request payload, it must match the
project version ID specified in the API URI.

## Deprecated Vulnerabilities API Removed

As a follow-up to the deprecation announced in 2025.10.0, the `GET
/api/components/<component-id>/vulnerabilities` API endpoint has been
modified in version 2026.1.0 to return `HTTP 410 Gone`.

Users are strongly encouraged to transition to the following API endpoints:

- `GET
  /api/components/<component-id>/versions/<version-id>/vulnerabilities`
- `GET
  /api/components/<component-id>/versions/<version-id>/origin/<origin-id>/vulnerabilities`

These endpoints provide more accurate and efficient access to vulnerability data for
specific component versions and origins.

## Deprecation and Removal of Data Retention APIs

The following changes have been made to the Data Retention API endpoints:

- `GET /api/settings/data-retention` (v4 and v5) — These
  endpoints have been **removed** and are no longer available.
- `PATCH /api/settings/data-retention` (v4 and v5) — These
  endpoints are now **deprecated** and will be removed in a future
  release.
- `GET /api/settings/data-retention` (v6) and `PATCH
  /api/settings/data-retention` (v6) — These endpoints remain
  **fully supported and available**.

These updates retire legacy versions of the Data Retention APIs and consolidate
ongoing support into the v6 endpoints.

## API Changes: ARCHIVED Phase No Longer Supported

The following APIs no longer accept the `ARCHIVED`
`phase` as part of their requests:

- `POST /api/projects/{projectID}/versions`
- `PUT /api/projects/{projectID}/versions/{projectVersionID}`

Users who previously utilized the ARCHIVED phase in these endpoints will need to
update their API calls accordingly. Please refer to the API documentation for
current supported phases and recommended alternatives.

## Deprecation of User Token API

The following API related to user tokens have been deprecated and will be removed
in a future update. It will now return `HTTP 410 Gone`:

- `PUT /api/current-user/tokens/<token-id>`
