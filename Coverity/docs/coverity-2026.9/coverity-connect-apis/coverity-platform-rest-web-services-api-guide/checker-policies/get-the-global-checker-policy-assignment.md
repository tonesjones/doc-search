---
title: "Get the global checker policy assignment"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/get-the-global-checker-policy-assignment.html"
content_id: "~u_mOzfu5LAPOjHwRhF5EQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:04.154246+00:00"
---

# Get the global checker policy assignment

Example GET request to retrieve the active global checker policy
assignment.

## **cURL request**

```
curl -X 'GET' \
  'http://localhost:8080/api/v2/checkerPolicy/assignments/global?locale=en_us' \
  --user my_username:my_password \
  -H 'accept: application/json'
```

## **Response body**

```
{
    "id": "10001",
    "name": "my-policy",
    "noncomplianceAction": "WARN_AND_ACCEPT",
    "precedenceOrder": "BOTTOM_UP",
    "dateModified": "2026-08-24T13:08:40.838Z",
    "userCreated": "admin",
    "userModified": "admin"
}
```
