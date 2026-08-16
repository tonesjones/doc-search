---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "DAr~8puJmhVuajbVX3YXDg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:49.099671+00:00"
---

# API enhancements

## Removal of PUT /api/settings/data-retention

As mentioned in the 2023.4.0 release notes, `PUT
/api/settings/data-retention` was deprecated in favor of `PATCH
/api/settings/data-retention` and would return a HTTP 405
METHOD_NOT_ALLOWED error message when invoked. It has now been completely removed in
Black Duck 2023.7.0 and will now return a HTTP 404 NOT_FOUND error message if
used.

## Deprecation of GET api/external-config/detect-uri

The `GET api/external-config/detect-uri` API request has been
deprecated and replaced by `GET api/settings/detect`. Users can still
use the old API while it is deprecated.

Authenticated users with no roles can still use `GET
api/external-config/detect-uri` to get the API string while it is
deprecated. If those users use the `GET api/settings/detect` API,
they will get the detectUri (if it is set) and nothing else.

## Improved performance for PUT /api/policy-rules/{policyRuleId}

Performance for the `PUT /api/policy-rules/{policyRuleId}` API request
has been improved by limiting policy profile calculations to only run when a change
in violation is found after evaluating components in a project version.

## Updated POST api/components/{componentId}/versions

The `POST api/components/{componentId}/versions` API request has been
updated to allow users to map an external ID to a new custom component version when
created.

## New public SBOM field endpoint

The `PUT
/api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/sbom-fields`
endpoint updates the saved values for sbom fields for a BOM component.
