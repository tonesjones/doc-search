---
title: "API Enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "WYAt6yRh8Gk6IY6b1ygqjA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:30.818943+00:00"
---

# API Enhancements

For more details on new or changed API requests, please refer to the API doc
available in Black Duck.

## New scan monitoring API endpoint

A new REST API endpoint has been added which analyzes scan error rates and allows you to get
the scan monitoring information from terminal scans in the system in a given time
frame (default is set to the last hour):

- `GET /api/scan-monitor`

Request parameters are as follows:

- `level` (*mandatory*). Number value 1 or 2 or 3, default is '1'.

  Example request: `GET
  /api/scan-monitor?level=1`

  Level 1 is a simple binary
  response, either `OK` or `NOT OK` if the
  failure rate exceeds the set maximum threshold amount (default is 30%).

  Level 2 returns a hex color code (green, yellow, or red) depending on
  the status. Green (#00FF00) indicates that the failure rate in the monitored
  timeframe (default is the last hour) is less than the set minimum threshold
  amount (default is 10%). Yellow (#FFFF00) indicates that the failure rate is
  between the minimum and maximum thresholds (10% and 30%). Red (#FF0000)
  indicates that the failure rate is greater than the maximum threshold amount
  (30%).

  Level 3 returns aggregated scan counts based on scan
  states.

  The monitored timeframe, minimum, and maximum thresholds can
  all be configured in the `blackduck-config.env` file for your
  environment.

## Enhanced handling of null values for custom fields

The following public API requests have been updated to return an error message if the custom field values are null:

- `PUT /api/projects/{projectId}/custom-fields/{customFieldId}`
- `PUT /api/projects/{projectId}/versions/{projectVersionId}/custom-fields/{customFieldId}`
- `PUT /api/components/{componentId}/custom-fields/{customFieldId}`
- `PUT /api/components/{componentId}/versions/{componentVersionId}/custom-fields/{customFieldId}`
- `PUT
  /api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/custom-fields`
- `PUT /api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/custom-fields/{customFieldId}`
- `PUT /api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/versions/{componentVersionId}/custom-fields`
- `PUT /api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/versions/{componentVersionId}/custom-fields/{customFieldId}`
