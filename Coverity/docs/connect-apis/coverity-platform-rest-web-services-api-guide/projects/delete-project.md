---
title: "Delete project"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/delete-project.html"
content_id: "X1BflrBW0QI~vMMQN6gQOg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:31.479317+00:00"
---

# Delete project

Example DELETE request to delete the specified project.

**cURL request**

```
curl --location \
--request DELETE "http://my_connect_host:8080/api/v2/projects/test-c?locale=en_us" \
--header 'Accept: application/json' \
--user my_username:my_password
```
