---
title: "Fixed Issues in 2021.8.3"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2021.8.3.html"
content_id: "IHTkwk2x6rYYutrmR4BJww"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:35.303585+00:00"
content_hash: "c820f2a8fb7a96aa2e913b23b79ff594dde0f5f04c51e0f2abcec13b5504e55a"
---

# Fixed Issues in 2021.8.3

The following customer-reported issues were fixed in this release:

- (HUB-29959, HUB-30391, and HUB-30397). Fixed an issue where scans would not complete due to a 500 Internal Error response from the KnowledgeBase while preparing the Bill of Materials.
- (HUB-31047). Fixed an issue when populating the version BOM components page, the UI makes duplicate calls to the back-end generating unnecessary stress to the database.
- (HUB-30074). Fixed an issue where very small code locations snippet scans sometimes finish before upload source info is updated giving the appearance that the uploaded source was lost.
