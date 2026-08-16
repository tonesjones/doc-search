---
title: "Update configuration for purge analysis summaries process"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/update-configuration-for-purge-analysis-summaries-process.html"
content_id: "nh2X2ijj6rLjZXD7_sBBUQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:21.764919+00:00"
---

# Update configuration for purge analysis summaries process

Example PUT request to update the configuration for the "purge analysis summaries"
process.

**cURL request**

```
curl --location \
--request PUT "http://my_connect_host:8080/api/v2/maintenance/purgeAnalysisSummaries" \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "daysBeforePurge": 600, 
  "minSnapshotsToKeep": 200
}'
```
