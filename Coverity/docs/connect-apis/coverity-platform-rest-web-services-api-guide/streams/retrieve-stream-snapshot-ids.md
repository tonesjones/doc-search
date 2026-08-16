---
title: "Retrieve stream snapshot IDs"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-stream-snapshot-ids.html"
content_id: "FJivEd0TyL5IUlY3iR253A"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:01.475225+00:00"
---

# Retrieve stream snapshot IDs

Example GET request to retrieve the IDs of the snapshots in the specified stream.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/streams/stream/snapshots?\
idType=byName&name=defectorstream" \
--header 'Accept: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "snapshotsForStream": [
    {
      "id": 10035
    },
    {
      "id": 10036
    },
    {
      "id": 10037
    },
    {
      "id": 10038
    },
    {
      "id": 10039
    },
    {
      "id": 10040
    }
  ],
  "code": null,
  "message": null
}
```
