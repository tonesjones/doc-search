---
title: "New and Changed Features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "VQlscT6BihM8r5fGW6nV6A"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:34:59.000997+00:00"
---

# New and Changed Features

## Integration of EUVD Vulnerability Data into VEX Reports

As part of compliance with the NIS2 directive, we are introducing support for
European vulnerability data from the European Vulnerability Database (EUVD) in VEX
(Vulnerability Exploitability eXchange) reports. This enhancement aligns with
efforts to improve coordinated vulnerability reporting under NIS2 and the Cyber
Resilience Act (CRA).

**Key Features:**

- **EUVD Reference Integration:** Vulnerability data published from the EUVD
  will be included as related reference IDs in our BDSA and CVE VEX reporting
  processes. Note that EUVD vulnerabilities will not be directly ingested as a
  separate type of vulnerability.
- **Link to EUVD Records:** Each EUVD record will be linked in the
  vulnerability description field on the Vulnerabilities tab, mirroring the link
  to the external EUVD site found in the corresponding CVE record. A warning will
  be displayed about navigating to an external site.
- **API Support:** APIs are available to obtain additional EUVD details.
- **CSAF 2.0 VEX Report Enhancements:** The EUVD ID and description will be
  included as additional identifiers in the existing vulnerability entries in the
  vulnerabilities/id and vulnerabilities/id/description fields of the CSAF 2.0 VEX
  report.
- **System Setting for VEX Reports:** A system setting will allow toggling the
  exclusion of BDSA IDs in VEX reports, located under Administration > System
  Settings > SBOM. The toggle's default value will be "Off."

## Introduction of TLP Designation for VEX Documents

Black Duck SCA 2026.4.0 introduces the Traffic Light Protocol
(TLP) designation feature for VEX (Vulnerability Exploitability eXchange) documents.
This enhancement allows users to specify the appropriate TLP label for information
sharing, ensuring clarity on how the information should be treated by
recipients.

Users can select the appropriate TLP designation from a dropdown menu within the
project-level SBOM fields. The selected TLP value will be included in the VEX
document, adhering to the format defined by [FIRST.org](https://www.first.org/tlp/).

## Enhanced SBOM PURL Field for Component Versions

The SBOM PURL field for component versions has been updated to display all matching
origin IDs when multiple PURL matches are available. Users will see a notification
indicating the number of PURL matches for a component version, allowing for better
visibility and selection options. When there are multiple PURL matches, users can
choose one of the displayed matches or enter their own custom PURL to override the
default selection. Each selected PURL will be included in the SBOM report.

## Central Configuration for Correlated Scanning

To streamline the enablement of correlated scanning for all customers, Black Duck SCA 2026.4.0 introduces a new global configuration option
for the Detect parameter
`detect.blackduck.correlated.scanning.enabled`.

To take advantage of this feature, you must have Detect 11.4.0+ and SCASS must be
enabled on your product registration key.

Correlated Scanning can be enabled from **Admin** → **System Settings** →
**Black Duck Detect**.

## Option to Globally Disable Automatic Unmapping for SBOM Import Scan Types

Black Duck SCA now includes an option to globally disable the
automatic unmapping of scan types for SBOM (Software Bill of Materials) imports.

This enhancement prevents unintended unmapping of SBOMs when multiple SBOMs are
imported into the same project version. By excluding SBOM scan types from the
automatic unmapping functionality, users can maintain their manual mappings,
ensuring greater accuracy and control over the mapping process.

## Enhanced Data Table and Dashboard Row Selection

The user interface has been updated to allow users to select the number of rows
displayed per page in data tables and dashboards throughout the application. Users
can now choose from page size options of 25, 50, 100, 250, and 500 items per page.
Please be aware that selecting larger page sizes may result in slower loading times,
as the backend processes a greater number of rows.

## Deprecation of Detect 9 in Detect Version Management

With the release of Detect 11 on October 30, 2025, and the end of service for Detect
9.x scheduled for April 2026, Black Duck SCA has deprecated
support for Detect 9 in the Detect Version Management page.

For customers upgrading with Detect 9.x already selected, a red warning indicator and
message will appear, advising that Detect 9 has reached end of support and
recommending an upgrade. Additionally, users will be warned that switching the
central configuration away from Detect 9.x is irreversible. Detect 9.x will no
longer appear as an option for fresh installs, remaining visible only for customers
who had it selected prior to upgrading. Furthermore, Detect 11 will be set as the
default version for new customers or upgrades to version 2026.4.0 where the detect
version property was previously null.

## Removal of Multi-Project Option from Global CSAF VEX Report

The Multi-Project option has been removed from the Global CSAF VEX report. This
decision was made to simplify the management of document-level attributes, as the
use case for including multiple projects in a single VEX document is deemed
unlikely.

**Key Changes:**

- The project selection in the Global CSAF VEX report has been modified to a
  single selection dropdown, allowing users to type and filter project names.
  The multi-select feature is no longer available, and reports can only be
  generated for a single project.
- The API supporting multiple projects in a single VEX report has been
  deprecated. Users will receive a warning when using the old endpoint,
  indicating that they may encounter unexpected results regarding
  document-level data.

## Removal of Datadog from Helm Charts

Datadog has been discontinued, and as a result, all references to Datadog will be
removed from the Helm Charts. With the removal of Datadog from our Helm Charts,
customers are encouraged to review their current monitoring setups and explore
alternative solutions to ensure your monitoring needs are met.

## Added Support for Docker versions 29.x & 28.x

Black Duck SCA has aded support for the latest Docker versions
29.x and 28.x. This enhancement ensures compatibility with the newest features and
improvements in Docker, allowing users to effectively manage and secure their
containerized applications. Customers are encouraged to update to these versions to
take advantage of the latest capabilities in Black Duck SCA.

## Minimum supported browser versions

- Safari Version 17.4
- Chrome Version 124 (x86_64)
- Firefox Version 125 (64-bit)
- Microsoft Edge Version 124 (64-bit)

## Container versions

- blackducksoftware/blackduck-postgres:16-2.7
- blackducksoftware/blackduck-postgres-upgrader:16-1.3
- blackducksoftware/blackduck-postgres-waiter:1.0.20
- blackducksoftware/blackduck-cfssl:1.0.36
- blackducksoftware/blackduck-nginx:2026.4.0
- blackducksoftware/blackduck-logstash:1.0.45
- blackducksoftware/bdba-worker:2026.3.1
- blackducksoftware/rabbitmq:1.2.49
- blackducksoftware/blackduck-authentication:2026.4.0
- blackducksoftware/blackduck-bomengine:2026.4.0
- blackducksoftware/blackduck-documentation:2026.4.0
- blackducksoftware/blackduck-integration:2026.4.0
- blackducksoftware/blackduck-jobrunner:2026.4.0
- blackducksoftware/blackduck-redis:2026.4.0
- blackducksoftware/blackduck-registration:2026.4.0
- blackducksoftware/blackduck-scanmatch:2026.4.0
- blackducksoftware/blackduck-storage:2026.4.0
- blackducksoftware/blackduck-webapp:2026.4.0
