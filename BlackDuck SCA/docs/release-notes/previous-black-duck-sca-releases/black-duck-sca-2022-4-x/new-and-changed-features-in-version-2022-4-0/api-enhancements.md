---
title: "API Enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "UTHNXGmMM2_eriRnqjP_MQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:40.140019+00:00"
---

# API Enhancements

For more details on new or changed API requests, please refer to the API doc
available in Black Duck.

## Performance Improvements for project endpoints

The following API project endpoints were found to be underperforming and have
been optimized:

- ```
  /api/projects/{ID}/versions/{ID}/compare/projects/{ID}/versions/{ID}/components
  ```
- ```
  /api/projects/{ID}/versions/{ID}/components
  ```
