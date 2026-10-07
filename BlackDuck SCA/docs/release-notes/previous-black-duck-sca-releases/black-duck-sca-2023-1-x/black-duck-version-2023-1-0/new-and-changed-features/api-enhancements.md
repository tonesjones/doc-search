---
title: "API Enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "WX3RsiGBV1FpePkKGWtqWw"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:32.941909+00:00"
content_hash: "e5f5af6af2c6e71110b4f9782dff428abb919c1c136145f274f64e76dee61125"
---

# API Enhancements

For more information on API requests, please refer to the REST API Developers Guide available in Black Duck.

## Enhanced project endpoints

The following endpoints have been updated to include OSS component pURL coordinates:

- `/api/projects/<projectId>/versions/<projectVersionId>/components`
- `/api/projects/<projectId>/versions/<projectVersionId>/vulnerable-bom-components`
- `/api/projects/<projectId>/versions/<projectVersionId>/components?filter=licensePolicy`

## Updated data-retention API endpoint

The following endpoint has been changed from a PUT to a PATCH request:

- `/api/settings/data-retention`

## New tool list API endpoint

A new public endpoint is now available to list all available tool versions:

- `/api/tools`

## New fetch for SBOM fields for specific project group

A new public endpoint is now available to read a project's SBOM fields:

- `/api/project-groups/{projectGroupId}/sbom-fields`
