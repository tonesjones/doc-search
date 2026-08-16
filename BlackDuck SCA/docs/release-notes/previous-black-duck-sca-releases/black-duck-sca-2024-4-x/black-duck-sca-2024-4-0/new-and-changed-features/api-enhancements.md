---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "vYOxOrczR8Phz7r6etljXA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:16.900570+00:00"
---

# API enhancements

For more information on API requests, please refer to the REST API Developers Guide
available in Black Duck.

## New component filter keys for SBOM creator and SBOM name fields

New filter keys have been added to the following API request which return the
possible values for BOM components' SBOM names and creators.:

- `GET
  /api/projects/{projectId}/versions/{projectVersionId}/components-filters`

Filter keys:

- `sbomName`
- `sbomCreator`

## New component filtering support for SBOM creator and SBOM name fields

New filters have been added for the following API request:

- `GET
  /api/projects/{projectId}/versions/{projectVersionId}/components`

Filters:

- `sbomName:<File-UUID>`
- `sbomCreator:<Creator-UUID>`

## New snippet matching REST API request (Generative AI Compliance)

The following API request has been added which allows you to find snippet matches for
a given code snippet:

- `POST /api/snippet-matching`

These matches are sorted by license family to better display the risk a particular
match represents (`PERMISSIVE`, `WEAK_RECIPROCAL`,
`RECIPROCAL`, `RECIPROCAL_AGPL`,
`RECIPROCAL_NETWORK`, `UNKNOWN`).

## Deprecation of matched component API request

The following matched component API request has been deprecated and will be removed
in Black Duck 2024.7.0:

- `GET
  /api/projects/{projectId}/versions/{projectVersionId}/matched-components`
