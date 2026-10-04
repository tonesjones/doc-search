---
title: "Remove the global checker policy assignment"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/remove-the-global-checker-policy-assignment.html"
content_id: "LYrcV2PAmKohLObKV~xecg"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:04.240282+00:00"
---

# Remove the global checker policy assignment

Example DELETE request to remove the active global checker policy
assignment.

## **cURL request**

```
curl -X 'DELETE' \
  'http://localhost:8080/api/v2/checkerPolicy/assignments/global?locale=en_us' \
  --user my_username:my_password \
  -H 'accept: application/json'
```

## **Response body**

```
{
  "message": "Global assignment removed."
}
```
