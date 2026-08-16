---
title: "Back up the database now"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/back-up-the-database-now.html"
content_id: "USnfrBDjXxHfVxD~BEzMpA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:20.454443+00:00"
---

# Back up the database now

Example POST request to immediately begin backing up the Coverity Connect database.

**cURL request**

```
curl --location --request POST "http://my_connect_host:8080/api/v2/maintenance/backupNow\
?backupLocation=C:%5CProducts%5CCoverity%5CPlatform%5Cbackups" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
```
