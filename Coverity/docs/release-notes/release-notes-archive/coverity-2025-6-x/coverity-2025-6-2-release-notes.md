---
title: "Coverity 2025.6.2 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2025.6.2-release-notes.html"
content_id: "y2K~8ws82B353cULpgse0g"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:18.937222+00:00"
---

# Coverity 2025.6.2 Release Notes

## Important information for 2025.6.2

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

If you are upgrading a Coverity cloud deployment, refer to [Upgrading a Coverity cloud deployment](https://documentation.blackduck.com/bundle/coverity-docs/page/cnc/topics/upgrade-coverity.html) in the Coverity Cloud Deployment Administrator and User Guide. This document provides important information for administrators who are deploying or upgrading Coverity in a Kubernetes container environment.

## Coverity Platform 2025.6.2

This section provides release notes for Coverity Platform components.

### Coverity Connect 2025.6.2

#### Bug fixes

CNC-4047
:   Reported in version: 2024.9.0
:   There is no change in the application features.

CNC-4064
:   Reported in version: 2024.9.0
:   Fixed performance issues of the updateUser API.

IM-32089
:   Reported in version: 2023.12.2
:   Fixed issues with source code display after XREF linksets was enabled.

## Coverity Analysis 2025.6.2

This section provides release notes for Coverity Analysis components.

### Coverity Analysis - General 2025.6.2

#### Bug fixes

CMPCPP-15213
:   Reported in version: unspecified
:   Fixed FP for MISRA C++ 2023 Rule 6.4.1 in lambda expressions.

CMPCPP-15216
:   Reported in version: 2025.3.0
:   Fixed FP on MISRA C++2023 Rule 6.4.3 for unqualified name lookup when dependent base does not define symbol.

### Coverity CLI 2025.6.2

#### Bug fixes

COVCLI-3968
:   Reported in version: 2025.6.0
:   Stream names containing certain special characters, such as "[", "]", and ";", were causing Coverity CLI scans to fail. This has now been corrected.

### Coverity Checkers 2025.6.2

For a summary of checkers that have been added or changed in this release, refer to the "Coverity Checker Change History" table in the *Coverity Checker Reference*.

#### Bug fixes

SATW-6585
:   Reported in version: 2024.12.0
:   Fixed FP for MISRA C++ 2023 Rule-16.6.1

### Coverity Compilers and Capture 2025.6.2

#### Bug fixes

CMPCPP-15122, CMPCPP-15176
:   Reported in version: 2025.3.0
:   Fixed sometimes incorrectly issued error "empty initializer not allowed here" for C++ compilations.

CMPCPP-15265
:   Reported in version: 2025.6.0
:   Fixed a compilation error in cov-emit when using the flag /utf-8 with MSVC mode.

## Coverity Documentation 2025.6.2

This section provides release notes for Coverity Documentation components.

### Coverity Documentation 2025.6.2

#### Bug fixes

COVDOCS-1701
:   Reported in version: unspecified
:   In the _Coverity Cloud Deployment Administrator and User Guide, created a new comprehensive chapter "Managing container images" that consolidates information on managing container images, and documents procedures to set up either your own private registry (recommended) or use the Black Duck private registry as the source for container images during deployment.

COVDOCS-1704
:   Reported in version: unspecified
:   In the *Coverity Cloud Deployment Administrator and User Guide*, fixed typo instances where the `scan-services` Helm subchart was labeled `scan.services`. Using this name with a '.' can cause scan-services deployment to fail. Also changed a `storage.service` instance to `storage-service`.

COVDOCS-1807
:   Reported in version: unspecified
:   In the *Coverity Cloud Deployment Administrator and User Guide*, reviewed Helm chart and code examples for YAML indentation and syntax issues and fixed as needed. Used the YAML 2-space indent standard.
