---
title: "Purge and skeletonize snapshots"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/purge-and-skeletonize-snapshots.html"
content_id: "UUOyLk1VHCf~GIO_pVGVcw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:53.731561+00:00"
---

# Purge and skeletonize snapshots

Example POST request to purge and skeletonize snapshot details. This operation accepts a list of snapshot IDs, skeletonizes each snapshot, and then deletes any orphaned architecture or desktop analysis data.

**cURL request**

```
curl --location \
--request POST "http://my_connect_host:8080/api/v2/snapshots/purge?locale=en_us" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "snapshotIds": [10010, 10015, 10020]
}'
```

**Response body**

```
{
  "code": null,
  "message": "Snapshots purged successfully."
}
```
