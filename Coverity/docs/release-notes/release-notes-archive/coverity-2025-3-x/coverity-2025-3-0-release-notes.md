---
title: "Coverity 2025.3.0 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2025.3.0-release-notes.html"
content_id: "AU5PxX46YwMt37bdIQUxYw"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:22.387660+00:00"
---

# Coverity 2025.3.0 Release Notes

## Important information for 2025.3.0

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

If you are upgrading a Coverity cloud deployment, refer to [Upgrading a Coverity cloud deployment](https://documentation.blackduck.com/bundle/coverity-docs/page/cnc/topics/upgrade-coverity.html) in the Coverity Cloud Deployment Administrator and User Guide. This document provides important information for administrators who are deploying or upgrading Coverity in a Kubernetes container environment.

**Release highlights**

- .NET 9 is now supported.
- Kotlin 2.1 is now supported.
- GCC 14 is now supported.
- The NULL_FIELD checker is now GA and enabled by default.
- Database Read Replicas are now available for Coverity Connect cloud deployments.
- Coverity Connect color contrast has been improved and ALT text has been added to all images for better accessibility.

Please see below for full details of these and other enhancements included in this release.

## Coverity Analysis 2025.3.0

This section provides release notes for Coverity Analysis components.

### Coverity Analysis - General 2025.3.0

#### End-of-life products

COVDOCS-1641
:   Support for the Synopsys Coverity for Jenkins plug-in, which was deprecated in release 2024.12.0, has now been removed. Please begin using the new Bridge-based plug-in, Black Duck Security Scan for Coverity (see https://documentation.blackduck.com/bundle/bridge/page/documentation/security_scan_for_coverity.html).

    Support for the Synopsys Coverity for Azure DevOps plug-in was deprecated in release 2024.12.0. This has also been removed.

SATSEC-16048
:   Support for JSHint has been removed in Coverity 2025.3.0.

#### Deprecated products and features

CMPCPP-14860
:   Support for the integration with IncrediBuild was deprecated as of 2023.3.0 and support has been removed from the 2025.3.0 release.

#### New or changed features

SAT-45853
:   Improved handling of `scanf` and related functions.

#### Bug fixes

CMPCPP-14940
:   Reported in version: 2024.9.0
:   Corrected the acceptance criteria for user identifiers in Rule 5.10.1 of MISRA C++ 2023 compliance standard.

SAT-45934
:   Reported in version: 2024.6.0
:   Improved the tracking of ranges of known values within and after a loop construct. Affects `INTEGER_OVERFLOW, OVERRUN` and other checkers.

SAT-46193
:   Reported in version: 2023.12.0, 2024.6.0
:   Improved the tracking of ranges of known values within and after a loop. Affects `INTEGER_OVERFLOW, OVERRUN` and other checkers.

SAT-46305
:   Reported in version: 2025.3.0
:   Improved the tracking of ranges of known values within and after a loop. Affects `INTEGER_OVERFLOW, OVERRUN` and other checkers.

SAT-46511, SAT-46512, SAT-46513
:   Reported in version: 2024.12.0, 2024.9.0
:   Fixed an unrecoverable analysis crash with messages `"assertion failed: object" and "! isPhaseFinalNode()"` in some cases involving C++ non-static data member initializers.

SAT-46519, SAT-46631
:   Reported in version: 2024.9.0, 2024.9.1
:   Fixed an issue that could cause an unrecoverable crash in cov-analyze or cov-run-desktop when using enums with an assigned alignment.

SAT-46521
:   Reported in version: 2022.3.3
:   Fixed an issue where analysis could take a very large amount of time in the presence of class hierarchies where the same interface is inherited in multiple ways.

SAT-46581
:   Reported in version: 2024.12.0
:   Fixed an issue that could cause work unit analysis to run for a very long time or to time out when a variable is updated in a loop by multiplication by zero.

SAT-46630
:   Reported in version: 2024.12.0
:   Fixed a crash-causing issue in the Extend SDK when using `FunctionPattern::get_owner_class` after matching a call through a pointer-to-member.

SAT-46654, SAT-46681, SAT-46742
:   Reported in version: 2024.12.0
:   Fixed an issue that caused an unrecoverable cov-analyze crash in some C# cases. It is now a recoverable issue.

SATSEC-16141
:   Reported in version: 2024.9.0
:   Fixed a framework analyzer crash.

### Coverity CLI 2025.3.0

#### New or changed features

COVCLI-3724
:   Coverity CLI now recognizes `pyproject.toml` files as Python project files. This change impacts the Coverity CLI list output which will show these files as `Module` files.

COVCLI-3793
:   By default, Coverity CLI will pass a new analysis flag called `--recommended-security-checkers` to the analysis. However this behavior can be controlled by a new Coverity CLI configuration setting at `analyze.checkers.recommended-security-checkers`.

#### Bug fixes

COVCLI-3680
:   Reported in version: 2024.12.0
:   Coverity CLI will no longer delete files captured by build capture located in a directory or sub-directory called `vendor`.

COVCLI-3727
:   Reported in version: 2024.12.0
:   The Coverity CLI will no longer automatically validate Java web applications. Validation of exploded EARs and WARs and compressed EARs and WARs will no longer be done to avoid issues where valid web applications are not captured.

### Coverity Checkers 2025.3.0

For a summary of checkers that have been added or changed in this release, refer to the "Coverity Checker Change History" table in the *Coverity Checker Reference*.

#### New or changed features

SAT-39158, SAT-45958
:   Added a new primitive and annotation to allow suppression of `CHECKED_RETURN` defects.

SAT-39999
:   Fixed a source of `FORWARD_NULL` false positives when taking the address of element 0 of a null array.

SAT-43625
:   A new checker option `REPORT_UNPROTECTED_INDEXING` reports any indexing where there is no local checking of the index range.

SAT-45782
:   Improved the event text associated with an `INTEGER_OVERFLOW` defect pattern to better explain the defect.

SAT-46334
:   The `DEADCODE` checker now leverages more information about set and unset bits.

SAT-46336
:   The `NULL_FIELD` checker is now enabled by default for C, C++, and CUDA.

SAT-46388
:   In `INTEGER_OVERFLOW`, do not immediately report a defect on the overflow of an unsigned value. Instead, wait until that value is used in a sensitive context. The former behavior can be recovered with a new checker option: `report_unsigned_overflow_immediately`.

SAT-46612
:   Fixed a number of false positives and false negatives with MISRA C++-2023 Rule 7.0.6. Triage has been refined to make it more precise.

SATSEC-3206
:   The `URL_MANIPULATION` checker now supports C# and Visual Basic.

SATSEC-15764
:   The `OS_CMD_INJECTION` checker was enhanced to address some false negatives for Java, C# and Visual Basic.

SATSEC-16023
:   Fixed a false negative for the `XSS` checker. [Go]

SATSEC-16146
:   Fixed a false negative for the `OS_CMD_INJECITON` checker. [Python]

SATW-6399
:   Fixed a number of false positives and false negatives with MISRA C++-2023 Rule 7.0.6. Triage has been refined so it is more precise.

#### Bug fixes

SAT-45081
:   Reported in version: 2023.12.0
:   Fixed the `USELESS_CALL` checker to remove false positives when calling methods from interfaces that do not have an implementation. [Java]

SAT-45720
:   Reported in version: 2022.3.0, 2023.12.0
:   Fixed an issue that caused a CERT STR50-CPP false positive due to incorrect use of models.

SAT-45900
:   Reported in version: 2024.3.1
:   Fixed a problem in `INTEGER_OVERFLOW` related to keeping track of known values after conditional checks.

SAT-45971
:   Reported in version: 2024.3.0
:   Fixed an issue where `CHECKED_RETURN` didn't report some defects.

SAT-46300, SAT-46322
:   Reported in version: 2024.9.0, 2025.3.0
:   Improved the tracking of ranges of known values within and after a loop construct. Affects `INTEGER_OVERFLOW, OVERRUN` and other checkers.

SAT-46337
:   Reported in version: 2024.12.0
:   Fixed a false positive in `NULL_FIELD` involving functions that return objects whose fields are null-checked.

SAT-46372
:   Reported in version: 2024.12.0
:   Replace an event for the `DIVIDE_BY_ZERO` checker on defects for floating-point types. Replaced "has undefined behavior" by "results in either +infinity, -infinity, or NaN". [all languages]

SAT-46469
:   Reported in version: 2024.12.0
:   Fixed some `NULL_FIELD` false positives reported with bad statistical data.

SAT-46496
:   Reported in version: 2024.9.0
:   Fixed a recoverable error that could occur when using `INTEGER_OVERFLOW` in certain conditions with mixed sign variables in a `+=` operation. [C, C++, Objective C/C++, CUDA]

SAT-46502
:   Reported in version: 2024.9.0
:   An issue where MISRA C++-2023 Dir 0.3.1 is reported as `FLOATING_POINT_EQUALITY_MISRA` is fixed.

SAT-46551
:   Reported in version: 2024.12.0
:   Fixed an issue that could cause a crash in the `INTEGER_OVERFLOW` checker when encountering certain pointer casts.

SAT-46593
:   Reported in version: 2024.9.0, 2024.12.0
:   Fixed a crash in `INTEGER_OVERFLOW` related to casts of values between integer and floating-point types.

SAT-46635
:   Reported in version: 2024.9.0
:   Fixed a recoverable crash in the `NULL_RETURNS` checker involving a range-based `for` loop and a container whose `end()` function can return a null value.

SAT-46792
:   Reported in version: 2024.9.0, 2024.12.0
:   Fixed an issue where the `default` keyword could incorrectly be considered a null pointer in cases where it represents a value type.

SATSEC-3299
:   Reported in version: 2022.3.0
:   Fixed a false positive for the `INSUFFICIENT_LOGGING` checker. [Go]

SATSEC-16151
:   Reported in version: 2024.12.0
:   Fixed a bug where C# nested classes and enumerators were not properly separated in the CodeXM `ScopeList` property. [C#]

SATSEC-16158
:   Reported in version: 2024.12.0
:   Fixed a false negative for the `MASS_ASSIGNMENT` checker. [C#]

SATW-5426
:   Reported in version: 2022.12.0
:   Fixed a false positive for the `AUTOSAR C++14 A4-7-1` checker.

SATW-6357
:   Reported in version: 2024.9.0, 2024.3.1
:   Fixed a false negative for the `CERT MSC24-C` checker.

SATW-6358
:   Reported in version: 2024.9.0
:   Fixed a false negative of MISRA CPP 2023 Rule 7.0.3, pertaining to variable declaration using data types from 'cstdint' library.

SATW-6427
:   Reported in version: 2024.9.0
:   Fixed a false positive for the `MISRA C++-2023 Rule 0.1.2` checker.

### Coverity Commands 2025.3.0

#### Bug fixes

COVDOCS-1686
:   Reported in version: unspecified
:   For the pages on Coverity Connect commands (with one exception), added an "Exit codes" subsection with a link to the main description of these.

SAT-46545
:   Reported in version: 2024.9.0
:   Fixed an issue that could cause response files to be incorrectly parsed on Linux if they were generated on Windows.

SAT-46717, SAT-46759
:   Reported in version: 2024.12.0
:   Fixed an issue that could cause Desktop Analysis to crash in certain C++ cases.

### Coverity Compilers and Capture 2025.3.0

#### End-of-life products

CAP-2405
:   Support for Bazel 5 has been removed as of 2025.3.0.

CMPFG-1363
:   Support for Kotlin 1.9 is at EOL.

#### Deprecated products and features

CMPJ-2342
:   Support for Oracle/Open JDK 23 is deprecated as of 2025.3.0 and will be removed in a future release.

#### New or changed features

CAP-2393
:   Added support for Bazel 8.

CMPCPP-13670
:   Added support for GCC 14.1 in 2025.3.

CMPCSH-2094
:   Added support for C# 13.

COVP-2634
:   Support for .NET 9 has been added as of 2025.3.0.

#### Bug fixes

CAP-2323
:   Reported in version: 2024.3.0
:   `cov-build --bazel` will now capture compilations specified via a `source_files` attribute.

CAP-2359
:   Reported in version: 2024.6.0
:   `cov-build --bazel` previously failed for some builds with "Error: type 'Target' is not iterable". This has been resolved.

CAP-2361
:   Reported in version: 2024.12.0
:   `cov-build --bazel` can now capture `cc_library` rules that make use of the `include_prefix` and `strip_include_prefix` attributes.

CAP-2402
:   Reported in version: 2024.12.0
:   `cov-build` will no longer fail if `/usr/bin/file` is not present. Instead it will produce a warning and continue.

CAP-2409
:   Reported in version: 2024.12.0
:   Capturing Bazel Java targets that don't compile anything can no longer cause failures during emit.

CAP-2412
:   Reported in version: 2024.12.0
:   Long Bazel package names can no longer cause the Coverity-Bazel integration to crash.

CMPCPP-14922
:   Reported in version: 2025.3.0
:   Fixed an issue for complex situations involving templates and friend declarations in which cov-emit could become stuck in an unbounded loop.

CMPCPP-14944, CMPCPP-15009
:   Reported in version: 2024.9.0
:   Fixed a catastrophic error in cov-emit happening sometimes when using precompiled headers with MSVC 17.0 and newer.

### Rapid Scan Static (Sigma engine) 2025.3.0

#### New or changed features

COVDOCS-1700
:   A new table, "Software issues and impact by check" has been added to the Sigma Checker Reference. This table provides additional information to the "Software issues by checker" table, showing the impact level (either Low, Medium, or High) for each check.

## Coverity Desktop 2025.3.0

This section provides release notes for Coverity Desktop components.

### Coverity Desktop for Eclipse 2025.3.0

#### End-of-life products

PRD-13189
:   Support for Eclipse 2021-09 has been removed as of 2025.3.0.

#### Deprecated products and features

PRD-13190
:   Support for Eclipse 2022-03 is deprecated as of 2025.3.0 and will be removed in a future release.

#### New or changed features

PRD-13186
:   Added support for Eclipse 2024-12.

### Coverity Desktop for Microsoft Visual Studio 2025.3.0

#### Bug fixes

PRD-13193
:   Reported in version: 2024.9.0, 2024.12.0
:   Added support for .xsd file analysis in Coverity Desktop plugin for Visual Studio.

## Coverity Documentation 2025.3.0

This section provides release notes for Coverity Documentation components.

### Coverity Documentation 2025.3.0

#### Bug fixes

COVDOCS-1631
:   Reported in version: 2024.6.0, 2024.9.0
:   To avoid Coverity cloud deployment errors that result when pod names exceed 36 characters, in the *Coverity Cloud Administrator and User Guide*, added the following note in several places to inform administrators that pod names cannot exceed 36 characters: "Important: The Connect (cim) hostname that you specify in cim.ingress.hosts must NOT exceed 36 characters in length. This restriction excludes the https:// characters that are used when you specify the URL, as well as any port specification."

COVDOCS-1685
:   Reported in version: unspecified
:   In the *Command Reference* description of `cov-admin-db`, removed mentions of a `--dir` option that does not exist.

COVDOCS-1688
:   Reported in version: 2024.9.0
:   Updated documentation with information about override of the server.xml file after an in-place upgrade.
