---
title: "API Enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "B8Nx47Y4Ztj6pGy0vpiI7w"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:27.730947+00:00"
content_hash: "240a72d4a133475cc60493f7d7915f5a67b0bf2351f4c345f02eea4d34c0639e"
---

# API Enhancements

For more information on API requests, please refer to the REST API Developers Guide available in Black Duck SCA.

## New endpoints to support setting Detect parameters

The following API endpoints have been added to support setting Detect parameters in Black Duck SCA.

- `PATCH api/settings/detect/properties`
- `GET api/settings/detect/properties`

## Removal of [PUT] /api/current-user/tokens/<token-id> links

The `PUT /api/current-user/tokens/<token-id>` endpoint was marked for deprecation starting in Black Duck SCA 2026.1.0. In Black Duck SCA 2026.4.0, all meta link references to this deprecated endpoint has been removed.
