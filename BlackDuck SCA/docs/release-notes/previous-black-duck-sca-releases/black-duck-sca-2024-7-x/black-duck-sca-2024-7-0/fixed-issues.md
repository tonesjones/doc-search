---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "Wig0jZbkvw3NOZ1FrCCaMg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:10.010830+00:00"
---

# Fixed issues

The following customer-reported issues have been fixed in this release:

- (HUB-34550). Fixed the way short numeric dates are display based on web browser
  locale. For example, European locales will now display day/month/year date
  format.
- (HUB-40168). Fixed copyright display issues. See Improved copyright handling in reports for more information.
- (HUB-40687). Fixed an issue where the last scanned time was not displayed
  correctly on the Find page.
- (HUB-40774). Fixed an issue where vulnerabilities with a CVSS 3 attack vector
  value of "adjacent network" were previously mapped in Black Duck with a null value. As of 2024.7.0 the value is properly mapped, and a
  one-time job will be triggered to fill in that data for any cached
  vulnerabilities with a null CVSS 3 attack vector field.
- (HUB-41220). Fixed an issue where the incorrect severity level could be displayed
  when searching for vulnerabilities on the Find page.
- (HUB-41264). Fixed an issue where the scan size displayed was inconsistent
  between the Scan page (with snippet matching) and the .CSV file generated when
  clicking ‘Export Current View’ button.
- (HUB-41348). Fixed an issue on the Scan page where the sorting of scans by size
  was incorrect when snippets are included.
- (HUB-41683). Removed the `vulnerabilityName` field from the
  `/api/projects/<project-id>/versions/<version-id>/vulnerable-bom-components`
  API request in the new lightweight version as `vulnerabilityName`
  and `vulnerabilityId` fields possessed same value and
  `vulnerabilityId` is more commonly used.
- (HUB-41851). Renamed a duplicate "Component Origin Id" column in the Version
  Details Report (Project Version Upgrade Guidance) to Component Origin External
  ID.
- (HUB-42041). Fixed an issue where once edits to a component details
  setting/license/custom field is made on the global level and you try to revert
  back to previous pages visited in Black Duck, it loses the
  navigation and never brings you back.
- (HUB-42054). Fixed an issue where the
  `/api/projects/{projectId}/versions/{projectVersionId}/risk-profile`
  API request was returning unknown security risk for ignored confirmed snippets
  match types on components tab.
- (HUB-42155). Fixed an issue where the Last Updated timestamp for project version
  auto-deletion was being erroneously modified by system computations and other
  project adjustments.
- (HUB-42225). Fixed an issue on the project version's Source tab where the
  Unmatched filter option displayed both unmatched files and unmatched components,
  which made it difficult to find unmatched components amongst the results. This
  filter has now been split into two separate values: Unmatched Files (displays
  only unmatched files) and Unmatched IDs (displays only unmatched component
  ids).
- (HUB-42260). Fixed an issue where the exploit available status of CVE
  vulnerabilities in the UI and in the vulnerability report may not match in
  certain circumstances.
- (HUB-42363). Fixed an issue where users with direct/indirect access to a project
  could not see layer information for container scans.
- (HUB-42402, HUB-42471). Fixed an issue where project versions without mapped scans were not
  being scheduled for project version auto-deletion.
- (HUB-42466). Fixed an issue where scanning a large project with a package manager
  scan could result in an output file containing over 10,000 graph nodes,
  potentially causing the scan container to eventually time out.
- (HUB-42478). Fixed an issue where the reporting database was not getting
  populated when using `hub_db_migrate.sh` due to
  `search_path` not being passed correctly in the definitions
  of the reporting database matviews.
- (HUB-42531). Fixed an issue where attempting to download system logs could
  generate a "Log files not found" error when deploying with read only YAML
  file.
- (HUB-42545). Fixed an issue where long term support (LTS) projects did not show
  up in the modal for adding projects to a project version, and when manually
  calling the API to do so, they did not appear in the list of components.
- (HUB-42753). Fixed an issue where binary matches incorrectly added an extra ID to
  the count set by the API for BOM matches. This discrepancy affected the match
  confidence, causing it to misalign with the number of alternatives in fuzzy
  matches.
- (HUB-42760). Fixed an issue where the Snippet Review Status column was missing
  when creating a Version Details report with the Components category added.
- (HUB-42811). Fixed a pagination issue where the `offset` value for
  the `vulnerable-bom-components` API endpoint was returning the
  same result regardless of what the value was set to.
- (HUB-42873). Fixed an issue where SBOM Copyright reports could fail due to not
  validating if the component exists in the BOM.
- (HUB-42953). Fixed an issue where the risk profile in the Version Details Report
  incorrectly used the operational risk medium count instead of license medium
  risk count.
- (HUB-43001). Fixed an issue regarding the documentation regarding the
  configuration of the automatic scan retry header.
