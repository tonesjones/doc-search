---
title: "Retrieve scan transparency data"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-scan-transparency-data.html"
content_id: "KPocp_wjAv2_mnOmNd2LSQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:02.116390+00:00"
---

# Retrieve scan transparency data

Example GET request to retrieve JSON-formatted scan transparency data associated with the
latest snapshot of a stream named *my_stream*.

The data is returned as a binary string. You can use the `curl`
`--output` option to save the data to a file as shown in the example:

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/streams/my_stream/scantransparency" \
--header 'Accept: application/json' \
--user my_username:my_password \
--output my_stream_tp_data.zip
```
