---
title: "Clear role assignments for streams"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/clear-role-assignments-for-streams.html"
content_id: "OOMVju_ytcFun9UGB4a4gw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:02.790900+00:00"
---

# Clear role assignments for streams

Example POST request to remove role assignments for streams that match the specified filter criteria. If multiple filters are provided, only streams that match all of the specified criteria will be affected.

**cURL request**

```
curl --location \
--request POST "http://my_connect_host:8080/api/v2/streams/roleAssignments/cleanup?locale=en_us" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "namePattern": "*test*",
  "descriptionPattern": "*temporary*",
  "languageList": ["JAVA", "CXX"]
}'
```

**Response body**

```
{
  "code": null,
  "message": "Role assignments cleared successfully."
}
```
