---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "rNEtZOM29cr09TZU0429jQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:45.281515+00:00"
---

# Fixed issues

The following customer-reported issues have been fixed in this release:

- (HUB-43061). Fixed an issue when using the
  `--detect.blackduck.signature.scanner.individual.file.matching=SOURCE`
  option could produce no results when scanning `.js` files.
- (HUB-43374). Added the missing description, source, and severity fields for the
  V8
  `/api/projects/{projectId}/versions/{projectVersionId}/vulnerable-bom-components`
  endpoint.
- (HUB-43389, HUB-44090). Fixed an issue where security risks were still being counted in the
  BOM when the status of their vulnerabilities were set as
  Ignored/Mitigated/Remediation complete.
- (HUB-43931). Fixed an issue where components might not be consolidated in the
  project's Source tab.
- (HUB-44076). Fixed an issue where a blank page could be displayed when visiting
  https://HUB_URL/alert/ after updating Black Duck from version 2023.1.2 to
  2024.4.1, and Alert from version 6.12.2 to 7.2.0.
- (HUB-44089). Fixed an issue where security vulnerabilities from removed
  components could still show up in the Security tab for a project.
- (HUB-44104). Fixed an issue where snippet matches continued to display with
  policy violations in the BOM and Source tab after being remediated as Confirmed
  and then marked as Ignore Match on the Source tab.
- (HUB-44185). Fixed a proxy issue that could cause the What's New window to be
  blank.
- (HUB-44186). Fixed database deadlock issues that could occur when updating
  `version_bom_risk_profile`.
- (HUB-44190). Fixed an issue where SPDX report generation could fail for projects
  with a CycloneDX SBOM mapped.
- (HUB-44210). Fixed an issue where expanding the Source tree in a BOM could result
  in a 400 Bad Request error.
- (HUB-44253). Fixed database deadlock issues that could occur when updating
  `version_bom_component`.
- (HUB-44365). Fixed an issue where a Duplicate key error could be generated when
  importing a CycloneDX SBOM that was merged using cyclonedx-cli tool into a
  single SBOM JSON file.
- (HUB-44366). Fixed an issue where the “scans” array was no longer included in the
  `aggregateBomViewEntries` array of the REST API doc for
  Version Report Endpoints.
- (HUB-44486). Fixed an issue where component matches in a Container scan were
  incorrectly stored when the same component identifier was present in both the
  base image layer and a custom layer.
- (HUB-44515). Migrated Detect Desktop to Black Duck, including download links and
  branding.
- (HUB-44549). Fixed an issue where Container Scans could generate different
  results after running apt update.
- (HUB-44584, HUB-44623). Fixed an issue where the
  `blackduck-postgres-init` job could fail in hosted
  environments, preventing the successful execution of the Create Hub job.
