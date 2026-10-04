---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "dOoYKr4ewYMer5zZ5m_qnA"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:33.261931+00:00"
content_hash: "3f10aaf45b8fcb143a607ce6bf5442bb853cbbd2d0e9848c8435402e1ae195d4"
---

# Fixed issues

The following customer-reported issues were fixed in this release:

- (HUB-35377). Fixed an issue where unconfirmed snippets and ignored component were showing up in component or license usage counts anywhere within Black Duck except the source view when reviewing unconfirmed/ignored snippets.
- (HUB-35850). Fixed an issue where Redis could not access data on default Openshift environments.
- (HUB-36049). Fixed an issue where `FileBackedOutputStream` temp files were written to `/tmp` directory under the scan container and are not cleaned up.
- (HUB-36149). Fixed an issue when printing a BOM as a PDF, it did not include the project name and version name.
- (HUB-36359). Fixed the missing link to the `blackduck-webui` container on the Guthub release page.
- (HUB-36495). Fixed some outdated images the online help.
