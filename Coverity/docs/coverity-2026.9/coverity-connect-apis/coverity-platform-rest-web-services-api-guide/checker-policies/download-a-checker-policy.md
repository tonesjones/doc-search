---
title: "Download a checker policy"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/download-a-checker-policy.html"
content_id: "7K_zVPnls63uHatKiNgvjQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:04.112805+00:00"
---

# Download a checker policy

Example GET request to download a checker policy file by name.

## **cURL request**

```
curl -X 'GET' \
  'http://localhost:8080/api/v2/checkerPolicy/policies/download?name=sample&locale=en_us' \
  --user my_username:my_password \ 
  -H 'accept: application/octet-stream' \
  -o my-policy.yaml
```

## **Response**

Returns the policy file content. The following example shows a YAML policy
file.

```
versions:
  min: 2026.12.0
require:
  analyze:
    aggressiveness-level: high
    enable-check-set:
      - cwe-top-25-2023
```
