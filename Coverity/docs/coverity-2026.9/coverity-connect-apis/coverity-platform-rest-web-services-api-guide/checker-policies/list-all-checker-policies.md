---
title: "List all checker policies"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/list-all-checker-policies.html"
content_id: "mkr271y9GGYAa_EoX4RSCg"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:03.939807+00:00"
---

# List all checker policies

Example GET request to list all checker policies.

## **cURL request**

```
curl -X 'GET' \
  'http://localhost:8080/api/v2/checkerPolicy/policies?offset=0&rowCount=200&locale=en_us' \
  --user my_username:my_password \
  -H 'accept: application/json'
```

## **Response body**

```
{
  "offset": 0,
  "totalRows": 0,
  "policies": [
    {
      "id": 10001,
      "name": "my-config"
    }
  ]
}
```
