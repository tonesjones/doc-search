---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "9W2RkxX3aIPgxz1Y5tsv8A"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:05.465379+00:00"
---

# API enhancements

For more information on API requests, please refer to the REST API Developers Guide
available in Black Duck.

## New `ltsReleaseCount` property for risk-profile-dashboard request

A new property has been added to the `GET /api/risk-profile-dashboard`
API request. The `ltsReleaseCount` property returns the number of
versions that are converted to LTS.

## Updated /api/versions/{projectVersionId}/license-reports (POST)

The categories LICENSE_TEXT and LICENSE_DATA are no longer added to all notices
reports. If the request includes no categories, it will default to LICENSE_TEXT and
LICENSE_DATA. If the request includes DEEP_LICENSE_DATA or FILE_LICENSE_DATA,
LICENSE_TEXT and LICENSE_DATA is added to the request. In all other cases, the
report will only include the categories in the API request.

## Updated vulnerable-bom-components API request

A new, optional `showUnscoredRelatedVulnerability` request parameter has been
added to the `GET
/api/projects/{projectId}/versions/{projectVersionId}/vulnerable-bom-components`
API request. This parameter accepts a true/false value to include or exclude
unscored related vulnerabilities in the response for the vulnerable-bom-components
API.

If the parameter is not included or is set to false, the API response will remain
consistent with the existing behavior. When set to true BDSAs will always list
related CVEs, even if the affect component version ranges differ between the BDSA
and CVE. This is to aid customers who use the CVE ID as a part of downstream
vulnerability processes.

## API deprecation notice

As of Black Duck 2024.7.1, the following three APIs have been
marked as deprecated and will be removed in an upcoming release:

- `GET /api/sbom-fields/scopes`
- `GET /api/sbom-fields/scopes/{scopeName}/fields`
- `PUT /api/sbom-fields/scopes/{scopeName}/fields/{fieldId}`
