---
title: "API Enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "RT7wF9gLto39lHgL8A7MAw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:33.158182+00:00"
---

# API Enhancements

For more details on new or changed API requests, please refer to the API doc available in
Black Duck.

## New API to download Sigma Scanner

A new endpoint has been created to download the Sigma binary from upload-cache
directly. The API request has a path variable, `arch`, which is
required to indicate the desired architecture as well as an optional header
parameter called `version`.

- ```
  GET /api/tools/sigma?arch={arch}
  ```
