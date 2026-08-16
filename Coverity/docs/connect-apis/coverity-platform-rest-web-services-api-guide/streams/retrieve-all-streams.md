---
title: "Retrieve all streams"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-all-streams.html"
content_id: "wUtOpyRzj1ecFH6DpkMTNA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:58.252186+00:00"
---

# Retrieve all streams

Example GET request to retrieve all streams and filter the result set.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/streams?\
descriptionPattern=*test*&locale=en_us&namePattern=test-c*" \
--header 'Accept: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "streams": [
    {
      "analysisVersionOverride": "2021.06",
      "autoDeleteOnExpiry": true,
      "componentMapName": "Default",
      "description": "This is a test stream",
      "enableDesktopAnalysis": true,
      "language": "MIXED",
      "name": "test-c-stream",
      "allowCommitWithoutPassword": null,
      "outdated": true,
      "ownerAssignmentOption": "default_component_owner",
      "pluginVersionOverride": "1.7.5",
      "primaryProjectName": "test-c",
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
    },
    {
        "analysisVersionOverride": null,
        "autoDeleteOnExpiry": false,
        "componentMapName": "Default",
        "description": "A test stream",
        "enableDesktopAnalysis": true,
        "language": "MIXED",
        "name": "test-c-stream2",
        "allowCommitWithoutPassword": null,
        "outdated": false,
        "ownerAssignmentOption": "default_component_owner",
        "pluginVersionOverride": null,
        "primaryProjectName": null,
        "roleAssignments": [
          {
            "group": null,
            "roleAssignmentType": "user",
            "roleName": "streamOwner",
            "scope": "stream",
            "username": "bar"
          }
        ],
        "summaryExpirationDays": null,
        "triageStoreName": "Default Triage Store",
        "versionMismatchMessage": null
      }
    ],
  "code": null,
  "message": null
}
```
