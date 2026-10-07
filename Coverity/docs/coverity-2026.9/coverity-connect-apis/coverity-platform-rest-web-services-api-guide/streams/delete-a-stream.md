---
title: "Delete a stream"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/delete-a-stream.html"
content_id: "Ay55HqJRxs3SAovtLJZmRA"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:09.786819+00:00"
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
