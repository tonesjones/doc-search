---
title: "Create a project"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-project.html"
content_id: "fFcasVcXQvSkO0ilr9qJaQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:28.906603+00:00"
---

# Create a project

Example POST request to create a project.

**cURL request**

```
curl --location --request POST "http://my_connect_host:8080/api/v2/projects" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "name": "test-c",
  "description": "This is a test project",
  "roleAssignments": [
    {
      "roleAssignmentType": "user",
      "roleName": "projetOwner",
      "scope": "project",
      "username": "foo"
    },
    {
      "group": {
        "name": "Users"
        },
        "roleAssignmentType": "group",
        "roleName": "developer",
        "scope": "project"
      }
    ],
  "streamLinks": [
    {
      "name": "tar stream"
    }
  ],
  "streams": [
    {
      "name": "CERT_JAVA"
    }
  ]
}'
```
