---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "k8TKpsyBWuSiCr~Bzc4Z4Q"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:37.380565+00:00"
---

# Fixed issues

The following customer-reported issues have been fixed in this release:

- (HUB-45290, HUB-45293, HUB-45332, HUB-45360). This release re-addresses an issue
  where vulnerability remediation status was incorrectly applied to all origins of
  a component version. The original fix included a database migration and code
  changes, but remediation statuses could still fall out of sync due to
  KnowledgeBase update jobs. This update corrects the issue more comprehensively
  to ensure remediation status is consistently applied per origin.

  Additionally, the database migration script has been updated to prevent
  subproject risk counts from being reset during the upgrade process. After
  upgrade, subproject risks may briefly appear missing from project rollups; these
  values are automatically recalculated by the BOM Vulnerability Recomputation
  Check within approximately 10 minutes for the server restarting. Once this job
  is completed, the counts will be updated for subprojects. Archived projects must
  be unarchived in order to get their BOMs refreshed. Please contact Black Duck
  customer support for further assistance.

  Note: This fix includes a database migration. For customers with large databases,
  the migration process may take up to an hour or more to complete.
- (HUB-45300). Fixed an issue where stricter timestamp parsing in the API caused
  failures when processing issueCreateAt and issueUpdatedAT fields, impacting
  integrations with issue trackers such as JIRA via Alert 8.0.1. The issue was
  resolved by introducing a fallback parser to accept additional timestamp
  formats.
- (HUB-45349). Temporarily removed the vulnerability count label on the Security
  tab of a component version page. To avoid confusion, the count label has been
  removed while we address an issue with its accuracy. It may be reinstated in a
  future release once the issue is resolved.
