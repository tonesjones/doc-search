---
title: "New and changed features in 2022.10.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features-in-2022.10.0.html"
content_id: "9zpEyBGgMXC_q41clf9viw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:24.655845+00:00"
---

# New and changed features in 2022.10.0

## Git repository SCM integration - Phase 2

Black Duck 2022.10.0 has updated the way users can add repository/branch fields when
creating a project and version. You now have the ability to add authorized SCM
providers (GitHub Standard and GitHub Enterprise only at this time) which can then
be selected when creating a new project. Doing so will automatically pre-populate
the repository URL and branch version in the Project Settings page for your new
project.

This feature is compatible with Detect 8.x and above, and will take effect with new
package manager scans.

Please note that SCM integration is not enabled by default in Black Duck and must be
activated by adding the following in your environment:

For Swarm users, add the following to your `blackduck-config.env` file:

```
blackduck.scan.scm.enableIntegration=true
```

For Kubernetes users, add the following to your `values.yaml` file under the environs
section:

```
environs:
    blackduck.scan.scm.enableIntegration: "true"
```

## New bulk actions for project version components

The bulk update feature now supports the following actions on components on the
project versions page:

1. Ignore/unignore components
2. Set component usage type
3. Mark as reviewed/unreviewed
4. Set include/exclude in notices file

## Creating reports using UTF8 with BOM

*Please note that this feature was added in Black Duck 2022.7.0 and was accidentally omited from that
version's release notes.*

Black Duck 2022.7.0 introduced support for UTF8 with BOM character encoding in reports for customers
using non-Western characters. To enable this feature, add the following to the `blackduck-config.env`
file:

```
USE_CSV_BOM=true
```

## New heatmap data download

You can now review and analyze terminal scan trends by downloading the heatmap as a
compressed CSV and create the heatmap as a pivot in a spreadsheet program. This data
can be downloaded by navigating to
Admin > Diagnostics > System Information.

## New SBOM report fields

You can now add new additional SBOM fields to your projects to include more detail to
your software bill of materials (SBOM) reports. SBOM fields include the following
new fields.

Set on the BOM component level:

- Package URL: Listed in the `externalRefs` section as
  `referenceType: purl` for `referenceCategory:
  PACKAGE_MANAGER` elements in SPDX reports, and under the
  `components` section as `purl` for
  CycloneDX reports.
- Package Supplier: Listed as (`supplier`) for both report
  types.
- CPE: Listed in the `externalRefs` section as
  `referenceLocator` for `referenceCategory:
  SECURITY` elements in SPDX reports, and under the
  `components` section as `cpe` for
  CycloneDX reports.

Set on the component level:

- Description: Listed as `description` for both report
  types.
- Originator: Listed as `originator` under the
  `packages` section for SPDX reports, and as
  `author` under the `components`
  CycloneDX reports.

## New Global Notification Viewer role

A new role has been created that has read only access to all projects and receives
all system notifications regardless of user preferences.

## New notification subscription management

You now have the ability to enable or disable which notifications your users receive.
You can manage these settings by going to Admin > System Settings > Notifications. Please note that users with the Global Notification Viewer role will
still receive all notifications on the system.

## Updated notifications management for watched projects

You can now manage which watched projects you receive notifications from in your My
Settings page. To do so, click your user name on the top right menu, click Watched
Projects, and then select the Watched Projects tab.

## Updated notification retention period

The default configuration value for notification retention has been reduced to 14
days from 30. This can be modified by setting the
`BLACKDUCK_HUB_NOTIFICATIONS_DELETE_DAYS` variable in
`blackduck-config.env`.

## New vulnerability conditions for policies

A new Vulnerability Tags category has been added to the Vulnerability Conditions of
policies replacing and including the Remote Code Execution (RCE) vulnerability. This
category includes the following filter options when creating or editing
policies:

- **Zero-click Remote Code Execution**: Vulnerabilities which can result in
  the execution of code on the system, triggered by a remote attacker without
  requiring or relying on any third party action.
- **Malicious Code Identified**: Software containing code with malicious
  intent and is designed to have harmful or destructive consequences if
  executed within your system.
- **Embargoed Vulnerability Details**: Vulnerabilities whose technical
  details are currently under embargo and the details are not published by the
  vendor at this time.
- **Unconfirmed Vulnerability**: Vulnerabilities that do not have a
  code-based fix because the vendor has decided that the behavior of the
  component is intended and does not believe there is a vulnerability.

## New vulerability tags added to Vulnerablity Update reports

Vulnerability Update reports will now display vulnerability tags where applicable.
These include the Vulnerability tags listed above.

## New export functionality for lists and tables

You can now export lists and tables to CSV on the following pages:

- Dashboard page: Found in the Results Summary section of the Dashboard.
- Find page: Found above the search field on the left side of the Find page.
- Scans page: Found next to the delete button on the top left side of the Scans
  page.
- Users & Groups page: Found next to the Create User button on the top left
  side of the Users & Groups page.

## Enhanced source view when importing BDIO for binary scanning and Protex BOM imports

Currently, the Scans page lists the *Components Not Found* in the BOM Import
Log. Now with the 2022.10.0 release, unmatched components will also be surfaced in
the Source View tab. Please note that unmatched components will be surfaced in the
Source view for new scans only. Existing scans will be unchanged.

## Reporting schema enhancements

The `reporting.component` view now has three additional fields:

- `reporting.component.created_at`: The created at time for the
  component, copied from the BOM. Represents the first time the component was
  added to the BOM.
- `reporting.component.updated_at`: The updated at time for the
  component, copied from the BOM. Represents the most recent time that
  component was updated in it's BOM.
- `reporting.user_group_project_mapping`: Adds which user is
  mapped to which group/groups and which user is mapped to which
  project/projects.

## New Ephemeral Signature Scan - Limited customer availability

The Ephemeral Signature Scan is a new scan mode that does not create or use any
permanent storage within Black Duck, thus there is no bill of material (BOM) stored.
It is used to quickly find policy violations within the designated scan target. In
order to use the Ephemeral Signature Scan, you must have the following:

- Black Duck Detect 8.2.0 or later
- Black Duck 2022.10.0 or later
- Hosted KnowledgeBase
- Match as a Service must be enabled

Please note that this feature is limited customer availability and is not generally
available in Black Duck 2022.10.0.

## Updated synopsysctl

Black Duckctl has been updated to work with the new PostgreSQL 13 container.

## Container versions

- blackducksoftware/blackduck-postgres:13-2.13
- blackducksoftware/blackduck-authentication:2022.10.0
- blackducksoftware/blackduck-webapp:2022.10.0
- blackducksoftware/blackduck-scan:2022.10.0
- blackducksoftware/blackduck-jobrunner:2022.10.0
- blackducksoftware/blackduck-cfssl:1.0.10
- blackducksoftware/blackduck-logstash:1.0.21
- blackducksoftware/blackduck-registration:2022.10.0
- blackducksoftware/blackduck-nginx:2.0.28
- blackducksoftware/blackduck-documentation:2022.10.0
- blackducksoftware/blackduck-upload-cache:1.0.29
- blackducksoftware/blackduck-redis:2022.10.0
- blackducksoftware/blackduck-bomengine:2022.10.0
- blackducksoftware/blackduck-matchengine:2022.10.0
- blackducksoftware/blackduck-webui:2022.10.0
- blackducksoftware/bdba-worker:2022.9.1
- blackducksoftware/rabbitmq:1.2.14
