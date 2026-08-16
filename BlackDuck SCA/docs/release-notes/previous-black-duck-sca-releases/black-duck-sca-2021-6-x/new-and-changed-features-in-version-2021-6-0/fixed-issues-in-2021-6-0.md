---
title: "Fixed Issues in 2021.6.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2021.6.0.html"
content_id: "E_tJ_FWiHXVdvREifuql2A"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:12.555741+00:00"
---

# Fixed Issues in 2021.6.0

The following customer-reported issues were fixed in this release:

- No BD fix: 23686, 25775; 28512 - I think this is just a new container for
  bdba; 29012
- New feature in release - not listed here: 25405, 26367, 26521, 26692, 27298,
  27947, 28240,29316
- 26042 - no BD change, but may need doc change in the future
- (Hub-21613). Fixed an issue where the scan.cli version 2019.8.x displayed a
  non-meaningful warning message about performance degradation due to Java
  version used.
- (Hub-25227, 25521). Fixed an issue where the scan's status of Scan Complete
  on the Scans page was misleading.
- (Hub-26108). Fixed an issue where deploying Black Duck with Alert when using
  a customer certificate required manual intervention with the nginx alert
  configuration file.
- (Hub-26924). Fixed an issue so that a user-friendly error message now appears
  when a SAML SSO user login fails.
- (Hub-27209). Fixed an issue where the VersionBomComputationJob failed with
  the following error: "Error in job execution: could not extract ResultSet;
  SQL [n/a]; constraint [cvss2_severity]."
- (Hub-27681). Fixed an issue whereby the BOM Engine had to be started by a
  root user when deployed on Kubernetes with a custom security context.
- (Hub-27894). Fixed an issue so that the reset is set to 0 in new Black Duck
  searches.
- (Hub-28171). Fixed an issue where the copyright search failed for one
  project.
- (Hub-28305). Fixed an issue where the following error was seen in the logs:
  Failed class
  com.blackducksoftware.job.integration.domain.impl.JobMaintenanceJob.
- (Hub-28347). Fixed an issue whereby a snippet adjustment resulted in a
  duplicate key SnippetAdjustment error.
- (Hub-28351). Fixed a performance issue when saving BOM license changes.
- (Hub-28469). Fixed an issue where custom certificates could not be configured
  with Docker 20.10.x.
- (Hub-28726). Fixed an issue whereby Black Duck displayed the name of the user
  who cloned a project as the name of the component reviewer after the project
  was cloned.
- (Hub-). Fixed an issue where the following error was seen in the logs: Failed
  class
  com.blackducksoftware.job.integration.domain.impl.JobMaintenanceJob.
- (Hub-28909). Fixed an issue where an incorrect error message appeared in the
  Black Duck UI after a user account was locked out.
- (Hub-29071). Fixed an issue with performance when bulk editing snippets.
- (Hub-29168). Fixed an issue where if there were no matches in a scan that was
  mapped to a project version, then project-level file adjustments were not
  applied to that project version.
