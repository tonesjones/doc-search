---
title: "Get the project checker policy assignment"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/get-the-project-checker-policy-assignment.html"
content_id: "wnLj5ojn9Khbkyoj9i9jNA"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:04.281870+00:00"
---

# Get the project checker policy assignment

Example GET request to retrieve the active checker policy assignment for a specific
project.

## **cURL request**

```
curl --location 'http://localhost:8080/api/v2/checkerPolicy/assignments/projects?projectName=sample' \
--header 'Accept: application/json' \
--user my_username:my_password \
```

## **Response body**

```
  {
    "id": "10001",
    "name": "test",
    "precedenceOrder": "TOP_DOWN",
    "dateModified": "2026-08-24T13:42:08.148Z",
    "userCreated": "admin",
    "userModified": "admin"
}
```
