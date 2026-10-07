---
title: "EU-CRA support overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/eu-cra-support-overview.html"
content_id: "NuvRvhuufF2CXKtxMVUZQA"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:15.039965+00:00"
---

# EU-CRA support overview

Use Coverity to perform CRA-aligned analysis, review security-relevant findings, and
generate artifacts that support EU Cyber Resilience Act (EU-CRA) workflows.

Coverity provides CRA-aligned analysis, reporting, and disclosure capabilities that help
organizations analyze code, review security-relevant findings, and generate technical
evidence to support EU-CRA workflows.

Important: Coverity provides technical evidence and reporting capabilities.
Coverity does not certify EU-CRA compliance and does not provide legal or regulatory
advice.

## EU-CRA workflow

An EU-CRA workflow in Coverity can include the following steps:

- Perform analysis using CRA-aligned settings.
- Apply Checker Enforcement Policies to ensure that required analysis settings are
  used consistently.
- Review and prioritize issues by Security Impact classifications.
- Generate an EU-CRA report or CSAF/VEX report.
- Review and download generated artifacts.

For information about CRA-aligned analysis, see Configure CRA-aligned analysis.

For information about enforcing analysis settings, see Coverity Checker Policy Enforcement overview.

## Permissions

To generate and access EU-CRA artifacts, a user must have at least
one of the following permissions:

- Manage Stream
- Manage Project
- Triage Issue
- Manage Checker Policy

Users without one of these permissions cannot generate CRA artifacts.

Administrator users can generate and download EU-CRA artifacts
without additional permission assignments.

## Security Lenses and EU-CRA

Security Lenses use Security Impact classifications to help security practitioners
identify, review, and prioritize security-relevant issues.

EU-CRA workflows use Security Impact information when reviewing issues and generating
artifacts.

For more information, see Security Lenses overview.

## EU-CRA artifacts

Coverity can generate the following EU-CRA artifacts:

EU-CRA report
:   Provides human-readable technical evidence about the analysis
    configuration and the state of security-relevant issues. The report is
    generated as a ZIP archive containing PDF and HTML files.

    The EU-CRA report uses the following terminology:

    Security issue
    :   A security-relevant finding reported by Coverity for the
        analyzed snapshot.

    Security vulnerability
    :   A security issue that matches the configured CSAF/VEX scope and
        remains in the source code.

    Important: The report includes a checker table and a
    manual-verification reminder. Verify the checker list manually to
    determine whether it satisfies the required baseline settings.

CSAF/VEX report
:   Provides machine-readable vulnerability disclosure information for
    downstream security advisory and disclosure workflows. The report is
    generated as a JSON artifact.
