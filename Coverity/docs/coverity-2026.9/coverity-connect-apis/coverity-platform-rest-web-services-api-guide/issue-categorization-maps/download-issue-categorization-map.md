---
title: "Download issue categorization map"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/download-issue-categorization-map.html"
content_id: "0B4eX~7ptUQTdx7j8e8PmA"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:05.493183+00:00"
---

# Download issue categorization map

Example GET request to download the issue categorization map.

**cURL request**

```
curl -X 'GET' \
  'http://localhost:8080/api/v2/issueCategorizationMaps?streamName=name&locale=en_us' \
  -H 'accept: application/json'
```

**Response body**

```
{
  "name": "named-map",
  "types": {
    "named-error": {
      "category": "Security best practices violations",
      "impact": "Low"
    }
  }
}
```
