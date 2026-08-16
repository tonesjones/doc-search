---
title: "Coverity 2024.12.1 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2024.12.1-release-notes.html"
content_id: "_tf8dsGt31cIzuCB4v55uQ"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:24.307487+00:00"
---

# Coverity 2024.12.1 Release Notes

## Important information for 2024.12.1

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

If you are upgrading a Coverity cloud deployment, refer to [Upgrading a Coverity cloud deployment](https://documentation.blackduck.com/bundle/coverity-docs/page/cnc/topics/upgrade-coverity.html) in the Coverity Cloud Deployment Administrator and User Guide. This document provides important information for administrators who are deploying or upgrading Coverity in a Kubernetes container environment.

## Coverity Platform 2024.12.1

This section provides release notes for Coverity Platform components.

### Coverity Connect 2024.12.1

#### Bug fixes

IM-31643
:   Reported in version: 2023.12.0
:   Configuration->Projects and Streams->Snapshots now correctly shows the date and time in the "time created" column for Chinese language users.

### Coverity Report Generators 2024.12.1

#### Bug fixes

RG-1916
:   Reported in version: unspecified
:   Black Duck Software Integrity Report now displays Top 40 CWE/SANS issues correctly.

RG-1920
:   Reported in version: 2024.6.0
:   Fixed an issue that caused report generation to fail due to the inability to invoke `com.coverity.ces.domain.StandardAttribute.getId()` when "definition" is null. Coverity can now generate a CVSS report without error.
