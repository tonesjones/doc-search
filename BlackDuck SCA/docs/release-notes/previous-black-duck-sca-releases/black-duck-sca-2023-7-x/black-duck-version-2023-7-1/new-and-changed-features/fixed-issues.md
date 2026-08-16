---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "1rQbgQ04JFymMB3~Jrs0sA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:46.801270+00:00"
---

# Fixed issues

The following customer-reported issues were fixed in this release:

- (HUB-38374). Fixed an issue with Black Duck SCM integration when using a
  different date/time format could cause an error when trying to pull
  repositories.
- (HUB-38790). Fixed issues with some migration scripts that were causing syntax
  errors.
- (HUB-38968). Fixed an issue where uploading a SBOM to Black Duck could fail due
  to the namespace UUID value not following SBOM best practices.
- (HUB-39026). Fixed an issue where the unmatched components badge, which is now
  enabled by default, would erroneously count package files when Detect 8 was run
  or when BDIO aggregation was used. This caused the number of package managers
  run to be added to the unmatched component count due to the hierarchy in the
  BDIO file.
- (HUB-39072). Fixed the `CreatedAt` and `UpdatedAt`
  definitions for the BOM Component Vulnerability Remediation Representation in
  the REST API documentation to state that they are the date the vulnerability was
  added to the BOM component origin or updated on the BOM component origin.
- (HUB-39168). Fixed an UI issue where the "Add Filter" and "Filter versions..."
  text field options could disappear for modified components and the vulnerability
  history graph could disappear when a component is modified.
- (HUB-39211). Fixed an issue with the Japanese localization where the policy
  override date information was not being displayed correctly.
- (HUB-39274). Fixed an issue where the KbUpdateJob was not validating BDSA
  licensing from the customer's product registration which could cause a HTTP 403
  Forbidden response during the request.
- (HUB-39367). Fixed an issue where license names containing "" could cause
  KbUpdateWorkflowJob-License Update to fail.
