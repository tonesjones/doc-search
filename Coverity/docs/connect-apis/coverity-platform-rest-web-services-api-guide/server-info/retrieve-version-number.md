---
title: "Retrieve version number"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-version-number.html"
content_id: "S99dHkx3XWKbZmZsbgcy7A"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:47.200200+00:00"
---

# Retrieve version number

Example GET request to retrieve the version number of the Coverity Connect server.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/serverInfo/version" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "internalVersion": "ccfd5f5b1f im-2022.6-push-2",
  "externalVersion": "2022.6.0",
  "code": null,
  "message": null
}
```
