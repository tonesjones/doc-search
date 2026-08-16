---
title: "New and Changed Features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "_lZotlD0QKUrrOmupkfXAw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:09.708328+00:00"
---

# New and Changed Features

## Preserve Component Relationships on SBOM Import

Black Duck SCA now preserves component relationships when importing
SBOM reports, supporting compliance with CISA SBOM minimum requirements. This
feature retains dependency information from SPDX v2 and v3 SBOMs, enabling accurate
reproduction of relationships in exported reports and supporting enhanced
vulnerability and license analysis.

## New Footer Helper Bar

Black Duck SCA now includes a default footer helper bar that provides
users with quick access to essential support resources. This enhancement improves
user accessibility by offering convenient links to key services directly from the
interface:

- **Community Portal**: Easy access to the Black Duck community for
  collaboration and knowledge sharing.
- **Share an Idea**: Quick link for users to submit feature requests and
  suggestions.

The footer is automatically added to new installations and upgrades that do not have
existing footers, ensuring minimal disruption to current configurations.

## Updated Functionality for Project Version Data Retention

In this release, we have enhanced the Project Version Auto-Deletion feature, now
named Project Version Auto Actions, to provide users with greater control over
managing project versions. Key updates include:

- **Automatic Progression to LTS**: Users can now configure project versions to
  automatically transition to Long-Term Support (LTS) status, ensuring that critical
  versions receive ongoing maintenance and security updates.
- **Updated UI**: The user interface has been updated to simplify the
  configuration process for these actions, making it more intuitive for users
  to set up automatic progression and deletion of project versions.

## New Younger Than Operator for Components

A new date age operator, **"younger than,"** has been added to the **Component
Release Age** and **Vulnerability Published Age** expression types. This
operator allows users to identify components with release dates that are younger
than a specified number of days (e.g., finding components released within the last
30 days):

- If a component is found to be in violation due to this operator, it will not
  automatically transition to **NOT_VIOLATION** status. The violation status
  will remain until a new scan or relevant BOM computation occurs.
- The minimum user value for this operator is set to 3 days, as rules to find
  components with release dates before now are not supported.

## Updated Component Version Overview

We have made significant improvements to the Component Version Overview in the user
interface. The layout has been updated to provide a more intuitive and streamlined
experience.

- **New Layout:** The updated design enhances usability, making it easier to
  navigate and access important information about component versions.
- **Improved Information Display:** Key details are presented more clearly,
  allowing users to quickly find relevant data such as descriptions, known
  vulnerabilities, and associated licenses.
- **Enhanced User Experience:** The overall user experience has been
  improved, ensuring that users can efficiently manage and review component
  information.

## Enhanced Bitbucket Data Center Onboarding

The user interface has been updated to allow for Bitbucket Data Center (BBDC) to
onboard SCM projects in alignment with other workflows. This enhancement ensures
that the existing workflow for BBDC now looks and operates similarly to other SCM
options:

- Users can select one or multiple repositories for scanning on the same
  page.
- The scanning process will create a project for the selected repository.
- Users can delve into the project to find Bill of Materials (BOMs).
- The option to select other versions of the repository is now available, enabling
  users to initiate additional scans and retrieve BOMs.

This update streamlines the onboarding process for Bitbucket Data Center, providing a
consistent experience across all SCM providers.

## Support for Additional Image Formats in Logo Customization

We have enhanced the logo customization feature to support additional image formats.
Users can now upload logos in various formats, including PNG, GIF, SVG, WEBP, JPEG,
and AVIF.

## Removal of Edit Feature for User Access Tokens

In this release, the edit feature for user access tokens has been removed. This
change addresses security concerns associated with storing newly generated access
tokens in plaintext, which can lead to poor security practices.

Access tokens are intended for single use upon generation, and users are encouraged
to create new tokens as needed rather than copying and pasting existing ones.
Inactive tokens will be purged, ensuring better management of access
credentials.

## Enhancement to External Link Confirmation UI Workflow

We have improved the external link confirmation workflow to enhance user experience.
Previously, users were required to dismiss the confirmation popup every time they
clicked an external link, even when the full URL was displayed.

**Key Changes:**

- The confirmation modal now appears only when the link text does not match the
  actual URL, ensuring transparency about the link's destination.
- The confirmation modal will close automatically after the user clicks "Confirm,"
  streamlining the process.

## Removal of SCASS Enablement Documentation

The documentation page describing how to manually enable SCASS has been removed. This
information is now outdated, as customers can no longer enable SCASS themselves.
SCASS enablement is now handled entirely through the customer’s registration key,
and no configuration file changes are required. Customers who wish to enable SCASS
or need guidance regarding their SCASS eligibility should contact Support for
assistance.

## Minimum supported browser versions

- Safari Version 17.1
- Chrome Version 119 (x86_64)
- Firefox Version 119 (64-bit)
- Microsoft Edge Version 119 (64-bit)

## Container versions

- blackducksoftware/blackduck-postgres:16-2.6
- blackducksoftware/blackduck-postgres-upgrader:16-1.2
- blackducksoftware/blackduck-postgres-waiter:1.0.19
- blackducksoftware/blackduck-cfssl:1.0.35
- blackducksoftware/blackduck-nginx:2026.1.0
- blackducksoftware/blackduck-logstash:1.0.45
- blackducksoftware/bdba-worker:2025.12.1
- blackducksoftware/rabbitmq:1.2.49
- blackducksoftware/blackduck-authentication:2026.1.0
- blackducksoftware/blackduck-bomengine:2026.1.0
- blackducksoftware/blackduck-documentation:2026.1.0
- blackducksoftware/blackduck-integration:2026.1.0
- blackducksoftware/blackduck-jobrunner:2026.1.0
- blackducksoftware/blackduck-redis:2026.1.0
- blackducksoftware/blackduck-registration:2026.1.0
- blackducksoftware/blackduck-scanmatch:2026.1.0
- blackducksoftware/blackduck-storage:2026.1.0
- blackducksoftware/blackduck-webapp:2026.1.0
