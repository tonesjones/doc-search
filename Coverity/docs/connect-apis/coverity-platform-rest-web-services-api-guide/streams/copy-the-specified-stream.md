---
title: "Copy the specified stream"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/copy-the-specified-stream.html"
content_id: "6GzKhr_I8l6J8Mcut0da_g"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:59.536265+00:00"
---

# Copy the specified stream

Example POST request to create a copy of the specified stream.

**cURL request**

```
curl --location \
--request POST "http://my_connect_host:8080/api/v2/streams/test-c-stream?\
locale=en_us&projectName=test-c" \
--header 'Accept: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "streams": [
    {
      "analysisVersionOverride": null,
      "autoDeleteOnExpiry": false,
      "componentMapName": "Default",
      "description": "This is a test stream - updated",
      "enableDesktopAnalysis": false,
      "language": "MIXED",
      "name": "test-c-stream copy",
      "allowCommitWithoutPassword": null,
      "outdated": false,
      "ownerAssignmentOption": "default_component_owner",
      "pluginVersionOverride": null,
      "primaryProjectName": "test-c",
      "roleAssignments": [],
      "summaryExpirationDays": null,
      "triageStoreName": "Default Triage Store",
      "versionMismatchMessage": null
    }
  ],
  "code": null,
  "message": null
}
```
