---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "5mSZLCAn8tMPsPtVUx~qRg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:59.912884+00:00"
---

# API enhancements

## Updated components endpoints

The following public API endpoints have been updated to allow the updating of
component, version and origin id.

- PUT /api/projects/{projectId}/versions/{projectVersionId}/components
- PUT /api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/versions/{componentVersionId}

## New JobHistoryAppService API endpoints

Two new public REST API endpoints have been added which uses the JobRuntimeRepository
to get information about job runtimes and provide information about them:

- `/api/jobs-histories`
- `/api/jobs-histories-filters`

## New JobRuntimeAppService API endpoint

Two new public REST API endpoints have been added which uses the JobRuntimeRepository to
get information about job runtimes and provide information about them:

- `/api/jobs-runtimes`
- `/api/jobs-runtimes-filters`

Please note that you should use the `/api/job-runtimes` endpoint to
view running jobs. The existing `/api/jobs` endpoint will be
deprecated in favor of the new endpoint.

## New JobScheduleAppService API endpoint

Three new public REST API endpoints have been added which outputs a list of jobs that
are scheduled on the system.

- `/api/jobs-schedules`
- `/api/jobs/schedulers/{scheduler}/trigger-groups/{triggerGroup}/triggers/{triggerId}`
- `/api/jobs-schedules-filters`

Please note that you should use the `/api/job-schedules` endpoint to
view scheduled jobs. The existing `/api/jobs` endpoint will be
deprecated in favor of the new endpoint.

## New JobRunner API endpoint

A new public REST API endpoint has been added which allow users to enable/disable
periodic jobs. Please note that changing settings in this way can cause unexpected
behavior on your system.

- `/api/jobs-schedules-configurations`

## New centralized Detect version management API endpoints

The following endpoints have been added to support the new centralized Detect version
management functionality offered in Black Duck 2023.4.0:

- `GET /api/settings/detect`

  - Gets the current detect version management settings
  - If accessed by an authenticated non-system administrator user, they
    will only receive `detectUri` (if it has a value)
  - If accessed by an authenticated system administrator user, they will
    receive the following information:

    - `detectUri`: The Detect URI saved by a system
      administrator.
    - `useInternalHosting`: Boolean, determines the
      type of hosting used for Detect (internally hosted or
      Black Duck hosted). Returns false if not using an internally
      hosted version of Detect.
    - `useMajorVersion`: Boolean, determines if the
      latest of a major version of Detect is used. Returns true if
      "Latest 8.x" or "Latest 7.x" was selected in UI.
    - `selectedVersion`: String, returns the version
      of Detect used.
    - `allowDowngrade`: Boolean, notifies if the
      system setting allows the user use an older version of
      Detect.
    - `majorVersions`: String, the list of current
      valid major versions of Detect.
    - `allVersions`: String, the list of all current
      valid versions of detect.
- `PATCH /api/settings/detect`

  - Updates the detect version management settings
  - Requires authenticated access by a system administrator user
  - Updates the following information:

    - `detectUri`: Internal Detect URI.
    - `useInternalHosting`: Boolean, sets the type
      of hosting used for Detect (internally hosted or Black Duck
      hosted).
    - `useMajorVersion`: Boolean, sets the latest
      major version or an explicit version of Detect. Updated and
      required if `useInternalHosting` is
      false.
    - `selectedVersion`: String, the Detect version
      to use, either a major version or exact version. Only
      updated if `useInternalHosting` is false.
    - `allowDowngrade`: Boolean, if managed, allows
      earlier versions of Detect to be used.

## Deprecation of PUT /api/settings/data-retention

As mentioned in the 2022.10.0 release notes, `PUT
/api/settings/data-retention` has been deprecated and replaced with
`PATCH /api/settings/data-retention`. In Black Duck 2023.4.0,
`PUT /api/settings/data-retention` will now return a HTTP 405
METHOD_NOT_ALLOWED error message.
