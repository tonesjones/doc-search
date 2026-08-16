---
title: "New and changed features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "746OmZTOT0OfBBL_qKFUGg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:28.391875+00:00"
---

# New and changed features

## **New integration support for GitHub App**

Black Duck now supports integration with the new GitHub App, a
new SCM onboarding application designed to simplify and automate the process of
connecting GitHub to Black Duck. Once integrated, the GitHub
App performs scans and send results directly to Black Duck,
enabling streamlined onboarding and centralized visibility into open source risk.
For setup details and configuration guidance, see [GitHub App Integration Guide](https://docs.blackduck.com/p/bridgeintegrations).

## Added support for SPDX v3.0

Black Duck now supports both importing and exporting Software
Bill of Materials (SBOMs) in the SPDX v3.0 format. This allows greater compatibility
with modern tooling and enhanced SBOM data structure support.

For more information about the SPDX v3.0 specification, visit the [SPDX v3.0 reference page](https://spdx.github.io/spdx-spec/v3.0/).

## Added support for SBOM Type field in SBOM reports

Black Duck SBOM reports now include a new SBOM Type field that
identifies the phase of the software lifecycle the SBOM represents. Supported values
are `Design`, `Source`, `Build`,
`Analyzed`, `Deployed`, and
`Runtime` in alignment with guidance from CISA's SBOM
documentation.

This enhancement improves the clarity and traceability of SBOMs by helping consumers
understand the context and completeness of the data provided.

## New Component Hash support added to SBOMs

Black Duck SBOMs now support a new Component Hash feature that
allows users to include a cryptographic identifier for components. When enabled in a
SBOM template, users can populate two new fields:

- Hash Value: A unique cryptographic hash value identifying the component's
  contents.
- Hash Algorithm: The algorithm used to compute the hash value (e.g., SHA-256).

This enhancement improves the traceability and supports integrity verification across
SBOMs.

## ReversingLabs Functionality Sunset

Support for ReversingLabs functionality has been fully removed from
Black Duck. The
includes removal of all previously deprecated features, APIs, and schema references
related to ReversingLabs. Any public ReversingLabs APIs that remain will now return
a `410 Gone` response or are marked as deprecated. As part of this
change, all documentation references have also been removed.

If you were using ReversingLabs integrations, we recommend reviewing your workflows
and transitioning to supported alternatives.

## Updated terminology from "Overall Roles" to "Global Roles"

To improve clarity and consistency across the product, all references to Overall
Roles have been updated to Global Roles. This change consolidates terminology and
better reflects the scope and function of these roles within Black Duck. Only the name has changed—role functionality and
permissions remain the same.

## Updated filter behavior to include LTS projects

The Affecting Projects filter on the Find → Vulnerabilities page has been updated to
include Long-Term Support (LTS) projects. When enabled, this filter now limits
results to vulnerabilities found in both Active and LTS projects, giving users a
more complete view of risks affecting supported versions.

## New file types supported for snippet scans

Black Duck now supports snippet scanning for Kotlin (.kt) and
Rust (.rs) files. These additions expand language coverage and improve
identification of code snippets during analysis. No configuration changes are
required—scans will automatically detect and process these file types.

## Accessibility improvements

This release introduces several updates aimed at enhancing the overall accessibility
and usability of Black Duck. These changes improve support for
assistive technology and align more closely with accessibility standards such as
WCAG.

- Improved Global Search → dropdown menu accessibility.
- Manage and Admin side menus can now be accessed via keyboard.
- Dropdown menus are now navigable by keyboard when expanded and closable when the Escape key. Focus remains within the menu component until it’s closed.
- Improved contrast ratio for scan error messages.
- Improved labeling for SBOM input fields to support better keyboard and screen reader navigation.

## Container versions

- blackducksoftware/blackduck-postgres:15-2.4
- blackducksoftware/blackduck-postgres-upgrader:15-2.6
- blackducksoftware/blackduck-postgres-waiter:1.0.18
- blackducksoftware/blackduck-cfssl:1.0.34
- blackducksoftware/blackduck-nginx:2025.7.0
- blackducksoftware/blackduck-logstash:1.0.43
- blackducksoftware/bdba-worker:2025.3.1
- blackducksoftware/rabbitmq:1.2.46
- blackducksoftware/blackduck-authentication:2025.7.0
- blackducksoftware/blackduck-bomengine:2025.7.0
- blackducksoftware/blackduck-documentation:2025.7.0
- blackducksoftware/blackduck-integration:2025.7.0
- blackducksoftware/blackduck-jobrunner:2025.7.0
- blackducksoftware/blackduck-matchengine:2025.7.0
- blackducksoftware/blackduck-redis:2025.7.0
- blackducksoftware/blackduck-registration:2025.7.0
- blackducksoftware/blackduck-scan:2025.7.0
- blackducksoftware/blackduck-storage:2025.7.0
- blackducksoftware/blackduck-webapp:2025.7.0
