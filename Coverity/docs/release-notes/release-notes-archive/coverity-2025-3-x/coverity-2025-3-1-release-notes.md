---
title: "Coverity 2025.3.1 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2025.3.1-release-notes.html"
content_id: "WZxgrS1KRS7kcCrdgcJ4Gw"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:21.644237+00:00"
---

# Coverity 2025.3.1 Release Notes

## Important information for 2025.3.1

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

If you are upgrading a Coverity cloud deployment, refer to [Upgrading a Coverity cloud deployment](https://documentation.blackduck.com/bundle/coverity-docs/page/cnc/topics/upgrade-coverity.html) in the Coverity Cloud Deployment Administrator and User Guide. This document provides important information for administrators who are deploying or upgrading Coverity in a Kubernetes container environment.

## Coverity Analysis 2025.3.1

This section provides release notes for Coverity Analysis components.

### Coverity Analysis - General 2025.3.1

#### Bug fixes

CMPCPP-14942
:   Reported in version: 2024.9.0
:   Improved checker for MISRA C++ 2023 Rule 6.0.1 which reported a false positive when a template dependent type is used with direct list initialization.

CMPCPP-14958
:   Reported in version: 2024.9.0
:   Improved MISRA C++ 2023 Rule 6.4.1 checker fixing false positives related to variables hiding functions.

CMPCPP-14970
:   Reported in version: 2024.12.0
:   Fixed false positive for MISRA C++ 2023 Rule 0.2.1 where an object of a class with a user defined constructor or destructor is falsely reported as unused when it appears in a templated method or function.

SAT-46448
:   Reported in version: 2024.9.0
:   Misra CPP 2023 Rule 6.2.4 had an issue reporting certain cases of legitimate C++ NSDMI (Non-static data member Initialization). The issue has been fixed.

### Coverity Checkers 2025.3.1

For a summary of checkers that have been added or changed in this release, refer to the "Coverity Checker Change History" table in the *Coverity Checker Reference*.

#### New or changed features

SAT-46479
:   MISRA C++-2023 Rule 0.1.1 no longer reports on cases where the unused value comes from a non-static data member initializer.

SAT-46600
:   Lint annotations are no longer considered commented-out code for the purpose of rules such as MISRA C++-2023 Rule 5.7.2.

## Coverity Documentation 2025.3.1

This section provides release notes for Coverity Documentation components.

### Coverity Documentation 2025.3.1

#### Bug fixes

COVDOCS-1689
:   Reported in version: 2024.12.0
:   In the document, *Coverity Cloud Deployment Administrator and User Guide*, in the chapter, *Sizing a Coverity Connect (cim) pod for optimum performance*, added the following note to clarify `cim` pod resource applicability:
    Important: In a deployment with multiple Coverity Connect (`cim`) pods, the resource guidance applies equally to all pods deployed. Provide the full resources for each pod that you deploy; do not split up calculated CPU and memory resources between pods.

COVDOCS-1729
:   Reported in version: unspecified
:   In the document, *Coverity Cloud Deployment Administrator and User Guide*, in the chapter, *Sizing a Coverity Connect (cim) pod for optimum performance*, added the following note in several places:
    Important: Do not enable TLS sidecar if you are deploying only Connect (not deploying Scan Service).

COVDOCS-1733
:   Reported in version: 2024.9.0
:   In the document, *Coverity Cloud Deployment Administrator and User Guide*, in the chapter, *Troubleshooting*, added the new section, *NGINX HTTP error 504: Gateway Timeout*, that describes how to resolve and prevent NGINX HTTP error 504 occurrences. For further database management, consolidated all PostgreSQL information in the chapter, *PostgreSQL databases and PostgreSQL pod*, and enhanced the section, *Managing Connect PostgreSQL databases*.

COVDOCS-1745
:   Reported in version: 2025.3.0
:   In the document, *Coverity Cloud Deployment Administrator and User Guide*, removed obsolete maximum resource guidance from the sections, *PostgreSQL pod minimum resource requirements* and *Coverity Connect (cim) pod minimum resource requirements*.
