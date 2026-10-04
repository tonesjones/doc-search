---
title: "Verify compliance against the effective checker policy"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/verify-compliance-against-the-effective-checker-policy.html"
content_id: "~WMYyA1ZwNZWFs8txqlU_Q"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:04.453720+00:00"
---

# Verify compliance against the effective checker policy

Example POST request to verify a scan configuration file against the effective
checker policy.

## **cURL request**

Note: The following parameters are required:

- `config` or `command`– exactly one of these
  parameters must be provided.
- `analysisVersion`– must be specified as a query
  parameter.

The request fails if any required parameter is missing.

```
curl -X 'POST' \
  'http://localhost:8080/api/v2/checkerPolicy/verify-compliance?analysisVersion=2026.9.0&locale=en_us' \
  --user my_username:my_password \
  -H 'accept: application/json' \
  -F 'config=@my-scan-config.json'
```

## **Response body**

```
{
  "result": "string",
  "status": 0,
  "noncomplianceAction": "reject"
}
```
