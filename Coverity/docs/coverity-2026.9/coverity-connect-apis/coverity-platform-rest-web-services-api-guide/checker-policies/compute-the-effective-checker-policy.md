---
title: "Compute the effective checker policy"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/compute-the-effective-checker-policy.html"
content_id: "2mov3vZFJCkVvabEdFcOwg"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:04.406770+00:00"
---

# Compute the effective checker policy

Example GET request to compute the effective checker policy, which reflects the
resolved result of the global and project policies based on the configured
precedence.

## **cURL request**

```
curl -X 'GET' \
  'http://localhost:8080/api/v2/checkerPolicy/effective-policy?outputFormat=json&locale=en_us' \
  --user my_username:my_password \
  -H 'accept: application/json'
```

## **Response body**

Returns the effective policy content in the requested format. The following example
shows a JSON policy.

```
{
  "versions": {
    "min": "2026.12.0"
  },
  "require": {
    "analyze": {
      "aggressiveness-level": "high",
      "enable-check-set": ["cwe-top-25-2023"]
    }
  }
}
```
