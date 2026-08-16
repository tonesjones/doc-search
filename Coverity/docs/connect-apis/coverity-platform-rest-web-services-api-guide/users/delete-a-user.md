---
title: "Delete a user"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/delete-a-user.html"
content_id: "FpolhnQZuHBuTeUN3z0kIg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:18.895058+00:00"
---

# Delete a user

Example DELETE request to delete the specified user.

**cURL request**

```
curl --location \
--request DELETE "http://my_connect_host:8080/api/v2/users/john-doe" \
--header 'Accept: application/json' \
--user my_username:my_password
```
