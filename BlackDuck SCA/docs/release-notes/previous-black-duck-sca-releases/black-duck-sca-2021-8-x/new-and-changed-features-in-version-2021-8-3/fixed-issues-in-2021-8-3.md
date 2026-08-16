---
title: "Fixed Issues in 2021.8.3"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2021.8.3.html"
content_id: "NRxxdU7o3a_ostl6~s5msQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:02.870471+00:00"
---

# Fixed Issues in 2021.8.3

The following customer-reported issues were fixed in this release:

- (HUB-29959, HUB-30391, and HUB-30397). Fixed an issue where scans would
  not complete due to a 500 Internal Error response from the KnowledgeBase
  while preparing the Bill of Materials.
- (HUB-31047). Fixed an issue when populating the version BOM components
  page, the UI makes duplicate calls to the back-end generating
  unnecessary stress to the database.
- (HUB-30074). Fixed an issue where very small code locations snippet scans
  sometimes finish before upload source info is updated giving the
  appearance that the uploaded source was lost.
