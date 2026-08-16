---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "sVBwt7vy3Ga6O8EAM6NK8g"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:34.021112+00:00"
---

# Fixed issues

The following customer-reported issues have been fixed in this release:

- (HUB-45342). Fixed an issue that caused the ignored status flag in
  `version_bom_risk_warning` to become inconsistent with the
  remediation status due to residual data in
  `version_bom_risk_status`. The issue was traced to leftover
  data in `version_bom_risk_status` from migration scripts, which
  caused ignored flags to revert incorrectly. The fix involved rerunning migration
  scripts and deleting specific records where the status was REMEDIATED but
  ignored was false, ensuring proper synchronization between ignored flags and
  remediation status.
- (HUB-45481). Resolved an issue where the upgrade to version 2025.4.1 took an
  excessive amount of time due to an unoptimized upgrade script. The script has
  been optimized to significantly improve upgrade performance.
- (HUB-45490). Addressed an issue where the KB update job occasionally failed to
  update certain project versions with newly identified vulnerabilities. During
  the investigation, it was identified that vulnerability counts for component
  versions were out of sync across various project versions. As part of this
  update, the BOM for affected component versions has been refreshed to improve
  accuracy. However, new components that appear after the BOM refresh are not
  automatically updated at this time. Further improvements are being actively
  developed to provide a more comprehensive solution in future releases.
- (HUB-45609). Fixed a SQL error caused by incorrect argument ordering in the query
  for the endpoint
  `/api/vulnerabilities/{vulnerability_id}/affected-bom-components`.
  The issue resulted in a `BadSqlGrammarException` and a PostgreSQL
  error indicating a mismatch between the `~~*` operator and
  argument types (`text` vs. `UUID`). The fix
  corrected the query's argument order to ensure proper execution across all
  namespaces.
- (HUB-45699). Improved the performance of the components-in-use API by optimizing
  the query plan to significantly reduce execution time and resource usage. The
  previous implementation caused excessive data processing and disk spill during
  sorting. By streamlining the query logic, the fix greatly reduces system
  overhead and improves response times, making the API more efficient and
  usable.
