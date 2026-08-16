---
title: "Coverity 2024.9.1 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2024.9.1-release-notes.html"
content_id: "EB3K__PxsE6Fs5JTeNrW2A"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:27.195809+00:00"
---

# Coverity 2024.9.1 Release Notes

## Important information for 2024.9.1

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

If you are upgrading a Coverity cloud deployment, refer to [Upgrading a Coverity cloud deployment](https://documentation.blackduck.com/bundle/coverity-docs/page/cnc/topics/upgrade-coverity.html) in the Coverity Cloud Deployment Administrator and User Guide. This document provides important information for administrators who are deploying or upgrading Coverity in a Kubernetes container environment.

## Coverity Platform 2024.9.1

This section provides release notes for Coverity Platform components.

### Coverity Connect 2024.9.1

#### New or changed features

COVDOCS-1518
:   Starting with 2024.9.1, the Synopsys SIG registry URL (<https://sig-repo.synopsys.com/>) is deprecated. Customers should use the new URL, <https://repo.blackduck.com/>.

    Similarly, <https://sig-updates.synopsys.com/> is deprecated in favor of <https://updates.lic.blackduck.com>.

    Customers should also add the new URL, <https://repo.blackduck.com/> and IP address (34.110.245.127) to the allowed list.

    Support for the deprecated URLs will be removed on March 1st, 2025.

COVDOCS-1538
:   Starting with 2024.9.1, the Coverity Cloud artifacts will be located at [https://repo.blackduck.com/blackduck/](https://repo.blackduck.com/blackduck). Previous artifacts can be found at [https://repo.blackduck.com/synopsys](https://repo.blackduck.com/blackduck) and will also be available at <https://sig-repo.synopsys.com/synopsys> until March 1st, 2025.

#### Bug fixes

IM-32235
:   Reported in version: 2024.6.0, 2024.6.1
:   Fixed Coverity Connect issue where the **Snapshot"" view did not show the full list of enabled checkers.

## Coverity Analysis 2024.9.1

This section provides release notes for Coverity Analysis components.

### Coverity Analysis - General 2024.9.1

#### Deprecated products and features

COVDOCS-1529
:   Support for the Synopsys Coverity for Jenkins plug-in has been deprecated and will be removed in a future release.

COVDOCS-1530
:   Support for the Synopsys Coverity for Azure DevOps extension (plug-in) has been deprecated and will be removed in a future release.

#### Bug fixes

SAT-45994
:   Reported in version: 2024.3.1
:   Fixed an issue that caused an unrecoverable crash for some deeply nested code constructs. This now causes a recoverable error instead.

### Coverity CLI 2024.9.1

#### New or changed features

COVCLI-3381
:   Added new configuration setting called `replay-processes` that makes it possible to control the number of processes used for replay if a project has been captured using `record-with-source`.

COVCLI-3588
:   Coverity CLI will now enable the Android security and Web application security checkers by default instead of enabling all security checkers by default. In terms of the arguments passed to `cov-analyze", instead of passing`--all-security`by default, the Coverity CLI will now pass "--android-security --webapp-security --webapp-security-aggressiveness-level low` by default.

### Coverity Compilers and Capture 2024.9.1

#### Bug fixes

CAP-2370
:   Reported in version: 2024.9.0
:   Fixed an issue with `cov-build`'s collection of scan transparency data that could significantly slow down builds that run large numbers of the same command.

## Coverity Desktop 2024.9.1

This section provides release notes for Coverity Desktop components.

### Coverity Desktop for Eclipse 2024.9.1

#### New or changed features

COVDOCS-1518
:   Starting with 2024.9.1, the Synopsys SIG registry URL (<https://sig-repo.synopsys.com/>) is deprecated. Customers should use the new URL, <https://repo.blackduck.com/>.

    Similarly, <https://sig-updates.synopsys.com/> is deprecated in favor of <https://updates.lic.blackduck.com>.

    Customers should also add the new URL, <https://repo.blackduck.com/> and IP address (34.110.245.127) to the allowed list.

    Support for the deprecated URLs will be removed on March 1st, 2025.

### Coverity Desktop for Intellij IDEA 2024.9.1

#### New or changed features

COVDOCS-1518
:   Starting with 2024.9.1, the Synopsys SIG registry URL (<https://sig-repo.synopsys.com/>) is deprecated. Customers should use the new URL, <https://repo.blackduck.com/>.

    Similarly, <https://sig-updates.synopsys.com/> is deprecated in favor of <https://updates.lic.blackduck.com>.

    Customers should also add the new URL, <https://repo.blackduck.com/> and IP address (34.110.245.127) to the allowed list.

    Support for the deprecated URLs will be removed on March 1st, 2025.

### Coverity Desktop for Microsoft Visual Studio 2024.9.1

#### New or changed features

COVDOCS-1518
:   Starting with 2024.9.1, the Synopsys SIG registry URL (<https://sig-repo.synopsys.com/>) is deprecated. Customers should use the new URL, <https://repo.blackduck.com/>.

    Similarly, <https://sig-updates.synopsys.com/> is deprecated in favor of <https://updates.lic.blackduck.com>.

    Customers should also add the new URL, <https://repo.blackduck.com/> and IP address (34.110.245.127) to the allowed list.

    Support for the deprecated URLs will be removed on March 1st, 2025.

#### Bug fixes

PRD-13134
:   Reported in version: 2024.9.0
:   Fixed issue for the Coverity Desktop for Visual Studio extension for Visual Studio 2022 which resulted in an error when trying to exit the application.

PRD-13137
:   Reported in version: 2024.9.0
:   Fixed installation error when installing the Coverity Desktop for Visual Studio extension for Visual Studio Community 2019.

## Coverity Documentation 2024.9.1

This section provides release notes for Coverity Documentation components.

### Coverity Documentation 2024.9.1

#### New or changed features

COVDOCS-1518
:   Starting with 2024.9.1, the Synopsys SIG registry URL (<https://sig-repo.synopsys.com/>) is deprecated. Customers should use the new URL, <https://repo.blackduck.com/>.

    Similarly, <https://sig-updates.synopsys.com/> is deprecated in favor of <https://updates.lic.blackduck.com>.

    Customers should also add the new URL, <https://repo.blackduck.com/> and IP address (34.110.245.127) to the allowed list.

    Support for the deprecated URLs will be removed on March 1st, 2025.

COVDOCS-1545
:   A new section, ["Coverity integrations and APIs"](https://documentation.blackduck.com/bundle/coverity-docs/page/deploy-install-guide/topics/integrations/coverity_integrations_and_apis.html), has been added to the *Coverity Installation and Upgrade Guide*. This section presents all available options for Coverity customers for CI/CD integration: CLI clients, plug-ins, and APIs.
