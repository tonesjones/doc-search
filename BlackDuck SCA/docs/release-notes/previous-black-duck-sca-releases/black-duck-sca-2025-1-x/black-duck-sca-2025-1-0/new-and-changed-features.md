---
title: "New and changed features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "_7aFaFzXZVdYfrBgFnNyZQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:46.961454+00:00"
---

# New and changed features

## New scan types available for SCA Scan Service (SCASS)

The SCA Scan Service (SCASS) has been enhanced to include support for Binary and
Container scanning. This update expands the service's capabilities, enabling broader
analysis and improved flexibility for users managing diverse scanning
requirements.

## New remediation statuses added

Black Duck now includes VEX (Vulnerability Exploitability
eXchange) remediation status values, as described by the Cybersecurity and
Infrastructure Security Agency (CISA). These values provide detailed tracking of the
exploitability and remediation efforts for vulnerabilities, helping you assess and
manage vulnerability risks more effectively. The following remediation status values
have been added:

- Known Affected (AFFECTED): Actions are recommended to remediate or address
  this vulnerability.
- Known Not Affected (NOT AFFECTED): A justification must be provided to ensure
  that the decision is properly documented.
- Under Investigation (UNDER INVESTIGATION): It is not yet known whether these
  product versions are affected by the vulnerability. An update will be
  provided in a later release.

## New feature to define default CPE for component versions

Black Duck now includes the ability to define a default Common
Platform Enumeration (CPE) for component versions. This feature simplifies
vulnerability tracking by ensuring that a consistent CPE is associated with each
component version, reducing the need for manual updates. Users can configure a
default CPE directly in the component version settings, steamlining SBOM generation
and improving data accuracy.

## New slide-out panel for BOM component information

In the Components tab for a project version, clicking a component now opens a
slide-out panel instead of navigating to a new page. This update preserves the
context of where the component is being used, eliminating the need to switch back
and forth between pages for additional information.

## New Exclude Unconfirmed Snippet Matches option added to SBOM Templates

A new SBOM template option, "Exclude Unconfirmed Snippet Matches" has been added to
the Component Data section in SBOM templates. This option allows users to exclude
components with unconfirmed snippet matches from their SBOM, providing a cleaner and
more precise representation of the project's open source composition.

## New scan CSV data

Black Duck now supports generating CSV data during scans using
the new `--upload-csv` parameter in the scan CLI. This feature allows
users to create a CSV file during the scan and automatically upload it to Black Duck. Additionally, users can download the CSV data
directly from the Scans page and the project version's Settings tab in the Black Duck interface, providing flexible access to scan results
for further analysis and reporting.

## Added support for CycloneDX 1.6

You can now export the Software Bill of Materials report for your projects in
CycloneDX v1.6 format. This can be done by viewing a project version, clicking the
Reports tab, clicking the Create Report button, and then selecting CycloneDX v1.6 -
JSON. For more information on CycloneDX v1.6, please visit the [CycloneDX v1.6 reference page](https://cyclonedx.org/docs/1.6/json/).

## Added support for CVSS v4.x vulnerability score ranking

Black Duck now includes support for CVSS (Common Vulnerability
Scoring System) version 4.0, providing enhanced granularity for Base metrics, a new
Supplemental metric group, and an updated methodology for determining severity,
among other improvements. For more details on CVSS v4.0, visit the official
specification documentation at <https://www.first.org/cvss/v4.0/specification-document>.

## Added support for SAML signed authentication certificates

Black Duck now supports SAML signed authentication certificates,
enhancing security by validating authentication requests against a trusted
certificate. System Administrators can manage certificates directly in the SAML
configuration settings.

## Updated JWT session token invalidation enabled by default

The feature to invalidate JWT session tokens upon logout is now enabled by default.
This update enhances security by ensuring that session tokens are no longer valid
after a user logs out.

## Discontinued support for CVSS v2 vulnerability score ranking

CVSS v2 will no longer be supported as the highest-priority CVSS ranking. However, it
will still be displayed if no CVSS v3.x or CVSS v4.x score exists for a
vulnerability.

## Container versions

- blackducksoftware/blackduck-postgres:15-1.10
- blackducksoftware/blackduck-postgres-upgrader:15-1.3
- blackducksoftware/blackduck-postgres-waiter:1.0.14
- blackducksoftware/blackduck-cfssl:1.0.30
- blackducksoftware/blackduck-nginx:2025.1.0
- blackducksoftware/blackduck-logstash:1.0.40
- blackducksoftware/bdba-worker:2024.12.2
- blackducksoftware/rabbitmq:1.2.42
- blackducksoftware/blackduck-authentication:2025.1.0
- blackducksoftware/blackduck-bomengine:2025.1.0
- blackducksoftware/blackduck-documentation:2025.1.0
- blackducksoftware/blackduck-integration:2025.1.0
- blackducksoftware/blackduck-jobrunner:2025.1.0
- blackducksoftware/blackduck-matchengine:2025.1.0
- blackducksoftware/blackduck-redis:2025.1.0
- blackducksoftware/blackduck-registration:2025.1.0
- blackducksoftware/blackduck-scan:2025.1.0
- blackducksoftware/blackduck-storage:2025.1.0
- blackducksoftware/blackduck-webapp:2025.1.0
