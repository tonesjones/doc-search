---
title: "Fixed Issues in 2020.10.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2020.10.0.html"
content_id: "83uVnDZNcQnS3UZVxH0OTg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:27.430588+00:00"
---

# Fixed Issues in 2020.10.0

The following customer-reported issues were fixed in this release:

- hub-20916, 24149, 24459, 24480, 25254, 25269, 25387, 25416, 25442 25848-
  FIXED IN AN EARLIER RELEASE
- HUB-24669, 24769, 25320, 25414 25614- no hub fix (match type terms)
- hub-24970 - dup of issue not yet fixed.
- (Hub-20559, 22100). Fixed an issue where snippet adjustments were lost when
  scanning the same code location from a different root directory or when
  cloning a project version.
- (Hub-21421). Fixed an issue where the print functionality did not work for
  large projects.
- (Hub-23705, 25560). Fixed an issue where users could not delete reports that
  they created.
- (Hub-23709). Fixed an issue whereby the following scan.cli.sh warning message
  appeared when scanning: "Unable to find manifest from all manifests."
- (Hub-24330). Fixed an issue whereby an error message ("Duplicate key value
  violates unique constraint") appeared when importing a Protex
  project into Black Duck version 2019.10.3.
- (Hub-24574). Fixed an issue whereby ComponentDashboardRefeshJob failed with
  "No Space left on device" error THIS JOB REMOVED IN 2020.10.0
- (Hub-24673). Fixed an issue whereby navigating from a Dashboard page failed
  if there were more than 32,000 components.
- (Hub-24675). Fixed an issue whereby the root_bom_consumer_node_id was set
  incorrectly
- (Hub-24769). Fixed an issue whereby the ReportingDatabaseTrasferJob failed occasionally on a
  system with approximately one million components. OPEN - no hub fix?
- (Hub-24871). Fixed an issue with PostgreSQL database growth since release 2019.10.0. OPEN
- (Hub-24772). Fixed an issue where the default `.pdf` filename
  when printing a BOM was not the project name and version name.
- (Hub-24839). Fixed an issue where some component origin IDs could not be
  selected from the Add/Edit Component dialog box.
- (Hub-24947). Fixed an issue whereby search results when adding a project to a
  BOM were listed inconsistently.
- (Hub-25171). Fixed an issue whereby the vulnerability count was not updated
  when remediated using an API until after a rescan (PUT
  /api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/versions/{componentVersionId}/origins/{originId}/vulnerabilities/{vulnerabilityId}/remediation).
- (Hub-25196). Fixed an issue whereby Signature scanner hangs when WRITE permissions are not
  given to scan.cli-2020.6.0
  OPEN
- Hub-25211 Resource limits Kubernetes containers OPEN - no hub fix
- (Hub-25219). Fixed an issue with creating reports through the API, wherein
  specifying a locale such as "locale" : "ja_JP" was ignored. Now, the locale
  field correctly sets the language of the generated report.
- (Hub-25234). Fixed an issue where the **Print** button to print a BOM was
  occasionally missing bar graph counts.
- (Hub-25240). Fixed an issue where browser or API calls for a specific
  vulnerability (BDSA-2020-1674) failed.
- (Hub-25241). Fixed an issue where the VersionBomComputationJob failed for
  scans with the following error message: "Data integrity violation
  (Constraint:not_null, Detail: on column source_start_lines)".
- (Hub-25244). Fixed an issue whereby manually added components were deleted
  from the BOM after upgrading to Black Duck release 2020.4.2.
- (Hub-25247). Fixed an issue whereby the following error message appeared in
  the Black Duck PostgreSQL logs: "ERROR: duplicate key value violates unique
  constraint "scan_component_scan_id_bdio_node_id_key".
- (Hub-25310). Fixed an issue where updating a user required fields API DOC
  FIX
- (Hub-25321). Fixed an issue where when scrolling the BOM page, text appeared
  in areas on the page where text should not appear.
- (Hub-25324). Fixed an issue where the Scan *Name* page did not word
  wrap.
- (Hub-25478). Fixed an issue where the security risk filter on the Security
  page became invisible.
- (Hub-25508). Fixed an issue where old media types (v4 and v5) did not always
  work for the policy rules API (GET
  /api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/versions/{componentVersionId}/policy-rules).
- (Hub-25515). Fixed an issue where the Signature Scanner failed to load with the following
  error message: "unable to secure the connection to the host". 10.1
- (Hub-25522, 25523). Fixed an issue where formatting issues appeared in the
  BOM print preview window in Chrome for Black Duck version 2020.8.0.
- (Hub-25548). Fixed an issue where selecting new component matches in the
  hierarchical view did not update component matches in the Source view.
- (Hub-25570). Fixed an issue whereby the Security Dashboard page only
  partially loaded.
- (Hub-25608). Fixed an issue where vulnerabilities were counted twice in the
  "New Vulnerabilities" and "New Remediated Vulnerabilities" categories in the
  Vulnerability Update report.
- (Hub-25649). Fixed an issue where the policy violation popup windows on the
  Dashboard page would not close.
- (Hub-25841). Fixed an issue whereby numbers entered into a custom field of
  type Text were converted into a date format.
