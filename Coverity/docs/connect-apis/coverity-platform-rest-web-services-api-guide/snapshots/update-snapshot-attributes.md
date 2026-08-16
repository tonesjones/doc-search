---
title: "Update snapshot attributes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/update-snapshot-attributes.html"
content_id: "0nxaBspV9oouQFCnHDNtqw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:51.122158+00:00"
---

# Update snapshot attributes

Example PUT request to update the attributes of the specified snapshot.

**cURL request**

```
curl --location \
--request PUT "http://my_connect_host:8080/api/v2/snapshots/10261" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "description":  "My snapshot description.",
  "sourceVersion" : "3.5.2",
  "target": "x86_64"
}'
```
