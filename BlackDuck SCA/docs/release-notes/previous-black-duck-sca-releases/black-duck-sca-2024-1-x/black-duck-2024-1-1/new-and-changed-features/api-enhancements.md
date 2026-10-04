---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "rQ~GE2VTES8v_ILUZgiF_g"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:30.913505+00:00"
content_hash: "37e68bcc8d609b597eb067a4d87c3ca5c0bf93264c416b9938f9a90404b81b02"
---

# API enhancements

## Updated project version policy rule summary API

A new version of the project version policy rule summary API has been added which offers a paginated list of policy rule violations and their associated BOM component count:

- `api/projects/{projectId}/versions/{projectVersionId}/policy-rules`

The previous version has been deprecated, and will be removed in an upcoming Black Duck release.

## Updated BOM vulnerability endpoint

A new version (V8) of the vulnerable BOM components endpoint has been added which contains performance improvements:

- `/api/projects/{ProjectID}/versions/{VersionID}/vulnerable-bom-components`

Version 8 of the endpoint only contains the minimum amount of data to serve current UI/UX views or custom integration utility in order to produce faster results and prevent timeout failures. Note that V7 of this API endpoint also exists and mapped to the existing V6.
