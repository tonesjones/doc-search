---
title: "Coverity 2023.12.2 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2023.12.2-release-notes.html"
content_id: "t9Hommxzm3GoQKjO8z7nQQ"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:37.009304+00:00"
---

# Coverity 2023.12.2 Release Notes

## Important information for 2023.12.2

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

## Coverity Platform 2023.12.2

This section provides release notes for Coverity Platform components.

### Coverity Connect 2023.12.2

#### New or changed features

IM-31423
:   The Apache Tomcat version has been upgraded to 9.0.83.

#### Bug fixes

CNC-2478
:   Reported in version: 2022.12.0
:   The OpenSSL binary is now available in the web app UBI image. Customers don't need to install OpenSSL separately.

CNC-2585
:   Reported in version: 2023.12.0
:   Customers can now successfully deploy Coverity in the cloud on ARM64 machines.

IM-30988
:   Reported in version: 2023.6.0
:   Fixed a bug where **Quality Advisor** and **Security Advisor** views would render incorrectly with a customer banner enabled.

IM-31159
:   Reported in version: 2023.9.0
:   Fixed a bug where the source viewer file bar showed the incorrect file in some cases.

IM-31203
:   Reported in version: 2022.12.1, 2023.6.0, 2023.9.0
:   Fixed a bug where users with many shared views could not scroll through the list of shared views.

IM-31241
:   Reported in version: 2023.6.0, 2023.9.0
:   Fixed a bug for Connect instances where users were unable to download all configuration files from the diagnostics area when a context path was set.

IM-31309
:   Reported in version: 2023.3.0
:   Fixed a bug where the file tree dialog was not moveable.

IM-31365
:   Reported in version: 2023.9.0
:   Fixed a bug where users could not change their password if their email domain contained ".co.jp".

## Coverity Analysis 2023.12.2

This section provides release notes for Coverity Analysis components.

### Coverity Analysis - General 2023.12.2

#### Bug fixes

CMPJS-1150
:   Reported in version: 2023.12.0
:   Fixed issue that was introduced into `cov-internal-js-fe` in the Coverity 2023.12.0 release, which would sometimes cause crashes in `cov-analyze`.

SAT-45233, SAT-45269
:   Reported in version: 2023.12.0, 2023.9.0, 2023.12.0
:   Fixed a deadlock affecting some analyses running on macOS.

#### Known issues and solutions

COVGUI-2527
:   With the introduction of 2-step authentication, the browser needs to be opened to complete the SSO authentication. Using the `coverity scan` command directly may cause an issue on Linux ARM machines as the scan may not get triggered immediately after completing SSO sign-in due to Wayland protocol error. However, the authentication process will be completed successfully.

### Coverity Checkers 2023.12.2

For a summary of checkers that have been added or changed in this release, refer to the "Coverity Checker Change History" table in the *Coverity Checker Reference*.

#### Bug fixes

SATSEC-15654
:   Reported in version: 2023.9.2
:   Fixed a bug with in the Java `SQLI` checker for MyBatis. [Java]

### Coverity Compilers and Capture 2023.12.2

#### Bug fixes

CMPCPP-13939
:   Reported in version: 2023.3.2
:   Fixed an issue where C++ anonymous unions caused a segmentation fault.

CMPCSH-1987
:   Reported in version: unspecified
:   Fixed an issue in `cov-emit-cs` where DLL files that encountered an unrecoverable failure when being decompiled could leave the database in a state where DLL caching would not work correctly for those DLL files.

CMPJS-1158
:   Reported in version: 2023.12.0
:   Fixed issue that was introduced into `cov-internal-js-fe` in the Coverity 2023.12.0 release, which could cause crashes in `cov-analyze`.

### Coverity Point and Scan 2023.12.2

#### Known issues and solutions

COVGUI-2527
:   With the introduction of 2-step authentication, the browser needs to be opened to complete the SSO authentication. Using the `coverity scan` command directly may cause an issue on Linux ARM machines as the scan may not get triggered immediately after completing SSO sign-in due to Wayland protocol error. However, the authentication process will be completed successfully.

## Coverity Documentation 2023.12.2

This section provides release notes for Coverity Documentation components.

### Coverity Documentation 2023.12.2

#### Bug fixes

COVDOCS-1264
:   Reported in version: 2023.12.0
:   Fixed a typo in Table 9, "SIG Docker registries", in the *Coverity Cloud Deployment Administrator and User Guide*. The SIG private Docker registry URL is `sig-repo.coverity.com`, not `sig.repo.coverity.com`.

COVDOCS-1270
:   Reported in version: 2023.12.0
:   Added a note to Section 5.7, "Coverity container images", in the *Coverity Cloud Administrator and User Guide* that all container images work with both ARM64 and Intel/AMD.

COVDOCS-1287
:   Reported in version: 2023.12.0
:   The 2023.12.0 Release Notes incorrectly stated that Coverity Connect supports PostgreSQL 11–15 (including all minor releases). Since PostgreSQL support for version 11 has ended in November 2023, Coverity Connect 2023.12.x does not support PostgreSQL 11.

COVDOCS-1310
:   Reported in version: 2023.12.0
:   Corrected inconsistencies regarding aggresiveness level for several checkers in the *Coverity Command Reference* and *Coverity Checker Reference* documents.

COVDOCS-1314
:   Reported in version: 2023.12.0
:   Fixed localization issue in `coverity-checker-coverage.html`.
