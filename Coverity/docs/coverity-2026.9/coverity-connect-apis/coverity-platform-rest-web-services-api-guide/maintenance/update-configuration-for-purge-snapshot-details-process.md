---
title: "Update configuration for purge snapshot details process"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/update-configuration-for-purge-snapshot-details-process.html"
content_id: "f6zlVJnPfeqQSr23LHtNYQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:07.063603+00:00"
---

# Update configuration for purge snapshot details process

Example PUT request to update the configuration for the "purge snapshot details"
process.

**cURL request**

```
curl --location \
--request PUT "http://my_connect_host:8080/api/v2/maintenance/purgeSnapshotDetails" \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "daysBeforePurge": 120,
  "daysEnabled": [
    "MONDAY", 
    "THURSDAY"
  ],
  "minSnapshotsToKeep": 10,
  "time": "06:00"
}'
```
