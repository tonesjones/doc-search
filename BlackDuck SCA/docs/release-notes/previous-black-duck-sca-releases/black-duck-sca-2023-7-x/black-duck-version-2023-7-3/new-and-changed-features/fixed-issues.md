---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "QCG4Fit9w~xeDoltYKwSWw"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:31.701723+00:00"
content_hash: "16af8cea5ff2c3f555f0e7fd8ee3760bf747d6ec101b1a3951363a24d057ea78"
---

# Fixed issues

The following customer-reported issues were fixed in this release:

- (HUB-40080). Fixed an issue where the refresh materialized view query for updating the `reporting.component_vulnerability` view could execute multiple times in parallel from multiple different ReportingDatabaseTransferJobs.
