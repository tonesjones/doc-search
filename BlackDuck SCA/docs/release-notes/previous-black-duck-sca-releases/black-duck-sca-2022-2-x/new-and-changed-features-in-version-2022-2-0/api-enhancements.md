---
title: "API Enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "J6jRpKxzADuFkkcxBboK0w"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:46.499042+00:00"
---

# API Enhancements

For more details on new or changed API requests, please refer to the API doc
available in Blackduck.

## New Signed Authentication Request Field

A new `sendSignedAuthenticationRequest` field has been added to
the API request below to determine whether Blackduck should send signed
authentication request to IdP. The default value for this field is FALSE. The
Meta link to download certificate will be available only if the Signed
Authentication Request configuration is set to TRUE.

- ```
  GET, POST /api/sso/configuration
  ```

## New /api/active-users Endpoint

This new query will return all the user last-login information for users who have
logged into the system since the provided date. This query takes the same
`sinceDays` query parameter as dormant-users.

## New Project Version Report Endpoints

The following public endpoints have been added to support all version reports
regardless of type (Notices File, Version Report, Vulnerability Remediation,
Vulnerability Status, Vulnerability Update, Software Bill of Materials
Report):

- ```
  GET /api/projects/{projectId}/versions/{projectVersionId}/reports
  ```
- ```
  GET /api/projects/{projectId}/versions/{projectVersionId}/reports/{reportId}
  ```
- ```
  DELETE /api/projects/{projectId}/versions/{projectVersionId}/reports/{reportId}
  ```
- ```
  GET /api/projects/{projectId}/versions/{projectVersionId}/reports/{reportId}/contents
  ```
- ```
  GET /api/projects/{projectId}/versions/{projectVersionId}/reports/{reportId}/download
  ```

## New Policy Rules Public Endpoint

A new public API request has been added to retrieve active policy rules:

- ```
  GET /api/projects/{projectId}/versions/{projectVersionId}/policy-rules
  ```

## New /api/cpes/{cpeId}/origins Endpoint

With Blackduck 2022.2.0, the `/api/cpes/{cpeId}/variants` endpoint
will be deprecated, to be replaced with
`/api/cpes/{cpeId}/origins`. The
`/api/cpes/{cpeId}/variants` will be removed in Blackduck
2022.4.0. The API link in the metadata for `/api/cpes` has also
been updated to return `/api/cpes/{cpeId}/origins` instead of
`/api/cpes/{cpeId}/variants`.

## Page Limit Maximums on API Requests

The following API requests now have a page limit maximum in order to better
moderate system resource usage. The limit is currently set to 1000 items.

- ```
  GET /api/projects/<id>/versions/<id>/components
  ```
- ```
  GET /api/projects/<id>/versions/<id>/vulnerable-bom-components
  ```
- ```
  GET /api/codelocations
  ```
- ```
  GET /api/projects/<id>/versions
  ```
- ```
  GET /api/projects
  ```
- ```
  GET /api/users
  ```

## New Sorting filter for API Endpoints

A new sort option called `parentProjectGroupName` is available for
the following API endpoints. This will allow for sorting project versions by
parent project group name.

- ```
  /api/search/project-versions
  ```
- ```
  /api/watched-projects
  ```
- ```
  /api/dashboards/users/{id}/saved-searches/{id}
  ```

## New GET /api/scan-readiness API Endpoint

A new public API endpoint has been added which provides the readiness state of
all scan containers.

- ```
  GET /api/scan-readiness
  ```

Sample response:

```
{
	"readiness": "ACCEPTING",
	"items": [
		{
			"id": "9dc7653a462b",
			"service": "scan",
			"readiness": "ACCEPTING",
			"updatedAt": "2021-12-21T17:26:01.495Z",
			"versionId": 1
		}
	]
}
```

- In a multiple scan replica environment, if all scan container replicas
  are healthy, the aggregated state will be `ACCEPTING`.
  The system can accept and process new scans without issue.
- In a multiple scan replica environment, if one scan container is not
  healthy and other replicas are healthy the aggregated state will be
  `PARTIAL`. In this state, the system is becoming
  overloaded. Scan performance may be degraded. Scans have a slight chance
  of timing out or failing.
- In a multiple scan replica environment, if all the scan containers are
  not healthy, the aggregated state will be `DEGRADED`. The
  system is overloaded cannot accept new scans. If set to reject, new scan
  requests will not be accepted and a HTTP 429 return code will be sent
  back.
- If a container goes down, its entry will be removed after 5 minutes
  (interval which is configurable).

## Updated Response for GET /api/codelocations/{codeLocationId}/scan-summaries

The `scanType` value found in the API response generated for the
`/api/codelocations/{codeLocationId}/scan-summaries` will now
split into different types to avoid ambiguity. The new values now include:

- ```
  PACKAGE_MANAGER
  ```
- ```
  BINARY
  ```
- ```
  BOM_IMPORT
  ```
- ```
  SIGNATURE
  ```

Traditional scans will still use `BDIO` for
`scanType` value.

Please note that this change was introduced in Black Duck 2021.8.0.
