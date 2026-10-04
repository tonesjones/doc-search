---
title: "Update project"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/update-project.html"
content_id: "kvsZOx1war4YtcVvy6wRuw"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:07.586837+00:00"
---

# Update project

Example PUT request to update the specified project.

**cURL request**

```
curl --location \
--request PUT "http://my_connect_host:8080/api/v2/projects/test-c?locale=en_us" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "name": "test-c-1",
  "description": "This is a test project",
  "roleAssignments": [
    {
      "roleAssignmentType": "user",
      "roleName": "projectOwner",
      "scope": "project",
      "username": "admin"
    }
  ],
  "streamLinks": [
    {
      "name": "CERT-CPP"
    }
  ],
  "streams": [
    {
      "name": "git-stream"
    }
  ]
}'
```
