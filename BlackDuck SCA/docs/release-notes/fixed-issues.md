---
title: "Fixed Issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "XcuqciMHjJaUIr_gAGEtKA"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:27.233295+00:00"
content_hash: "c71bbc55a072129aa6fcbf7639e571959f76b37cf48796fc1c67fabbebdcd631"
---

# Fixed Issues

The following customer-reported issues have been fixed in this release:

- (HUB-47450). Fixed an issue where component adjustments (such as modifying component origin, usage, or version) failed to save or apply to the BOM when existing adjustment records were present.
- (HUB-47462). Fixed an issue where users who were previous project owners or project creators did not appear in the assignable project owner dropdown under Project Settings > Project Details.
- (HUB-47795). Fixed an issue where updating the remediation status via the LTS BOM Remediation API for CVE-primary entries with linked BDSAs failed to persist the new remediation status.
- (HUB-47891). Fixed an issue where configured security rankings (such as NVD > BDSA) were not consistently applied to vulnerability displays at the Project BOM level.
- (HUB-48013). Fixed a `NullPointerException` in background reporting jobs that occurred when generating CycloneDX or SPDX SBOM reports for components containing non-standard or unlisted licenses.
- (HUB-48250). Resolved an issue where snippet matches marked as ignored were incorrectly included in generated SBOM reports.
- (HUB-48371). Resolved an issue where vulnerabilities from nested subprojects were not rolled up or displayed transitively in the parent project BOM view.
- (HUB-48416). Resolved an issue where duplicate KbUpdateWorkflowJob-Component Version Security Update background jobs could run concurrently, causing elevated JobRunner resource utilization.
- (HUB-48466). Resolved an issue where quoted exact-match search queries on the `/api/search/components-in-use` endpoint did not prioritize exact matches at the top of search results.
- (HUB-48571). Improved query performance and reduced response latency when searching components via the `/api/search/components-in-use` endpoint.
- (HUB-48689). Fixed an issue where querying the `/api/projects/{projectId}/versions/{versionId}/vulnerable-bom-components` endpoint with `filter=ignored:true` failed to return ignored BOM components.
- (HUB-48696). Resolved an RBAC permission restriction on `/api/usergroups` that prevented non-admin users from assigning project user groups when running scans with `detect.project.user.groups`.
- (HUB-48744). Fixed an issue where updating the remediation status via the LTS BOM Remediation PUT endpoint for CVE-primary entries with linked BDSAs failed to persist the updated status when origin mappings lacked explicit IDs.
- (HUB-48767). Resolved an issue where generated CycloneDX 1.6 SBOM reports populated CVE identifiers instead of the corresponding BDSA records associated with vulnerable components.
- (HUB-48842). Fixed an issue that caused binary scans to intermittently fail with `ERR05_1079 Internal Server Error ({integration.scass.unauthorized})` during status polling between Match Engine and SCASS.
- (HUB-48857). Resolved an issue where generated SBOM reports included CVEs from unassociated component versions that were not present in the project BOM.
- (HUB-48896). Fixed a UI rendering regression in Snippet View where candidate match details (component version, license, release date, and match percentage) in the Alternative Matches dropdown were misaligned and truncated.
