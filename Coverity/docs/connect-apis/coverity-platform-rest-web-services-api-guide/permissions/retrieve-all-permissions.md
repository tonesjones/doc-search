---
title: "Retrieve all permissions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-all-permissions.html"
content_id: "hPTXiUdL85Zs4TBd8dn56g"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:26.343205+00:00"
---

# Retrieve all permissions

Example GET request to retrieve all permissions.

**cURL request**

```
curl -X 'GET' \
  'http://localhost:8080/api/v2/permissions?locale=en_us' \
  -H 'accept: application/json'
```

**Response body**

```
{
  "permissions": [
    "string"
  ],
  "displayPermissions": [
    {
      "name": "string",
      "displayName": "string"
    }
  ]
}
```
