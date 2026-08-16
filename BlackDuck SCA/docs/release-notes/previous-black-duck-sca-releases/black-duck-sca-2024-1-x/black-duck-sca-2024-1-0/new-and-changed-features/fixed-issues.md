---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "EE9j6l8HpsXWaFUQmRh32Q"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:25.330849+00:00"
---

# Fixed issues

The following customer-reported issues were fixed in this release:

- (HUB-37413). Resolved an issue with using upload source code in AzureFile as SC.
  The upload-cache service has been removed entirely, replaced by the storage
  service.
- (HUB-38991). Fixed an inconsistent display issue on the Scans page when counting
  the size of code location.
- (HUB-39012). Fixed a REST API issue when updating the component version approval
  status with an invalid value, the Approval Status would be set to "UNREVIEWED".
- (HUB-39160). Fixed an issue where Black Duck did not verify that a project
  version is part of a project if the URL is manipulated. Doing so will now return
  a HTTP 404 error page.
- (HUB-39361). Fixed an issue where timestamps only appeared as a tooltip in the
  Scans table.
- (HUB-39378). Fixed an issue where edits of BOM component usage were sometimes
  ignored if the component had multiple matches with different usages.
- (HUB-39736). Fixed a performance issue with the KB API
  `/component/<uuid>/versions` endpoint.
- (HUB-39864). Fixed an issue where BOM component edit could delete multiple
  origins if the component had multiple origins per match,
- (HUB-39948). Fixed a bomengine deadlocking issue caused by concurrently deleting
  a project and a corresponding code location.
- (HUB-39959). Fixed a validation issue with the IDP URL or XML. The UI will now
  display a proper error message and will not change the system if the IDP
  validation fails.
- (HUB-39983). Fixed an issue where rescan a repository where a failed scan could
  cause a 412 error in the Black Duck UI. The scanning workflow has been improved
  to better handle errors occurring during the scanning process.
- (HUB-39987). Fixed an issue where the Last Scanned Date and Updated Date was
  empty on SCM Project Versions.
- (HUB-40104). Fixed an issue where the Cryptography tab of a component could
  display a blank page if Cryptography was registered and then unregistered on a
  user's product registration key.
- (HUB-40667). Fixed an issue where project policy violations by tier on the
  Summary dashboard view could not populate any information.
- (HUB-40685). Fixed an issue where the Detect rate limiting parameters missing
  from the Black Duck documentation.
- (HUB-40898). Fixed a localization issue where the Maximum Snippet File Size was
  displaying an incorrect value.
