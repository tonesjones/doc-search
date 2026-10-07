---
title: "Update a checker policy"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/update-a-checker-policy.html"
content_id: "tMsZZKUMQo8YTHGGKyP~3A"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:04.025913+00:00"
---

# Update a checker policy

Example PUT request to update an existing checker policy by name.

Replaces the content of an existing checker policy. The policy name is derived from
the name of the uploaded file. Duplicate content is rejected, including re-uploads
of the same file. Only administrators can modify global policies. Project policies
that are shared across multiple projects cannot be updated in place.

## **cURL request**

```
curl -X 'PUT' \
  'http://localhost:8080/api/v2/checkerPolicy/policies?name=policy&locale=en_us' \
  --user my_username:my_password \
  -H 'accept: application/json' \
  -F 'file=@my-policy.yaml'
```

## **Response body**

```
{
  "id": 10001,
  "name": "my-policy"
}
```
