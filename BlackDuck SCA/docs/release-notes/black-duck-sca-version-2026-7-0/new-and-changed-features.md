---
title: "New and Changed Features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "~C1gbG6qNZF~nxPnaiNNFw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:34:47.727305+00:00"
---

# New and Changed Features

## Black Duck SCA MCP Server

Black Duck now includes an MCP (Model Context Protocol) server that connects AI
coding assistants directly to your Black Duck SCA instance.
This enables developers to investigate security posture, triage vulnerabilities,
generate compliance reports, and run scans — all from within their IDE or AI
assistant.

**Supported capabilities:**

- **SBOM, VEX, and Notices report generation** — Generate SBOMs (with
  template selection), VEX reports, and basic notices reports for scanned
  projects.
- **Vulnerability triage and remediation** — Ignore or triage CVEs/BDSAs,
  and upgrade vulnerable components directly using the project-version-level
  API.
- **Policy violation summary** — Retrieve and review policy violations with
  remediation suggestions based on criticality.
- **Project and version search** — Search for existing projects using
  package manager or git metadata.
- **Source, binary, container, and SBOM scanning** — Run scans, check scan
  status, and match code snippets.
- **Dashboard summary** — View instance-wide security posture, activity
  trends, and vulnerability breakdowns.

For full installation, configuration, and troubleshooting details, see the [Black Duck SCA MCP Server documentation](https://docs.blackduck.com/access?ft:originId=739f91b516f72427ad6a9b76240ff744/0da74b147b2cfd3da7ebbcd0a376814f.topic).

## Custom component vulnerability association Using CPEs

Custom component versions can now be associated with vulnerabilities using Common
Platform Enumeration (CPE) identifiers. When a valid CPE 2.3 value is assigned to a
custom component version, Black Duck SCA displays associated
vulnerabilities on a dedicated Vulnerabilities tab and includes them in BOM risk
calculations, policy evaluation, notifications, and reports. This helps
organizations better manage vulnerability risk for commercial, proprietary,
internal, or otherwise non-KnowledgeBase components.

## VEX export templates

Create and manage VEX templates to control the content of CSAF 2.0 (VEX) reports.
Templates are configured under the renamed **SBOM and VEX Templates** page
(Manage > SBOM and VEX Templates), which now contains separate tabs for SBOM and VEX
templates.

**What's new:**

- Reusable VEX templates with configurable fields: Legal Disclaimer, TLP
  Designation, Subprojects Vulnerabilities, Comments, and Vulnerability Type
  (CVE, BDSA, EUVD)
- VEX Template dropdown added to the report generation dialog
- Pre-configured System template included out of the box
- VEX Templates tab visible when the VEX module is enabled in your license

## KnowledgeBase support bundle generation

You can now generate a KnowledgeBase (KB) support bundle directly from the BOM and
the Match Review page. When you encounter discrepancies in component identification,
licensing, or vulnerability data, select one or more components and choose
**Generate Support Bundle**. The bundle collects all relevant component data
— including match details, license information, vulnerability data, and optionally
BDIO files — into a downloadable `.zip` file that you can attach to a
support case. This eliminates the manual back-and-forth of gathering diagnostic
information and helps the support team investigate issues more efficiently.

## EUVD vulnerability identifiers now included in SBOM reports

SBOM reports now include EUVD (European Vulnerability Database) identifiers alongside
CVE and BDSA identifiers, supporting Cyber Resilience Act (CRA) compliance
requirements. EUVD data appears in CycloneDX (all versions) and SPDX 3.0
reports.

Existing SBOM export templates will have EUVD enabled automatically after upgrading
to 2026.7.0.

SPDX 2.x reports are not affected by this change.

## Configurable retention for New Vulnerabilities data

Administrators can now configure retention for **New Vulnerabilities** data. The
new option in **Admin > System Settings > Data Retention** allows you to specify
a retention period of **7 to 30 days**, with a default of **10 days**.

The configured retention period also determines the amount of historical data
available through the date range filter on the **New Vulnerabilities**
dashboard.

## Vulnerability sub-status support in policy rules

You can now create more granular policy rules using vulnerability sub-statuses. When
configuring a Vulnerability Condition with a Remediation Status of **Known
Affected** or **Known Not Affected**, you can optionally specify a
sub-status to narrow the policy evaluation.

Available sub-statuses for Known Affected: Mitigation, No Fix Planned, None
Available, Vendor Fix, Workaround.

Available sub-statuses for Known Not Affected: Component Not Present, Vulnerable Code
Not Present, Vulnerable Code Cannot be Controlled by Adversary, Vulnerable Code Not
in Execute Path, Inline Mitigations Already Exist.

If no sub-status is selected, the policy evaluates against the status alone (matching
existing behavior). Existing policy rules are unaffected by this change.

## AI-assisted documentation search

Black Duck SCA 2026.7.0 introduces an AI-assisted documentation
search experience that helps users quickly find relevant documentation directly from
within the application.

- Access AI-assisted documentation search from the Help menu without leaving
  Black Duck SCA.
- Improve documentation discovery with AI-powered search capabilities designed
  to return more relevant results.
- System Administrators can enable or disable the AI-Assisted Documentation
  Service from **Admin → System Settings → System → Help**. The service is
  enabled by default.
- When enabled, documentation search requests are processed by an external
  cloud-based service to provide AI-assisted search functionality.
  Organizations that do not want documentation search requests processed
  externally can disable the service and continue using the legacy
  documentation experience.
- Air-gapped deployments continue to use the legacy documentation experience
  and are not affected by this feature.

## Centralized component catalog (Phase 1)

Black Duck SCA 2026.7.0 introduces a centralized component
catalog that normalizes component, component version, component origin, and
vulnerability data into shared local database tables. This architectural improvement
reduces the number of API requests made to KnowledgeBase services during BOM
computation and KB update processing.

Customers can expect:

- **Faster BOM computation** — Component and vulnerability data is now
  cached locally, reducing round trips to the KnowledgeBase. Since most scans
  are rescans, the required data will typically already be present in the
  local catalog.
- **More reliable scan processing** — Fewer external KB API calls during BOM
  computation means fewer scan failures caused by KB connectivity or
  availability issues.
- **Faster and more reliable KB updates** — Data normalization allows the KB
  update job to process component and vulnerability updates more
  efficiently.
- **Reduced network egress** — Individual Black Duck SCA deployments will make fewer API requests to KB API services for
  components, versions, origins, and mapped vulnerabilities, reducing network
  egress costs.

There are no changes to the user interface, public APIs, or existing workflows. All
BOM computation results, component data, vulnerability data, policy evaluations, and
SBOM exports remain functionally identical.

**Note:** The database migration that runs during the upgrade to 2026.7.0 moves
component data into centralized catalog tables. Depending on the size of your
database, this migration may extend the upgrade window. Plan accordingly.

## Updated BDSA auto-remediation behavior

BDSA auto-remediation no longer supports “apply” functionality. End-users may still
enable or disable BDSA auto-remediation but it will only apply for following scans
and changes.

## Minimum supported browser versions

- Safari Version 17.6
- Chrome Version 127 (x86_64)
- Firefox Version 128 (64-bit)
- Microsoft Edge Version 127 (64-bit)

## Container versions

- blackducksoftware/blackduck-postgres:16-2.9
- blackducksoftware/blackduck-postgres-upgrader:16-1.4
- blackducksoftware/blackduck-postgres-waiter:1.0.21
- blackducksoftware/blackduck-cfssl:1.0.38
- blackducksoftware/blackduck-nginx:2026.7.0
- blackducksoftware/blackduck-logstash:1.0.47
- blackducksoftware/bdba-worker:2026.6.1
- blackducksoftware/rabbitmq:1.2.50
- blackducksoftware/blackduck-authentication:2026.7.0
- blackducksoftware/blackduck-bomengine:2026.7.0
- blackducksoftware/blackduck-documentation:2026.7.0
- blackducksoftware/blackduck-integration:2026.7.0
- blackducksoftware/blackduck-jobrunner:2026.7.0
- blackducksoftware/blackduck-redis:2026.7.0
- blackducksoftware/blackduck-registration:2026.7.0
- blackducksoftware/blackduck-scanmatch:2026.7.0
- blackducksoftware/blackduck-storage:2026.7.0
- blackducksoftware/blackduck-webapp:2026.7.0
