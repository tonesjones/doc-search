---
title: "Fixed Issues in 2022.7.2"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2022.7.2.html"
content_id: "x8KSfKqIs01yoOCs69vHFA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:29.166547+00:00"
---

# Fixed Issues in 2022.7.2

The following customer-reported issues were fixed in this release:

- (HUB-35687). Fixed an issue when a CVE and BDSA vulnerability are related and the
  related vulnerability could be incorrectly added to a vulnerability remediation. If
  this occurs, the `vulnerable-bom-components` API would return a HTTP
  Response 400 / Bad Request error when applied to a component with this issue.
