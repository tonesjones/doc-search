---
title: "Retrieve the Developer Streams project"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/retrieve-the-developer-streams-project.html"
content_id: "hHjxRhe8ppE8rICPL1IGpg"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:07.751739+00:00"
---

# Retrieve the Developer Streams project

Example GET request to retrieve the Developer Streams project.

**cURL request**

```
curl --location \
--request GET "http://my_connecthost:8080/api/v2/projects/developerStreams?\
includeChildren=true&includeStreams=true&locale=en_us" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "projects": [
    {
      "createdBy": "system",
      "dateCreated": "2021-04-21T01:12:44.042896Z",
      "dateModified": "2021-04-21T01:12:44.042896Z",
      "description": "Developers Streams project",
      "modifiedBy": "system",
      "name": "Developer Streams",
      "projectKey": 10001,
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
