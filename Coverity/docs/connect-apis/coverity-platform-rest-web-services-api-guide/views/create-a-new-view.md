---
title: "Create a new view"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-new-view.html"
content_id: "88m0xlIf3fS9_xt64bFxkw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:20.811922+00:00"
---

# Create a new view

Example POST request to create a new view.

**cURL request**

```
curl --location \
--request POST "http://my_connect_host:8080/api/v2/views?viewType=issuesBySnapshots" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "name" : "MyView",
}'
```

**Response body**

```
{
  "id": 10024
}
```
