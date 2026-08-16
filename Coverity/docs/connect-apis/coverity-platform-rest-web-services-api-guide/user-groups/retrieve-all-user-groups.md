---
title: "Retrieve all user groups"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-all-user-groups.html"
content_id: "ixvMJq6fpStLWneY9C~04A"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:15.712499+00:00"
---

# Retrieve all user groups

Example GET request to retrieve all user groups.

**cURL request**

```
curl -X 'GET' \
  'http://localhost:8080/api/v2/groups?excludeRoles=false&locale=en_us&offset=0&namePattern=Bob%2A&rowCount=200&sortOrder=asc' \
  -H 'accept: application/json'
```

**Response body**

```
{
  "groups": [
    {
      "name": {
        "domainName": "string",
        "ldapServer": "string",
        "name": "string"
      },
      "syncEnabled": true,
      "local": true,
      "roleAssignments": [
        {
          "group": {
            "domainName": "string",
            "ldapServer": "string",
            "name": "string"
          },
          "roleAssignmentType": "group",
          "roleName": "string",
          "scope": "component",
          "username": "string"
        }
      ]
    }
  ]
}
```
