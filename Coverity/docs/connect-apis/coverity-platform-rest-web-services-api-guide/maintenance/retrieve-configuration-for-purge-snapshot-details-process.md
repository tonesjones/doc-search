---
title: "Retrieve configuration for purge snapshot details process"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-configuration-for-purge-snapshot-details-process.html"
content_id: "RH_34aCIOJgpSKko4gZUvQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:22.417344+00:00"
---

# Retrieve configuration for purge snapshot details process

Example GET request to retrieve the configuration for the "purge snapshot details"
process.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/maintenance/purgeSnapshotDetails" \
--header 'Accept: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "daysBeforePurge": 120,
  "daysEnabled": [
    "MONDAY", 
    "THURSDAY"
  ],
  "minSnapshotsToKeep": 5,
  "time": "05:00"
}
```
