---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "fEulCE2MCh~GsO09DW4V3g"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:31.935059+00:00"
content_hash: "ade1eea419973cc46cb61ed80f34b3a55a84df4d6d31161086637de2dd284f94"
---

# API enhancements

For more information on API requests, please refer to the REST API Developers Guide available in Black Duck.

## New component metadata lookup via pURL API request

The following API request can be used to search a single component by using a package URL as search term. The response provides endpoints to fetch detailed information about the component, version and variant:

- `GET /api/search/kb-purl-component`

## Updated components API endpoint response

The response of the following components API endpoint has been updated to include the `bomMatchInclusion` filter option (`true` or `false`) used in the request:

- `/api/projects/{projectId}/versions/{projectVersionId}/components`
