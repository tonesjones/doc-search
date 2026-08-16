---
title: "Retrieve available values for the issue status attribute"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-available-values-for-the-issue-status-attribute.html"
content_id: "9C4xZxrI~BMC8bQX9PA4Wg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:57.013737+00:00"
---

# Retrieve available values for the issue status attribute

Example GET request to retrieve all available values for the issue
`status` attribute.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/issueAttributes/status" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
[
  "New",
  "Triaged",
  "Dismissed",
  "Fixed",
  "Absent Dismissed"
]
```
