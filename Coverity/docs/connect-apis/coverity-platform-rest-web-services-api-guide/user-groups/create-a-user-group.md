---
title: "Create a user group"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-user-group.html"
content_id: "_PoPQYeM4AcZ_ZUroBkylQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:13.107397+00:00"
---

# Create a user group

Example POST request to create a user group.

**cURL request**

```
 curl --location \
--request POST "http://my_connect_host:8080/api/v2/groups" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{ 
  "name" : "Group2", 
  "local": true, 
  "roleAssignments": [
    {
      "group": {
        "domainName": null,
        "ldapServer": null,
        "name": "Group2"
      },
      "roleAssignmentType": "group",
      "roleName": "visitor",
      "scope": "global",
      "username": null
    }
  ]
}'
```
