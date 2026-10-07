---
title: "Delete a view"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/delete-a-view.html"
content_id: "~uEig4UPRsPB4t3nxd1qEA"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:11.163932+00:00"
---

# Delete a view

Example DELETE request to delete a view.

**cURL request**

```
curl --location \
--request DELETE "http://my_connect_host:8080/api/v2/views/MyView?viewType=issuesBySnapshots" \
--header 'Accept: application/json' \
--user my_username:my_password
```
