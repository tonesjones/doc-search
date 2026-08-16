---
title: "Update a stream"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/update-a-stream.html"
content_id: "2LdyuShK_8r61cImFXHvkw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:58.894879+00:00"
---

# Update a stream

Example PUT request to update the specified stream.

**cURL request**

```
curl --location \
--request PUT "http://my_connect_host:8080/api/v2/streams/test-c-stream?locale=en_us" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "name": "test-c-stream",
  "description": "This is a test stream - updated",
  "primaryProjectName": "test-c",
  "outdated": false,
  "analysisVersionOverride": "2021.03",
  "autoDeleteOnExpiry": true,
  "componentMapName": "Default",
  "enableDesktopAnalysis": false,
  "ownerAssignmentOption": "default_component_owner",
  "pluginVersionOverride": "1.7.2",
  "roleAssignments": [
    {
      "roleAssignmentType": "user",
      "roleName": "streamOwner",
      "scope": "stream",
      "username": "bar"
    }
  ],
  "summaryExpirationDays": 31,
  "triageStoreName": "Default Triage Store",
  "versionMismatchMessage": "version 2021.03 should be used"
}'
```
