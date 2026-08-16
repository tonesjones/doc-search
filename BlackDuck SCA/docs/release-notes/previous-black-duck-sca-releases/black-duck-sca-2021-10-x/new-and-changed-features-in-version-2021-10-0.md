---
title: "New and Changed Features in Version 2021.10.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features-in-version-2021.10.0.html"
content_id: "2i2wLElQDq~aBP6wooko2Q"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:53.336100+00:00"
---

# New and Changed Features in Version 2021.10.0

## Updated error messages for the Enhanced Signature Generation

Signature scanning server-side error messages have been updated. A complete list of
error messages will be made available in the user guide in an upcoming release.

## Unmapped scans data retention configuration setting

A new configuration setting is now available for administrators to change the default
retention period for unmapped scans. Starting with Black Duck 2021.10.0, this
setting will be enabled by default and set to a period of 30 days (previously 365
days). This retention setting can be updated and set to as low as 1 day and to as
high as 365 days.

To change this setting in the UI, click [image: image] , click Settings, and then click
Data Retention.

## Estimated Security Risk

This estimated risk statistic is formulated by looking at all the versions of a
component sorted by security vulnerability severity category and calculating the
maximum vulnerability count for each severity category for each component version.
The maximum vulnerability count for each severity category is shown in the
“Estimated Security Risk by Severity Category" on the Bill of Material for Security
risk. The highest severity category counts may reference different component
versions. For example:

- Version 1.1 has 2 Critical, 3 High, 15 Medium, 4 Low
- Version 1.2 has 2 Critical, 4 High, 12 Medium, 1 Low
- Estimated Security Risk by severity category for components with unknown
  versions would return as 2 Critical, 4 High, 15 Medium, 4 Low on the
  BoM.

Users should choose the exact version used in the application to view the accurate
risk instead of the estimated risk. This estimated risk information is provided to
help prioritize what components to review first. Users are encouraged to use
estimated risk information in conjunction with BD Policy Management to further
prioritize what components to triage first based on their company’s security
policies.

Note: The information presented is only a statistical data estimation. As a result, the estimated
security risks will not have CVE data.

## Generating Notices report when deep license data is enabled

The notices file will now place any declared licenses before additional ones. The
declared and additional licenses will then be sorted alphabetically.

## Addition of comments to the Source view and the Source report

Comments can now be added to entries in the Source view of a project. File comments
are also shown in the snippet view. These comments also appear in the Source Report
in the new column labeled Comments. Select the Source check box for the Version
Detail Report in the Report tab to create a Source Report.

You can leave a comment for a particular entry in the Source tab by:

- clicking the [image: image]
  icon found at the end of that component's row and selecting Comments from
  the dropdown menu or clicking the [image: image] icon if there
  are already comments present.
- clicking the entry in the Source view, clicking the Name of the component,
  clicking the [image: image] icon, and
  then selecting Comments from the dropdown menu or by clicking the [image: image] icon if there
  are already comments present.

## Policy Management Enhancement - Project Groups

Black Duck users will now have the ability to apply policy rules to project group(s)
and its descendants. To do so, go to **Policy Management** and either click the
**Create Policy Rule** button or the [image: image] button and select
**Edit**. When the Create/Edit Policy Rule modal opens, ensure the **A
Subset of Projects, filtered by...** option is enabled to see the Project
Conditions filter dropdown.

## Policy Management Enhancement - Added (RCE) Remote Code Execution to Vulnerability Conditions

Black Duck users will now have the ability to add Remote Code Execution (RCE) as a
filter option when creating or editing policies. To do so, go to **Policy
Management** and either click the **Create Policy Rule** button or the
[image: image] button and select
**Edit**. The new (RCE) Remote Code Execution value will be displayed in the
Vulnerability Conditions dropdown menu.

## Changes to Project Group Manager permissions

Previously, the actual permissions of the Project Group Manager were not affected by
the global settings for allowing a project manager to remediate vulnerabilities or
override policy. Now, the Project Group Manager role permissions will be adjusted
based on Project Manager Role Settings.

## Signature scanner dry run update

Previously, when performing a Signature Scanner dry run, the output would produce a
JSON file. Starting with Black Duck 2021.10.0, the produced output file will be a
.bdio extension, and is a zip file. It will continue to be generated in the same
directory as dry run as traditional signature scanning.

## Supported browser versions

- Safari Version 15.0 (16612.1.29.41.4, 16612)
  - Safari versions 13.0 and below are no longer supported
- Chrome Version 94.0.4606.71 (Official Build) (x86_64)
- Firefox Version 92.0.1 (64-bit)
- Microsoft Edge Version 94.0.992.38 (Official build) (64-bit)
  - Microsoft Edge versions 79 and below are no longer supported

## Container versions

- blackducksoftware/blackduck-postgres:9.6-1.3
- blackducksoftware/blackduck-authentication:2021.10.0
- blackducksoftware/blackduck-webapp:2021.10.0
- blackducksoftware/blackduck-scan:2021.10.0
- blackducksoftware/blackduck-jobrunner:2021.10.0
- blackducksoftware/blackduck-cfssl:1.0.4
- blackducksoftware/blackduck-logstash:1.0.11
- blackducksoftware/blackduck-registration:2021.10.0
- blackducksoftware/blackduck-nginx:2.0.9
- blackducksoftware/blackduck-documentation:2021.10.0
- blackducksoftware/blackduck-upload-cache:1.0.19
- blackducksoftware/blackduck-redis:2021.10.0
- blackducksoftware/blackduck-bomengine:2021.10.0
- blackducksoftware/blackduck-matchengine:2021.10.0
- blackducksoftware/blackduck-webui:2021.10.0
- blackducksoftware/bdba-worker:2021.9.1
- blackducksoftware/rabbitmq:1.2.5
