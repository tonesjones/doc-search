---
title: "Retrieve snapshot output file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-snapshot-output-file.html"
content_id: "Y~IC7mCw21tgXOqnAR8miw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:53.089545+00:00"
---

# Retrieve snapshot output file

Example GET request to retrieve the specified output file for the specified snapshot.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/snapshots/10261/outputFile/summary.txt" \
--header 'Accept: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "contents": "eJytkk9rAjEQxe/5FHOXbLJRXLq3YutJpPjnXLLZEVM3yZLMFu2n725rUVr01CEQJvyYN+8RQZgoCXKt6O+DpZTl01wWwoR3rr1uTskm3ljfHacTrqTKs1xlMkukqwZFZf2F/EDgnKw5YOQu1Ag++OGpthFErUlLKb7lkomazF6MC1WoybgYtIWzMYYojHXcRNSEPOKO15VQUq69btM+9JT1hNEBfwOnj5N+eqJoW95q2v+bSD8V/eAPltvF4nX1vNmulmtgj+c8IHXO6XiCiG2IVDJ+o9jcNpjgnE4Nv6uEHDaBdMOGbjYa/SEuIPsCYRFmYH3bEVCA6+hLUEo+FGzeeUM2+BuyPcZe+rDubqXYxjoE0gf0UJ3g5yNcIVKWw1HsCXdoCIIxXYzoTe93FzpfX0j2CarhtgY=",
  "name": "/summary.txt",
  "code": null,
  "message": null
}
```
