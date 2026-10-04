---
title: "Retrieve message of the day"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/retrieve-message-of-the-day.html"
content_id: "SpsiS8ur~5Elvww6RQnCsQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:08.740263+00:00"
---

# Retrieve message of the day

Example GET request to retrieve the message of the day.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/serverInfo/messageOfTheDay?locale=en_us" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "message": "This is a test message.",
  "code": null
}
```
