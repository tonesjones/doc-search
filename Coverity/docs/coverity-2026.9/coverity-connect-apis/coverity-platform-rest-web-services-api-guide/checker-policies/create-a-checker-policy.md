---
title: "Create a checker policy"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/create-a-checker-policy.html"
content_id: "i4KhjtFApF8o~Scr6XeRBA"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:03.982552+00:00"
---

# Create a checker policy

Example POST request to create a checker policy by uploading a policy
file.

## **cURL request**

```
curl -X 'POST' \
  'http://localhost:8080/api/v2/checkerPolicy/policies?locale=en_us' \
  --user my_username:my_password \
  -H 'accept: application/json' \
  -F 'file=@my-policy.yaml'
```

## **Response body**

```
{
    "id": 10001,
    "name": "my-policy",
    "message": "Policy created successfully."
}
```
