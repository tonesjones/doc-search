---
title: "Retrieve snapshot deletion status"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-snapshot-deletion-status.html"
content_id: "kUULMDIOvEnTEB0cxVi7Qg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:52.454487+00:00"
---

# Retrieve snapshot deletion status

Example GET request to retrieve the status of the deletion process for the specified
snapshot.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/snapshots/status/10254" \
--header 'Accept: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "snapshotId":10254,
  "status":"QUEUED",
  "code":null,
  "message":null
}
```
