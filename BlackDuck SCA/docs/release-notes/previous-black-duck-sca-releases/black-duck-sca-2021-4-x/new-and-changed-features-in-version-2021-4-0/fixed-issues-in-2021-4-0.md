---
title: "Fixed Issues in 2021.4.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2021.4.0.html"
content_id: "CjH3DDnGNo9qUYnHzMbHyA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:16.547539+00:00"
---

# Fixed Issues in 2021.4.0

The following customer-reported issues were fixed in this release:

- NO HUB FIX/ISSUE: 25860, 25454, 25765, 25860, 25945, 26315, 26941, 27213,
  27695, 27982, 28089 - project page - click for policy; 28138-kb issue;
  28185; 28307; 28433
- (Hub-24015, 26281). Fixed an intermittent permission denied error seen in the
  Black Duck user interface.
- (HUB-25116). Fixed an issue where red dots appeared in the Snippet View
  dialog box for a file encoded in UCS-2, rendering the text unreadable.
- (HUB-25549). Fixed an issue with `/api/uploads` where the
  created code location was not mapped to the project version when
  codeLocationName contained Japanese characters.
- (HUB-25550). Added BOM update information to a project version's
  activity/journal.
- (HUB-25605, 27618). Fixed an issue when using
  `/api/tokens/authenticate` to authenticate with an API
  token, where after the token expired, the HTTP client got redirected to the
  SAML provider page or an error occurred when generating PDF reports.
- (Hub-25993). Fixed an issue where a duplicate record caused the following
  error message to appear in the job runner log: 'A conflicting object already
  exists.'
- (Hub-26481). Fixed an issue where a page would refresh completely after
  saving a new remediation status.
- (HUB-26588). Fixed an issue where running a binary scan on
  android-studio-ide-201.7199119-windows.exe failed.
- (Hub-26695). Fixed an issue where scans took significantly longer during
  certain times of the day.
- (Hub-26897). Fixed an issue so that a 404 Not Found error code appears for
  invalid versions which are those not listed on the *Component Name*
  page.
- (Hub-26911). Fixed an issue where selecting an alternate snippet match
  incorrectly identified a component as having cryptography.

- (Hub-27159). Fixed an issue for policy rules using the 'Contributors in the
  past year', 'Commits in the past year' or 'New Version Count' component
  conditions. Although these conditions were defined to trigger a violation if
  the value was equal to 0, policy violations were triggered when the value
  was greater than 0 or a component had no commit history.

  Note: With this fix, new scans or rescans may remove some policy violations that were
  previously triggered.
- (Hub-27167). Fixed an issue whereby active users assigned to an inactive
  group with the Global Project Viewer role could see all projects in the
  Dashboard.
- (Hub-27175). Fixed an issue where the **Used count** value on the
  *Component Name* page was inaccurate as it was based on the number
  of component origins, not the component versions.
- (Hub-27282). Fixed an issue where the policy violation popup in the BOM
  occasionally got stuck open and could not be closed unless the page was
  refreshed.
- (Hub-27284, 27660). Fixed an issue where some dynamically linked components
  with a match type of transitive dependency were missing the match
  information in the **Source** column in the project version BOM.
- (Hub-27287). Fixed an issue so that risk counts shown on the **Overview**
  tab on the *Project Name* page use component version values (as the BOM
  page does), instead of by component origin.
- (Hub-27293). Fixed an issue where components marked as Reviewed were noted as
  Unreviewed when the project was rescanned.
- (Hub-27306). Fixed an issue where components were listed in case sensitive
  order in the Notices Report.
- (Hub-27308). Fixed an issue where the Black Duck KB
  *Component Name* page did not correctly show the number of
  vulnerabilities after the license for a component version was changed.
- (Hub-27326). Fixed an issue whereby deleting the application ID using the
  project's **Settings** tab did not actually delete the application
  ID.
- (Hub-27613). Fixed an issue where the source files for binaries could not be
  navigated in the **Source** tab.
- (Hub-27961). Fixed the legends for the graphs on the Dashboard page so that
  they did not appear clickable.
- (Hub-27982). Fixed an issue where the binary scan only identified the first
  and last files in an MSI archive.
- (Hub-27985). Fixed an issue with the message that appears when Black Duck is
  building the BOM which would disappear when you scrolled down the BOM
  page.
- (Hub-28094). Fixed an issue where the `/api/usergroups`
  endpoint was not properly using "_" or "%" in the search term.
- (Hub-28165). Fixed an issue with editing a license on the BOM page where
  selecting Cancel/Close still applied the changes.
- (Hub-28208). Fixed an issue where the code base size shown on the
  Registration page was incorrect.
- (Hub-28226). Fixed an issue so that components that are in violation of one
  or more policies will now generate a "policy cleared" notification when the
  code location that brought them in is unmapped or deleted.
- (Hub-28259). Fixed an issue with an unreview/unignore SQL query analysis.
- (Hub-28292). Fixed an issue where the HELM t-shirt sizing
  `.yml` files did not scale the BOM engine container.
- (Hub-28370). Fixed an issue where critical vulnerabilities were not shown
  when using the comparison view of the BOM.
- (Hub-28375). Fixed an issue so that the **Affected Projects** tab for a
  CVE or BDBA record no longer displays vulnerabilities from components that
  have been ignored.
- (Hub-28383). Fixed an issue where if the *Project Name* page was
  filtered and as a result only one version appeared on the page, the version
  could not be deleted.
- (Hub-28416). Fixed an issue where the AND or OR operator for a group of
  licenses could not be modified.
- (Hub-28458). Fixed an issue where the SnippetScanAutoBom job displayed an
  "Error in job execution: Duplicate key" error message.
- (Hub-28562). Fixed an issue with a binary scan where the scan failed to
  complete post work and the following error message appeared: "Path is not a
  parent of null."
- (Hub-28580). Fixed an issue when attempting to access the **My Access
  Tokens** page caused the following error "The application has
  encountered an unknown error."
- (Hub-28639). Fixed an issue where the suffix of the downloaded report file
  had a `.json` extension instead of `.zip` if
  the project name contained both English and Chinese characters.
- (Hub-28681). Fixed an issue so that the usage is shown on the **Source**
  tab when the match type is direct or transitive dependency.
- (Hub-28765). Fixed an issue where the BOM page displayed snippets that were
  both confirmed and ignored.
- (Hub-28773). Fixed an issue so that TLSv1.1 was removed from the
  TLS_PROTOCOLS option in the `hub-webserver.env` file.
