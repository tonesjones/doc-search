---
title: "API Enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "TOzAbV6Lh8AzpKBjsdsumw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:34:59.555955+00:00"
---

# API Enhancements

For more information on API requests, please refer to the REST API Developers Guide
available in Black Duck SCA.

## New endpoints to support setting Detect parameters

The following API endpoints have been added to support setting Detect parameters in
Black Duck SCA.

- `PATCH api/settings/detect/properties`
- `GET api/settings/detect/properties`

## Removal of [PUT] /api/current-user/tokens/<token-id> links

The `PUT /api/current-user/tokens/<token-id>` endpoint was marked
for deprecation starting in Black Duck SCA 2026.1.0. In
Black Duck SCA 2026.4.0, all meta link references to this
deprecated endpoint has been removed.
