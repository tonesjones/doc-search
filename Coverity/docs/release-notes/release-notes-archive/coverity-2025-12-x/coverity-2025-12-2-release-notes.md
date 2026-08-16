---
title: "Coverity 2025.12.2 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2025.12.2-release-notes.html"
content_id: "bbp42pNJ2Tj643gYU2P3Ag"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:11.989366+00:00"
---

# Coverity 2025.12.2 Release Notes

## Important information for 2025.12.2

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

If you are upgrading a Coverity cloud deployment, refer to [Upgrading a Coverity cloud deployment](https://documentation.blackduck.com/bundle/coverity-docs/page/cnc/topics/upgrade-coverity.html) in the Coverity Cloud Deployment Administrator and User Guide. This document provides important information for administrators who are deploying or upgrading Coverity in a Kubernetes container environment.

## Coverity Platform 2025.12.2

This section provides release notes for Coverity Platform components.

### Coverity Connect 2025.12.2

#### New or changed features

COVDOCS-1977
:   For Coverity classic deployments, this release introduces a new Coverity Connect property that you must provide when using custom domains for storage service configurations. For further information, refer to the Use guide.

IM-33370
:   This release leverages PostgreSQL's contrib modules for significant performance improvements. The contrib package is a standard, production-recommended component of every PostgreSQL deployment and contains essential extensions used by most PostgreSQL applications.

    Important: While called "contrib," these are first-class PostgreSQL features maintained by the PostgreSQL core team, not third-party add-ons. They ship with every PostgreSQL release but require a separate package installation.

    This is not optional. The upgrade will fail without this extension - btree_gist.

    Industry standard: Major cloud providers (AWS, Azure, GCP) include all contrib modules by default because they're considered essential PostgreSQL functionality.

    Action Required: Install postgresql-contrib package before upgrading to 2025.12.1, if you missed or got the related error.

    Why: Contrib modules are industry-standard PostgreSQL components that enable critical functionality including the performance optimizations in this release.

    Time Required: 2-5 minutes installation + verification

    Risk of Skipping: Upgrade will fail without “btree_gist” etension. Issue query performance improvements will not be available.

#### Bug fixes

IM-32063
:   Reported in version: 2023.9.0
:   Ensure that file name event is properly shown and the file is also accessible for all the events.

IM-33162
:   Reported in version: 2024.12.0
:   Significant improvements to query performance have been made, enhancing the API's efficiency. A database upgrade is necessary to implement these changes alongside the product upgrade. See https://blackduck.atlassian.net/browse/IM-33370.

IM-33212
:   Reported in version: 2021.12.0, 2024.12.0
:   Fixed an issue with the Coverity Connect UI running slowly when clicking Outstanding Issues/High Impact Outstanding views.

IM-33512
:   Reported in version: 2025.9.0
:   Fixes an issue where the Projects & Streams section should only be listing the streams from the latest snapshot and not where the defect is already fixed.

IM-33617
:   Reported in version: 2025.12.0
:   Performance regressions may occur in certain query patterns due to changes in Hibernate 6.6’s SQL generation and parameter binding. These changes are intentional improvements for query plan caching and JDBC compliance but can negatively impact some scenarios.

IM-33620
:   Reported in version: 2025.12.0
:   We should support SAML Auth with both FQN (https://aws-igor.eng.aws.internal:2708) and without FQN https://aws-igor:2708 as supported prior to the 2025.12.0 release of Coverity Connect, before adding security enhancements. This fix will implement the same.

IM-33680
:   Reported in version: 2025.12.0
:   Fixed benign Log4j2 reconfiguration error messages that appeared during the schema upgrade phase on Linux platform upgrades.

IM-33724, IM-33805
:   Reported in version: 2025.12.0
:   Downgrade Hibernate to a stable version to avoid the hibernate-related regression issues caused after the Spring upgrade. This will fix the intermittent cache failures in the connect application.

IM-33772
:   Reported in version: 2025.12.0
:   Downgrade Hibernate to a stable version to avoid the hibernate related-regression issues caused after the Spring upgrade. This will fix the intermittent cache failures in the connect application.

### Coverity Report Generators 2025.12.2

#### Bug fixes

RG-1976
:   Reported in version: 2024.9.0, 2025.6.0, 2025.9.0
:   Fixed issue with MISRA rule descriptions containing unwanted tags.

## Coverity Analysis 2025.12.2

This section provides release notes for Coverity Analysis components.

### Coverity Checkers 2025.12.2

For a summary of checkers that have been added or changed in this release, refer to the "Coverity Checker Change History" table in the *Coverity Checker Reference*.

#### New or changed features

SATW-6806
:   Updated the Hyundai Rule MP-OOP-011 checker to flag violations only when a public method returns a handle to a private data member.

#### Bug fixes

SATW-6851
:   Reported in version: 2025.12.0
:   Updated the Misra C 2012 Rule 17.7 checker description to include function call details.

### Coverity Compilers and Capture 2025.12.2

#### Bug fixes

CAP-2597
:   Reported in version: 2025.12.0
:   Bazel arguments that include multiple `=` characters will no longer be parsed incorrectly when running `cov-build` with the `--bazel` argument.
