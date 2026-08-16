---
title: "Retrieve the latest snapshot ID for a stream"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-the-latest-snapshot-id-for-a-stream.html"
content_id: "kQXlReqEllJVjN1gsCt7zg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:03.427502+00:00"
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
