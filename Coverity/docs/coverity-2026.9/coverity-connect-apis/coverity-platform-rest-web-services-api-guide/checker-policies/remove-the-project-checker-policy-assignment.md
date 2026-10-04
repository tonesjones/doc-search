---
title: "Remove the project checker policy assignment"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/remove-the-project-checker-policy-assignment.html"
content_id: "uy3NkutTEjiT8u59SqfCPg"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:04.364383+00:00"
---

# Remove the project checker policy assignment

Example DELETE request to remove the checker policy assignment for a specific
project.

## **cURL request**

```
curl --location --request DELETE 'http://localhost:8080/api/v2/checkerPolicy/assignments/
projects?projectName=sample' \
--header 'Accept: application/json' \
--user my_username:my_password \
```

## **Response body**

```
{
  "message": "Project assignment removed."
}
```
