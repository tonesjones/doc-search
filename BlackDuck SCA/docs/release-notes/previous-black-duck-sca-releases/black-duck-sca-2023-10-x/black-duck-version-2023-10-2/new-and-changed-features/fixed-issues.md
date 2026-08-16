---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "deJSgTsZgXJ79FsJzmih5w"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:29.223269+00:00"
---

# Fixed issues

The following issues were fixed in this release:

- (HUB-40763). Fixed an intermittent issue where logging into Black Duck via SSO
  page could cause an authenticaton error after some time if the user did not log
  in immediately.
- (HUB-40944). Readded missing `created_at` and
  `updated_at` columns in the component table of the Reporting
  database.
- (HUB-40960). Fixed an issue where build packages in the manifest file were being
  captured by the Binary Scanner.
