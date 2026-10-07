---
title: "Fixed Issues in 2022.7.2"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2022.7.2.html"
content_id: "91uj9kPnR8SFoea5uCzc9w"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:33.681153+00:00"
content_hash: "fb9fc48a2a39a4a18fa6701ca70dd751537e7acad7e5ce5f2ab43d322e1435aa"
---

# Fixed Issues in 2022.7.2

The following customer-reported issues were fixed in this release:

- (HUB-35687). Fixed an issue when a CVE and BDSA vulnerability are related and the related vulnerability could be incorrectly added to a vulnerability remediation. If this occurs, the `vulnerable-bom-components` API would return a HTTP Response 400 / Bad Request error when applied to a component with this issue.
