---
title: "Fixed Issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "9mSEC0EohcG0dn4O~cTtLg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:11.968590+00:00"
---

# Fixed Issues

The following customer-reported issues have been fixed in this release:

- (HUB-44108). Fixed excessive warning messages related to source VBC ID detection
  failures, specifically the message "Could not determine source VBC ID for child
  project when calculating license conflicts."
- (HUB-44352). Resolved a bug in the reporting database materialized view where
  reporting.component was counting/showing unconfirmed snippets in a
  project/version, causing discrepancies in BOM component counts.
- (HUB-45050). Resolved an SSL certificate mismatch issue during a Kubernetes
  upgrade that affected jobrunner health checks. The IPv4 address was added to the
  jobrunner's certificate SANs, eliminating SSLPeerUnverifiedException errors.
- (HUB-45320). Updated API Documentation to include the previously missing fields
  in the project representation for the projects API endpoint. The fields to be
  added are `deepLicenseDataEnabled`,
  `deepLicenseDataSnippetEnabled`, and
  `licenseConflictsEnabled`, which are returned in the response
  of the `GET /api/projects/{projectId}` endpoint.
- (HUB-45475). Resolved a bug that caused vulnerabilities to be omitted from the
  `components.csv` file after editing manual snippets with an
  origin set. Specifically, if components added as "Manually Identified, Snippet"
  were bulk edited using the 'Adjust Snippets and Confirm' option in the Source
  tab, their associated vulnerabilities were not included in the
  `components.csv` file. The fix ensures that vulnerabilities
  are correctly captured and reported in the file.
- (HUB-45694). Resolved the issue of missing supplier names in CycloneDX SBOM
  reports generated in Black Duck SCA.
- (HUB-45944). Resolved an issue where components present in an earlier (inner)
  layer of a container image but deleted in a higher (outer) layer were not
  recognized by the scanner as part of the final image. This issue resulted in
  components that had been removed still appearing in the Vulnerability
  Remediation Report during container scans.
- (HUB-46037). Addressed an issue where Nginx returned a 403 Forbidden response for
  requests to non-existent files (e.g., /metrics.json) instead of the expected 404
  Not Found status.
- (HUB-46115). Manually added component BOM matches can no longer be ignored by
  bulk adjustments.
- (HUB-46291). Resolved an issue where uploading a BDIO file exceeding the "Maximum
  code location size" silently failed without providing an error message to the
  user. Previously, users would see that the upload appeared successful, but the
  scan data would not be listed due to the failure occurring between upload and
  scan creation.
- (HUB-46359). Resolved a regression issue related to project settings that caused
  an invalid error message when setting unmatched file purging options.
- (HUB-46551). Fixed an issue where the License Terms page did not auto-refresh
  when activating or deactivating a license term.
- (HUB-46572). Resolved issue with remediation comments not showing in the UI after
  upgrading to version 2025.7.1. Previously, comments associated with components
  having a single origin were visible, but changes in functionality to display
  multiple origins for a component led to the disappearance of these comments in
  the UI.
- (HUB-46598). Resolved issues with large binary multi-part uploads in multi-node
  AKS deployments, which led to connection resets and message digest errors during
  re-assembly.
- (HUB-46642). Resolved issue where an inactive project group link was shown to a
  non-admin project group user.
- (HUB-46656). Improved performance of the `/api/projects` endpoint
  by optimizing view conversion in `ProjectV6ViewConverter` and
  reducing repetitive database queries, resulting in faster project listing and
  typeahead operations.
- (HUB-46669). Resolved a bug that caused an HTTP 400 Bad Request error when
  attempting to remove a hash from the Project Version SBOM fields.
