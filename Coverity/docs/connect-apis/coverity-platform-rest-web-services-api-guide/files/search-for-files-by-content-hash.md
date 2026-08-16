---
title: "Search for files by content hash"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/search-for-files-by-content-hash.html"
content_id: "YgVkn46P6sCRKynnFPnw4w"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:52.519047+00:00"
---

# Search for files by content hash

Example POST request to retrieve information on source code files and associated streams
by specifying a content hash.

**cURL request**

```
curl --location --request POST "http://my_connect_host:8080/api/v2/files/search" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data '{ "contentHash": "5983d9fba67310a25bb9bd6104f555f3" }'
```

**Response body**

```
{
  "files": [
    {
      "name": "TestClass.vb",
      "path": "/testvb/TestClass.vb",
      "contentHash": "5983d9fba67310a25bb9bd6104f555f3",
      "streams": [
        {
          "name": "testvbstream",
          "primaryProjectName": "testvb"
        }
      ]
    }
  ],
  "offset": 0,
  "totalRows": 200
}
```
