---
title: "Update message of the day"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/update-message-of-the-day.html"
content_id: "ZhoWgZMUKJd0gSkNqUUEvQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:08.781199+00:00"
---

# Update message of the day

Example PUT request to update the message of the day.

**cURL request**

```
curl --location \
--request PUT "http://my_connect_host:8080/api/v2/serverInfo/messageOfTheDay" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "message": "This is a test message."
}'
```
