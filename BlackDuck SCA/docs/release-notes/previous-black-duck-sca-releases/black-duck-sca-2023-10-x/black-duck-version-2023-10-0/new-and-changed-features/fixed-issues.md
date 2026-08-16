---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "0DbAoHz6VOW18jJDMEKCPg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:36.076822+00:00"
---

# Fixed issues

The following customer-reported issues were fixed in this release:

- (HUB-27209). Fixed issue where KB Update Job could fail due to a vulnerability
  with no CVSS 2.0 score.
- (HUB-32753). Fixed an issue where upload cache cleaning did not handle outdated
  docker inspector uploads.
- (HUB-33560). The policy rule for the Archived project phase has been disabled.
  Any components that were in violation are cleared (even in archived project
  versions). New policy rules are NOT evaluated against 'archived' project
  versions. Expression changes are NOT evaluated against 'archived' project
  versions. Disabled and deleted policy rules - ARE cleared in 'archived' project
  versions.
- (HUB-35760). Fixed an issue where the Complete filter on the Scans page was
  incorrectly displaying scans currently in progress.
- (HUB-35836). Fixed an issue where users without any other direct access to a
  project could remove a project owner user and in doing so would assign the user
  without direct access as a project manager role for the project. Users without
  direct access to a project will now be blocked from removing users from that
  project.
- (HUB-38385, HUB-38654). Fixed timeout issues related to the traditional method of
  processing scans.
- (HUB-38595). Updated the sample response for the `GET
  /api/codelocations/{codeLocationId}/latest-scan-summary` request in
  the REST API developer guide.
- (HUB-38682). Fixed an issue when clicking on the "N matches" link in the BOM view
  under Source column would not clear the previous selection in the Source tab and
  display the previously remembered matching folders/files.
- (HUB-38753). Fixed an issue where bulk edits of component version usage could
  incorrectly fail to update policy violations.
- (HUB-38766). Fixed an issue where project viewer users could access a project's
  settings page and make updates to the project. With this fix, Project Viewer
  users without permission will still be able to access the project settings page,
  but will now not be able to update anything. All update/delete actions will be
  disabled.
- (HUB-38803). Fixed an issue where snippets marked as ignored were still displayed
  when clicking the Unconfirmed Snippets link on the BOM page. Clicking this link
  will now automatically apply the Match Ignore: Not Ignored filter to the
  Snippets page.
- (HUB-38806). Fixed an issue where remediating the BDSA-2023-1225 via API
  vulnerability could generate a HTTP 404 error.
- (HUB-38841). Fixed the text size in the License notes and attribution statement
  of the Component License modal.
- (HUB-38878). Fixed an issue where a component could be deleted from BOM when a
  component merge occurred.
- (HUB-39079). Fixed an issue where trying to render large HTML reports could
  generate a HTTP 503 Service Unavailable server error response. Trying to render
  large HTML reports will now generate a validation error with the actual report
  size as well as the current limit. The current limit is determined by the
  `HUB_MAX_HTML_REPORT_SIZE_KB` environment variable which is
  set to 3000 KB by default.
- (HUB-39275). Fixed an issue where if the unmapped scan retention was set beyond
  365 days in the UI, it would be reset it to 30 days when the purge job runs.
- (HUB-39318). Fixed an issue where it was not possible to highlight the origin in
  the Copyrights tab of a specific component's version.
- (HUB-39368). Fixed an issue when users would click on the other tabs, the global
  search was overriding the query for the currently selected search. Search
  requests will now not persist, meaning if a user refreshes the browser, or logs
  out and back in, previous filters will not be remembered.
- (HUB-39441). Fixed an issue with the ScmServerAppService where it would only
  check the scm integration registration key when initializing.
- (HUB-39496). Fixed an issue where BDIO generated from BDBA scans could fail to
  upload to Black Duck if the file size exceeded 16 GB. The limit has been
  increased to 90 GB.
- (HUB-39744). Fixed a discrepancy issue between the vulnerability results
  displayed on the BOM/versions page and the Dashboard after the
  KBUpdateWorkflowJob runs.
- (HUB-39836). Fixed an issue where the `component_matches`
  materialized view was not including all match types.
- (HUB-39864). Fixed an issue where editing a BOM component (changing usage or
  comment) with multiple origins (seen in hover over) could delete all origins.
- (HUB-40060). Fixed an issue when editing a component with many origins in a BOM,
  the selection was limited to 10 origins. This has been increased to 100.
- (HUB-40085). Fixed a performance issue with creating reports where generation
  could take much longer than expected, resulting in wait time in pipelines.
