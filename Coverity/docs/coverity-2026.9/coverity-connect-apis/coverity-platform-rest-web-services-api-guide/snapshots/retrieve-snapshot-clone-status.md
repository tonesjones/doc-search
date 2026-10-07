---
title: "Retrieve snapshot clone status"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/retrieve-snapshot-clone-status.html"
content_id: "ZwqHGnO5O4VIDalVglcayQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:09.372625+00:00"
---

# Retrieve snapshot clone status

Example GET request to retrieve snapshot clone status.

**cURL request**

```
curl -X 'GET' \
  'http://localhost:8080/api/v2/snapshots/cloneStatus/10352?locale=en_us' \
  -H 'accept: application/json'
```

**Response body**

```
{
  "sourceStreamId": 201,
  "targetStreamId": 202,
  "sourceSnapshotId": 10100,
  "targetSnapshotId": 10110,
  "status": "IN_PROGRESS",
  "errMsg": "",
  "completionPercentage": 40
}
```
