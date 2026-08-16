---
title: "Retrieve a stream"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-a-stream.html"
content_id: "O5xDhKVzay05HxDPpM1xRA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:57.617868+00:00"
---

# Retrieve a stream

Example GET request to retrieve the specified stream.

**cURL request**

```
curl --location \
--request GET "http://localhost:8080/api/v2/streams/test-c-stream?locale=en_us" \
--header 'Accept: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "streams": [
    {
      "name": "test-c-stream",
      "primaryProjectName": "test-c",
      "description": "This is a test stream",
      "allowCommitWithoutPassword": null,
      "analysisVersionOverride": "2021.06",
      "autoDeleteOnExpiry": true,
      "componentMapName": "Default",           
      "enableDesktopAnalysis": true,
      "language": "MIXED",            
      "outdated": true,
      "ownerAssignmentOption": "default_component_owner",
      "pluginVersionOverride": "1.7.5",            
      "roleAssignments": [
        {
          "group": {
            "domainName": null,
            "ldapServer": null,
            "name": "Users"
          },
          "roleAssignmentType": "group",
          "roleName": "developer",
          "scope": "stream",
          "username": null
        },
        {
          "group": null,
          "roleAssignmentType": "user",
          "roleName": "streamOwner",
          "scope": "stream",
          "username": "foo"
        }
      ],
      "summaryExpirationDays": 30,
      "triageStoreName": "Default Triage Store",
      "versionMismatchMessage": "wrong version"
    }
  ],
  "code": null,
  "message": null
}
```
