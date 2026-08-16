---
title: "New and changed features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "MVXGnU5qBa6N1UesG1rJFQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:48.550072+00:00"
---

# New and changed features

## PostgreSQL 15 support for external databases

Black Duck now supports and recommends PostgreSQL 15 for new installations that use
external PostgreSQL. PostgreSQL 15 is not yet supported on Azure Database for
PostgreSQL, therefore Black Duck recommends PostgreSQL 14 Flexible Server for users of
that environment.

Migrating to Black Duck 2023.7.x does not require migration to PostgreSQL 15.

No action is required for users of the internal PostgreSQL container.

## Encryption of report object types

Black Duck 2023.7.0 now marks report objects stored in the object store as sensitive,
making them eligible to be encrypted at rest in the FILE volume where they are
persisted. In order for them to be encrypted, Black Duck Crypto must be enabled in
your environment with appropriate secrets provided. The following behavior changes
will apply based on your environment's Black Duck Crypto setting:

**For environments without Black Duck Crypto enabled at the time of upgrade to
2023.7.0**

All existing reports and all new reports will remain unencrypted on disk - but marked
as sensitive. If Black Duck Crypto is enabled later on, these objects will be
encrypted in the background in order to comply with their sensitive nature.

**For environments with Black Duck Crypto already enabled at the time of upgrade to
2023.7.0**

If you have already enabled Black Duck Crypto, the existing reports will remain
unencrypted and all new reports will be encrypted. If you need to force everything
to be encrypted, set the environment variable
`SYNOPSYS_CRYPTO_ROTATE_RESOURCES_ON_STARTUP=true` which will
force the system to rotate the internal key and re-encrypt everything, including the
old unencrypted reports.

## Encryption for storage service objects

Sensitive objects stored in object storage FILE volumes will be encrypted at rest if
Black Duck Crypto is enabled.

## Updated Jobs page

The Jobs page has been redesigned to improve usability and scalabilty of the
information displayed. The Jobs page has been broken down into three tabs:

- Finished: Displays all completed jobs, sucessful or failed.
- Scheduled: Displays all jobs scheduled to run in your environment.
- Processing: Displays all jobs currently in progress.

## New Unmatched Origins management page

You can now more easily manage origin IDs that Black Duck identified during a package
scan but could not be mapped to a component version. From the Unmatched Origins
page, you can add or remove mappings to custom components which will then be added
to subsequent package manager scans. The Unmatched Origins page can be reached by
clicking Manage > Unmatched Origins.

In addition, you can now manage origin IDs mapped to custom components on their
component version page.

Matching to custom components requires the use of Detect 7 or higher and is currently
only supported for package manager scans.

## Enhanced Notices File report

New options that can be added to the Notices File report:

- Deep License Data: Deep licenses discovered via component origin. Only available if deep
  licenses are enabled for the project.
- File Copyright Text: Copyright texts discovered in file matches. Only available if file
  matches are present.
- Unmatched File Discoveries: File discoveries unassociated with components in the project.
  Only available if unmatched files are present in the project.
- File License Data: Licenses discovered in file matches. Only available if file matches are
  present.

## New SBOM report fields

The SPDX version of the SBOM report now includes two new optional fields:

- Package Comment: General comments about the package being described.
- Package Valid Until Date: The end of the support period for a package from the
  supplier.

You must first activate these fields under Manage > SBOM > BOM Component. Once
enabled, you can update them by navigating to the project version's BOM, clicking
the options button at the end of the component's row, and then selecting SBOM
Fields.

## Updated BOM filter label

The Match Status filter on the Component tab of the BOM project version page was
ambiguously named. This filter only applies to snippet matches therefore the name
was changed to Snippet Match Status to correctly capture that very specific use
case.

## Enhanced logging information

Added logging information (auth container) when a user logs in using
username/password for both successful and failed logins.

## Updated permission access for reports containing deleted projects

Access permission to reports have been updated where if one of the projects has been
deleted, users can access if they have permission for all the remaining projects in
the report (that haven't been deleted), or global project read access as part of
their user role. Users not falling into either category above will not be able to
access the report.

## Enhanced Version Details report

The Version Details report now includes updates for sub-projects:

- The Version Details update guidance report now includes upgrade guidance for
  sub-projects.
- The first column of the project version update guidance report is now "Used by"
  which, if not blank, reports the subproject for the upgrade guidance.

## Enhanced report generation

The mechanism for report data gathering and report format writing has been improved
to constrain memory consumption. Please note that, as a result of this change, may
result in longer report generation.

## Consolidation of KnowledgeBase environment variables

Black Duck has a variety of environment variables to control KnowledgeBase scheme,
host, and port configuration for a variety of KnowledgeBase services. Starting with
Black Duck 2023.7.0, KnowledgeBase environment variable configurations have been
unified on the following variables to simplify configuration:

- BLACKDUCK_KB_SCHEME
- BLACKDUCK_KB_HOST
- BLACKDUCK_KB_PORT

The following property prefixes have been explicitly removed and no longer
referenced:

- BLACKDUCK_KBCLOUD
- BLACKDUCK_KBDETAIL
- BLACKDUCK_JSONWEBTOKEN

Users that have manually overridden old KnowledgeBase environment variables for
customization should verify their environment to ensure functionality.

## Updated date picker tool in UI

The date picker used in the UI has been updated which will change its appearance
(depending on the browser) and functionality. Please note that, it does not get
localized by the browsers language (except Firefox). It now depends on the operating
systems locale for Chrome, Edge and Safari.

## Supported browser versions

- Safari Version 16.4
  - Safari versions 14 and below are no longer supported
- Chrome Version 114.0.5735.198 (Official Build) (x86_64)
  - Chrome versions 91 and below are no longer supported
- Firefox Version 114.0.2 (64-bit)
  - Firefox versions 89 and below are no longer supported
- Microsoft Edge Version 114.0.1823.67 (Official build) (64-bit)
  - Microsoft Edge versions 91 and below are no longer supported

## Container versions

- blackducksoftware/blackduck-postgres:13-2.27
- blackducksoftware/blackduck-authentication:2023.7.0
- blackducksoftware/blackduck-webapp:2023.7.0
- blackducksoftware/blackduck-scan:2023.7.0
- blackducksoftware/blackduck-jobrunner:2023.7.0
- blackducksoftware/blackduck-cfssl:1.0.20
- blackducksoftware/blackduck-logstash:1.0.32
- blackducksoftware/blackduck-registration:2023.7.0
- blackducksoftware/blackduck-nginx:2.0.47
- blackducksoftware/blackduck-documentation:2023.7.0
- blackducksoftware/blackduck-upload-cache:1.0.45
- blackducksoftware/blackduck-redis:2023.7.0
- blackducksoftware/blackduck-bomengine:2023.7.0
- blackducksoftware/blackduck-matchengine:2023.7.0
- blackducksoftware/blackduck-webui:2023.7.0
- blackducksoftware/blackduck-storage:2023.7.0
- blackducksoftware/bdba-worker:2023.6.0
- blackducksoftware/rabbitmq:1.2.28
