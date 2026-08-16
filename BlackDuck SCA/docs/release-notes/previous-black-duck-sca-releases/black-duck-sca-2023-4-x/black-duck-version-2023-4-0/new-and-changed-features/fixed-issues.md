---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "9o041cvXYvnsJA8uwhnrig"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:01.023887+00:00"
---

# Fixed issues

The following customer-reported issues were fixed in this release:

- (HUB-32471). Fixed an issue when scans had KnowledgeBase connectivity issues, it
  was not reported in the UI and resulted in an empty BOM.
- (HUB-33018). Fixed an issue where vertical and horizontal scrollbars could appear
  when printing a BOM.
- (HUB-34474). Fixed an issue where filtering projects would not display correctly
  when project names have full-width uppercase letters.
- (HUB-34616). Fixed an issue where the jobs listed on the Diagnostics page did not
  display milliseconds for completed jobs.
- (HUB-34964). Fixed issue where vulnerability "used by" count on the find page was
  inconsistent with the vulnerability affected projects page.
- (HUB-34981). Fixed an issue where the "used by" count on the component version
  list view was inconsistent with the component version details view.
- (HUB-35075). Fixed a display issue when trying to Save to PDF the BOM page in the
  Chrome browser.
- (HUB-35092, HUB-35171, HUB-36088). Fixed an issue where adding or deleting a component to a
  project/version in the Archived phase using the API request would result in a
  200 OK response, but the component was not actually added or deleted. Now, an
  error will be displayed if this is attempted. The UI will also no longer display
  a Delete option.
- (HUB-35773, HUB-37305). Fixed an issue where, as a result of binary scan, in the Source
  tab of a BOM, a single file matched to more than one component would only
  display one of the components.
- (HUB-35836). Fixed an issue when removing a project owner from a project, Black
  Duck was not preventing the project from becoming orphaned. A direct access User
  assignment check has now been added to prevent this action from being
  performed.
- (HUB-36108). Fixed an issue where snippet scanning was facing long running and
  timeout issues due to QuartzSnippetScanAutoBomJob.
- (HUB-36351). Fixed the API documentation regaring Updating a Custom Component
  Version and Creating a Custom Component Version.
- (HUB-36387). Fixed a concurrency issue in remediation status update where
  mitigating particular vulnerabilities via API would allow the mitigation to be
  applied, but the riskPriorityDistribution does not reflect all the mitigations.
- (HUB-36446). Fixed an issue where downloading the Sigma tool could fail with an
  HTTP 401 unauthorized message.
- (HUB-36676). Fixed a file permission issue when trying to install Platform One
  Black Duck on OpenShift environments.
- (HUB-36716). Fixed an issue where BDSA auto-remediated vulnerabilities do not get
  removed from being displayed on ignored components in new project versions or
  clones.
- (HUB-36719). Fixed an issue when adding a subproject to a parent project,
  unchecking the "Include in Notices File Report" checkbox would include the
  subject in the notice report regardless. Unchecking this checkbox for a subject
  will now exclude the subproject from all projects above in the project
  hierarchy.
- (HUB-36763). Fixed an issue where the SigmaToolStoreStateCheckAndRetryJob could
  fail due to the user's configured proxy. The job should no longer fail in the
  case where access to sig-repo is unreachable when not using a proxy, but
  reachable when using it.
- (HUB-36905). Fixed an issue where signature scanning a single leaf file could
  cause a null pointer exception error.
- (HUB-36952). Fixed null pointer exception in file and package adjustment
  operations.
- (HUB-37031). Fixed an issue with match count discrepencies and missing URI
  property from matched-files response when MaaS is enabled.
- (HUB-37078). Fixed issues on multiple UI pages where the back button in the
  browser could take multiple tries for function to work.
- (HUB-37109). Removed the ability to set the usage on snippet matches as it is
  currently not supported in the product. It remains available for all other match
  types.
- (HUB-37232). Fixed an issue where auto scroll sometimes did not work when opening
  discoveries with source code upload for: License, License Reference,
  Copyright.
- (HUB-37233). Fixed a REST API documentation issue where the "BOM component
  representations" link in the description of "The specific sub-set of BOM
  component representations requested" would go to "BOM Component Version
  Representation" instead of "BOM Component Representation".
- (HUB-37308). Fixed an issue where the scan size in the list of Scans page would
  include snippet scan size, incorrectly displaying the sum of both totals.
- (HUB-37312). Fixed an issue where a "Unable to access tool" error could be
  generated if the `/opt/blackduck/hub/uploads/tools` directory
  doesn't exist in the mounted storage volume when looking for objects.
- (HUB-37414). Fixed an issue where the Scans status on Project BOM page could get
  stuck in processing state and only refreshing the page would update the status.
- (HUB-37439). Fixed an issue where the length of the path matched by the snippet
  is very long, the path will not be fully displayed on the snippet view.
- (HUB-37453). Fixed an issue where applying any filter to the project versions
  page would not persist after refreshing or navigating away from the page.
- (HUB-37505). Fixed an issue with the ordering of jobs on the Jobs page
  (/api/jobs) was incorrect. The jobs will now be listed by end time
  descending.
- (HUB-37554). Fixed an issue when using the
  `/api/projects/<id>/versions/<id>/components/<id>/versions/<id>`
  API request with the parameters `component` and
  `componentVersion` missing could cause an error. To set a component
  to have an unknown version, set the componentVersion field to the empty string
  "".
- (HUB-37648). Fixed an issue with binary scans (with BDBA integrated) where the
  Source tab and Source report would only shows a single component match for each
  binary file even if the Components tab and Component report shows multiple
  components.
- (HUB-37661). Fixed an issue when BOM references another project, the Security tab
  could display blank loading areas.
- (HUB-37696). Fixed an issue where comment containing URLs for components would
  not word wrap correctly, causing it to go offscreen. Due to the security
  reasons, links will be displayed as plain text. Users would need to copy paste
  to navigate to them.
- (HUB-37757). Fixed an issue the Delete button on the Scans page could stop
  working after being used due to the page not refreshing as expected after
  use.
- (HUB-37775). Fixed an issue when trying to manually add the component origin
  using the edit option, the full path of the origin ID would not being displayed
  completely.
- (HUB-37789). Fixed an issue where it was no longer possible to copy the name of
  the match file/folder from source tree view.
- (HUB-37925). Fixed an issue where after filtering projects by an option on
  Summary tab, it was not possible to remove the filter via UI.
