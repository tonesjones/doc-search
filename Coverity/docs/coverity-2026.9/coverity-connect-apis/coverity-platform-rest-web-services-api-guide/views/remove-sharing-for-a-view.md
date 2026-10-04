---
title: "Remove sharing for a view"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/remove-sharing-for-a-view.html"
content_id: "a8A1kGB02MuojdsYIdBohg"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:11.586632+00:00"
---

# Remove sharing for a view

Example DELETE request to remove sharing for a view.

**cURL request**

```
curl -X 'DELETE' \
  'http://localhost:8080/api/v2/views/sharing?name=name&viewType=issuesBySnapshots&locale=en_us' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "usernames": [
    "string"
  ],
  "groupnames": [
    "string"
  ]
}'
```
