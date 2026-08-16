---
title: "Update a triage store"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/update-a-triage-store.html"
content_id: "wIJViE_YruxS_lp2UkHcDA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:11.166706+00:00"
---

# Update a triage store

Example PUT request to update the specified triage store.

**cURL request**

```
curl --location \
--request PUT "http://localhost:8080/api/v2/triageStores/abc" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw '{
  "name": "abc-1",
  "description": "This is a triage store-1",
  "roleAssignments": [
    {
      "group": {
        "domainName": null,
        "ldapServer": null,
        "name": "Users"
      },
      "roleAssignmentType": "group",
      "roleName": "developer",
      "scope": "triageStore",
      "username": null
    },
    {
      "group": null,
      "roleAssignmentType": "user",
      "roleName": "triageStoreOwner",
      "scope": "triageStore",
      "username": "admin"
    },
    {
      "group": null,
      "roleAssignmentType": "user",
      "roleName": "triageStoreOwner",
      "scope": "triageStore",
      "username": "foo"
    }
  ]
}'
```
