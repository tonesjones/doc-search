---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "_vsfcDMmBGGynYP_JrHRWg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:25.286380+00:00"
---

# API enhancements

For more information on API requests, please refer to the REST API Developers Guide
available in Black Duck.

## New scan monitoring API endpoint

A new REST API endpoint has been added which analyzes scan error rates and allows you to get
the scan monitoring information from terminal scans in the system in a given time
frame (default is set to the last hour):

- `GET /api/scan-monitor`

Request parameters are as follows:

- `level` (*mandatory*). Number value `1` or
  `2`, default is `1`.

  Example request:
  `GET /api/scan-monitor?level=1`

  Level
  `1` is a simple binary response, either
  `OK` or `NOT OK` if the failure rate
  exceeds the set maximum threshold amount (default is 30%).

  Level
  `2` returns a hex color code (green, yellow, or red)
  depending on the status. Green (`#00FF00`) indicates that the
  failure rate in the monitored timeframe (default is the last hour) is less
  than the set minimum threshold amount (default is 10%). Yellow
  (`#FFFF00`) indicates that the failure rate is between
  the minimum and maximum thresholds (10% and 30%). Red
  (`#FF0000`) indicates that the failure rate is greater
  than the maximum threshold amount (30%).

## Enhanced handling of null values for custom fields

The following public API requests have been updated to return an error message if the
custom field values are null:

- `PUT
  /api/projects/{projectId}/custom-fields/{customFieldId}`
- `PUT
  /api/projects/{projectId}/versions/{projectVersionId}/custom-fields/{customFieldId}`
- `PUT
  /api/components/{componentId}/custom-fields/{customFieldId}`
- `PUT
  /api/components/{componentId}/versions/{componentVersionId}/customfields/{customFieldId}`
- `PUT
  /api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/custom-fields`
- `PUT
  /api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/custom-fields/{customFieldId}`
- `PUT
  /api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/versions/{componentVersionId}/custom-fields`
- `PUT
  /api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/versions/{componentVersionId}/custom-fields/{customFieldId}`

## Updated notification endpoints

The following REST API public endpoints have been updated to return the
`notifyUser` field based on whether the user should receive
notifications for the subscription:

- `GET
  /api/users/{userId}/notification-subscriptions/{subscriptionId}`
- `GET /api/users/{userId}/notification-subscriptions`

## New BOM status endpoint

A new REST API endpoint has been created to determine when a BOM has been updated for
a given scan:

- `GET
  /api/projects/{projectId}/versions/{versionId}/bom-status/{scanId}`

Possible status values are `NOT_INCLUDED`, `BUILDING`,
`SUCCESS`, `FAILURE`.

## Deprecation of PUT /api/settings/auto-remediate-unmapped

In Black Duck 2022.4.1, the public endpoint `PUT
/api/settings/auto-remediate-unmapped` was changed to `PATCH
/api/settings/auto-remediate-unmapped` but the `PUT`
endpoint was deprecated and kept in order to maintain backward supportability. As of
this release, the `PUT /api/settings/auto-remediate-unmapped`
endpoint is now deleted.

## Deprecation and removal of licenses API requests

The following API requests have been removed:

- `GET /api/licenses/{licenseId}/obligations`
- `GET /api/licenses/{licenseId}/obligations-filters`

As a result of the removal of `GET
api/licenses/{licenseId}/obligations`, the obligation API will no longer
be returned by any APIs. The license term API
(`/api/licenses/{licenseId}/license-terms`) will be returned
instead.

In addition, the following API requests have been deprecated:

- `GET /api/licenses`
- `POST /api/licenses`
- `GET /api/licenses-filters`
- `GET /api/licenses/{licenseId}`
- `PUT /api/licenses/{licenseId}`
- `GET /api/licenses/{licenseId}/text`
- `PUT /api/licenses/{licenseId}/text`

## New and enhanced component endpoints

A new REST API endpoint has been added to get/modify SBOM field values on component
level:

- `GET /api/components/{componentId}/sbom-fields`
- `PUT /api/components/{componentId}/sbom-fields`

The following REST API endpoint has been enhanced to get SBOM field values for a
component which includes `sbom-field` endpoint in meta/links section
:

- `GET /api/components/{componentId}`

## New PATCH /api/settings/data-retention endpoint

The new `PATCH /api/settings/data-retention` REST API endpoint will
replace the existing `PUT /api/settings/data-retention`. As a result,
`PUT /api/settings/data-retention` has been deprecated and will
be removed in an upcoming release.

## New Dependency Upgrade Guidance public API endpoint

A new REST API endpoint has been added to provide data for Dependency Upgrade
Guidance:

- `GET
  /api/components/{componentId}/versions/{componentVersionId}/origins/{originId}/transitive-upgrade-guidance`

## Updated /api/projects/{projectId}/versions/{projectVersionId}/matched-files endpoint

The
`/api/projects/{projectId}/versions/{projectVersionId}/matched-files`
endpoint now includes a "matchTypeFilterValue" flag to better handle inconsistency
when viewing the results. The following table displays how
`matchType` is mapped to `matchTypeFilterValue`:

|  |  |
| --- | --- |
| matchType | matchTypeFilterValue |
| FILE_EXACT | FILES_EXACT |
| FILE_EXACT_FILE_MATCH | FILE_EXACT |
| FILE_SOME_FILES_MODIFIED | FILES_MODIFIED |
| FILE_DEPENDENCY_DIRECT | FILE_DEPENDENCY_DIRECT |
| FILE_DEPENDENCY_TRANSITIVE | FILE_DEPENDENCY_TRANSITIVE |
| FILE_FILES_ADDED_DELETED_AND_MODIFIED | FILES_ADDED_DELETED |
