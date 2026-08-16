---
title: "API Enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "nBOdKxi3Bylk1ODUINf80w"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:53.912369+00:00"
---

# API Enhancements

## Permission fixes to GET /api/project-groups

The following fixes have been made to the `GET
/api/project-groups` api endpoints:

- `GET api/project-groups` will only return the project
  groups the user is authorized to view as search results.
- `GET api/project-groups/<project group ID>` will
  return a HTTP 200 OK for users with the Super User role or a HTTP
  403 FORBIDDEN response otherwise.

## Permission changes to GET /api/users/{userId}

The `GET /api/users/{userId}` endpoint now no longer has a
permission check (previously required a USERMGMT_READ check).

- The `GET /api/users/`endpoint (that lists all users)
  will continue to be protected with the USERMGMT_READ
  permissions.
- The projectOwner user (regardless of the user's permission status) in
  the `/api/projects/{projectId}` API will still be
  provided.
- The USERMGMT_READ permission that was added to project roles in Black
  Duck version 2021.8.2 will still be removed.

## New filter parameter for GET /api/project-groups

A new filter parameter called `exactName` has been added to help
find specific project groups. When true, the `exactName` filter
will ensure only the project group that matches the name value in
`q` is returned. The search criteria for the project group is
case-insensitive. If none match, then nothing is returned. Also, the
`q` parameter must be specified when the `exactName`filter is true otherwise no project groups will be returned.

See below for how the filter is used in a `/api/project-groups`
request:

```
/api/project-groups?q=name:<project group name>&filter=exactName:true
```

## Improved CPE Support APIs

Three new public APIs have been added:

- `GET /api/cpes` [Requires a searchParam. Returns matching
  CPE IDs]
- `GET /api/cpes/{cpeId}/versions` [Returns
  component-versions matching the CPE ID]
- `GET /api/cpes/{cpeId}/variants` [Returns
  component-origins matching the CPE ID]

## Copyright 2.0 data and new legacy endpoint

Black Duck is now rolling out Copyright 2.0 data using the existing endpoint
(below) to serve this new copyright data. No response fields are being dropped
or added.

```
GET /api/components/{componentId}/versions/{componentVersionId}/origin/{originId}/file-copyrights
```

We will continue to serve Copyright 1.0 (aka legacy) data by creating a new
endpoint :

```
GET /api/components/{componentId}/versions/{componentVersionId}/origin/{originId}/file-copyrights-legacy
```

Note: This new endpoint is not directly used in Black Duck UI, only through the
public API directly. Also, since the existing endpoint will now return Copyright
2.0 data, all Black Duck customers (regardless of the version they use) should
see this new data.

## Exposure of lastScanDate through a Public API

The following API will now expose `lastScanDate` in the Public API
response:

- ```
  GET /api/projects/{projectId}/versions/{projectVersionId}/bom-status
  ```
