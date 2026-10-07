---
title: "Create a stream"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/create-a-stream.html"
content_id: "PKDkjvb_XBBb4uW3jteCcQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:09.579670+00:00"
---

# Create a stream

Example POST request to create a stream.

**cURL request**

```
curl --location \
--request POST "http://my_connect_host:8080/api/v2/streams?locale=en_us" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "name": "test-c-stream",
  "description": "This is a test stream",
  "triageStoreName": "Default Triage Store",
  "primaryProjectName": "test-c",
  "ownerAssignmentOption": "default_component_owner",
  "autoDeleteOnExpiry": true,
  "enableDesktopAnalysis": true,
  "outdated": true,
  "summaryExpirationDays": 30,
  "analysisVersionOverride": "2021.06",
  "pluginVersionOverride": "1.7.5",
  "componentMapName": "Default",
  "versionMismatchMessage": "wrong version",
  "roleAssignments": [
    {
      "roleAssignmentType": "user",
      "roleName": "streamOwner",
      "scope": "stream",
      "username": "foo"
    },
    {
      "group": {
        "name": "Users"
      },
      "roleAssignmentType": "group",
      "roleName": "developer",
      "scope": "stream"
    }
  ]
}'
```
