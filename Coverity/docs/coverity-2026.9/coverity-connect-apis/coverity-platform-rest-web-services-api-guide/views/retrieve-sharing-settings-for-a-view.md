---
title: "Retrieve sharing settings for a view"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/retrieve-sharing-settings-for-a-view.html"
content_id: "nR9qzVjfulFHkq3kfDJ4bQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:11.545281+00:00"
---

# Retrieve sharing settings for a view

Example GET request to retrieve sharing settings for the specified view.

**cURL request**

```
curl -X 'GET' \
  'http://localhost:8080/api/v2/views/sharing?name=Test&viewType=issuesBySnapshots&locale=en_us' \
  -H 'accept: application/json'
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
  ]
}
```
