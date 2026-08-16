---
title: "Update a user group"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/update-a-user-group.html"
content_id: "3hgRiwQ~ihnYxw6wp0q_cQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:14.388650+00:00"
---

# Update a user group

Example PUT request to update the user group with new role assignments.

**cURL request**

```
curl --location \
--request PUT "http://my_connect_host:8180/api/v2/groups/Group3" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{ 
  "name" : "Group3",
  "local" : true,
  "roleAssignment": [
    {
      "group": {
      "domainName": null,
      "ldapServer": null,
      "name": "Group3"
    },
    "roleAssignmentType": "group",
    "roleName": "committer",
    "scope": "global",
    "username": null
    },
    {
      "group": {
        "domainName": null,
        "ldapServer": null,
        "name": "Group3"
      },
      "roleAssignmentType": "group",
      "roleName": "developer",
      "scope": "global",
      "username": null
    }
  ]
}'
```
