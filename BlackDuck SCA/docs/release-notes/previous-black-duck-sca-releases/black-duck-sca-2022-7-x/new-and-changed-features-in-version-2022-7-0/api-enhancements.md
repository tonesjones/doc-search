---
title: "API Enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "wDOlRAy3IZpKEprao3J2CQ"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:33.868079+00:00"
content_hash: "de3e4c4d638898f606076dd6be339120f42ba1d32f7b61806cef401fa6bca088"
---

# API Enhancements

For more details on new or changed API requests, please refer to the API doc available in Black Duck.

## New API to download Sigma Scanner

A new endpoint has been created to download the Sigma binary from upload-cache directly. The API request has a path variable, `arch`, which is required to indicate the desired architecture as well as an optional header parameter called `version`.

- ```
  GET /api/tools/sigma?arch={arch}
  ```
