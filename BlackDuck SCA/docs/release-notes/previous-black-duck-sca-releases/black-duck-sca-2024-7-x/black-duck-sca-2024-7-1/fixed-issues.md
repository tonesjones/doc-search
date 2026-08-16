---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "vqxmqoSnUy~2AVSPwWNxFg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:06.575061+00:00"
---

# Fixed issues

The following customer-reported issues have been fixed in this release:

- (HUB-42054). Fixed an issue with the
  `/api/projects/{projectId}/versions/{projectVersionId}/risk-profile`
  API request returning unknown security risk for ignored confirmed snippets match
  types on components tab.
- (HUB-42392). Fixed an issue where an `ERR05_1028` exception error
  could occur when old, unmapped Scans were being purged.
- (HUB-42549). Fixed an issue where a `LicenseConflictBaseStrategy`
  warning was appearing repeatedly during BOM computation.
- (HUB-42626). Added a workaround for an issue where, under certain situations
  where a DNS server is configured, a bug in the curl/c-ares package (included in
  all alpine based images) prevented resolution of the cfssl domain, which caused
  the containers to crash because they weren't able to obtain the necessary
  certificates to deploy.

  **NOTE:** The maintainer of c-ares has release a patch for this bug. However,
  it is not yet available in a stable release of Alpine Linux, and the
  availability timeline is currently uncertain.
- (HUB-42786). Fixed a snippet match query optimisation issue where project
  versions with a large number of unconfirmed snippet matches could cause the BOM
  component page to load more slowly.
- (HUB-42811). Fixed an API pagination issue with the
  `vulnerable-bom-components` endpoint which could affect
  projects with large amount of vulnerabilities (500+).
- (HUB-42922). Fixed an issue where modifying the remediation status could fail on
  the Vulnerability Affected Projects page, displaying a "Cannot read properties
  of undefined (reading 'protocol')" error in the Update Remediation Plan
  dialog.
- (HUB-42939). Fixed an issue where IdP metadata was not being refreshed. Black Duck will now reload the configuration for SAML every
  half hour, which includes the IdP metadata.
- (HUB-43029). Fixed an issue where running the webapp with a non standard set of
  user and group could cause the logfiles to not be available on the UI due to an
  error generating the zip file.
- (HUB-43052). Fixed a sorting issue on the Scans page where sorting the "Updated"
  column multiple times and then sorting by another column, navigating away and
  returning to the page without refreshing could result in the page not retaining
  the "Updated" sort order.
- (HUB-43060). Fixed an issue where custom field details were not wrapped on the
  Settings page despite line breaks being set.
- (HUB-43257). Fixed an issue where the content displayed in the What's New window
  would not render if the browser local was set to an unsupported language.
- (HUB-43258). Fixed an issue where the Component policy status and Overridden By
  columns of the Version details report were empty in source.csv report.
- (HUB-43378). Fixed an issue where the
  `--detect.code.location.name` parameter was not working with
  BDBA scans.
