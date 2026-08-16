---
title: "Update a role"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/update-a-role.html"
content_id: "ARAeCqpdcmnKJ6SgmTk0yA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:37.237848+00:00"
---

# Update a role

Example PUT request to update the specified role.

**cURL request**

```
curl --location \
--request PUT "http://my_connect_host:8080/api/v2/roles/Project%20X%20supervisor" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "name" : "Project X supervisor",
  "description" : "Role for Project X-2",
}'
```
