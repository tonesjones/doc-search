---
title: "New and Changed Features in Version 2021.8.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features-in-version-2021.8.0.html"
content_id: "6ExpGoL6msqWgos0onCucQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:06.320561+00:00"
---

# New and Changed Features in Version 2021.8.0

## PostgreSQL 13 support for external databases

Black Duck now supports and recommends PostgreSQL 13 for new installs that use
external PostgreSQL. Migrating to 2021.8.x does not require migration to PostgreSQL
13.

No action is required for users of the internal PostgreSQL container.

Please note that PostgreSQL 12 is not supported.

Installation documentation will be updated in an upcoming release.

## Notice for Azure customers

Support for Black Duck on Azure PostgreSQL 13 will be best-effort only with no
guarantee of resolution until Azure PostgreSQL 13 is fully released. As such, we
very strongly recommend against using Azure PostgreSQL 13 for production deployments
and customer should use Azure PostgreSQL 11.

For more information on Azure support for PostgreSQL 13, please visit
https://docs.microsoft.com/en-us/azure/postgresql/concepts-version-policy.

## New System Setting for scans: Component Dependency Duplication Sensitivity

This setting allows users to change how the system displays duplicate package ID's
for components on the Source page that are found during scans. In previous releases
and as the default setting in 2021.8.0 (set to 1), the Source page will only display
one package ID discovery regardless of how often it is found in your scan. Changing
this setting to greater than 1 will display more entries allowing for greater
layer-by-layer insight to help determine from which layer each component originated.
This feature is especially useful to customers who are scanning in Detect with BOM
aggregation enabled and want to see package ID references across the various modules
that have been aggregated into 1 scan.

## New System Setting for scans: Minimum Scan Interval

This setting allows users to change the minimum hourly frequency of which signature
scans can be performed for a given code location when using the LCA enhanced
signature scanning. The default setting is set to 0, or no minimum scan interval,
meaning scans are not prevented from occurring regardless of frequency. If set to
greater than 0, signature scans will not be processed if they occur before the set
scan interval. For example, a setting of 4 will not allow signature rescans before 4
hours of time have elapsed. This setting may be configured globally in the
Administration > System Settings > Scan page or through the Detect client as a
command line option. Note: This setting is only used if customer scan using the
parameter
--detect.blackduck.signature.scanner.arguments='--signature-generation'.

Note: When this feature is enabled, signature scans with Detect will finish with a status of
success even if the signature scan was not run due to the scan interval. A warning
message will appear in the logs indicating the scan was not run, but there will be
no other indication given to the user.

## Changes in Rapid Scan policy application

Rapid Scan users now have the ability to configure how policies are applied to the
results of Full (traditional) scans, Rapid Scans, or both. The default setting for
new installations of Black Duck starting from version 2021.8.0 will be set to apply
to full scans only. To use Rapid Scan to fetch all vulnerabilities regardless of
policies, simply create a single policy, setting the condition severity >=0.

## Added phone-home cumulative count of the number of rapid scans done

This count is accurate and data is not lost, but there might be some timing issues
where some of the scans are from the subsequent day’s data.

## Rapid Scan vulnerability conditions added to Policy Management

The following vulnerability conditions are now available in Policy Management:

- CWE IDs
- Solution Available
- Workaround Available
- Exploit Available
- Reachable from Source
- Remediation Status

## Project Group Management

Black Duck now provides the ability to logically group all your projects in the Hub,
allowing you to organize which projects belong to which business unit making it
easier for you to view risk across the organization. Project groups can contain both
projects and other project groups to provide a multi-level hierarchy.

Users and Groups can be assigned to Project Groups with any number of roles. That
assignment will give those users access to the projects below that group with the
specified roles unless that assignment is explicitly overridden at the lower levels.
This concept allows for setting users with default access to projects that haven't
been created yet.

In addition, the search dashboard has been enhanced to return search results for
projects the user has access to via a project group.

## New Global Release Creator, Project Group BOM Annotator user roles, and changes to existing roles

The Project Creator and Global Code Scanner roles have had their access to the Global
Release Create permission revoked and will no longer be able to create releases of
projects they do not own or have access to. A new role, Global Release Creator, has
been made to fill in the gap for users who depended on this functionality. All
current users with Project Creator and/or Global Code Scanner will automatically
inherit this role as part of the upgrade migration script. That means this change
will be specifically opt-out for current users looking to take advantage of the more
narrow security change.

The Project Group BOM Annotator has the BOM Annotator permissions for every project
in the assigned project group. This means they can add or edit comments and edit
custom fields for projects associated with the project group.

## Protex BOM Tool token access support enhancement

The Protex BOM tool now supports the BD_HUB_TOKEN environment variable to upload json
exported from Protex to the Hub. You can set the token by adding "-T " using command
prompt.

Add `BD_HUB_TOKEN=[insert token here]` variable to
`.bash_profile` to make the change permanent.

## Vulnerability Notifications enhancement

Added a new environment variable: `BLACKDUCK_NOTIFY_WHEN_REMEDIATED`
in the `blackduck-config.ev` file. It defaults to true, but when set
to false Black Duck will no longer send/create "new" vulnerability notifications for
vulnerabilities with a remediation status of "Ignored, Remediation Complete,
Mitigated, or Patched."

## Signature scan timeout message enhancement

Network timeouts during a signature scan (waiting for a response from HUB) now return
an accurate error message that indicates a network timeout and not an I/O error
(code 74). The new message format will display `Scan <Corresponding Scan
ID> failed: [<Reason why it happened and whether to contact an administrator
or retry the scan>]`.

## Request Retry mechanism for Black Duck Hub enhancement

A waiter has been introduced which will retry uploading the scan to Hub when it
receives HTTP 502/503/504 responses. It will retry in increments of 30 seconds for
10 minutes before declaring that the scan is failed.

## Scans page enhancement

A new Created column was added to the Scans page allowing you to see when the scan
was created. The date displayed in the column with make it easier to compare dates
when filtering scans using the Created Date option.

## Surface license risk info for Components without versions

New logic has been introduced to determine a default license for components with an
unknown version. This is an estimated license based on greatest number of times it
shows up across the top 1,000 versions of the component. With this, you will be able
to calculate license risk without requiring a version to be selected. It is,
however, recommended that you review these components and manually specify a version
for more accurate results.

## Reporting database enhancements

Added the following data to scan_stats_view under the reporting schema:

- user_id
- project_id
- project_name
- version_id
- version_name
- scan_id
- scan_name
- code_location_id
- code_location_name
- scan_type
- scan_status
- scan_start_at
- scan_end_at
- scan_duration
- scan_age
- scan_archived_at
- application_id

## Policy rule condition enhancement

A new policy condition operator was added for policy rules Vulnerability Conditions
Category for Overall Score. You may now select "Less than or equal to" when creating
or editing policy rules.

## Container versions

- blackducksoftware/blackduck-postgres:9.6-1.1
- blackducksoftware/blackduck-authentication:2021.8.0
- blackducksoftware/blackduck-webapp:2021.8.0
- blackducksoftware/blackduck-scan:2021.8.0
- blackducksoftware/blackduck-jobrunner:2021.8.0
- blackducksoftware/blackduck-cfssl:1.0.3
- blackducksoftware/blackduck-logstash:1.0.10
- blackducksoftware/blackduck-registration:2021.8.0
- blackducksoftware/blackduck-nginx:2.0.5
- blackducksoftware/blackduck-documentation:2021.8.0
- blackducksoftware/blackduck-upload-cache:1.0.18
- blackducksoftware/blackduck-redis:2021.8.0
- blackducksoftware/blackduck-bomengine:2021.8.0
- blackducksoftware/blackduck-matchengine:2021.8.0
- blackducksoftware/blackduck-webui:2021.8.0
- blackducksoftware/bdba-worker:2021.7.0
- blackducksoftware/rabbitmq:1.2.3
