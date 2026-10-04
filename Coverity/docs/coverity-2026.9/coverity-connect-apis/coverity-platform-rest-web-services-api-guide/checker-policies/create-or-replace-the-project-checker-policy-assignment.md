---
title: "Create or replace the project checker policy assignment"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/create-or-replace-the-project-checker-policy-assignment.html"
content_id: "7Vg75GDVLOuEGrakalFAMQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:04.322286+00:00"
---

# Create or replace the project checker policy assignment

Example PUT request to create or replace the checker policy assignment for a specific
project.

## **cURL request**

```
curl --location --request PUT 'http://localhost:8080/api/v2/checkerPolicy/assignments
/projects?policyName=test&precedenceOrder=TOP_DOWN&projectName=sample' \
--header 'Accept: application/json' \
--user my_username:my_password \
```

## **Response body**

```
{
    "message": "Policy test successfully assigned to project sample."
}
```
