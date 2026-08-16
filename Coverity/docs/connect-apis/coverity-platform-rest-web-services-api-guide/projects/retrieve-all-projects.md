---
title: "Retrieve all projects"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-all-projects.html"
content_id: "V30PpNymrbcSrd2TqfaJ4g"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:30.188798+00:00"
---

# Retrieve all projects

Example GET request to retrieve all projects and filter the result set.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/projects?descriptionPattern=*test*&\
locale=en_us&includeChildren=true&includeStreams=true&namePattern=*c" \
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
    },
    {
      "createdBy": "admin",
      "dateCreated": "2021-08-11T22:30:15.359Z",
      "dateModified": "2021-08-11T22:30:15.359Z",
      "description": "This is a test project",
      "modifiedBy": "admin",
      "name": "test-cc",
      "projectKey": 10078,
      "roleAssignments": [
        {
          "group": null,
          "roleAssignmentType": "user",
          "roleName": "projectOwner",
          "scope": "project",
          "username": "admin"
        }
      ],
      "streamLinks": [],
      "streams": []
    }
  ],
  "code": null,
  "message": null
}
```
