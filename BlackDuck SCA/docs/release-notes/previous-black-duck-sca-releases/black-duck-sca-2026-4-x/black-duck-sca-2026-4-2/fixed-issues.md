---
title: "Fixed Issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "aiApyCihSr8Cs_apyRXk_w"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:34:53.904018+00:00"
---

# Fixed Issues

The following customer-reported issues have been fixed in this release:

- (HUB-47911). Fixed an issue where BOM file adjustments would intermittently fail
  with an "Unknown error" when editing matches on project versions with multiple
  contributing code locations. This was due to a temporary database table being
  created multiple times within a single transaction.
