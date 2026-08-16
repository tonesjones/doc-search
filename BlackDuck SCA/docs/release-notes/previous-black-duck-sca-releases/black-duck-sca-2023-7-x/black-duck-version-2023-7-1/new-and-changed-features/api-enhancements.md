---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "7i0coJKE0VPbDA~wE~btlQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:45.695501+00:00"
---

# API enhancements

For more information on API requests, please refer to the REST API Developers Guide available in Black
Duck.

## New component metadata lookup via pURL API request

The following API request can be used to search a single component by using a package
URL as search term. The response provides endpoints to fetch detailed information
about the component, version and variant:

- `GET /api/search/kb-purl-component`

## Updated components API endpoint response

The response of the following components API endpoint has been updated to include the
`bomMatchInclusion` filter option (`true` or
`false`) used in the request:

- `/api/projects/{projectId}/versions/{projectVersionId}/components`
