---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "6K_aAZM7W3oXMPpMZZBH7Q"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:57.548987+00:00"
---

# Fixed issues

The following customer-reported issues were fixed in this release:

- (HUB-33736). Updated a number of API endpoints to use project and version names
  from the BDIO header instead of from HTTP headers. See the API enhancements
  section for more details.
- (HUB-36776). Fixed an issue where selecting 'Reveal in file tree' for a component
  in the Source tab did not show the file in the left side file tree for files
  part of the binary scan.
- (HUB-37280). Fixed an issue in SPDX 2.2 where all project files were listed
  despite "filesAnalyzed" being set to false.
- (HUB-38005). Removed the 'Vulnerability Reported' sorting option from the Find >
  Components page as it is no longer supported.
- (HUB-38141). Fixed a race condition when the scan client requested source files
  that did not belong to any matched directory/archive and were not stored in the
  database yet could cause inconsistent snippet scan results.
- (HUB-38212). Fixed an issue where a null pointer exception error could occur when
  importing a CycloneDX report.
- (HUB-38244). Fixed an issue where the Detect configuration page could display an
  error messsage when communicating with SIG Artifactory while running behind a
  proxy.
- (HUB-38279). Fixed an issue in the Black Duck UI under the 'Dashboard' tab where
  the 'Export Current View' button did not export the current view for 'Saved
  Searches'.
- (HUB-38312). Fixed an issue where vulnerability changes for bulk ignored
  components within Sub-Projects were not rolling up to the parent project.
- (HUB-38328). Fixed an issue where the policy override date info was not displayed
  correctly in Japanese settings due to an incorrect i18n character.
