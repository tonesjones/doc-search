---
title: "Delete project"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/delete-project.html"
content_id: "X1BflrBW0QI~vMMQN6gQOg"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:07.627270+00:00"
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
