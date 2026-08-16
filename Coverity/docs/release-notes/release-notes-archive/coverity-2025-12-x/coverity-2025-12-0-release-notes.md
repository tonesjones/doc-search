---
title: "Coverity 2025.12.0 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2025.12.0-release-notes.html"
content_id: "2IQG6LHRy5cufd9O~VGClQ"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:13.487671+00:00"
---

# Coverity 2025.12.0 Release Notes

## Important information for 2025.12.0

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

If you are upgrading a Coverity cloud deployment, refer to [Upgrading a Coverity cloud deployment](https://documentation.blackduck.com/bundle/coverity-docs/page/cnc/topics/upgrade-coverity.html) in the Coverity Cloud Deployment Administrator and User Guide. This document provides important information for administrators who are deploying or upgrading Coverity in a Kubernetes container environment.

**Release Highlights**

- Full support in Connect for MISRA C 2025
- Updated support for Java 25
- Updated support for Go 1.25
- Updated support for Kotlin 2.2
- Updated support for GCC 15
- Added New checker REVERSE_INVALID_ITERATOR
- Support for Kotlin quality checkers has been deprecated as of 2025.12.0 and will be removed in a future version

Please see below for full details of these and other enhancements included in this release.

## Coverity Platform 2025.12.0

This section provides release notes for Coverity Platform components.

### Coverity Connect 2025.12.0

#### New or changed features

CNC-2630
:   For routes from Connect clients into an OpenShift Coverity cloud deployment, this release includes new `cim.route` Helm keys in the `cnc` Helm chart that enable you to either automatically or manually create OpenShift routes to Connect. See 'OpenShift routing - exposing the Coverity cloud instance outside an OpenShift cluster` in the *Coverity Cloud Deployment Administrator and User Guide*.

COVDOCS-1962
:   For Coverity cloud deployments, added `*.okta.com` as a default configured custom domain for storage service configurations. For documentation, see the *Coverity Cloud Deployment Administrator and User Guide*.

IM-32634
:   As part of this ticket, we have added an optional snapshotId parameter (integer) to the existing /metrics/functions API. The upgraded API validates that the provided snapshotId belongs to the specified stream. If snapshotId is provided, return metrics from that snapshot only. If snapshotId is not provided, return metrics from the latest snapshot in the stream.

IM-33387
:   Release 2025.12.0 adds support for MISRA C 2025.

#### Bug fixes

CNC-3558
:   Reported in version: 2024.9.0
:   Resolved a Coverity cloud issue where large IDIRs were failing to upload to Connect storage in AWS S3, S3 Express, GCP S3, and MinIO. S3 does not support HTTP PUT requests for files over 5 GB. To solve this problem, this release supports automatic chunking and multipart uploads, where files larger than 5MB are uploaded in multiple smaller transfers. User intervention is not required. This feature is supported with AWS S3, S3 Express, GCP S3, and MinIO. Azure blob previously and still supports automatic chunking and multipart uploads.

IM-33011
:   Reported in version: 2024.12.0
:   Major performance improvements have been added for CIDs with huge triage history while loading the source browser so that it does not time out or return a blank screen.

IM-33071
:   Reported in version: 2025.3.0
:   The cov-manage-im command executes successfully without errors when using the --component-not option.

IM-33093
:   Reported in version: 2024.9.0, 2024.12.0, 2025.3.0
:   Bug fix: GET /projects end point now displays the example in "try-it-out" mode.

IM-33155
:   Reported in version: 2025.6.0
:   When validations fail, the output will now include the stream name. Eg: "Stream sample_stream_name does not exist or you do not have permission to access it."

IM-33332
:   Reported in version: 2024.3.2
:   Fixed a bug that occurred when rendering large minified js files where the source browser would fail to load, eventually crashing the tab. Added limits to detect when such cases will be encountered and an error message explaining to users why the operation failed.

IM-33472
:   Reported in version: 2025.9.0
:   Added default-src as none, and frame-ancestors as self, form-action as self.

#### Known issues and solutions

COVDOCS-1860
:   Using special characters within a Coverity Connect project name or stream name can cause a failure. In Coverity Connect, for both projects and streams, do not use the following special characters:
    * `:` (colon)
    * `*` (asterisk)
    * `/` (forward slash)
    * `\` (back slash)
    * ``` `` (backtick)
    * ```'`(single quote)
    *`"`(double quote)
    This restriction applies to the user interface, REST API, and Web service calls, including`cov-manage-im`.

### Coverity Report Generators 2025.12.0

#### New or changed features

RG-1967
:   The Coverity MISRA report now includes supported MISRA C 2025 rules.

    reference :- https://blackduck-dev.zoominsoftware.io/bundle/coverity-docs-2024.9/page/webhelp-files/relnotes_latest.html#relnotes_latest

## Coverity Analysis 2025.12.0

This section provides release notes for Coverity Analysis components.

### Coverity Analysis - General 2025.12.0

#### Deprecated products and features

CAP-2566
:   Coverity analysis support for macOS on Intel (macosx) is deprecated as of 2025.12.0 and will be removed in 2026.12.0.

COVDOCS-1866
:   SpotBugs and Detekt have been deprecated.

COVDOCS-1885
:   Support for SpotBugs has been deprecated as of 2025.12.0 and will be removed in a future version.

COVDOCS-1886
:   Support for Detekt is deprecated as of 2025.12.0 and will be removed in a future version.

COVDOCS-1887
:   Support for JavaScript/TypeScript quality checkers has been deprecated as of 2025.12.0 and will be removed in a future version.

COVDOCS-1888
:   Support for Go quality checkers has been deprecated as of 2025.12.0 and will be removed in a future version.

COVDOCS-1889
:   Support for Python quality checkers has been deprecated as of 2025.12.0 and will be removed in a future version.

COVDOCS-1968
:   Support for Kotlin quality checkers has been deprecated as of 2025.12.0 and will be removed in a future version.

#### New or changed features

SATSEC-16328
:   The versions of Ruby and dependencies used to run Brakeman Pro have been updated.

SATSEC-16343
:   The SpotBugs integration has been updated to version 4.9.7

SATSEC-16425
:   The output of cov-format-sarif-for-github.js now includes the startColumn field for events.

#### Bug fixes

SAT-5793
:   Reported in version: 5.5.1
:   An OVERRUN FP is fixed where OVERRUN was previous erroneously reported on certain calls to functions such as memset when the length parameter is zero.

SAT-46259
:   Reported in version: 2023.12.0
:   Fixed a source of crashes, sometimes with no error message, during the "export summaries" phase.

SAT-46331
:   Reported in version: 2024.6.0
:   Fixed an issue that could cause `HIS` metrics to be incorrect and nondeterministic for functions that are defined several times in the same location, like `inline` functions in headers.

SAT-46670
:   Reported in version: 2024.12.0
:   A `RESOURCE_LEAK` issue related to linux `IS_ERR_OR_NULL` function is fixed.

SAT-47516
:   Reported in version: 2025.12.0
:   Fix an OVERRUN issue in android kernel by adding a model for size_mul and related functions.

SATSEC-16370
:   Reported in version: 2025.6.0
:   Fixed a crash in the dataflow engine when C# pointer types are unexpectedly used.

### Coverity CLI 2025.12.0

#### New or changed features

COVCLI-3397
:   It is now possible to commit defect results to both Coverity Connect and the local file system, or to either destination independently. The option `--local` (or the configuration-file section `commit.local`) has been modified to commit results to the file system as well as to Coverity Connect when `commit.connect` is specified, instead of forcing the commit to the file system only.

COVCLI-3790
:   This release introduces a new capture configuration parameter, `capture.delete-stale-tus`, that enables (default) or disables the deletion of all stale translation units (TUs) from the intermediate directory after a capture completes. With `capture.delete-stale-tus` set to `true` (default value) or not specified, after a capture completes, stale TUs are automatically deleted. With `capture.delete-stale-tus` set to `false`, stale TUs are not deleted. For further information, in the *Guide to the Coverity Point and Scan UI and the Coverity CLI*, see "Using the Coverity CLI" > "Options reference" > "Capture configuration" > `delete-stale-tus`.

COVCLI-4078
:   Add Scala support to Coverity CLI.

COVDOCS-1877
:   (See COVCLI-3397.)

#### Bug fixes

COVCLI-3748
:   Reported in version: 2024.9.0
:   Coverity capture would occasionally hang when caching was enabled on Windows. A mitigation has been implemented which may prevent this.

COVCLI-3996
:   Reported in version: 2025.9.0
:   The Coverity CLI will now refuse to commit high fidelity incremental (HFI) results to Connect to prevent the loss of scan results from previous full scans. When HFI results would be committed to Connect, if local results are also configured, then only the local results will be committed. Otherwise, the Coverity CLI will take no action and notify the user with an error message.

COVCLI-4002
:   Reported in version: 2025.3.0
:   JSP source files are now correctly captured for projects which have no maven or gradle project file.

COVCLI-4075
:   Reported in version: 2025.6.0, 2025.6.2
:   Providing a custom compiler configuration to the Coverity CLI previously caused capture of JSP files to fail. This has now been fixed.

COVCLI-4108
:   Reported in version: 2025.9.0
:   Fixed a bug where the wrong working directory was being used when executing the configured clean and build commands.

COVCLI-4133
:   Reported in version: 2025.9.0
:   Fix capture bug where capturing files in a root directory, e.g. files in `Z:\` on Windows or `/` on Unix, resulted in memory exhaustion.

COVCLI-4148
:   Reported in version: 2025.6.2
:   In rare circumstances, the `coverity list` command could fail with a nil pointer dereference. The underlying cause has been fixed and this no longer occurs.

### Coverity Checkers 2025.12.0

For a summary of checkers that have been added or changed in this release, refer to the "Coverity Checker Change History" table in the *Coverity Checker Reference*.

#### End-of-life products

SIGMACOV-858
:   Support for Scala in Coverity Quality checkers has been removed.

#### New or changed features

CCK-2995
:   Added support for xtensa 2023.11 on Linux.

CCK-3000
:   Added support for xtensa 2024.4 on Linux.

CCK-3001
:   Added support for xtensa 2025.5 on Linux.

SAT-9343
:   The `TAINTED_SCALAR` checker now offers the `propagate_taint_on_rshift` option.

SAT-46233
:   Added a new C/C++ checker, `HARDCODED_SECRET`, which finds cases
    where a secret, such as a password, cryptographic key, or token is stored in
    plaintext directly in the source code. This checker is disabled by default.

SAT-46250
:   Improved the `WRAPPER_ESCAPE` checker to avoid reporting false positives when a pointer cannot be stored in a global variable in a call to a function because parameters prevents it.

SAT-47543
:   Fixed a bug where the triage information for `MISRA C-2012` checkers was not getting inherited by equivalent `MISRA C-2023` checkers.

SATSEC-16252
:   The `SSRF` checker now supports C# and VB.

SATSEC-16342
:   The integrated version of PMD has been updated from 7.4.0 to 7.17.0 [Apex].

SATSEC-16344
:   Brakeman Pro for Ruby on Rails security analysis has been upgraded to version 7.1.0

SATSEC-16400
:   Fixed a false positive for the `UNLOGGED_SECURITY_EXCEPTION` checker. [C#]

SATSEC-16407
:   Fixed a false positive for the `RISKY_CRYPTO` checker. [C#]

SATW-6432
:   Fixed false positive for rule MISRA C-2012 Directive 4.7.

SATW-6675, SATW-6750, SATW-6751, SATW-6752, SATW-6768
:   Reimplemented Misra C++ 2023 Rule 7.0.2 to fix FP.

#### Bug fixes

SAT-18922
:   Reported in version: 8.1.0
:   The HARDCODED_SECRET checker now find instances where a password string is compared against hard-coded passwords.

SAT-46375
:   Reported in version: 2024.12.0
:   Fixed a bug in `AUTO_CAUSES_COPY` where the end of a container is copied and then immediately popped is considered a defect.

SAT-46418
:   Reported in version: 2024.9.0
:   Fixed a false positive report in INTEGER_OVERFLOW related to bounds checks not being taken into account when values were cast between signed and unsigned.

SAT-46459
:   Reported in version: 2024.9.0, 2023.12.2
:   The INVALIDATE_ITERATOR checker now handles comparison against std::cend.

SAT-46492
:   Reported in version: 2024.9.0
:   Fixed a bug where `INFINITE_LOOP` would incorrectly track the upper bound with the report_bound_type_mismatch option.

SAT-46575
:   Reported in version: 2024.9.0
:   Fixed an issue that could cause false negatives in desktop analysis with statistical checkers such as `CHECKED_RETURN` or `NULL_RETURNS`, in some cases involving large functions.

SAT-46720
:   Reported in version: 2024.3.0
:   Fixed an `OVERRUN` FP involving unions with 1-byte sized arrays.

SAT-46862, SAT-46872, SAT-46883, SAT-47441
:   Reported in version: 2024.12.0, 2025.3.0
:   Fixed an FN pattern in `RESOURCE_LEAK` involving `shm_open()`.

SAT-46941
:   Reported in version: 2024.12.0
:   A false positive was fixed in INTEGER_OVERFLOW related to clearing the contents of containers.

SAT-47116
:   Reported in version: 2024.6.0
:   Fixed an issue that prevented the `PRECEDENCE_ERROR` checker to report in some cases involving constants, such as `a & constant1 == constant2`.

SAT-47387
:   Reported in version: 2025.3.0
:   Fixed a bug where the primitive `__coverity_no_check_return()` needed to be declared before being used.

SAT-47501
:   Reported in version: 2025.9.0
:   Fixed a bug where some compilers would cause an STL class to incorrectly be considered not part of the STL.

SATW-5355
:   Reported in version: 2023.6.0
:   Fixed False Positive for AUTOSAR C++14 A4-7-1.

SATW-5377
:   Reported in version: 2022.12.0, 2023.9.0
:   Fixed False Positive for AUTOSAR C++14 A12-8-4.

SATW-5381
:   Reported in version: 2022.12.0
:   Fixed False Positive for AUTOSAR C++14 M9-3-3.

SATW-5473
:   Reported in version: 2023.6.0, 2023.12.0
:   Fixed False Positive for Autosar C++14 rule A4-7-1.

SATW-5487
:   Reported in version: 2023.6.0, 2023.12.0
:   Fixed False Positive for AUTOSAR C++14 Rule A9-6-1.

SATW-5509
:   Reported in version: 2023.12.0
:   Fixed False Positive for AUTOSAR C++14 M6-3-1.

SATW-6328
:   Reported in version: 2024.9.0
:   Fixed False Positive for AUTOSAR A0-1-3.

SATW-6545
:   Reported in version: 2024.12.0
:   FP for AUTOSAR C++14 M5-2-6 fixed.

SATW-6620
:   Reported in version: 2025.3.0
:   Fixed False Positive for AUTOSAR C++14 M7-3-1.

SATW-6674
:   Reported in version: 2025.6.0
:   Fixed False Positive for MISRA C++-2023 Rule 7.0.5.

SATW-6676
:   Reported in version: 2025.6.0
:   Fixed False Positive for the MISRA C++-2023 Rule 15.1.4.

SATW-6677
:   Reported in version: 2025.6.0
:   FP Misra CPP 2023 Rule 10.2.3 fixed.

SATW-6693
:   Reported in version: 2025.6.0
:   Fixed False Positives for MISRA C++-2023 Rule 15.0.1 where valid customized destructor having non-empty compound statements were reported.

SATW-6778
:   Reported in version: 2025.9.0
:   Updated MISRA C++-2023 Rule 7.0.5 event description to reflect operand type conversion from original to casted type.

### Coverity Commands 2025.12.0

#### Bug fixes

IM-31346
:   Reported in version: 2023.9.0
:   cov-admin-db.log and cov-archive.log files generation.

IM-33398
:   Reported in version: 2025.6.0, 2025.9.0
:   Internal pagination have been introduced, for users they must be able to get all projects and streams not just limited to 200

#### Known issues and solutions

COVDOCS-1971
:   In Coverity Connect, the `cov-manage-im` command does not accept project names with a special character '%' when using the `--project update` flag.

### Coverity Compilers and Capture 2025.12.0

#### End-of-life products

CAP-2489
:   Support for the win32 Coverity installers (cov-analysis-win32-<version>.exe) have been removed as of 2025.12.0. 32-bit builds can still be captured on 64-bit Windows with a win64 version of Coverity.

CMPGO-533
:   Support for Go 1.23 has been removed as of 2025.12.0.

CMPJ-2459
:   Support for Open JDK 24 and Oracle JDK 24 has been removed as of 2025.12.0.

COVP-2650
:   Support for macOS 13 has been removed as of 2025.12.0.

COVP-2652
:   Support for Windows 10 has been removed as of 2025.12.0.

#### Deprecated products and features

CAP-2497
:   Support for Bazel 6 has been deprecated and will be removed in a future release.

CMPCPP-15451
:   Support for Xcode 12.x-14.x is deprecated as of 2025.12 and will be removed in a future release.

CMPGO-532
:   Support for Go 1.24 is deprecated as of 2025.12.0 and will be removed in a future release.

#### New or changed features

CAP-2471
:   The default mode for build capture used by `cov-build` on platforms other than Windows has changed. No user-visible change is anticipated, but the previous default mode can be used by adding `--original-capture` to the `cov-build` command. If you were previously using the `--new-capture` argument, that argument is no longer necessary and should be removed, as the mode that was enabled by that argument is now the default.

CCK-2671
:   Added support for xtensa 2023.11 on Linux.

CCK-2674
:   Added support for XC-DSC v3.20.

CCK-2679
:   Added support for Paradigm 5.0.

CCK-2684
:   Added support for TI Cl6x version c6000-8.3.12.

CMPCPP-15385
:   cov-build has a new switch --mem-limit that can be used to limit how much memory compilers can use. The compilers will be terminated when they reach the limit. This can be useful to avoid the computer from running out of memory.

CMPGO-494
:   Added support for Go version 1.25.

CMPJ-2456
:   Upgraded Tomcat to 9.0.112.

CMPJ-2461
:   Support for Oracle JDK 25 and Open JDK 25 has been added as of 2025.12.0.

COVP-2655
:   Support for macOS 26 has been added as of 2025.12.0.

#### Bug fixes

CAP-2516
:   Reported in version: 2025.3.0
:   `cov-build --bazel --emit-link-units` no longer causes Bazel to crash with the error message "Error in extend: excessive capacity requested" when capturing certain very large builds.

CAP-2520
:   Reported in version: 2025.3.0, 2025.12.0
:   `cov-build` in `--bazel` mode will now correctly detect compilers that match compiler names given with wildcards in the given configuration.

CCK-2640
:   Reported in version: unspecified
:   Disabled exception for icx compiler by default.

CMPCPP-13272
:   Reported in version: 2022.12.0
:   Fixed compile error reporting unknown type `__int64`, `__int32`, `__int16`, `__int8` when configured for Intel oneAPI compiler on a Linux platform.

CMPCPP-13303
:   Reported in version: 2022.12.2
:   Removed invalid warning remark issued on switch statements.

CMPCPP-14218
:   Reported in version: 2025.9.0
:   Minimize line splitting in compiler error code messages to improve readability in parallel builds.

CMPCPP-15006
:   Reported in version: 2024.12.0
:   Fixed catastrophic failure during device compilation when capturing for Intel OneAPI compiler and using attribute `opencl_constant`.

CMPCPP-15007
:   Reported in version: 2024.12.0
:   Fixed the capture of `__bf16` type when compiling device code using the Intel OneAPI compiler.

CMPCPP-15263
:   Reported in version: 2024.12.0, 2025.6.0
:   Fixed an issue in `cov-emit` where the `restrict` keyword could cause an assertion in some modes.

CMPCPP-15333
:   Reported in version: 2025.9.0
:   Fixed a crash in cov-emit caused by using array delete expressions in Microsoft mode.

CMPCPP-15334
:   Reported in version: 2025.9.0
:   Xtensa compiler support now probes the native compiler to identify TIE datatype automatically. Previously, the compatibility headers contained a static list that needed to be edited for each compiler.

CMPCPP-15345
:   Reported in version: 2024.12.0
:   Eliminated assertion using --emit-complementary-info and type traits builtins like __remove_const.

CMPCPP-15349
:   Reported in version: 2025.9.0
:   cov-emit will now use anonymous memory map by default. This fixes an issue with disk usage spiking on Windows.

CMPCPP-15368
:   Reported in version: 2025.6.0
:   In some circumstances, the type of array elements were not considered used and this was resulting in un-used type false positives. This has been corrected.

CMPCPP-15425
:   Reported in version: 2025.9.0
:   The use of `-x` option to specify code generation target CPU for Intel OneAPI compiler is no longer treated as a skip translation.

CMPFG-1842
:   Reported in version: 2024.9.0
:   In the Kotlin Frontend, fixed the replacement of the kotlin-allopen plugin jar.

CMPGO-586
:   Reported in version: 2025.3.0
:   Resolved an issue causing cov-manage-emit add-other-hosts to fail for go.

CMPPY-438
:   Reported in version: 2024.12.0
:   fixed an issue causing a dead code false positive for Python.

### Coverity Point and Scan 2025.12.0

#### Known issues and solutions

COVGUI-2657
:   The Coverity Point and Scan UI is not supported on macOS 26. Attempts to use the UI on this operating system result in a blank screen with an inability to do anything further. This will be addressed in a future release.

### Rapid Scan Static (Sigma engine) 2025.12.0

#### New or changed features

SIGMACOV-852
:   Sigma analysis is now supported natively on MacOS ARM. Additionally, macOS x86 support for Sigma analysis is deprecated and will be removed in a future release.

SIGMACOV-859
:   Scala support is now available through Rapid Scan Static (Sigma), bundled with Coverity.

#### Bug fixes

SIGMACOV-898
:   Reported in version: unspecified
:   Scala capture is now supported by Sigma, resolving the Coverity AST capture issue.

## Coverity Desktop 2025.12.0

This section provides release notes for Coverity Desktop components.

### Coverity Desktop for Eclipse 2025.12.0

#### End-of-life products

PRD-13226
:   Support for Eclipse 2022-06 has been removed as of 2025.12.0.

#### Deprecated products and features

PRD-13227
:   Support for Eclipse 2022-12 is deprecated as of 2025.12.0 and will be removed in a future release.

#### New or changed features

PRD-13224
:   Added support for Eclipse 2025-09.

## Coverity Documentation 2025.12.0

This section provides release notes for Coverity Documentation components.

### Coverity Documentation 2025.12.0

#### New or changed features

COVDOCS-1847
:   Fixed a documentation issue where a customer was unable to specify analysis configuration values using `cov-analyze-args`. Provided an example of how to use `cov-analyze-args` to specify analysis configuration parameters. In the document, *Guide to the Coverity 2025.12.0 Point and Scan UI and the Coverity CLI*, refer to *Editing configuration settings* > *Analysis configuration* > `cov-analyze-args` .

#### Bug fixes

COVDOCS-1895
:   Reported in version: unspecified
:   The Coverity Checker column in the SEI CERT Java coding standard table has been updated to only reflect supported rules.

COVDOCS-1912
:   Reported in version: 2025.9.0
:   Fixed documentation bug regarding SAML group configuration. SAML SSO configuration parameters now clarifies the following: groups must be manually created in Coverity Connect prior to SAML login, group auto-creation is not supported, and group name in Coverity Connect must match group name in IDP. Changes can be found on this path: Coverity Connect > Coverity Connect administration > Configuring and managing the Coverity Connect server > Sign-on methods for Coverity Connect > SAML SSO configuration parameters.
