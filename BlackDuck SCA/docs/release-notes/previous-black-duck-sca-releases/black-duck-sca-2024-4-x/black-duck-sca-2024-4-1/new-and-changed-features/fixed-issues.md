---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "e44E19mqaMeOj39j_~_r7Q"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:14.640926+00:00"
---

# Fixed issues

The following customer-reported issues were fixed in this release:

- (HUB-39354). Fixed an issue where the Project Alias field in the Software Bill of
  Materials (SBOM) only overrode the Main Project name and Version at the Project
  level and did not extend to subprojects included in an SBOM report.
- (HUB-39807). Fixed an issue where the vulnerable-bom-components API endpoint in
  the UI could hang indefinitely.
- (HUB-41575). Fixed an issue where archive files being downloaded from the Scan
  list were downloaded with the wrong file type, resulting in an error when
  uploading as a BDIO file.
- (HUB-41670). Fixed an issue where the scan pod was having difficulties accessing
  the rabbitmq admin plugin to allow for the retry attempts to occur on hosted
  environments with rate limiting enabled.
- (HUB-41753). Fixed an issue where the `DESCRIBES` relationship was
  missing from the SPDX SBOM report exports.
- (HUB-41992). Fixed an issue where custom fields containing the "/" character
  could cause a blank list of conditions when creating policies for those custom
  fields.
- (HUB-42086). Fixed an issue where the
  `api/versions/<versionID>/reports` endpoint was displaying
  unclear information in the `riskProfile` section of the API
  output.
- (HUB-42101). Fixed an issue where the VULNERABILITY_REPRIORITIZATION job could
  get stuck when processing entries without a cvss3 score.
- (HUB-42158). Fixed an issue where the SBOM SPDX report was not displaying the
  correct license name for "SSLeay License - standalone".
- (HUB-42208). Fixed an issue where the Error Status filter was missing on Jobs
  page on some instances.
- (HUB-42304). Added an index for the
  `st.version_bom_entry(code_location_id)` table to help
  alleviate the pressure against the specific table in question.
- (HUB-42334). Fixed a sorting order issue on the Malware tab of the project
  version page which could result in duplicate rule ID entries.
- (HUB-42382). Fixed an issue where the Source tab did not redisplay matches after
  deselecting matched item in File Tree.
- (HUB-42585). Fixed an issue where new SAML and LDAP user accounts could not
  authenticate properly when added to the designated default user group.
