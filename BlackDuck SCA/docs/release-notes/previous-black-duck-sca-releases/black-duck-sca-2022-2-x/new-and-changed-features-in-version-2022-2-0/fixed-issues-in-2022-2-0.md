---
title: "Fixed Issues in 2022.2.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2022.2.0.html"
content_id: "6KSCJSoS6G1SOeXhnPXKiA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:47.075811+00:00"
---

# Fixed Issues in 2022.2.0

The following customer-reported issues were fixed in this release:

- (HUB-31267). Fixed an issue where users without any global roles had access
  to all projects via scans page or via the project URL directly. Users
  without scan permissions will now not see the Upload Scans button on the
  `projects/.../versions/.../codelocations` screen.
- (HUB-31734). Fixed an issue where the filters on the Components page did not
  work for project-level users.
- (HUB-31993). Fixed an issue where scans could fail if the uploaded BDIO file
  had a null value for version/release. Scans will no longer fail if the
  version/release value is missing.
- (HUB-31964). Fixed an issue where the some reports could not be generated due
  to VersionReportJob failing for a project-version as a result of JDBC query
  having too many parameters.
- (HUB-30479, HUB-31842). Fixed an issue where the remediation of
  vulnerabilities with both a BDSA and a CVE record did not work when the
  non-prioritized vulnerability record was used for remediation. In order to
  remediate a vulnerability, the prioritized vulnerability record type must be
  used.
- (HUB-31207). Fixed an issue where remediating a vulnerability under an
  archived project did not update the security risk counts once applied. Users
  cannot remediate vulnerabilities of archived project-versions, so now the
  "update" button for vulnerability remediations will be greyed-out when the
  project-version is archived.
- (HUB-32029). Fixed an issue where some "ignored" components could become
  "unignored" after a rescan.
- (HUB-31768). Fixed an issue when generating the notices file, copyrights
  based on ignored snippets were included erroneously.
- (HUB-32296, HUB-32255). Fixed an issue where REST API GET
  `/api/vulnerabilities/CVE-2021-44228/affected-projects`
  returns 0 items. Also note that the affected-projects count in both the
  search results and endpoint will now also count components with the related
  vulnerability.
- (HUB-31801, HUB-32424). Fixed an issue where the Refresh button for
  copyrights was appearing to the Super User role. This functionality will now
  only appear to roles who have the permission to update copyrights.
- (HUB-32692). Fixed an issue where if a component had multiple
  vulnerabilities, each with different vulnerability statuses, policy rules
  would not trigger a policy violation unless all vulnerabilities for the
  component matched the selected policy rules.
- (HUB-32357). Fixed an issue with the KnowledgeBase activity jobs that process
  KB Updates for components, component versions, licenses, NVD
  vulnerabilities, and BDSA vulnerabilities. Previously in the event of any
  errors/issues it would fall back to processing singular updates across all
  applicable project versions. This has the potential to create a lot of churn
  and slow down the KB Update jobs.
- (HUB-32543). Fixed an issue where the Project Manager and Project Group
  Manager roles could override policies and remediate vulnerabilities if the
  setting are turned off for the Project Manager role by assigning those
  roles. The security roles can now only be assigned by Project Managers with
  those permissions or super users.
- (HUB-31129). Fixed an issue where project versions reports in the Hub (for
  example the Vulnerability Detail report) would print out a URL for the
  vulnerabilities with CVEs containing a BDSA record if the component has a
  BDSA record as well. The vulnerability reports will now not print the CVE
  link with the BDSA number appended.
- (HUB-31044). Fixed an issue where setting the policy using the API with an
  incorrect custom field ID value would not display the policy screen
  correctly afterwards.
- (HUB-31753). Fixed an issue where the CollectScanStatsJob job could take
  longer than expected to compete, leading to unnecessary database bloat.
- (HUB-31663). Fixed an issue where the QuartzSearchDashboardRefreshJob could
  get into a condition where it tried to schedule multiple instances of this
  job potentially causing a large amount of blocked queries to the
  database.
- (HUB-31862). Fixed a missing translation for BOM Annotator Role in the
  Japanese localization.
- (HUB-31208). Fixed an issue where the IBM COS SDK For Java 2.10.0 component
  showed as vulnerable in the BOM and Component Version Security Tab, but
  Component Version page showed no vulnerabilities.
- (HUB-31735). Fixed an issue with snippet record discrepancies between the
  report (source.csv) and the Source page. The
  INCLUDE_IGNORED_COMPONENTS_IN_REPORT environment variable will now also
  drive if ignored snippets are included in a report.
- (HUB-31566). Fixed an issue where services could experience database
  connection errors due to job over-scheduling, out-of-memory issues, and/or
  long-running jobs.
- (HUB-31997). Corrected the vulnerability information for the json-schema
  v0.3.0 component.
- (HUB-32527). Fixed an issue when creating a Notices File Report, the
  following modal would display the incorrect report type name.
- (HUB-31750). Fixed broken links found on the BDSA-2021-0395 page.
- (HUB-31976). Fixed an issue where a user with 'Super User' role was unable to
  manage scans within the project version scans page.
- (HUB-32566). Fixed an issue where the user was unable to map a file to Apache
  Pulsar component.
- (HUB-31201). Fixed an issue where a user could not be assigned a user to a
  project (group) with only the project (group) viewer role.
- (HUB-31251). Fixed an issue where deleting a custom field option could break
  policy APIs.
- (HUB-29676, HUB-32912). Fixed an issue where some component versions could
  not be selected from the Add/Edit Component dialog box.
- (HUB-30847). Fixed an issue when the webapp container was run as a non root
  user, a Permission denied error was generated on the webapp-logstash pod
  which caused it to crash.
- (HUB-31375). Fixed an issue where the values of 'Last Updated' on Project
  Overview and 'Updated' on Find > Projects did not match.
- (HUB-30004). Fixed a permission issue in OpenShift environments where
  successful binary scans using Detect could produce blank BOMs on HUB.
- (HUB-32159). Fixed an issue where submitting an empty value for the custom
  signature level would generate an incorrect error message.
- (HUB-32142). Fixed an issue where RabbitMQ could fail to install on Openshift
  as a result of missing permissions.
- (HUB-32216). Fixed an issue when a user would try to override a policy
  violation for the component and the specific version then tried to undo it
  for the component version, nothing would happen.
- (HUB-32312). Fixed an issue where the KBUpdateWorkflow job Component Version
  Update would saturate and run out of memory, failing to advance the
  timestamp.
- (HUB-31916). Fixed an issue where the Project settings update API would not
  appear to take effect until the UI page was refreshed.
- (HUB-30088). Fixed an issue whereby the logout page did not appear when
  logging out of a SSO account.
- (HUB-32442). Fixed an issue where the API query used to retrieve dependency
  paths was taking significantly longer than expected to complete.
- (HUB-32538, HUB-32541). Fixed an issue where the kbUpdateJob could fail and
  fall back to granular updates which would take significantly longer to
  complete.
- (HUB-32708). Removed a statistics query introduced in Black Duck 2021.10.0
  which was taking a long time to execute, causing overall slowness on Azure
  systems running PostgreSQL 11. This has been raised with Microsoft support,
  who are investigating the problem. Other installations are not affected by
  this issue.
- (HUB-32364, HUB-31606). Fixed an issue where the scans page could freeze and
  become unresponsive if there were more than 15 scans in the table and the
  user attempted to bulk delete them.
- (HUB-32602). Fixed an issue where the ScanPurgeJob process could erroneously
  cause the current scan status for package manager scans done via the IP code
  path to be changed to FAILED.
- (HUB-31122). Fixed an issue where sometimes scans would get skipped in the
  bomengine due to the ScanPurgeJob process running in the background.
- (HUB-30882). Fixed an issue where the Target Date/Actual Date of
  vulnerability remediation in the Report would become 1 day before than the
  input date due to timezone conversion.
- (HUB-32434). Fixed an issue where clicking the bell icon to show all
  notifications and then clicking on a project name that had generated a
  notification would generate an error.
- (HUB-32027). Fixed an incorrect translation for Transitive Dependency Binary
  for the Japanese localization.
- (HUB-30788). Added new endpoints to support all version reports regardless of
  types. See API Enhancements section above for additional details.
- (HUB-32843). Fixed a missing translation for "Snippets" in "Components" tab
  of the project version page for the Japanese localization.
- (HUB-31964). Fixed an issue where some reports could not be generated due to
  VersionReportJob failing for a project-version as a result of JDBC having
  too many parameters.
- (HUB-32393). Fixed an issue where if a snippet match was present in the BOM,
  the upper view would sometimes not be populated with
  Security/License/Operational risks if the results were filtered.
- (HUB-32604). Fixed an issue when the environment variable
  `BLACKDUCK_CORS_ALLOWED_ORIGINS_PROP_NAME` was set as a
  wildcard, the CORS functionality would not work.
