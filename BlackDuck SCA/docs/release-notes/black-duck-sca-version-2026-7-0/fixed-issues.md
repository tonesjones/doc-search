---
title: "Fixed Issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "T7cdtR23KyyEu7hjrsSw4A"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:34:49.419985+00:00"
---

# Fixed Issues

The following customer-reported issues have been fixed in this release:

- (HUB-45901). Fixed an issue where BDBA integrated scanning of ISO files produced
  significantly more unmatched components compared to BDBA standalone results. The
  scanner was not correctly detecting the Linux distribution namespace for RPM
  packages, which prevented components from being matched in the Knowledge
  Base.
- (HUB-46960). Fixed an issue where the Results Summary Graph percentages did not
  add up to 100% when using Saved Searches. The "Unknown" risk category was not
  being included in the percentage calculation.
- (HUB-47100). Fixed an issue where a project version could become permanently
  stuck in "converting to LTS" mode, preventing rescans and blocking deletion via
  the API.
- (HUB-47372). Added Match Review APIs (filtering, reviewing, ignoring, editing,
  and bulk actions for unmatched components) to the public API documentation.
- (HUB-47731). Fixed a NullPointerException in the RunAsService that occurred when
  the registration ID was temporarily unavailable, causing KB vulnerability
  lookups to fail.
- (HUB-47732). Fixed a recurring JobPersistenceException in the Quartz scheduler's
  misfire handler caused by missing trigger records, which affected scheduled job
  recovery across many deployments.
- (HUB-47748). Fixed an issue where vulnerability counts displayed in the summary
  boxes (Critical, High, Medium, Low) on the Component Version Overview page did
  not match the actual number of vulnerabilities listed in the table.
- (HUB-47787). Improved performance of the project search API, which previously
  executed a complex authorization query that consumed excessive database
  resources.
- (HUB-47911). Fixed an intermittent 500 error when updating file adjustments in
  the BOM editor, caused by a temporary table conflict.
- (HUB-47932). Corrected the LDAP configuration form so that the "Test Connection"
  button uses an updated Manager password without requiring a save first.
- (HUB-48227). Fixed an issue where selecting a file checkbox on the Snippet
  Adjustments Unconfirmed view also toggled an unrelated file. This occurred in
  project versions with multiple scans, where duplicate internal row identifiers
  caused checkbox state to be shared between different files.
