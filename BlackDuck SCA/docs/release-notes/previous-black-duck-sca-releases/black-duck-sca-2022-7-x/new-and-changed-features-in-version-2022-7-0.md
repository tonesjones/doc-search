---
title: "New and Changed Features in Version 2022.7.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features-in-version-2022.7.0.html"
content_id: "9wl9whJZ5cK811foFgJXjQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:32.598288+00:00"
---

# New and Changed Features in Version 2022.7.0

## PostgreSQL 14 support for external databases

Black Duck now supports and recommends PostgreSQL 14 for new installations that use
external PostgreSQL. Migrating to Black Duck 2022.7.x does not require migration to
PostgreSQL 14.

No action is required for users of the internal PostgreSQL container.

Note: Due to an index corruption bug in PostgreSQL 14.0 through 14.3, the minimum
supported version of PostgreSQL 14 is 14.4.

## Split of super user role into Admin domain roles

Currently, any Black Duck user with the Super User role can create/amend the
permissions of all users such that they can assign the system administrator role to
any user including their own user. This leads to any Super User having the ability
to gain complete access and control of the Black Duck instance, including the
SysAdmin role. This appears as a privilege escalation defect however the role is
functioning as intended.

In order to prevent this scenario, the Super User role has been removed and new roles
have been created to handle various responsibilities formerly associated to it:
Global Project Administrator, Global Project Group Administrator, User Administrator
and Custom Field Administrator. Additional information on these new roles can be
found in the Black Duck Help.

## New Infrastructure as Code (IaC) issues display

Applications are not just the application code, the infrastructure and deployment
methods are a critical component for ensuring application security. IaC is therefore
being used to automate this deployment and setup of applications in different cloud
and on-prem environments. These configuration options play a key role in ensuring
application security and are particularly important for containerised or service
based applications.

Now with Black Duck 2022.7.0, you can now see IaC issues when viewing the BOM of a
project's version page if the scan included IaC. The information displayed will
provide you with information needed to take action on any potential issues found in
your code.

Please note that to run IaC scans, you must meet the following [operating system requirements](https://community.blackduck.com/s/document-item?bundleId=sigma-ug&topicId=topics%2Fsupport%2Fsupport-os.html&_LANG=enus) and have Detect 7.14 or
later.

For more information regarding Infrastructure as Code scanning, please refer to our
[Community page](https://community.blackduck.com/s/document-item?bundleId=sigma-ug&topicId=topics%2Fintro.html&_LANG=enus).

## Improved robustness for scan CLI

Scan CLI has been improved to prevent hanging when it completes on the server by
introducing a retry mechanism. This means that scans will complete and upload
normally even after Hub, scan, or nginx services restart.

## New support for bulk comments for a project version components

This new feature provides the ability to add bulk comments to ease user review and
curation of the BOM. For example, instead of applying comments to components
individually, you can select any number of components on the project version page
and add a comment to the selected items simultaneously.

## New automated API access token purging

This new feature will allow User Administrators of the Black Duck system to better
maintain and control access to Black Duck via access tokens by setting up a schedule
to automatically purge inactive access tokens. This functionality can be found on
the new Admin > Access Tokens page. You can also manually curate all existing access tokens as well
through this page.

## Increased binary scan container memory allocation

In order to prevent binary scans failures, we have increased the binary scan
container memory from 2GB to 4GB.

## Enhanced Policy Rule user experience

When creating or editing a policy, the Component Conditions will now display
instructions to clarify how to add or exclude a component version to a policy when
the "in" or "not in" operators are used.

## Updated Black Duck KnowledgeBase search

The Find > Black Duck KnowledgeBase page has had some minor changes to its appearance and how the results
are displayed after performing a search.

In the earlier releases, Black Duck KnowledgeBase searches displayed Black Duck
projects and Custom Components along with KnowledgeBase components in the result
set. Starting with 2022.7.0, Black Duck KnowledgeBase searches return only
KnowledgeBase Component data. In order to search for Custom Components, users should
leverage the Components search tab. To search for Black Duck projects, users should
use the Projects search tab.

In addition, the Component Source filters on the Black Duck KnowledgeBase page
(Custom Components and Black Duck Projects) have been removed.

## Enhanced KnowledgeBase update job tasks

Previously, tasks that made up a KnowledgeBase update job (component, component
version, license, NVD vulnerability, and BDSA vulnerability) were run in preset
order. If the component task failed, subsequent tasks would not be executed. New to
2022.7.0, a continuation mechanism has been introduced that manages failed tasks,
which prevents the blocking of the execution of subsequent tasks.

Additionally, this provides better optics from a jobs page perspective as long as
some detail is present on why a specific task failed.

## New Rapid Scan properties added

The following properties have been added to the output of Rapid Scans:

- `cweIds`: List of Common Weakness Enumeration (CWE) IDs for
  this security vulnerability.
- `shortTermUpgradeGuidance`: Suggested component version to
  upgrade to as a short term course of action to address this vulnerability as
  it is the same major version as the one in use.
- `longTermUpgradeGuidance`: Suggested component version to
  upgrade to as a long term course of action. Taking this course of action
  might require major version number upgrade and must be more carefully
  planned.

## New upgrade guidance information to Detect endpoint

The following have been added to the Detect component scan results:

- `shortTermUpgradeGuidance`: Suggested component version to
  upgrade to as a short term course of action to address this vulnerability as
  it is the same major version as the one in use.
- `longTermUpgradeGuidance`: Suggested component version to
  upgrade to as a long term course of action. Taking this course of action
  might require major version number upgrade and must be more carefully
  planned.

## Updated data retention management for project versions

You can now better manage your project versions' data retention policy. If Automatic
Data Removal has been enabled in your environment, you can now select specific
project versions to protect from deletion. This can be enabled when creating a new
project or by editing existing project versions. When viewing your project, project
versions protected from Automatic Data Removal will have a lock icon displayed at
the end of its row.

## Updated Software Bill of Materials (SBOM) Report type and export formats

You can now export the Software Bill of Materials report for your projects in
CycloneDX v1.4 format. The CycloneDX v1.4 format includes security vulnerability
information; BDSA records will now be included along with NVD records.

For more information on CycloneDX v1.4, please visit the [CycloneDX v1.4
reference page](https://cyclonedx.org/docs/1.4/json/).

The report type (SPDX, CycloneDX v1.3, or CycloneDX v1.4) will also be included in
the report name to better identify the type used after report generation.

In addition, new report formats are available when generating a SBOM report. You can
now select from JSON, YAML, RDF, and tag:value as an output for your report.

## New database partition job

The Journal table is now partitioned by months. The first partition is special and
contains all existing journal events. The JournalPartitionMaintenanceJob job creates
new database partitions for the project audit trails and drops old partitions and
Journal events older than 5 years.

## Scan state/status refactoring

Previously, scan status was a design combination of scan state and scan progress
which does not work well in the current queue-based scan architecture. The new
approach will provide a state and then a way to track the progress of the scan as it
progresses through the system. This approach should be flexible enough so the
traditional scan architecture can be retrofitted so a single approach is used. State
should remain in the database, while progress, being transient and updated more
frequently should be moved to cache.

## Reporting database enhancements

Added `exposed_on` field in
`reporting.component_vulnerability` materialized view.

## Minor Reporting schema change

In 2023.1.0, the type of the `basedir` column in
`reporting.scan_view` will change from `character
varying` to `text` to accommodate paths longer than 255
characters.

## Supported browser versions

- Safari Version 15.5 (17613.2.7.1.8)
  - Safari versions 13.0 and below are no longer supported
- Chrome Version 103.0.5060.114 (Official Build) (x86_64)
  - Chrome versions 71 and below are no longer supported
- Firefox Version 102.0 (64-bit)
  - Firefox versions 71 and below are no longer supported
- Microsoft Edge Version 103.0.1264.44 (Official build) (64-bit)
  - Microsoft Edge versions 78 and below are no longer supported

## Container versions

- blackducksoftware/blackduck-postgres:11-2.15
- blackducksoftware/blackduck-authentication:2022.7.0
- blackducksoftware/blackduck-webapp:2022.7.0
- blackducksoftware/blackduck-scan:2022.7.0
- blackducksoftware/blackduck-jobrunner:2022.7.0
- blackducksoftware/blackduck-cfssl:1.0.9
- blackducksoftware/blackduck-logstash:1.0.20
- blackducksoftware/blackduck-registration:2022.7.0
- blackducksoftware/blackduck-nginx:2.0.25
- blackducksoftware/blackduck-documentation:2022.7.0
- blackducksoftware/blackduck-upload-cache:1.0.27
- blackducksoftware/blackduck-redis:2022.7.0
- blackducksoftware/blackduck-bomengine:2022.7.0
- blackducksoftware/blackduck-matchengine:2022.7.0
- blackducksoftware/blackduck-webui:2022.7.0
- blackducksoftware/bdba-worker:2022.6.0
- blackducksoftware/rabbitmq:1.2.10
