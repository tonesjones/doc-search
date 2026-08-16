---
title: "Retrieve the specified project"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-the-specified-project.html"
content_id: "XD7pQzLpA5UllHhhOOawkg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:29.555115+00:00"
---

# Retrieve the specified project

Example GET request to retrieve the specified project.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/projects/test-c?\
includeChildren=true&includeStreams=true&locale=en_us" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "projects": [
    {
      "createdBy": "admin",
      "dateCreated": "2021-08-11T22:26:04.275Z",
      "dateModified": "2021-08-11T22:26:04.275Z",
      "description": "This is a test project",
      "modifiedBy": "admin",
      "name": "test-c",
      "projectKey": 10077,
      "roleAssignments": [
        {
          "group": {
            "domainName": null,
            "ldapServer": null,
            "name": "Users"
          },
          "roleAssignmentType": "group",
          "roleName": "developer",
          "scope": "project",
          "username": null
        },
        {
          "group": null,
          "roleAssignmentType": "user",
          "roleName": "projectOwner",
          "scope": "project",
          "username": "admin"
        }
      ],
      "streamLinks": [
        {
          "name": "tar stream"
        }
      ],
      "streams": [
        {
          "analysisVersionOverride": null,
          "autoDeleteOnExpiry": false,
          "componentMapName": "Default",
          "description": "CERT_JAVA testing",
          "enableDesktopAnalysis": true,
          "language": "JAVA",
          "name": "CERT_JAVA",
          "allowCommitWithoutPassword": null,
          "outdated": false,
          "ownerAssignmentOption": "default_component_owner",
          "pluginVersionOverride": null,
          "primaryProjectName": "test-c",
          "roleAssignments": [],
          "summaryExpirationDays": null,
          "triageStoreName": "CERT_JAVA_triage",
          "versionMismatchMessage": null
        }
      ]
    }
  ],
  "code": null,
  "message": null
}
```
