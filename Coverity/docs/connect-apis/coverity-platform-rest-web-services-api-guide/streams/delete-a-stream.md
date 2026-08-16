---
title: "Delete a stream"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/delete-a-stream.html"
content_id: "Ay55HqJRxs3SAovtLJZmRA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:00.170297+00:00"
---

# Delete a stream

Example DELETE request to delete the specified stream.

**cURL request**

```
curl --location \
--request DELETE "http://my_connect_host:8080/api/v2/streams/test-c-stream" \
--header 'Accept: application/json' \
--user my_username:my_password
```
