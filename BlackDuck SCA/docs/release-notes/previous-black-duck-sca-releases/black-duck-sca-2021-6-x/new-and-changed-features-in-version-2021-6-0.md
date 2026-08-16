---
title: "New and Changed Features in Version 2021.6.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features-in-version-2021.6.0.html"
content_id: "nYkVuxRoTafYWIuaQ~3lWQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:11.434528+00:00"
---

# New and Changed Features in Version 2021.6.0

## New containers and changes to system requirements

In the 2021.6.0 release:

- A new container, blackduck-webui, has been added for improved Black Duck
  performance, better caching, and future scalability.

- The Rapid Scanning feature is now available to all Black Duck customers. This
  feature requires a new container, blackduck-matchengine, which manages
  connections to the Black Duck KnowledgeBase and cache KnowledgeBase results
  for short intervals.

The following are now the minimum hardware that will be needed to run a single
instance of all containers. Note that memory requirements depend on the number of
concurrent Rapid Scans you want to support.

- 7 CPUs
- 28.5 GB RAM for the minimum Redis configuration; 31.5 GB RAM for an optimal
  configuration providing higher availability for Redis-driven caching. This
  will support up to 100 concurrent Rapid Scans.

  30 GB RAM for the minimum Redis configuration; 33 GB RAM for an optimal
  configuration providing higher availability for Redis-driven caching. This
  will support more than 150 Rapid Scans, however, the maximum number of
  supported Rapid Scans is still being determined.
- 250 GB of free disk space for the database and other Black Duck containers
- Commensurate space for database backups

The following is the minimum hardware that is needed to run Black Duck with Black Duck Binary Analysis.

- 8 CPUs
- 32.5 GB RAM for the minimum Redis configuration; 35.5 GB RAM for an optimal
  configuration providing higher availability for Redis-driven caching. This
  will support up to 100 concurrent Rapid Scans.

  34 GB RAM for the minimum Redis configuration; 37 GB RAM for an optimal
  configuration providing higher availability for Redis-driven caching. This
  will support more than 150 Rapid Scans, however, the maximum number of
  supported Rapid Scans is still being determined.
- 350 GB of free disk space for the database and other Black Duck containers
- Commensurate space for database backups

Note: An additional CPU, 2 GB RAM, and 100 GB of free disk space will be needed for every
additional binaryscanner container.

## Rapid Scanning

Rapid Scanning is now available for all customers.

Black Duck's Rapid Scanning provides a way for developers to quickly determine if the
versions of open source components included in a project violate corporate policies
surrounding the use of open source. Using Black Duck Detect, Rapid Scanning
quickly returns results as it only employs package manager scanning and does not
interact with the Black Duck server database. Use Rapid Scanning when you need quick
feedback and when persisting the data in Black Duck is not necessary.

Using Rapid Scanning enables you to run thousands of scans while eliminating the need
to deploy additional instances of Black Duck. It provides you with actionable
results (such as failing the build) that can be used without a project version or
without access to Black Duck's user interface.

## New jobs subsystem

The jobs subsystem has been replaced with a new implementation.

- Possible status for a job can now be:
  - Pending
  - In progress
  - Complete
  - Error

- You can filter jobs based on their schedule: periodic or on demand.
- With the new implementation, the following jobs have been added:
  - BomAggregatePurgeOrphansCheckJob. Checks to see if any BOM data is
    not associated with a project version and starts the necessary
    jobs.
  - BomVulnerabilityDataRecomputationCheckJob. Checks if BOM computations
    are required when certain settings change and starts the necessary
    jobs.
  - BomVulnerabilityDataRecomputationJob. Updates component information
    received from the KnowledgeBase.
  - HierarchicalVersionBomCheckJob. Checks if hierarchical BOM
    computations are required and starts the necessary jobs to process
    them
  - JobHistoryStatsJob-Calculate Daily Statistics. Calculates daily
    statistics based on job activity.
  - JobHistoryStatsJob-Calculate Five Minute Statistics. Calculates
    statistics in 5-minute intervals based on job activity.
  - JobHistoryStatsJob-Calculate Hourly Statistics. Calculates statistics
    in one-hour periods based on job activity.
  - JobHistoryStatsJob-Prune Job History. Prunes old records from the job
    history based on the retention settings.
  - KBUpdateCheckJob. Initiates updates received from the
    KnowledgeBase.
  - KbUpdateWorkflowJob-BDSA Vulnerability Update. Updates BDSA
    vulnerability information received from the KnowledgeBase.
  - KbUpdateWorkflowJob-Component Update. Updates component information
    received from the KnowledgeBase.
  - KbUpdateWorkflowJob-Component Version Update. Processes component
    version updates received from the KnowledgeBase.
  - KbUpdateWorkflowJob-License Update. Updates license information
    received from the KnowledgeBase.
  - KbUpdateWorkflowJob-NVD Vulnerability Update. Updates NVD
    vulnerability information received from the KnowledgeBase.
  - KbUpdateWorkflowJob-Summary.Issues a summary report about the most
    recent KnowledgeBase update.
  - LicenseTermFulfillmentCheckJob. Checks if license fulfillment
    processing is required and starts the necessary jobs.
  - NotificationPurgeCheckJob. Checks if there are notifications that
    need cleanup and starts the necessary jobs.
  - QuartzVersionBomEventCleanupJob. Cleans up BOM events based on the
    retention policy.
  - VersionBomComputationCheckJob. Checks if BOM computations are
    required and starts the necessary jobs to process them.
  - VersionBomNotificationCheckJob. Issues notifications for BOM
    computation results.
  - WatchdogJob. Monitors recurring jobs to ensure they are running
    properly and reports on or fixes issues as they are
    determined.

- The following jobs have been removed:
  - KbUpdateJob

## Report enhancements

- A new project version report,
  `license_conflicts_date_time.csv` has been added. It
  lists the license conflicts for this project version. This report has the
  following columns:
  - Component id
  - Version id
  - Component name
  - Component version name
  - Usage
  - License ids
  - License names
  - Source/Type
  - License Term Responsibility
  - License Term Category
  - License Term Name
  - Description
  - Conflicting License Id
  - Conflicting License Name
  - Conflicting License Term Source Type
  - Conflicting License Term Responsibility
  - Conflicting License Term Category
  - Conflicting License Term Name
  - Conflicting License Term Description
- A new column, Has License Conflicts, has been added to the end of the
  `components_date_time.csv` project version
  report. This column indicates whether this component version has a license
  conflict.
- (HUB-29152)File names for
  reports now use the system timezone instead of UTC.

## Ability to refresh Black Duck KnowledgeBase copyright information

Black Duck now provides the ability for you to view updated Black Duck KnowledgeBase
copyright information for a component origin. If there is new or updated data, Black
Duck updates the information shown while keeping any edits that you made.

## New role

A new role, BOM Annotator, has been added to Black Duck. Users with this role have
read-only access to a project and can add or edit comments in a BOM and update BOM
custom fields.

## LDAP or SAML group synchronization

if you enabled group synchronization when configuring LDAP or SAML for Black Duck,
the name of this group in the external authentication system (LDAP or SSO) now
appears in the **External Group Name** field on the *Group Name* page. Now,
if a group names changes on the external system, you can edit it to keep the Black
Duck group name in sync with the external authentication system group name.

## Enforcement of required custom fields

Black Duck now provides an option so that users *must* enter values when editing
objects which have required custom fields.

## New filters for project search

Black Duck now provides these filters when searching for projects:

- Never Scanned. Use this filter to find all project versions that were never
  part of a scan.
- Not Scanned Since. Use this filter to find all project version that have not
  been scanned since the selected time period.

## Retention period for unmapped code locations

(HUB-28195, 28355)The default
retention period for unmapped code locations has changed from 365 days to 30
days.

## Additional information in the Add/Edit Component dialog boxes

So that you can more easily determine the component you wish to use, the Add
Component and Edit Component dialog boxes now include the component's home page URL
and the number of project versions that use this component.

## Policy enhancements

The following component conditions now include a "false" option:

- License Conflict with Project Version
- Unfulfilled License Terms
- Unknown Component Version

## Improved C/C++ matching

In the 2021.6.0 release, BOM accuracy has been improved for customers scanning C/C++
in the Linux domain.

## New match types

Two new match types have been added in the 2021.6.0 release.

- Direct Dependency Binary. Scanning identified that the binaries in use are a
  direct dependency.
- Transitive Dependency Binary. Scanning identified that the binaries in use
  are a transitive dependency.

## Supported browser versions

- Safari Version 14.0.3 (15610.4.3.1.7, 15610)
- Chrome Version 90.0.4430.72 (Official Build) (x86_64)
- Firefox Version 88.0 (64-bit)
- Microsoft Edge Version 90.0.818.41 (Official build) (64-bit)

## Container versions

- blackducksoftware/blackduck-postgres:9.6-1.1
- blackducksoftware/blackduck-authentication:2021.6.0
- blackducksoftware/blackduck-webapp:2021.6.0
- blackducksoftware/blackduck-scan:2021.6.0
- blackducksoftware/blackduck-jobrunner:2021.6.0
- blackducksoftware/blackduck-cfssl:1.0.2
- blackducksoftware/blackduck-logstash:1.0.10
- blackducksoftware/blackduck-registration:2021.6.0
- blackducksoftware/blackduck-nginx:2.0.0
- blackducksoftware/blackduck-documentation:2021.6.0
- blackducksoftware/blackduck-upload-cache:1.0.17
- blackducksoftware/blackduck-redis:2021.6.0
- blackducksoftware/blackduck-bomengine:2021.6.0
- blackducksoftware/blackduck-matchengine:2021.6.0
- blackducksoftware/blackduck-webui:2021.6.0
- blackducksoftware/bdba-worker:2021.03
- blackducksoftware/rabbitmq:1.2.2

## Japanese language

The 2021.4.0 version of the UI, online help, and release notes has been localized to
Japanese.
