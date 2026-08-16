---
title: "Create a user"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-user.html"
content_id: "Kokmyp8imrgkG7Eqdzye6w"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:16.994823+00:00"
---

# Create a user

Example POST request to create a user.

**cURL request**

```
curl --location --request POST "http://my_connect_host:8080/api/v2/users" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "name" : "John-Doe", 
  "password" : "Sunshine314!" 
}'
```
