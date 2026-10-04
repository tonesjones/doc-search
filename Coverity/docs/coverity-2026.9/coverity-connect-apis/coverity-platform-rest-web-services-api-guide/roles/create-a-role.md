---
title: "Create a role"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/create-a-role.html"
content_id: "1c7FGCIvBPPsVadMTjTQvQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:08.101167+00:00"
---

# Create a role

Example POST request to create a role.

**cURL request**

```
curl --location \
--request POST "http://my_connect_host:8080/api/v2/roles" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "name" : "Project X supervisor",
  "description" : "Role for Project X",
  "deletable" : true,
  "permissions" : ["viewDefects"]
}'
```
