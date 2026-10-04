---
title: "Retrieve stream UUID"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/retrieve-stream-uuid.html"
content_id: "XXyFwEjpMrtdAx1uMnbUyg"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:09.826893+00:00"
---

# Retrieve stream UUID

Example GET request to retrieve the UUID of the specified stream.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/streams/CERT-C/uuid" \
--header 'Accept: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "uuid":"51816bab-9bf6-4dfa-848d-2eb0975a75d8",
  "name":"CERT-C",
  "code":null,
  "message":null
}
```
