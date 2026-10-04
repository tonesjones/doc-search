---
title: "Retrieve the latest snapshot ID for a stream"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/retrieve-the-latest-snapshot-id-for-a-stream.html"
content_id: "kQXlReqEllJVjN1gsCt7zg"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:09.990818+00:00"
---

# Retrieve the latest snapshot ID for a stream

Example GET request to retrieve the latest snapshot ID for a stream.

**cURL request**

```
curl -X 'GET' \
  'http://localhost:8080/api/v2/streams/latestsnapshot?name=My_Stream&locale=en_us' \
  -H 'accept: application/json'
```

**Response body**

```
{
  "snapshotsForStream": [
    {
      "id": 10010
    }
  ]
}
```
