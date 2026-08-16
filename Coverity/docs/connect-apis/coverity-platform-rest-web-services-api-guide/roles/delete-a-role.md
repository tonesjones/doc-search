---
title: "Delete a role"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/delete-a-role.html"
content_id: "0FhVrvTmuvkTMxlPyW~pPw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:38.182330+00:00"
---

# Delete a role

Example DELETE request to delete the specified role.

**cURL request**

```
curl --location \
--request DELETE "http://my_connect_host:8080/api/v2/roles/Project%20X%20supervisor" \
--header 'Accept: application/json' \
--user my_username:my_password
```
