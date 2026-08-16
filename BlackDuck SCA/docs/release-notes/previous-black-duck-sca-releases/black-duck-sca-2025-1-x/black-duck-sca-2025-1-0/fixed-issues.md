---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "TzONJ5GgvVa2OnUkuVcimw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:48.623508+00:00"
---

# Fixed issues

The following customer-reported issues have been fixed in this release:

- (HUB-39655). Fixed an issue in Kubernetes deployments where the Black Duck webapp
  can enter a crash loop when the logstash disk is filled due to high activity. To
  address this, a log deletion script has been implemented to manage logstash disk
  usage.
- (HUB-42725). Fixed an issue where pagination label on the Notification page may
  not display the actual amount of notifications on the page.
- (HUB-43212). Fixed an issue where changes to the
  `maxRamPercentage` setting were only applied with Gen04
  sizing, causing issues for hosted customers using Gen02 sizing.
- (HUB-43295). Fixed an issue on the Find page → Vulnerability tab where the "used
  by " section could display the wrong project version.
- (HUB-43394). Fixed an issue where the UI displayed "Conditionally Approved"
  instead of "Limited Approval" for policy conditions related to license statuses.
  The terms are now consistent across the platform.
- (HUB-43426). Fixed an issue where partition logs could overlap each other.
- (HUB-43431). Added increased error tolerance to the
  `upload-cache-source-migrator.pl` script to log failures but
  allow the process to continue.
- (HUB-43556). Fixed an issue where the project versions comparison view could
  display no results after changing the filter from "Total Changed" to "New
  Components".
- (HUB-43560). Fixed an issue where a user with the Project Creator role,
  designated as the manager of an individual project group, was able to move any
  project between groups. These users are now correctly restricted moving only the
  projects they have created.
- (HUB-43791). Fixed an issue where the `PUT
  /api/projects/{projectId}` endpoint required a
  `projectOwner` parameter/value to be present despite it only
  requiring the `name` parameter for the project.
- (HUB-43826). Fixed an issue with the `GET
  /api/projects/{projectId}/versions/{projectVersionId}/reports/{reportId}/contents`
  endpoint where the error message displayed describing the maximum limit on file
  size indicated that it applied only to HTML reports. The message now also
  includes JSON streams.
- (HUB-43839). Fixed an issue where the unconfirmed snippets policy did not return
  results using the priority tag under the Find page.
- (HUB-43841). Fixed an issue where adding a license to a project version under
  Settings → Version Details Tab and then generating an SBOM Report, the Extracted
  Text could display as NONE.
- (HUB-43847). Fixed an issue where special characters in the component name could
  cause the security tab to return zero vulnerability results.
- (HUB-44004). Fixed an issue where updating a subproject with version to
  subproject with unknown version could generate an error in the BOM.
- (HUB-44114). Fixed an issue where the
  `/api/projects/{projectId}/versions/{projectVersionId}/components`
  endpoint was allowing the addition of a project to a BOM without a version.
- (HUB-44184). Fixed an issue in the component bulk edit window when the number of
  selected items was displayed, it displayed “{count}” instead of actual numbers
  in the Japanese localization of Black Duck.
