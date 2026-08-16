---
title: "Update a user"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/update-a-user.html"
content_id: "CtXCsTm4diME5wNX1f2yIw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:18.264600+00:00"
---

# Update a user

Example PUT request to update the specified user.

**cURL request**

```
curl --location \
--request PUT "http://my_connect_host:8080/api/v2/users/john-doe" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{ 
  "name" : "john-doe", 
  "givenName" : "John" 
}'
```
