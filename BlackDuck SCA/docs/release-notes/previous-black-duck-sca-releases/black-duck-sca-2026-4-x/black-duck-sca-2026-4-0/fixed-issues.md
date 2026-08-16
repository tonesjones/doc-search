---
title: "Fixed Issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "vQUB59VUdF3vX84baoyxNQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:00.658001+00:00"
---

# Fixed Issues

The following customer-reported issues have been fixed in this release:

- (HUB-40429). Resolved an issue where the Black Duck binary scan failed to
  identify the Qt version 5.15.12. The scanner successfully detected the version
  in the BDIO export; however, it was not mapped to the correct channel, leading
  to identification issues.
- (HUB-46005). Resolved discrepancies in security risk counts following the upgrade
  to version 2025.4.2, where risk profiles were not updating correctly despite
  synchronized vulnerability counts.
- (HUB-46626). Investigated and addressed an issue where file paths were displayed
  as URL-encoded strings in the side-by-side snippet view.
- (HUB-46899). Resolved a bug affecting vulnerability prioritization where
  selecting NVD in Security Risk Ranking incorrectly displayed BDSA entries. The
  issue stemmed from a bug in the security re-ranking code, linked to changes in
  how vulnerability summaries are stored and processed following a recent update.
- (HUB-46929). Fixed an issue where custom component matches were ignored during
  the matching process when SCASS (cloud-based matching) was enabled, causing all
  custom-mapped origins to remain unmatched.
- (HUB-46968). Fixed a regression in version 2025.10.1 where converting a project
  version to LTS with the CycloneDX v1.6 specification incorrectly produced SPDX
  format reports.
- (HUB-46991). Fixed a bug in Black Duck SCA where scan sizes
  between 1,000 and 1,024 MB were incorrectly displayed as “KMB.”
- (HUB-47062). Resolved an issue where discrepancies between the notification
  workflow, activity logs, and database records were causing notifications for new
  vulnerabilities to go missing after KB updates in project versions.
- (HUB-47311). Resolved an issue with a security feature that incorrectly blocked
  the /api/search/components-in-use endpoint, resulting in 400 errors during
  normal usage.
