---
title: "API Enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "Edjm6o7rj9PBioGeBI5V8w"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:34.032478+00:00"
content_hash: "97ef7ae73d923208ba2e1fb7e75c800791cebd80052278178813f27365770d2e"
---

# API Enhancements

For more details on new or changed API requests, please refer to the API doc available in Black Duck.

## Performance Improvements for project endpoints

The following API project endpoints were found to be underperforming and have been optimized:

- ```
  /api/projects/{ID}/versions/{ID}/compare/projects/{ID}/versions/{ID}/components
  ```
- ```
  /api/projects/{ID}/versions/{ID}/components
  ```
