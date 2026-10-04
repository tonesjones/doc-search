---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "wdn8VQIepHYuiFKk6vTaZQ"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:31.252336+00:00"
content_hash: "b3ee6f92475579b01e9b66caae2e6d27eb3877160441c44c60a974bb2ed55b36"
---

# Fixed issues

The following issues were fixed in this release:

- (HUB-40763). Fixed an intermittent issue where logging into Black Duck via SSO page could cause an authenticaton error after some time if the user did not log in immediately.
- (HUB-40944). Readded missing `created_at` and `updated_at` columns in the component table of the Reporting database.
- (HUB-40960). Fixed an issue where build packages in the manifest file were being captured by the Binary Scanner.
