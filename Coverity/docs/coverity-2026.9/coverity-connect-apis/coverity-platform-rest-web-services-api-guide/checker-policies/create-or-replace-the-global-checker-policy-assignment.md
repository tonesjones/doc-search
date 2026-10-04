---
title: "Create or replace the global checker policy assignment"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/create-or-replace-the-global-checker-policy-assignment.html"
content_id: "mfiyEEsWNmQFIMWVht8vJg"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:04.198824+00:00"
---

# Create or replace the global checker policy assignment

Example PUT request to create or replace the active global checker policy
assignment.

## **cURL request**

```
curl -X 'PUT' \
  'http://localhost:8080/api/v2/checkerPolicy/assignments/global?name=test&noncomplianceAction=REJECT&locale=en_us' \
  --user my_username:my_password \
  -H 'accept: application/json'
```

## **Response body**

```
{
    "message": "Policy test successfully assigned as global policy."
}
```
