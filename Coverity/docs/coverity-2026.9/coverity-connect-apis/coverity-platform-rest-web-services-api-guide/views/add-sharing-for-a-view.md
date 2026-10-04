---
title: "Add sharing for a view"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/add-sharing-for-a-view.html"
content_id: "8qKVFSKhWFEU7UZapuHmpw"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:11.503162+00:00"
---

# Add sharing for a view

Example POST request to add sharing for a view.

**cURL request**

```
curl -X 'POST' \
  'http://localhost:8080/api/v2/views/sharing?name=test&viewType=issuesBySnapshots&locale=en_us' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "usernames": [
    "string"
  ],
  "groupnames": [
    "string"
  ]
}
```

**Response body**

```
{
  "shared": true,
  "sharedUsernames": [
    "string"
  ],
  "sharedGroupnames": [
    "string"
  ],
  "invalidUsernames": [
    "string"
  ],
  "invalidGroupnames": [
    "string"
  ]
}
```
