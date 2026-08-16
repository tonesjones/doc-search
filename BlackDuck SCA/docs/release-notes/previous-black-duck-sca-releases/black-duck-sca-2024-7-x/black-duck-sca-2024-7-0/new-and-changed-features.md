---
title: "New and changed features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "Oa6rxbEsnjVHvjl8xKSIoQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:08.333802+00:00"
---

# New and changed features

## What's New window

Discover the latest features and enhancements introduced in the current Black Duck
release with the new What's New window. After an upgrade, the What's New window will
appear upon login, highlighting the most impactful updates in this version.

Users can choose to disable this window for future logins, but it will reappear with
the next Black Duck server upgrade. Even after being dismissed, the
What's New content can be accessed under the Help menu. All major versions of Black Duck from 2024.7 onward will include What's New content.

## New Long-Term Support (LTS) feature

Long-Term Support (LTS) project versions enable tracking of vulnerability data for
released product versions. LTS projects are intended for software already in use by
end users or customers. Designed with scalability in mind, LTS projects can support
extremely high volumes of project versions.

LTS project versions retain minimal data from Active project versions, focusing on
tracking newly discovered vulnerabilities in the components within the LTS Bill of
Materials (BOM). When converting an Active version to LTS, a Software Bill of
Materials (SBOM) is automatically created to facilitate sharing with required third
parties. While LTS version do not currently support notifications, they will receive
new vulnerability data as it is published to the Black Duck KnowledgeBase.

## New BDSA AI Assisted tag

A new mechanism has been introduced to automate the creation of BDSAs using AI models
and have introduced an “AI Assisted” BDSA tag. AI Assisted Security Advisories are
automatically created by Black Duck's Cyber Security Research
Center using automated AI tools. These BDSAs have not been independently verified by
the BDSA team but are created using automated processes and Generative AI
assistance. These advisories are designed to supplement the BDSAs identified and
verified by our Cyber Security Research Center.

You will find the AI Assisted tag in all areas where other vulnerability tags are
found:

- As a filter on the Find page for vulnerabilities
- As a filter a project version's Security page
- As a Vulnerability condition for policies

## New internal SSL certificate expiration alert

Black Duck 2024.7.0 introduces a new internal SSL certificate
expiration alert. This alert notifies users 30 days in advance when their internal
SSL certificates are approaching their expiration date, ensuring timely renewals and
uninterrupted secure connections.

## New SBOM retention configuration

When customers generate an SBOM that is meant to be distributed, it's important that
an SBOM management solution retains the SBOM so it can be reproduced if needed. This
is different than other type of Black Duck reports and while it
typically happens as part of the release process at a point in time when no further
changes are expected to the BOM, that’s not always the case.

Using this new feature, you can now configure the retention period for project
version SBOM reports for both standard and LTS projects.

The SBOM retention settings can be configured in Admin → System Settings → Data
Retention → SBOM Retention.

## New option to filter indirect dependencies in SBOM templates

The SBOM Template now has an option to only include direct dependencies of components
or components with no dependencies in the SBOM. This option can be found at the
bottom of the Component Data section of the SBOM Templates page. The default state
is unchecked and applies to both CycloneDX and SPDX report types. If unchecked, all
components in the BOM are included.

Note: This information may only be available for certain components.

## Improved copyright handling in reports

Black Duck 2024.7.0 brings significant improvements to the way
copyrights are handled in SBOM and Notices File reports. Changes include:

- Enhancements to the algorithm used create lists of copyrights. The new
  algorithm will include previously missed copyrights, remove comment
  characters and make the entries more readable by replacing escaped character
  codes with real characters.
- Copyright lists which are now sorted alphabetically and removal of duplicate
  entries from the lists.
- More customizations for the Notices File report, including the ability to
  exclude license text and license data. The Notice File report now also
  includes a section displaying the selected options used when generating the
  content.
- A new Copyrights page in the Systems Settings which allows you to configure
  global copyright settings for SBOM and Notice File reports. Options include
  the ability to merge identical copyrights with different dates, remove
  copyright statements that do not include a date, or use a standard copyright
  tag.

## Improved Notices File report

The Notice File report has been enhanced with the addition of home page URLs and
clearer details when pertaining to components without a copyright. Starting in
2024.7.0, components without copyrights will display "No Copyrights found".

## Binary matching for versionless components via fuzzy match

Binary Matching introduces new capabilities into Black Duck
for identifying component versions from binary scans. This technique leverages a new
SaaS matching service for binary scanning, identifying the closest component version
match or matches when an exact match is not found through binary analysis. Match
scores for component versions range from 4 (lowest score) to 100 (highest
score).

This update also adds support for fuzzy match APIs. Binary matches that utilize fuzzy
match component versions will show their respective match score and how many
alternative matches were found. The scoring formula is sophisticated and further
enhancements to this matching process will be implemented as part ongoing
KnowledgeBase improvements along with ways to highlight the best possible match on
the BOM.

## Updated maximum binary scan size

We have increased the maximum size of binaries that can be scanned from 5GB to 20GB.
This change addresses security restrictions in the Black Duck
hosted environment, ensuring we maintain robust security while allowing the scanning
of larger binaries.

## Updated scan BOM Import Log

We have optimized the BOM Import Log for better performance and reduced storage
costs:

- Records of missing, not found, or mapped licenses will no longer be recorded
  in the BOM import log.
- Only the most recent BOM import log will be retained.

These improvements streamline the logging process and focus on the most relevant
data, ensuring a more efficient use of resources.

## Updated project creation process

The project creation process has been updated as follows:

- If SCM Integration is not enabled on your server, clicking the Create
  Project button brings you directly to the create project form. There is
  no change in this circumstance.
- If SCM Integration is enabled, clicking the Create Project button now
  shows a dropdown with the options, Standard Project and SCM Project.
  Clicking Standard Project will bring the user to the create project
  form. While clicking SCM Project will bring the user to the SCM Server
  selection page.

## Updated `component_vulnerability` table in the Reporting view

A new `remediation_updated_at` field has been added to the
`component_vulnerability` table. This field records the date when
the triage status of a vulnerability was last updated.

## Binary scans migration to protobuf format

Traditional jsonid binary scans have been migrated to protobuf format introduced in
2023.10.0 for all scans with BDBA. No action is required to update your environment
due to this migration, and scan results will remain unaffected.

## Added SBOM fields to project settings and components

The following SBOM fields have been added:

- Originator: Projects, BOM Components
- Download Location: Component Version, Custom Component Version

## Added macOS ARM64 support for Signature scanner

The Signature scanner now supports macOS ARM64. This update ensures compatibility
across Black Duck products, providing improved performance and
seamless operation for ARM64-based systems.

## Removal of the "IN" operator for specified policy rule conditions

The following policy rule conditions no longer allow the “IN” operator. This change
applies only on new and updated policy rules. Existing policies are not
affected.

- New Versions Count
- Critical Severity Vulnerability Count
- High Severity Vulnerability Count
- Medium Severity Vulnerability Count
- Low Severity Vulnerability Count

## Supported browser versions

- Safari Version 17.5

  - Safari versions 14 and below are no longer supported
- Chrome Version 126.0.6478.127 (Official Build) (x86_64)

  - Chrome versions 91 and below are no longer supported
- Firefox Version 128.0 (64-bit)

  - Firefox versions 89 and below are no longer supported
- Microsoft Edge Version 123.0.2420.97 (Official build) (64-bit)

  - Microsoft Edge versions 91 and below are no longer supported

## Container versions

- blackducksoftware/blackduck-postgres:14-1.25
- blackducksoftware/blackduck-postgres-upgrader:14-1.4
- blackducksoftware/blackduck-postgres-waiter:1.0.13
- blackducksoftware/blackduck-cfssl:1.0.28
- blackducksoftware/blackduck-nginx:2024.7.0
- blackducksoftware/blackduck-logstash:1.0.38
- blackducksoftware/bdba-worker:2024.6.2
- blackducksoftware/rabbitmq:1.2.39
- blackducksoftware/blackduck-authentication:2024.7.0
- blackducksoftware/blackduck-bomengine:2024.7.0
- blackducksoftware/blackduck-documentation:2024.7.0
- blackducksoftware/blackduck-integration:2024.7.0
- blackducksoftware/blackduck-jobrunner:2024.7.0
- blackducksoftware/blackduck-matchengine:2024.7.0
- blackducksoftware/blackduck-redis:2024.7.0
- blackducksoftware/blackduck-registration:2024.7.0
- blackducksoftware/blackduck-scan:2024.7.0
- blackducksoftware/blackduck-storage:2024.7.0
- blackducksoftware/blackduck-webapp:2024.7.0
