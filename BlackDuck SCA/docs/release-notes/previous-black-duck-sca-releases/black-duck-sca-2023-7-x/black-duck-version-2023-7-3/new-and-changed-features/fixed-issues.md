---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "oTLympR7E9MH8x9vq8m~xw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:39.994111+00:00"
---

# Fixed issues

The following customer-reported issues were fixed in this release:

- (HUB-40080). Fixed an issue where the refresh materialized view query for
  updating the `reporting.component_vulnerability` view could
  execute multiple times in parallel from multiple different
  ReportingDatabaseTransferJobs.
