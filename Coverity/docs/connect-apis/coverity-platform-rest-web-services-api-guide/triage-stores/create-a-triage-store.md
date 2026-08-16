---
title: "Create a triage store"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-triage-store.html"
content_id: "pw7ryb4UJF0aUviSKCsOeA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:09.881147+00:00"
---

# Create a triage store

Example POST request to create a triage store.

**cURL request**

```
curl --location \
--request POST "http://my_connect_host:8080/api/v2/triageStores" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "name": "abc",
  "description": "This is a triage store.",
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
    }
  ]
}'
```
