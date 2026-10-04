---
title: "Triage configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/triage-configuration.html"
content_id: "6fTvIUI29fOUc57U8NOrQA"
version: "2026.9"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-10-04T23:35:04.790277+00:00"
---

# Triage configuration

These options specify how new defects are handled.

| Key | Type | Description |
| --- | --- | --- |
| `new-defect-owner` | string | The user to whom any new defects will be assigned. The specified user must already exist in the Coverity Connect database. Default: The current user |
| `new-defect-owner-limit` | integer | A limit on the number of defects to assign to the specified user. If the number of discovered defects is greater than this limit, then no assignment is made. Default: 100 |
| `set-new-defect-owner` | Boolean | When `true`, the owner for newly detected defects that exist locally is set to the specified user. Default: `true` |
