---
title: "New and changed features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "bIps9zDXfC1wXsjx5g7rxw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:20.947825+00:00"
---

# New and changed features

## AI Model Support in Bill of Materials

Black Duck now supports the addition of AI models to your Bill
of Materials (BOM) as part of the Black Duck Supply Chain Edition, enabling
comprehensive tracking and management of artificial intelligence components within
your projects. This new feature allows organizations to maintain visibility into
their AI model usage alongside traditional software components.

Key capabilities include:

- Manual addition and editing of AI models to your BOM with detailed metadata
- Filtering and search options to quickly identify AI models within large
  BOMs

Note: This feature is currently available only for hosted customers, as it requires
signature scans to be processed through the SCA Scan Service (SCASS).

To use this feature, ensure your product registration has the AI Model Scanning
feature enabled and run Detect scans with the parameter
`--detect.blackduck.signature.scanner.individual.file.matching=ALL`.

This enhancement helps organizations address the growing need to track AI components
as part of their software supply chain management and compliance processes.

## New BDSA Rapid Review tag

With the introduction of AI assistance for generating fully automated BDSAs without
human research, we have introduced a new BDSA tag called "Rapid Review." This tag
alerts users to potential vulnerabilities identified through our automated
vulnerability process, which was partly developed in response to the need for timely
reporting of Linux Kernel vulnerabilities.

You will find the Rapid Review tag in all areas where other vulnerability tags are
found:

- Project and vulnerability pages
- Support on the Find page
- Conditions for policy violations
- Filter conditions for the vulnerabilities page

## New Vulnerabilities Dashboard

Black Duck SCA 2025.10.0 introduces the New Vulnerabilities
Dashboard, which provides users with an enhanced view of vulnerabilities detected
within their projects. This dashboard features a comprehensive overview of new
vulnerabilities, allowing users to filter by timeframe and access detailed
information about affected projects. With an intuitive layout and graphical
summaries of vulnerabilities by severity, the New Vulnerabilities Dashboard
streamlines the vulnerability management process, making it easier for users to
prioritize remediation efforts.

## New Component search functionality for LTS Projects

We have introduced the ability to search for components within Long-Term Support
(LTS) project versions in Black Duck SCA. Customers can now perform
the same search capabilities for components in LTS projects as they can for active
projects.

When searching for components, the results will now include relevant LTS project
versions, ensuring that all affected components are considered in your queries. This
enhancement aims to improve the effectiveness of component management across
different project types.

## New Vulnerability Exploitability eXchange (VEX) Reports

The new Vulnerability Exploitability eXchange (VEX) reports are now available in Black Duck SCA as part of the Black Duck Supply Chain Edition. These
reports provide a standardized method for communicating the exploitability status of
vulnerabilities associated with your products.

Users can generate VEX reports in the CSAF 2.0 (Profile 5) format, which includes key
metadata such as the CVE ID (if available), BDSA ID, and vulnerability ratings. The
reports will only include vulnerabilities that are relevant, filtering out those
marked as Duplicate, Ignored, or New.

VEX reports can be generated through the user interface or via API, allowing for
flexibility in accessing vulnerability information. This feature aims to help
organizations communicate security risks more effectively and enhance their
vulnerability management processes.

To take advantage of this new report, ensure your product registration has the
Vulnerability Exploitability eXchange (VEX) feature enabled.

## Enhanced Vulnerability Information in SBOM Reports

Black Duck now provides enhanced vulnerability information in
both SPDX 3 and CycloneDX SBOM reports, enabling more comprehensive security
insights for stakeholders. This update filters out vulnerabilities with "Duplicate,"
"Ignored," or "New" remediation statuses, ensuring reports focus on the most
relevant security information.

For CycloneDX reports, we've added detailed vulnerability ratings with scoring
methods and vectors, Common Weakness Enumeration (CWE) listings, and analysis
information including state, justification, and response details. SPDX 3 reports now
include vulnerability classes with CVE or BDSA IDs, CVSS assessment relationships
across multiple versions, and specific vulnerability remediation
representations.

These improvements align with industry standards and help organizations provide more
detailed security context in their software supply chain documentation.

## Update to SPDX License Handling in BD SBOMs

We have updated the license handling for Black Duck SBOMs to
ensure compliance with the latest SPDX license identifiers. With this change, if a
license ID in the SBOM is not part of the supported license list, it will be treated
as a custom license, requiring a license reference and inclusion of the full license
text. This enhancement is designed to prevent failures during SBOM validation.

Both CycloneDX and SPDX rely on the license identifiers defined in the [SPDX
License List](https://spdx.org/licenses/index.html). It is important to note that, following the transition from
SPDX 2.3 to SPDX 3.0, several license formats were changed, and some licenses were
marked as deprecated. While these deprecated licenses currently result in warnings
but are still processed as valid SBOMs, they may be removed in future updates,
leading to invalid SBOMs.

This update reinforces our commitment to maintaining the integrity and compliance of
SBOMs within Black Duck SCA.

## UX/UI Enhancements to Project Settings/Details Page

The Project Settings/Details page has been significantly improved with several user
experience enhancements designed to streamline navigation and configuration:

- **Reorganized Layout:** Straightforward project details (such as Name and
  Description) are now separated from more advanced features (such as Custom
  Scan Signature), creating a more intuitive workflow.
- **Enhanced Documentation:** "Learn More" links have been added throughout
  the settings and options, providing immediate access to relevant
  documentation and guidance.
- **Improved Text and Instructions:** UI text and explanations have been
  revised for clarity, making it easier to understand available options and
  their implications.
- **Refined Visual Elements:** Updates to layout, alignment, spacing, and
  behavior create a more consistent and polished interface, improving overall
  usability.

These enhancements aim to streamline project management and make configuration more
accessible for both new and experienced users.

## LTS BOM Count in Export CSV Reports

A new "LTS BOM Count" column has been added to the Export CSV report available on the
Find → Vulnerabilities page. This enhancement allows users to easily track the
number of Long-Term Support (LTS) Bill of Materials (BOM) components associated with
identified vulnerabilities. By including the LTS BOM Count in the exported reports,
users can gain better insights into their LTS components and enhance their
vulnerability management processes.

## Minimum supported browser versions

- Safari Version 17.1
- Chrome Version 119 (x86_64)
- Firefox Version 119 (64-bit)
- Microsoft Edge Version 119 (64-bit)

## Container versions

- blackducksoftware/blackduck-postgres:16-2.5
- blackducksoftware/blackduck-postgres-upgrader:16-1.1
- blackducksoftware/blackduck-postgres-waiter:1.0.18
- blackducksoftware/blackduck-cfssl:1.0.34
- blackducksoftware/blackduck-nginx:2025.10.0
- blackducksoftware/blackduck-logstash:1.0.45
- blackducksoftware/bdba-worker:2025.9.1
- blackducksoftware/rabbitmq:1.2.48
- blackducksoftware/blackduck-authentication:2025.10.0
- blackducksoftware/blackduck-bomengine:2025.10.0
- blackducksoftware/blackduck-documentation:2025.10.0
- blackducksoftware/blackduck-integration:2025.10.0
- blackducksoftware/blackduck-jobrunner:2025.10.0
- blackducksoftware/blackduck-redis:2025.10.0
- blackducksoftware/blackduck-registration:2025.10.0
- blackducksoftware/blackduck-scanmatch:2025.10.0
- blackducksoftware/blackduck-storage:2025.10.0
- blackducksoftware/blackduck-webapp:2025.10.0
