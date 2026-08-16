---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "shOSAaMmQk8Y2tkeffTjyw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:18.014707+00:00"
---

# Fixed issues

The following customer-reported issues were fixed in this release:

- (HUB-39206). Fixed an issue where the binary scanner was not detecting .DEB file
  components causing them to not appear in the resulting report.
- (HUB-39395). Fixed an issue where KnowledgeBase updates was showing the Last
  Updated user as the user who added the component in Component Management. Custom
  components updated by KnowledgeBase update jobs will now display as System
  User.
- (HUB-39635). Fixed an issue when a Detect CONTAINER_SCAN was run in conjuction
  with other scan types (e.g. DETECTOR or BINARY_SCAN), Detect was not returning
  the expected `412 Precondition Failed` error message.
- (HUB-40531). Fixed an issue where component reports could produce duplicate
  entries for some components.
- (HUB-40745). Fixed aSPDX SBOM report issue where the PackageSupplier field may be
  different from the origin name in the Purl field when there are multiple origins
  for a same component version in the BOM.
- (HUB-40769). Deprecated the API request GET
  /api/projects/{projectId}/versions/{projectVersionId}/matched-components as it
  was returning a 404 error when used.
- (HUB-40870). Fixed an issue when constructing the URL encoding the search
  parameters of the ‘origins-with-filters' link leading to the component's
  Copyright page.
- (HUB-40930). Fixed an issue in localized CSV files where garbled characters were
  displayed when opening search results in Excel.
- (HUB-40998). Fixed an issue where thePackage Valid Until Date field in SBOM
  report was not being cleared when removed by the user.
- (HUB-41041). Fixed a broken link in the SCAaaS helm chart readme file.
- (HUB-41063). Fixed an issue where only "Direct Dependency" would show if both
  "Transitive" and "Direct" matches existed within the same component version.
- (HUB-41132). Fixed an issue where searching for components containing the +
  special character could not return the expected results.
- (HUB-41167). Fixed the REST API documentation concerning the supported filters of
  the Listing Project Versions API. The only supported filters are phase, license,
  and distribution.
- (HUB-41276). Fixed an issue where components with Unknown Licenses would not be
  included into the Notices File report.
- (HUB-41299). Fixed an issue where custom components that were previously mapped
  and then deleted were being remapped erroneously, affecting unmatched components
  totals in subsequent scans.
- (HUB-41316). Fixed an issue where upgrading SaaS to 2023.7.3 could cause SSO to
  fail.
- (HUB-41318). Fixed an issue with inconsistent behavior when searching component
  versions.
- (HUB-41321). Fixed an issue where comments for snippet results in .ZIP files were
  not exported to the source report.
- (HUB-41362). Fixed an issue where the Discovery filter was displaying all
  discoveries instead of the search results based on the text typed into the
  search field.
- (HUB-41365). Fixed an issue when the `/api/projects` limit is set
  to 0 (`/api/projects?limit=0`) could cause the resulting page to
  never load.
- (HUB-41369). Fixed an issue where uploaded branding logos were not automatically
  scaled down to fit the size requirements as intended.
- (HUB-41391). Fixed an issue where incorrectly formed PURL fields in a SBOM could
  cause CycloneDX to fail importing the SBOM file.
- (HUB-41431). Fixed a documentation issue related to the Project Manager role and
  project deletion permissions.
- (HUB-41450). Updated the readme file to correctly the ordering of values.yaml
  file before the sizing.yaml in the deployment command.
- (HUB-41461). Fixed an issue where the Total Count displayed when using the
  Listing Affected Project Versions API was the number of projects, not project
  versions.
- (HUB-41502). Resolved security issues found in the SCAaaS deployment.
- (HUB-41542). Fixed an issue where the BOM Last Updated date was being reset by
  kbupdatejob component update on fuzzy BDBA scans.
- (HUB-41549). Fixed a localization issue when exporting the users list in CSV
  format.
- (HUB-41552). Fixed an issue with the Project Version Auto-Deletion function
  interaction with the Retain Project Version regardless of data retention
  policies when it is disabled and the system is restarted.
- (HUB-41570). Fixed an issue where the `scan_stats_view`
  materialised view taking excessive amount of time to execute.
- (HUB-41591). Fixed a deadlock issues in the HUB CloudSQL database caused by
  delete queries.
- (HUB-41773). Fixed an issue when attempting to upload multiple files in a folder
  and dragged them on the Upload SBOM-SPDX File or Upload SBOM-CycloneDX File.
- (HUB-41867). Fixed an issue where any vulnerability notification generated by KB
  Update job and BOM Package Adjustment (User manually mapped an unmatched
  external ID in a BOM to a KB component) had the incorrect "Unknown" event
  source.
- (HUB-41930). Fixed an issue where the nginx webserver would not start unless the
  user running the pod is either root (0) or nginx (101).
- (HUB-41974). Fixed an issue with the Unmatched Filter on the Project Version ->
  Source Tab displaying incorrect counts.
- (HUB-42004). Fixed an issue where access a page in Black Duck immediately after
  SSO login would not take the user to the intended page.
- (HUB-42051). Fixed an issue where the value of `download_location`
  in `version_bom_component` was not removed when the component
  download location in the UI was cleared.
