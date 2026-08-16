---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "2c1Rq3EALko9jbKac5Pi8g"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:21.506223+00:00"
---

# API enhancements

For more information on API requests, please refer to the REST API Developers Guide
available in Black Duck.

## Public hierarchical BOM APIs to return HTTP 410 Gone

The following APIs have been sunset and now return HTTP 410 Gone. The associated REST
API documentation for these endpoints have also been removed:

- `GET /api/projects/{projectId}/versions/{projectVersionId}/hierarchical-components`
- `PUT /api/projects/{projectId}/versions/{projectVersionId}/hierarchical-components`
- `GET /api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/hierarchical-components/{hierarchicalId}/children`
- `GET /api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/versions/{componentVersionId}/hierarchical-components/{hierarchicalId}/children`

## Behavior Change in Component Vulnerabilities API

As a follow-up to the deprecation announced in 2025.7.0, the `GET
/api/components/<component-id>/vulnerabilities` API endpoint has been
modified in version 2025.10.0 to limit results to the first 10 component versions'
vulnerabilities. This change serves as a performance protection measure for the
system.

Please note that this API remains deprecated and is scheduled for removal in version
2026.1.0. Users are strongly encouraged to transition to the following API
endpoints:

- `GET
  /api/components/<component-id>/versions/<version-id>/vulnerabilities`
- `GET
  /api/components/<component-id>/versions/<version-id>/origin/<origin-id>/vulnerabilities`

These endpoints provide more accurate and efficient access to vulnerability data for
specific component versions and origins.

## Upcoming Deprecation of Update Access Token API

In the 2026.1.0 release, the Update Access Token API (`PUT
/api/current-user/tokens/{tokenId}`) will be deprecated as part of our
ongoing security improvements. After this change, users will no longer be able to
update metadata for existing access tokens.

Users will still be able to:

- Create new access tokens with appropriate metadata
- Regenerate new access tokens
- Delete existing tokens

If you need to modify metadata for an existing token, the recommended approach will
be to delete the existing access token and create a new one with the required
metadata.

This change enhances our security posture while maintaining essential token
management functionality.

## REST API Documentation for Vulnerability Count Views

We have introduced three new endpoints that allow customers to retrieve additional
information from the Black Duck SCA system. These endpoints provide
summarized data, including vulnerability counts and projects with vulnerable
components, based on a specified time range:

- **Get a vulnerability digest summary:**

  `GET /api/vulnerabilities-digest-summary`
- **Get the vulnerability digest:**

  `GET /api/vulnerabilities-digest`
- **Get the project vulnerability digest:**

  `GET /api/project-vulnerabilities-digest`
