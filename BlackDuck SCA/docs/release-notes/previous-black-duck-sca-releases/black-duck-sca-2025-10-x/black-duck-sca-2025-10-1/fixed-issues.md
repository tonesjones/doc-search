---
title: "Fixed Issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "M~IeWQ7nbnULJDOeU_EmTQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:19.193025+00:00"
---

# Fixed Issues

The following customer-reported issues have been fixed in this release:

- (HUB-44483). Fixed an intermittent issue where 'Component Link' information was
  missing in Black Duck SCA reports, improving reliability for
  licensing and audit workflows. The fix ensures consistent link data across
  environments and versions.
- (HUB-44625). Fixed issues with stuck LTS transition jobs and failed rescans after
  upgrade, improving reliability of long-term support version conversions and
  preventing failures caused by database conflicts and residual data.
- (HUB-45472). Fixed an issue preventing updates to component origins for
  multi-origin components, ensuring consistent UI behavior and successful origin
  adjustments by removing legacy origin data and supporting only a single origin
  after changes.
- (HUB-45687). Fixed a license database access issue causing 400 errors in Black Duck SCA on-premises deployments, ensuring successful
  project creation and scans by improving header handling and configuration for
  secure connections.
- (HUB-45709). Fixed an issue where PURLs were modified during SBOM imports
  (especially for Golang components), ensuring user-defined PURLs are preserved
  and prioritized for accurate display and export.
- (HUB-45734). Fixed inconsistent BOM results for NPM packages by aligning fuzzy
  matching behavior between HUB and SCASS, improving handling of unknown versions,
  and adding configuration options for better accuracy across all scan paths.
- (HUB-45873). Fixed an issue where versions for the googleapis/go-genproto
  component were not detected in scans, improving signature matching to ensure
  accurate version identification for subcomponents.
- (HUB-46114). Fixed an issue where bulk editing the 'Usage' field on SBOM
  components did not update correctly, ensuring accurate updates for all usage
  types, including “Dynamically Linked,” in both UI and backend.
- (HUB-46306). Fixed an issue where Path and Archive Context fields were missing in
  source reports, ensuring all relevant scan data columns are correctly populated
  for accurate reporting.
- (HUB-46439). Fixed an issue where SBOM components identified only by CPE
  references were not logged during import, ensuring all components generate BOM
  Import Log entries with clear status messages for improved visibility.
- (HUB-46467). Resolved an issue in the notifications API where duplicate
  notifications caused inconsistent results when retrieving notification data. The
  problem arose from the handling of notifications with identical timestamps,
  leading to some expected notifications not being returned.
- (HUB-46573). Fixed an issue where SBOM uploads using CycloneDX v1.5 failed due to
  unsupported tools.services format, adding compliance with the current CycloneDX
  specification for Tools metadata.
- (HUB-46674). Resolved an issue causing SBOM scans to fail with an "ERR05_1022
  Internal Server Error" due to empty Component Hash arrays. The fix ensures that
  the import process handles such cases more robustly, preventing failures when
  valid SBOMs contain empty arrays.
