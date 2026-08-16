---
title: "Coverity 2024.12.0 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2024.12.0-release-notes.html"
content_id: "ClSqcjzVdt7Wg~gnaPxpPA"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:25.166934+00:00"
---

# Coverity 2024.12.0 Release Notes

## Important information for 2024.12.0

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

If you are upgrading a Coverity cloud deployment, refer to [Upgrading a Coverity cloud deployment](https://documentation.blackduck.com/bundle/coverity-docs/page/cnc/topics/upgrade-coverity.html) in the Coverity Cloud Deployment Administrator and User Guide. This document provides important information for administrators who are deploying or upgrading Coverity in a Kubernetes container environment.

**Special announcement**

Starting next year, the number of Coverity Connect installer releases will be reduced as we
focus on Coverity Connect in the Coverity cloud deployment. There will be no change to
the Coverity Analysis or the Coverity cloud deployment release cadence.

The Coverity 2025.3 release will not include a Coverity Connect installer and there will be no
more minor releases that include a Coverity Connect installer, except in cases where
there are critical security issues.

In 2025, there will only be 2 major releases that include the Coverity Connect installer: the 2025.6 release and the 2025.12 release.

**Release highlights**

- Coverity Connect and Coverity Analysis have been rebranded to Black Duck Software.
- MISRA C++ 2023 is now fully supported in Coverity Connect and Coverity Analysis.
- The Coverity Cloud Deployment configuration has been simplified.
- Coverity Connect has a new REST API for managing Views.
- The embedded PostgreSQL database of Coverity Connect has been updated to version 15.8.
- Java 23 and Go 1.23 are now supported.
- Added a new C/C++ and Java checker, NULL_FIELD, that is in **Early Access** and finds possible null dereferences of fields. This checker is not enabled by default.
- Added support for Xcode 16.
- Added support for DSC CodeWarrior 11.2 on Windows.
- Added support for HighTec TriCore 4.9.4.1 TC4x on Windows.
- Coverity Analysis is now compatible with macOS 15.
- The `cov-capture` and filesystem capture capabilities in Coverity Analysis have been removed; equivalent functionality is available via the Coverity CLI.​

Please see below for full details of these and other enhancements included in this release.

## Coverity Platform 2024.12.0

This section provides release notes for Coverity Platform components.

### Coverity Connect 2024.12.0

#### End-of-life products

COVDOCS-1640
:   Support for `glibc` 2.17 has been removed from Coverity Connect and Coverity report generators.

#### New or changed features

COVDOCS-1518
:   Starting with 2024.9.1, the Synopsys SIG registry URL (<https://sig-repo.synopsys.com/>) is deprecated. Customers should use the new URL, <https://repo.blackduck.com/>.

    Similarly, <https://sig-updates.synopsys.com/> is deprecated in favor of <https://updates.lic.blackduck.com>.

    Customers should also add the new URL, <https://repo.blackduck.com/> and IP address (34.110.245.127) to the allowed list.

    Support for the deprecated URLs will be removed on March 1st, 2025.

COVDOCS-1537
:   In Coverity cloud deployments, onPrem deployment of Minio and Redis is a new optional feature. Currently, we do not recommended enabling onPrem Minio or Redis on Red Hat OpenShift because we have not fully tested these deployments on OpenShift.

COVDOCS-1623
:   MISRA C++ 2023 is now fully supported in Coverity Connect and Coverity Analysis.

IM-27972
:   Added new REST API operations for Views. Users can now use `POST`/`DELETE`/`PUT` operations to create a new View, delete a View, or update View settings.

    For details, see the [Coverity Platform REST Web Services API](https://documentation.blackduck.com/bundle/coverity-docs/page/cim-api-docs/openapi/cim-openapi.html).

IM-31746
:   The Coverity CLI config file is now available in Connect and it can be retrieved using the `GET /snapshots/{id}/outputFile/cli-diagnostics.json` REST API operation. For details, see the "Retrieve snapshot output file" operation under "Snapshots" in the [Coverity Platform REST Web Services API](https://documentation.blackduck.com/bundle/coverity-docs/page/cim-api-docs/openapi/cim-openapi.html) documentation.

IM-31853
:   The administrative account for Coverity Connect must adhere to a strong password policy. The password needs to be at least 8 characters long and contain at least one digit, as well as lowercase, uppercase, and special characters.

    We recommend a strong password policy for all Connect users.

IM-32068
:   Changed the response for the `GET /api/v2/snapshots/{id}` API call to include the snapshot's associated stream name (`streamName`).

#### Bug fixes

CNC-3147
:   Reported in version: 2024.3.0, 2024.9.0
:   Starting with Coverity 2024.12.0, the supported PostgreSQL port range is 1-65535, as specified in the official PostgreSQL documentation.

IM-32235
:   Reported in version: 2024.6.0, 2024.6.1
:   Fixed Coverity Connect issue where the **Snapshot** view did not show the full list of enabled checkers. Note: the fix does not restore checkers of the existing snapshots created with the issue

#### Known issues and solutions

COVDOCS-1638
:   When upgrading Coverity Connect, clear all the cookies and browser history to ensure that the latest icons are loaded.

### Coverity Report Generators 2024.12.0

#### End-of-life products

COVDOCS-1640
:   Support for `glibc` 2.17 has been removed from Coverity Connect and Coverity report generators.

#### New or changed features

COVDOCS-1492
:   The Synopsys Software Integrity report is now the Black Duck Software Integrity report.

COVDOCS-1605
:   Coverity can now generate reports of MISRA C and C++ 2023 issues.

## Coverity Analysis 2024.12.0

This section provides release notes for Coverity Analysis components.

### Coverity Analysis - General 2024.12.0

#### Deprecated products and features

COVDOCS-1529
:   Support for the Synopsys Coverity for Jenkins plug-in has been deprecated and will be removed in Coverity 2025.3.0.

COVDOCS-1530
:   Support for the Synopsys Coverity for Azure DevOps extension (plug-in) has been deprecated and will be removed in Coverity 2025.3.0.

SATSEC-15966
:   Support for JSHint has been deprecated in Coverity 2024.12.0 and will be removed in Coverity 2025.3.0.

#### New or changed features

COVDOCS-1623
:   MISRA C++ 2023 is now fully supported in Coverity Connect and Coverity Analysis.

SAT-18192
:   The `OVERRUN` checker has been updated so that it handles cases where a condition that controls the increment of an offset is unchanged within a loop.

SAT-45404
:   Made improvements to the way Coverity handles correlated variables in loops in the presence of conditional branches that are always evaluated the same way for all iterations of the loop.

SAT-46137
:   The CodeXM C/C++ library has added a new property, `ownerClassType`, to the `classType` and `enumType` patterns. If the class or enum is a member of a higher-level class or enum, this property identifies the owner type.

SATSEC-15965
:   The integrated version of Detekt has been updated from 1.23.0 to 1.23.6. [Kotlin]

SATSEC-15968
:   The SpotBugs integration has been updated to a pre-release 4.9.0 version that supports Java 23.

SATSEC-16044
:   The module path for Coverity primitives in Go has been updated from `synopsys.com/coverity-primitives` to `blackduck.com/coverity-primitives`.

    This is a breaking change: Source code that currently contains import statements such as

    `import . "synopsys.com/coverity-primitives"`

    must be updated to read

    `import . "blackduck.com/coverity-primitives"`

    instead.

    This is a legal requirement, therefore it cannot be avoided or mitigated.

#### Bug fixes

SAT-45994
:   Reported in version: 2024.3.1
:   Fixed an issue that caused an unrecoverable crash for some deeply nested code constructs. This now causes a recoverable error instead.

#### Known issues and solutions

COVDOCS-1628
:   A current limitation with files provided to `--sigma-malicious-url-patterns-file` requires URLs to be in a file with Unix end-of-line characters. The URLs won’t be reported when the file has Windows end-of-line characters.

### Coverity CLI 2024.12.0

#### End-of-life products

COVCLI-2573
:   The `fs_capture_build_options` option under `cov_run_desktop` under `settings` in the `coverity.conf` file is no longer supported.

#### New or changed features

COVCLI-3197
:   The Coverity CLI now writes a JSON document to the `output/` subdirectory of the intermediate directory (`idir/`). The name of this file is `cli-diagnostics.json`. This JSON file contains diagnostic information about the scan.

COVCLI-3381
:   Added new configuration setting called `replay-processes` that makes it possible to control the number of processes used for replay if a project has been captured using `record-with-source`.

COVCLI-3595
:   Coverity CLI will now enable the Android security and Web application security checkers by default instead of enabling all security checkers by default. In terms of the arguments passed to `cov-analyze`, instead of passing `--all-security` by default, the Coverity CLI will now pass `--android-security --webapp-security --webapp-security-aggressiveness-level low` by default.

### Coverity Checkers 2024.12.0

For a summary of checkers that have been added or changed in this release, refer to the "Coverity Checker Change History" table in the *Coverity Checker Reference*.

#### New or changed features

SAT-2950, SAT-45668
:   Added a new C/C++ and Java checker, `NULL_FIELD`, which finds possible null dereferences of fields. This checker is disabled by default.

SAT-45804
:   The `NULL_RETURNS` and `FORWARD_NULL` checkers no longer report defects on variables asserted as non-null with AssertJ. [Java]

SAT-46037
:   The `RESOURCE_LEAK` checker can now track buffers allocated by the `scanf()` family of functions when using the `%m` dynamic allocation conversion specifier.

SAT-46223
:   Improved the results of the `POINTER_NONDETERMINISM` checker. It now reports fewer false positives, and defects involving templates are reported in better locations.

SAT-46311
:   The `TAINTED_SCALAR` checker will treat the volatile dereference of constant addresses as a source of tainted data by default. This can be disabled using the `TAINTED_SCALAR:tainting_volatile_hardware_ptr:false` option.

SAT-46335
:   Improved the `PRINTF_ARGS` checkers to recognize uses of `va_list` for more compilers. [C/C++, CUDA, Objective-C/C++]

SATSEC-8
:   Fixed a source of false negatives for the `UNSAFE_DESERIALIZATION` checker. [C#]

SATSEC-15795
:   The `MASS_ASSIGNMENT` checker now supports JavaScript and TypeScript.

SATSEC-15870
:   The `CSRF` checker now reports defects in `jsp` files. This behaviour can be disabled using the `disable_jsp_analysis` option. [Java]

SATSEC-15905
:   Models for additional `OS_CMD_INJECTION` sinks have been added.

SATSEC-15967
:   The integrated version of PMD has been updated from 6.55.0 to 7.4.0. [Apex]

SATSEC-16082
:   The `SESSION_FIXATION` checker is now enabled by default for the Go language.

#### Bug fixes

SAT-30096
:   Reported in version: 2019.03
:   Fixed an issue where the `OVERRUN` checker did not report certain defects related to loop bounds calculation. [C, C++]

SAT-45144
:   Reported in version: 2023.3.0
:   Improved issue differentiation for `MISRA C-2012 rule 10.3`.

SAT-45463
:   Reported in version: 2022.12.0, 2023.12.0
:   Fixed a false positive for the `CERT-ARR36-C` checker when comparing the address of an array field inside a struct and the address of the end of the same struct.

SAT-45470
:   Reported in version: 2023.12.0
:   Fixed a false positive for the `MISRA-C 2012 Rule 18.3` checker when comparing the address of an array field inside a struct and the address of the end of the same struct.

SAT-45473, SAT-46198
:   Reported in version: 2023.12.0, 2024.3.1
:   Fixed a false negative for the `OVERRUN` checker. `OVERRUN` defects with C++ `std::array` functions can now be reported. [C++]

SAT-45536
:   Reported in version: 2023.12.0
:   Improved handling of assignment through a ternary operator by the `INTEGER_OVERFLOW` checker.

SAT-45662
:   Reported in version: 2023.12.0
:   Fixed a false positive in the `INTEGER_OVERFLOW` checker related to compound assignments of values.

SAT-45792
:   Reported in version: 2024.3.0
:   Corrected description of the `BAD_CHECK_OF_WAIT_COND` defect, which deals with timed waits. [C#, C/C++, CUDA, Java, Objective-C/C++]

SAT-45854
:   Reported in version: 2024.3.1
:   Fixed an issue that could cause `MISRA Rule 11.3` false positives when the customer uses `clang`.

SAT-45868
:   Reported in version: 2024.3.1
:   Improved the handling of references by the `INTEGER_OVERFLOW` checker.

SAT-45915
:   Reported in version: 2024.6.0
:   Fixed a source of false positives for `FORWARD_NULL` involving `IS_ERR_OR_NULL`.

SAT-45931
:   Reported in version: 2024.6.0
:   Fixed a source of `COPY_INSTEAD_OF_MOVE` false positives that involved exceptional control flow. [C/C++, CUDA, Objective-C/C++]

SAT-45960
:   Reported in version: 2024.6.0
:   The `COPY_INSTEAD_OF_MOVE` checker will no longer suggest moving `const` variables. [C, C++]

SAT-46073
:   Reported in version: 2024.9.0
:   Fixed a false positive for the `DIVIDE_BY_ZERO` checker when using `Mathf.Approximately`. [C#]

SAT-46157
:   Reported in version: 2023.6.1
:   Fixed a recoverable assertion failure in the `OVERFLOW_BEFORE_WIDEN` checker. [C++]

SAT-46161
:   Reported in version: 2024.6.0
:   Fixed a number of false positives that occurred when using the TEE API, notably `TEE_DigestUpdate`.

SAT-46164
:   Reported in version: 2024.6.0, 2024.9.0
:   Fixed a crash in the `RETURN_LOCAL` checker that could happen in rare circumstances. [C++]

SAT-46229
:   Reported in version: 2024.6.0
:   Fixed a recoverable analysis crash involving the `COPY_INSTEAD_OF_MOVE` checker. [C/C++, CUDA, Objective-C/C++]

SAT-46344
:   Reported in version: 6.0.2
:   The `OVERRUN` checker now reports a defect when the value of an unsigned variable in the default clause of a `switch` instruction is guaranteed to overrun a buffer. [C, C++]

SATSEC-16011
:   Reported in version: 2024.9.0
:   Added `SQLI` sinks for the functions `read_sql` and `read_sql_query` in the `pandas` module. [Python]

    Corrected the taint type of the Python functions `input` and `raw_input` to be console taints instead of command line taints.

SATSEC-16025
:   Reported in version: 2024.6.0
:   The `FORWARD_NULL` and `NULL_RETURNS` checkers now correctly recognize `_.isNil()` as a null check function.

SATW-5239
:   Reported in version: 2022.12.0
:   Fixed a source of `CERT STR30-C` false positives when passing a string literal to an inherited constructor.

SATW-6269
:   Reported in version: 2024.6.0
:   Fixed false negatives for `MISRA C-2012 Rule 1.5`, enabling the rule in `required-only` deviation config file.

### Coverity Compilers and Capture 2024.12.0

#### End-of-life products

CMPCSH-2066
:   Support for C# on macOS on Intel is removed as of 2024.12.

CMPGO-496
:   Support for Go 1.21 has been removed as of 2024.12.0.

CMPJ-2286
:   Support for Oracle/Open JDK 22 has been removed as of 2024.12.0.

CMPJ-2310
:   Support for Open JDK 22 has been removed as of 2024.12.0.

COVCLI-3449
:   Buildless capture and filesystem capture have been discontinued. The `cov-capture` binaries and the related options for `cov-build` have been removed from Coverity. To analyze the source of a compiled language, you can use `cov-build`. To analyze source that is not compiled, such as scripts or an interpreted language, use `coverity capture` in the Command Line Interface (CLI).

COVP-2625
:   Support for macOS 12 has been removed as of 2024.12.0.

COVP-2629
:   Support for .NET 6 has been removed as of 2024.12.0.

#### Deprecated products and features

CAP-2341
:   Support for Bazel 5 has been deprecated in 2024.12.0 and will be removed in a future release.

CMPGO-495
:   Support for Go 1.22 is deprecated as of 2024.12.0 and will be removed in a future release.

#### New or changed features

CCK-2672
:   Added support for Intel oneAPI 2024.2.1 on Linux.

CCK-2691
:   Added support for the DSC compiler for CodeWarrior 11.2 on Windows.

CMPCPP-14806
:   Added support for Xcode 16.0.

CMPGO-500
:   Added support for Go version 1.23.

CMPJ-2284
:   Support for Oracle/Open JDK 23 has been added as of 2024.12.0.

CMPJ-2308
:   Added support for Java 23.

COVP-2623
:   Support for macOS 15 has been added as of 2024.12.0.

#### Bug fixes

CAP-2327
:   Reported in version: 2024.3.0
:   Fixed an issue where `cov-build` would cause a build failure when disengaging from binaries launched with a NULL environment (for example, `codesign` on macOS).

CAP-2333
:   Reported in version: 2024.6.0
:   Previously, `cov-build` could encounter issues when running the `codesign` tool on macOS with newer versions of Xcode. `cov-build` will now disengage from `codesign` automatically to avoid these issues.

CAP-2338
:   Reported in version: 2024.3.0, 2024.6.0, 2024.3.2
:   Running Gradle 8.9 under `cov-build` will no longer cause the build to fail.

CAP-2366
:   Reported in version: 2024.6.0
:   Fixed an issue where `cov-build` would run `cov-translate` in the wrong directory when building with Xcode 15.

CAP-2368
:   Reported in version: unspecified
:   Fixed an issue with `cov-build`'s collection of scan transparency data that could significantly slow down builds that ran large numbers of the same command.

CMPCPP-14774
:   Reported in version: 2024.6.0
:   Fixed issue where `cov-emit` failed with the catastrophic signal: 80000003 (EXCEPTION_BREAKPOINT) when Application Verifier for Windows was enabled.

CMPCSH-2085
:   Reported in version: 2024.9.0
:   In the .NET front-end, fixed an issue when parsing collection expressions contained in tuples.

CMPGO-519
:   Reported in version: unspecified
:   `coverity capture` provides diagnostic messages when `cov-internal-go-fe` is killed by `SIGKILL`.

#### Known issues and solutions

CAP-2373
:   When running Gradle 8.10 under `cov-build` on Windows, the build may fail to start the Gradle daemon. This can be avoided by adding `--instrument` to your `cov-build` command line.

### Coverity Point and Scan 2024.12.0

#### New or changed features

COVGUI-2560
:   As of the 2024.12.0 release, the contents of the `$HOME/.synopsys/point-and-scan` directory will be moved automatically to `$HOME/.coverity/point-and-scan`.

    If there is a need to downgrade the version of Coverity Point and Scan to one older than 2024.12.0, the contents will need to be moved manually back from `$HOME/.coverity/point-and-scan` to `$HOME/.synopsys/point-and-scan` in order for users to continue to see their previous scans, logged in accounts and other data in Coverity Point and Scan.

#### Known issues and solutions

COVDOCS-1646
:   A known Electron issue affects the Coverity Point and Scan installation: when running PAS UI on macOS15.2 in a virtualized environment, the UI renders a blank screen.

    The workaround for this issue is to launch the PAS UI with the following command line options: `--args --flags --disable-gpu`.

    For example: `open /Applications/cov-analysis-macos-arm-2024.12.0/bin/Coverity\ Point\ and\ Scan.app --args --flags --disable-gpu`

### Rapid Scan Static (Sigma engine) 2024.12.0

#### Known issues and solutions

COVDOCS-1628
:   A current limitation with files provided to `--sigma-malicious-url-patterns-file` requires URLs to be in a file with Unix end-of-line characters. The URLs won’t be reported when the file has Windows end-of-line characters.

## Coverity Desktop 2024.12.0

This section provides release notes for Coverity Desktop components.

### Coverity Desktop for Android Studio 2024.12.0

#### End-of-life products

PRD-13126
:   Support for Android Studio 2021.2 has been removed as of 2024.12.0.

#### Deprecated products and features

PRD-13146
:   Support for Android Studio 2022.2 is deprecated as of 2024.12.0 and will be removed in a future release.

### Coverity Desktop for Eclipse 2024.12.0

#### End-of-life products

PRD-13142
:   Support for Eclipse 2021-06 has been removed as of 2024.12.0.

#### Deprecated products and features

PRD-13143
:   Support for Eclipse 2021-12 is deprecated as of 2024.12.0 and will be removed in a future release.

#### New or changed features

COVDOCS-1518
:   Starting with 2024.9.1, the Synopsys SIG registry URL (<https://sig-repo.synopsys.com/>) is deprecated. Customers should use the new URL, <https://repo.blackduck.com/>.

    Similarly, <https://sig-updates.synopsys.com/> is deprecated in favor of <https://updates.lic.blackduck.com>.

    Customers should also add the new URL, <https://repo.blackduck.com/> and IP address (34.110.245.127) to the allowed list.

    Support for the deprecated URLs will be removed on March 1st, 2025.

PRD-13144
:   Added support for Eclipse 2024-09.

### Coverity Desktop for Intellij IDEA 2024.12.0

#### Deprecated products and features

PRD-13156
:   Support for Coverity Desktop plugins for all JetBrain IDEs and Android Studio has been deprecated in Coverity 2024.12.0 and will be removed in a future release. Support will not be added for any new versions of JetBrain IDEs or Android Studio. Please switch to the Black Duck Code Sight Plugin for continued support and updates.

#### New or changed features

COVDOCS-1518
:   Starting with 2024.9.1, the Synopsys SIG registry URL (<https://sig-repo.synopsys.com/>) is deprecated. Customers should use the new URL, <https://repo.blackduck.com/>.

    Similarly, <https://sig-updates.synopsys.com/> is deprecated in favor of <https://updates.lic.blackduck.com>.

    Customers should also add the new URL, <https://repo.blackduck.com/> and IP address (34.110.245.127) to the allowed list.

    Support for the deprecated URLs will be removed on March 1st, 2025.

### Coverity Desktop for Microsoft Visual Studio 2024.12.0

#### New or changed features

COVDOCS-1518
:   Starting with 2024.9.1, the Synopsys SIG registry URL (<https://sig-repo.synopsys.com/>) is deprecated. Customers should use the new URL, <https://repo.blackduck.com/>.

    Similarly, <https://sig-updates.synopsys.com/> is deprecated in favor of <https://updates.lic.blackduck.com>.

    Customers should also add the new URL, <https://repo.blackduck.com/> and IP address (34.110.245.127) to the allowed list.

    Support for the deprecated URLs will be removed on March 1st, 2025.

## Coverity Documentation 2024.12.0

This section provides release notes for Coverity Documentation components.

### Coverity Documentation 2024.12.0

#### New or changed features

COVDOCS-1492
:   The Synopsys Software Integrity report is now the Black Duck Software Integrity report.

COVDOCS-1518
:   Starting with 2024.9.1, the Synopsys SIG registry URL (<https://sig-repo.synopsys.com/>) is deprecated. Customers should use the new URL, <https://repo.blackduck.com/>.

    Similarly, <https://sig-updates.synopsys.com/> is deprecated in favor of <https://updates.lic.blackduck.com>.

    Customers should also add the new URL, <https://repo.blackduck.com/> and IP address (34.110.245.127) to the allowed list.

    Support for the deprecated URLs will be removed on March 1st, 2025.

COVDOCS-1545
:   A new section, ["Coverity integrations and APIs"](https://documentation.blackduck.com/bundle/coverity-docs/page/deploy-install-guide/topics/integrations/coverity_integrations_and_apis.html), has been added to the *Coverity Installation and Upgrade Guide*. This section presents all available options for Coverity customers for CI/CD integration: CLI clients, plug-ins, and APIs.

COVDOCS-1626
:   In the *Coverity Installation and Upgrade Guide,* added a note to clarify that the FlexNet license server must be run in a secure manner.

#### Bug fixes

COVDOCS-1532
:   Reported in version: 2024.3
:   Updated section "Creating a Coverity analysis kit for local analysis" of the *Coverity Cloud Deployment Administrator and User Guide* with missing information.

COVDOCS-1564
:   Reported in version: unspecified
:   In the *Configuring and Generating Coverity Reports* section on CVSS reports, added text to clarify that the `"version"` field should specify the CVSS Report Generator profile version and *not* the Coverity version.

COVDOCS-1572
:   Reported in version: 2024.9.0
:   Updated the "Coverity client support" section of the *Coverity Cloud Deployment Administrator and User Guide* to provide the full list of Coverity Analysis supported versions.

COVDOCS-1585
:   Reported in version: 2024.9.0
:   Fixed a doc error that implied users could use a space as a delimiter, rather than `T`, when specifying the expiration date for a Coverity Connect authentication key.
