---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "hFgybwZsGbUWn4iWJeBh5A"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:54.895848+00:00"
---

# API enhancements

For more information on API requests, please refer to the REST API Developers Guide
available in Black Duck.

## New and updated endpoints for Multi-Factor Authentication (MFA)

As part of the new Multi-Factor Authentication (MFA) feature, the following new API
endpoints have been introduced:

- **Get Current User MFA Secret**

  `GET /api/current-user/mfa`
- **Setup MFA for current user**

  `POST /api/current-user/mfa`
- **Reset MFA for current user**

  `DELETE /api/current-user/mfa`
- **Reset MFA for user**

  `DELETE /api/users/{userId}/reset-mfa`
- **Authenticate MFA for current user**

  `POST /api/mfa/authenticate`

In addition, the responses for the following endpoints have been updated to include
information on whether each user has Multi-Factor Authentication (MFA) set up.

- **Listing Users**

  `GET /api/users`
- **Reading the Current User**

  `GET /api/current-user`

## New endpoints for file adjustments

As part of the file adjustment simplification, the following new API endpoints have
been introduced to support the path-based adjustment process:

- **Create or update file adjustments**

  `PUT
  /api/projects/{projectId}/versions/{projectVersionId}/file-adjustments`
- **Delete file adjustments**

  `DELETE /api/projects/{projectId}/versions/{projectVersionId}/file-adjustments`

## Updated `users` and `current-user` endpoints

The `GET /api/users` and `GET /api/current-user`
endpoint response has been updated to include information on whether each user has
Multi-Factor Authentication (MFA) set up.

## New endpoints for container multi-part uploads

New API endpoints have been introduced to enhance the file upload process with
container multi-part uploads. These endpoints allows you to upload large files in
smaller chunks, improving efficiency and reliability. The new endpoints are:

- **Start Upload**

  `POST /api/storage/containers/{container_id}/multipart`
- **Upload Part of File**

  `PUT /api/storage/containers/{container_id}/multipart`
- **Finish Upload Request**

  `POST
  /api/storage/containers/{container_id}/multipart/completed`
- **Cancel Upload Request**

  `DELETE /api/storage/containers/{container_id}/multipart`

For detailed usage and payload instructions, please refer to the REST API Developers
Guide available in Black Duck.

## SBOM fields API discontinuation notice

As of Black Duck 2024.10.0, the following three sbom-fields APIs
have been discontinued and will return a `410 GONE` response with no
content:

- **Listing SBOM Field Scopes**

  `GET /api/sbom-fields/scopes`
- **Listing SBOM Fields In Scope**

  `GET /api/sbom-fields/scopes/{scopeName}/fields`
- **Updating a SBOM Field’s Status**

  `PUT /api/sbom-fields/scopes/{scopeName}/fields/{fieldId}`

These APIs have also been removed from the REST API Developer's Guide, and will be
fully removed in an upcoming release.

## Deprecated LTS API endpoints

The following LTS API endpoints have been deprecated and will be removed in an
upcoming release:

- **Updating a LTS Project by projectId**

  `PUT /api/lts-projects/{projectId}`

  LTS projects can be updated with the `PUT
  /api/projects/{projectId}` endpoint.
- **Deleting a LTS Project by projectId**

  `DELETE /api/lts-projects/{projectId}`

  LTS projects can be deleted with the `DELETE
  /api/projects/{projectId}` endpoint.
- **Updating a LTS Project Version**

  `PUT /api/lts-projects/{projectId}/lts-project-versions/{projectVersionId}`

  LTS project version information can be updated with the `PUT
  /api/projects/{projectId}/versions/{projectVersionId}`
  endpoint.

## Added HATEOAS links to API endpoints

The following endpoints have been updated to include HATEOAS links in their
responses. These links provide dynamic navigation and allow clients to discover
available actions or related resources without needing to hardcoded URLs.

- **Updating a Project Version’s BOM State**

  `PUT /api/projects/{projectId}/versions/{projectVersionId}/transition`
- **Reading LTS Projects**

  `GET /api/lts-projects`
- **Reading a LTS Project by projectId**

  `GET /api/lts-projects/{projectId}`
- **Updating a LTS Project by projectId**

  `PUT /api/lts-projects/{projectId}` (DEPRECATED)
- **Deleting a LTS Project by projectId**

  `DELETE /api/lts-projects/{projectId}` (DEPRECATED)

Although two of these endpoints are deprecated, they have also received HATEOAS links
as part of the update to the non-deprecated endpoints. While this update was
intended primarily for the active endpoints, the deprecated ones were impacted due
to shared response formatting.
