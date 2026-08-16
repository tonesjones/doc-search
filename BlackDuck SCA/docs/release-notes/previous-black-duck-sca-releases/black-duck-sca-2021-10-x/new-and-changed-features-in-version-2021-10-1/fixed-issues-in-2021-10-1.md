---
title: "Fixed Issues in 2021.10.1"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2021.10.1.html"
content_id: "p~d7Oswoznx8BO~1~qh2NA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:52.128422+00:00"
---

# Fixed Issues in 2021.10.1

The following customer-reported issues were fixed in this release:

- (HUB-31129). Fixed an issue where project versions reports in the Hub (for
  example the Vulnerability Detail report) would print out a URL for the
  vulnerabilities with CVEs containing a BDSA record if the component has a
  BDSA record as well. The vulnerability reports will now not print the CVE
  link with the BDSA number appended.
- (HUB-31293). Fixed an issue where Python transitive dependencies were changed
  to direct dependencies after upgrading to 2021.8.x.
- (HUB-31764). Fixed an issue causing Null Pointer Exceptions during BOM
  computation when the remediation status of a vulnerability was updated.
- (HUB-30004). Fixed a permission issue in OpenShift environments where
  successful binary scans using Detect could produce blank BOMs on HUB.
- (HUB-31879). Fixed an issue where scans could get stuck during the building
  bom phase. See the RestResponseErrorHandler improvement in the New and
  Changed Features section above for more details.
- (HUB-31896). Fixed an issue where remediation updates to BOM vulnerabilities
  via public api did not persist after re-scan.

- (HUB-31753). Fixed an issue where the CollectScanStatsJob job could take
  longer than expected to compete, leading to unnecessary database bloat.
- (HUB-31663). Fixed an issue where the QuartzSearchDashboardRefreshJob could
  get into a condition where it tried to schedule multiple instances of this
  job potentially causing a large amount of blocked queries to the
  database.
- (HUB-31755). Fixed an issue when generating a Project Version report that
  could cause VersionReportJob to run out of memory due to cyclic project
  structure.
- (HUB-31566). Fixed an issue where services could experience database
  connection errors due to job over-scheduling, out-of-memory issues, and/or
  long-running jobs.
