---
title: "Delete a view"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/delete-a-view.html"
content_id: "~uEig4UPRsPB4t3nxd1qEA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:21.443667+00:00"
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
