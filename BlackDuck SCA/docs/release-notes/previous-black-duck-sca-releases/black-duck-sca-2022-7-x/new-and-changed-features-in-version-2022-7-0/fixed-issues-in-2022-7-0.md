---
title: "Fixed Issues in 2022.7.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2022.7.0.html"
content_id: "ZVfY5EguDYKyC5QUNl77hw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:33.722295+00:00"
---

# Fixed Issues in 2022.7.0

The following customer-reported issues were fixed in this release:

- (HUB-33231). Fixed an issue where sorting scans by scan size on the Scans page
  was not displaying the list in the correct order.
- (HUB-33974). Fixed an issue where the affected project count for vulnerabilities
  might be misleading. Ignoring a component will change the number of components
  with a given risk on the summary page. Vulnerability searches will not count
  ignored components, but the component search will.
- (HUB-32773). Fixed an issue when a component has been modified locally would
  cause our system to consider it a local component and not originating from the
  KnowledgeBase. The BOM computation would not query the KnowledgeBase when
  fetching new information for the component.
- (HUB-34468). Fixed issue where rapid scans would time out while waiting in queue
  for other, longer running scan types to finish matching.
- (HUB-34459). Fixed an issue where the `--matchConfidenceThreshold`
  parameter was not functioning when used with the traditional scan.cli.
- (HUB-33477). Fixed an issue where the Black Duck Metadata URL download button was
  available if SAML was disabled.
- (HUB-33549). Fixed an issue where the "Match Type" selection list for "Policy Management > Create Policy Rule > Component Conditions" doesn't have "Direct Dependency Binary" and "Transitive
  Dependency Binary" options.
- (HUB-34215). Updated the jackson-databind and gson components in responses to
  finding 4 high vulnerabilities.
- (HUB-33551). Fixed an issue where uploading a BDIO file with a null code location
  would fail with status code 400.
- (HUB-32919). Fixed an issue when attempting to download a scan using aggregate
  mode BDIO from Hub would produce a corrupt/empty BDIO of 0 bytes.
- (HUB-29445). Fixed an issue where the Projects REST API filtering did not support
  project names with commas.
- (HUB-33164). Fixed an issue where system logs were not downloadable from the
  Blackduck UI when excessive in size.
- (HUB-34282). Fixed an issue with the system_check.sh script where it could
  produce false warnings if the limits and reservations for memory are set to
  exceeding 512MB higher than Java heap size. the script has been updated to flag
  when the overhead is >20% and >1024Mb of memory so that smaller containers will
  not cause false warnings when set up in accordance to the documentation.
- (HUB-33923). Fixed an issue when refreshing the Admin > Diagnostics > System Information > Job page, the statistics for job history could display significantly
  different counts.
- (HUB-34195). Updated the REST API documentation to remove `SBOM`
  as a value from `reportType` from the Creating a Version Report
  section (or the `/api/versions/{projectVersionId}/reports`
  request).
- (HUB-34296). Fixed an issue where the policy override date info cannot be
  displayed in Japanese settings due to an incorrect i18n character.
- (HUB-32008). Fixed an issue where the Security Risk Ranking page can get stuck
  Processing due to "Up-to-date with error" events not being auto-cleaned-up by
  the QuartzVersionBomEventCleanupJob job.
- (HUB-33727). Fixed a UI bug when updating remediation status or comment of a
  vulnerability (In Security tab of Project Version).
- (HUB-33691). Fixed a UI bug where the warning icons were missing on the
  Cryptography tab for encryption algorithms with known weaknesses.
- (HUB-34240). Fixed an issue with the
  `/api/projects/{projectId}/custom-fields/{customFieldId}`
  request where it could generate a 400 error when posting a null value.
- (HUB-34246). Fixed browser display issues on the Project Version Comparison
  view.
- (HUB-33246). Clarified the REST API documentation; replaced references to
  `https://.../` for
  `https://<server-url>/api/`.
- (HUB-33481). Fixed an issue with the inconsistent response of
  `/api/projects/{pid}/versions/{vid}/matched-files?offset={larger than
  totalCount}` between 2021.8.x and later versions. The matched-files
  endpoint should return now consistently return a 200 OK response with empty
  items even if the offset > totalCount.
- (HUB-34468). Fixed an issue where Rapid Scan was failing with the following
  error: "Error getting developer scan result. Timeout may have occurred." or a
  HTTP 404 Not Found response caused by a delay in the match engine.
- (HUB-33512). Updated the text for Test Connection, User Authentication and Field Mapping
  found under Administration > Settings > User Authentication. Removed the mention of "and shows result of mapping test-user's
  meta-data".
- (HUB-34836). Fixed an issue where it was possible to edit unmatched components as
  the project itself when the BLACKDUCK_HUB_SHOW_UNMATCHED flag was enabled.
- (HUB-34380). Fixed an issue when trying to scan a new version into a project that
  has had a very large number of adjustments made to it could cause the BOM scan
  of the new version to fail on the server with the message "Exception occurred
  Too many parameters".
- (HUB-33793). Fixed an issue where Project Version details report was failing when
  a registration key not licensed with “Black Duck Security Advisory” was used
  with a change in security risk ranking.
- (HUB-33375). Fixed some bad SQL grammar in the query building code where ORDER_BY
  was outside of the loop that determines which field by which to sort. If there
  were no sort fields, the ORDER_BY would be null.
- (HUB-34780). Fixed an issue where the statistics on Administration > Diagnostics > usage:
  project > Project_created/Version_Created/Version_Deleted was limited to 500
  even if more than 500 projects/version were created or deleted.
- (HUB-34592). Fixed a deserialization of CodeLocationBomMatchCacheEntry error when
  there are zero matched components, but both empty and existing fails in the
  test.
- (HUB-34588). Fixed an issue with the copyright links for the conan package not
  working due to unencoded hash character in link.
- (HUB-24664). Fixed an issue where BDSBackgroundUpdateWorker was still trying to
  communicate out to the registration servers over HTTP rather than HTTPS.
- (HUB-33679). Fixed an issue where MaaS enabled scans sometimes fail when
  extracting composite elements.
- (HUB-34218). Updated the REST API documentation to include "componentVersionName"
  and "componentVersion" for "BOM Component Representation".
