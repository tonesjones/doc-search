---
title: "Fixed Issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "MVziMmP1v5WfHH~NDTiHvA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:07.968020+00:00"
---

# Fixed Issues

The following issues have been fixed in this release:

- (HUB-46731). Improved the consistency of CPE (Common Platform Enumeration)
  selection in CycloneDX SBOM reports. When multiple CPEs are associated with a
  component, Black Duck SCA now selects the first CPE from an
  alphabetically sorted list, rather than a random selection.
- (HUB-46925). Resolved a critical bug causing upgrade failures during PostgreSQL
  migration when upgrading from version 2025.4.1 to 2025.10.1 in Helm/Kubernetes
  deployments. Fixed the migration script to correctly set recursive permissions
  on the certs and data directories, preventing permission errors that caused
  database startup failures and potential data corruption.
- (HUB-47003). Fixed SPDX import failures caused by underscores in repository names
  within download locations. Updated the SPDX Java model dependency to resolve the
  parsing issue.
- (HUB-47166). Resolved an issue where policy rules with multiple vulnerability
  conditions were not correctly evaluating the "Published Age" filter.
- (HUB-47174). Addressed an unspecified documentation gap regarding global roles in
  Black Duck SCA; users with roles such as Security Manager
  were previously unable to assign project-level roles due to a system setting
  that was not clearly documented, leading to confusion.The Role Matrix and
  supporting documentation has been updated to clarify this behavior.
- (HUB-47175). Fixed an issue where SPDX SBOM files containing certain license
  references (such as Artistic-dist and libpng-1.6.35) previously failed to import
  into Black Duck SCA due to the SPDX library's outdated vendored
  license list (version 3.26). The SPDX library has been updated to support
  license list version 3.27.0, resolving the parsing errors and allowing affected
  SPDX files to import successfully.
- (HUB-47226). Updated the documentation to clarify that policy rules based solely
  on vulnerability scores do not automatically exclude remediated vulnerabilities.
  To have violations clear upon remediation, policy rules must include remediation
  status conditions in addition to score-based criteria.
- (HUB-47282). Fixed an issue where ignored items could temporarily appear on the
  BOM Components tab after upgrading to a version with Match Review enabled; now
  ignored components and snippets are properly hidden from the BOM Components tab
  until the first BOM computation, while remaining visible in the Match Review
  tab.
