---
title: "Delete a checker policy"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/delete-a-checker-policy.html"
content_id: "xgCWRudlGFyHwAUIlgxIag"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:04.069285+00:00"
---

# Delete a checker policy

Example DELETE request to delete a checker policy by name.

## **cURL request**

```
curl -X 'DELETE' \
  'http://localhost:8080/api/v2/checkerPolicy/policies?name=test&locale=en_us' \
  --user my_username:my_password \
  -H 'accept: application/json'
```

## **Response body**

```
{
  "message": "Policy deleted successfully."
}
```
