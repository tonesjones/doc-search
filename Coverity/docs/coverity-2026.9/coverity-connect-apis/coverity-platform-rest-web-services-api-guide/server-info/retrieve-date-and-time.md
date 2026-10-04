---
title: "Retrieve date and time"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/retrieve-date-and-time.html"
content_id: "mcYxzpiaxnbGZKbt6F_4~w"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:08.822378+00:00"
---

# Retrieve date and time

Example GET request to retrieve the current date and time from the Coverity Connect
server.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/serverInfo/time" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "dateTime": "2022-05-18T11:48:20.956-06:00",
  "code": null,
  "message": null
}
```
