---
title: "Delete a snapshot"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/delete-a-snapshot.html"
content_id: "tMwsNBtC~nkPOoKQqF0DzA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:51.775505+00:00"
---

# Delete a snapshot

Example DELETE request to delete the specified snapshot and all associated data,
including snapshot attributes, build and analysis details, and defect data.

**cURL request**

```
curl --location \
--request DELETE "http://my_connect_host:8080/api/v2/snapshots/10261" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password
```
