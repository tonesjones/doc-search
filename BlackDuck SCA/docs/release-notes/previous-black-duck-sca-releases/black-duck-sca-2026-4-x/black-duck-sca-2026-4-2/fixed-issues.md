---
title: "Fixed Issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "TSGJDnHCPxBsBkQ_Q8oEbg"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:27.511045+00:00"
content_hash: "40f58af3635bd9e8cb6433b38134e3a5b7f2954dbf5830943a6cc08e7f39c7d0"
---

# Fixed Issues

The following customer-reported issues have been fixed in this release:

- (HUB-47911). Fixed an issue where BOM file adjustments would intermittently fail with an "Unknown error" when editing matches on project versions with multiple contributing code locations. This was due to a temporary database table being created multiple times within a single transaction.
