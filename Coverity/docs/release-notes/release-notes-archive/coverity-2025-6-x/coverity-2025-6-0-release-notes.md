---
title: "Coverity 2025.6.0 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2025.6.0-release-notes.html"
content_id: "VC3HNsbx~FJAOe9IH4G~Zg"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:19.689648+00:00"
---

# Coverity 2025.6.0 Release Notes

## Important information for 2025.6.0

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

If you are upgrading a Coverity cloud deployment, refer to [Upgrading a Coverity cloud deployment](https://documentation.blackduck.com/bundle/coverity-docs/page/cnc/topics/upgrade-coverity.html) in the Coverity Cloud Deployment Administrator and User Guide. This document provides important information for administrators who are deploying or upgrading Coverity in a Kubernetes container environment.

**Release Highlights**

·     Java 24 is now supported

·     Go 1.24 is now supported

·     PostgreSQL 16.x is now supported

·     Server-Side Request Forgery (SSRF) for Java is GA

·     REVERSE_INVALID_ITERATOR is GA

·     PATH_MANIPULATION for C# is GA

·     URL_MANIPULATION for Java/C# is GA

**NOTE:**

Coverity 2025.6.0 will ship on major platforms
(Mac, 64-bit Windows, 64-bit Linux) and Win32 and Linux32. All other minor
platforms will resume in 2025.9.0.

## Coverity Platform 2025.6.0

This section provides release notes for Coverity Platform components.

### Coverity Connect 2025.6.0

#### Deprecated products and features

COVDOCS-1722
:   Support for Connect coordinator-subscriber has been deprecated in the 2025.6.0 release for Coverity cloud deployments. Coordinator-subscriber has been removed from the *Coverity Cloud Deployment Administrator and User Guide*.

COVDOCS-1759
:   Support for the SOAP API has been deprecated, and will be discontinued in a future version of Coverity. We recommend that you begin the migration to the Coverity Platform REST web services API as soon as possible.

    If you identify a SOAP API feature that does not have equivalent functionality in the REST API, please open a Support case by contacting Black Duck Support at https://community.blackduck.com/s/contactsupport > Submit a Support Case. Create a Community account if you don’t already have one.

### Coverity Report Generators 2025.6.0

#### New or changed features

SATSEC-16223
:   Fixed a false positive for the `CSRF` checker [C#].

## Coverity Analysis 2025.6.0

This section provides release notes for Coverity Analysis components.

### Coverity Analysis - General 2025.6.0

#### New or changed features

SAT-45970
:   Overrun now offers a new option: `report_buffer_size_integer_arithmetic`. This option notifies when the division of a buffer size in bytes is involved in determining the buffer size of a new buffer with a different element type, when the buffer size in bytes is not confirmed to be a multiple of the new buffer's element size. This option is activated in high-aggressiveness mode and needs to be activated explicitly otherwise.

#### Bug fixes

SAT-7308
:   Reported in version: 6.0.2
:   The analysis better tracks the range of a numeric variable through a series of comparisons.

SAT-45616
:   Reported in version: 2023.12.0
:   Fixed CTOR_DTOR_LEAK FP caused by an exception in the destructor.

SAT-45998
:   Reported in version: 2024.3.1
:   Fixed a recoverable analysis issue with message "Unknown class <class>, make sure WUSymbolGatherer finds it." in some desktop analysis cases involving C# or Java generic methods.

SAT-46175
:   Reported in version: 2024.6.0
:   Fixed an issue related to the model of Tee_Malloc.

SAT-46425
:   Reported in version: 2024.9.0
:   USE_AFTER_MOVE will no longer report defects in linked system libraries.

SAT-46625
:   Reported in version: 2024.9.0
:   Fixed an issue where specifying an invalid classification in a defect annotation could cause `cov-format-errors` to crash. Now the invalid annotation is ignored.

SAT-46823
:   Reported in version: 2024.12.0
:   Specifying the `OVERRUN` checker option `aggressive_intervals_in_callees` no longer causes a recoverable exception.

SAT-46909
:   Reported in version: 2024.12.0
:   Fixed a recoverable analysis crash with message `assertion failed: f->index() < agg->inits->size()` in some cases involving unnamed bit fields.

SAT-46981
:   Reported in version: 2024.9.0
:   Some types of recoverable errors with message "Errors detected during evaluation of CodeXM checkers" no longer cause a failure status.

SATSEC-16142
:   Reported in version: 2023.12.2
:   Fixed an issue that caused a crash under `cov-run-desktop`.

SATSEC-16155
:   Reported in version: unspecified
:   Fixed a performance issue with security checkers.

SATSEC-16234
:   Reported in version: 2024.12.0
:   Fixed an analysis crash with the `XSS` checker.

### Coverity CLI 2025.6.0

#### New or changed features

COVCLI-3853
:   The Coverity CLI can now be configured to capture a list of files provided via a file. The new configuration setting is capture.files.include-list-file. Each line of the file specifies the name of the file to capture.

#### Bug fixes

COVCLI-3367
:   Reported in version: 2024.9.0
:   The Coverity CLI now reports an error when both `compiler-configuration` and `language` are specified, since a compiler configuration effectively ignores any language settings.

### Coverity Checkers 2025.6.0

For a summary of checkers that have been added or changed in this release, refer to the "Coverity Checker Change History" table in the *Coverity Checker Reference*.

#### New or changed features

SAT-6789
:   The RESOURCE_LEAK check now reports cases where an allocation happens inside a switch case, controlled by the new checker option track_allocations_in_switches. This option is enabled by default.

SAT-45750
:   Fixed a pattern of NO_EFFECT false positive in JavaScript involving "strict mode" directives and import statements.

SAT-45773
:   When set to `true`, the `USE_AFTER_FREE:report_out_parameter_free` checker option will report a defect whenever a function’s pointer argument is written to and later freed.

SAT-45811
:   Changed the behavior so when the number of defects exceeds the 'count' value specified in a pragma Coverity compliance directive, no defects are deviated. Also, added a new 'count' field to C/C++ code-line annotations that mimics the behavior of the same field for pragma directives.

SAT-46436
:   Improved the handling of small negative numbers in INTEGER_OVERFLOW, to better handle functions that can return a negative error code, but which otherwise only return positive values.

SAT-46524
:   Renamed `MISRA C++ 2023 Dir` checkers to `MISRA C++ 2023 Directive` while retaining compatibility for the previous naming.

SATSEC-13153
:   Added new checker `SSRF` for Java.

SATSEC-16007
:   Improved remediation guidance for the `URL_MANIPULATION` checker. [Java/C#]

SATSEC-16170
:   Improved remediation guidance for the `PATH_MANIPULATION` checker. [C#]

SATSEC-16181
:   Fixed a false positive for the `PATH_MANIPULATION` checker [C#].

SATSEC-16200
:   Fixed a false positive for `PATH_MANIPULATION` [C#].

SATSEC-16242
:   Improved the `MASS_ASSIGNMENT` checker documentation.

#### Bug fixes

SAT-44903
:   Reported in version: 2023.3.0
:   Fixed an `OVERRUN` FP involving unions with 1-byte sized arrays.

SAT-44994, SAT-45044
:   Reported in version: 2023.6.0
:   Fixed an issue which could cause INFINITE_LOOP false positives in C# code.

SAT-45686
:   Reported in version: 2024.6.0
:   Added support for 'fpclassify' in Directve 4.15, MISRA 2012-C.

SAT-45741
:   Reported in version: 2024.3.0
:   Fixed a `FORWARD_NULL` FP by improving the modeling of `EVP_EncryptInit_ex()`.

SAT-46009
:   Reported in version: 2024.6.0
:   Allow INTEGER_OVERFLOW to report multiple defects on the same variable when the variable is overwritten between defects, resetting its state to not overflowed, only to overflow again.

SAT-46200
:   Reported in version: 2020.12
:   Fixed a source of false positives with MISRA C++ 2008 Rule 0-1-10 when the same templated function was instantiated sometimes with a typedef, and sometimes without.

SAT-46272
:   Reported in version: 2024.9.0
:   An issue with DIVIDE_BY_ZERO:not_zero_checked option is fixed. Previously the checker reports FPs in some cases when there is a check in the program whether a divisor is zero.

SAT-46603
:   Reported in version: 2024.9.0
:   Fixed an issue where the `PW.RETURNING_PTR_TO_LOCAL_TEMP` parse warning was sometimes erroneously referred to as `PW.RETURN_PTR_TO_LOCAL_TEMP`.

SAT-46686
:   Reported in version: 2024.12.0
:   Improve the handling of reference-type variables in the INTEGER_OVERFLOW checker.

SAT-46803
:   Reported in version: 2024.12.0
:   Specifying the `OVERRUN` checker option `aggressive_intervals_in_callees` no longer causes a recoverable exception.

SAT-46824
:   Reported in version: 2024.12.0
:   The `INFINITE_LOOP` checker, when the `report_bound_type_mismatch` option is enabled, will consider that largest the enumerator of an enumeration is the maximum value for that type.

SAT-46835
:   Reported in version: 2024.12.0
:   Fixed an issue where the `INFINITE_LOOP` checker might incorrectly assume that bytes are 8 bits in some cases.

SAT-46910
:   Reported in version: 2024.12.0
:   Fixed a source of false positives in the `EXPOSED_NON_CONST_STATIC` checker when declaring a member as `constexpr auto`.

SATSEC-16195
:   Reported in version: unspecified
:   Fix Python defect instability issue due to project name changes.

### Coverity Commands 2025.6.0

#### New or changed features

SAT-14512, SAT-43076, SAT-44745, SAT-46607
:   Improved `cov-format-errors` HTML output to include more information, notably merge key, impact, and CID if available.

SAT-43464
:   `cov-cov-format-errors` now prints a summary of the effect of defect filters to the console.

SAT-46662
:   Fixed an issue in cov-run-desktop when trying to use selection regular expressions with UNIX-style path separators in a Windows environment.

#### Bug fixes

SAT-25891
:   Reported in version: 2017.07
:   The `--strip-path` option now correctly affects `cov-format-errors` HTML output.

SAT-45999, SAT-46850
:   Reported in version: 2023.6.0, 2025.3.0
:   The `--include-missing-locally` feature of `cov-run-desktop` will now include all applicable remote defects. Previously, it would skip some if the reference snapshot had more than 2,500 defects.

### Coverity Compilers and Capture 2025.6.0

#### End-of-life products

CMPGO-531
:   Support for Go 1.22 has been removed as of 2025.6.0.

CMPJ-2347
:   Support for Open JDK 23 has been removed as of 2025.6.0.

#### Deprecated products and features

CAP-2455
:   `cov-setup-bazel-registry` is deprecated as of 2025.6.0 and will be removed in a future release.

CMPGO-530
:   Support for Go 1.23 is deprecated as of 2025.6.0 and will be removed in a future release.

COVP-2641
:   The Win32 Coverity Analysis Installer (cov-analysis-win32) is deprecated as of 2025.6.0 and will be removed in 2025.12.0.

COVP-2644
:   Support for Windows 10 is deprecated as of 2025.6.0 and will be removed in 2025.12.0.

COVP-2646
:   Support for macOS 13 is deprecated as of 2025.6.0 and will be removed in a future release.

#### New or changed features

CAP-2308
:   The Coverity Bazel integration no longer requires any changes to be made to the MODULE.bazel or WORKSPACE files to function.

CAP-2444
:   When capturing Bazel builds, internal Coverity commands are now logged to the build-log.txt to aid in debugging.

CMPGO-493
:   Added support for Go version 1.24.

CMPJ-2360
:   Support for Oracle/Open JDK 24 has been added as of 2025.6.0.

SATSEC-16094
:   Minified JavaScript files are no longer captured or analyzed by default. To re-enable capturing of minified JavaScript, use Coverity CLI setting `emit-minified-js`.

#### Bug fixes

CAP-2429
:   Reported in version: 2025.6.0, 2024.12.1
:   Bazel capture will now correctly resolve header-only dependencies that may have previously been missed.

CAP-2433
:   Reported in version: 2024.6.0
:   Bazel projects that list dependencies in the "data" attribute of rules rather than the "deps" attribute will now be captured.

CMPCPP-13988
:   Reported in version: 2023.6.0
:   Fixed a performance issue that could occur when C or C++ source contained a large number of identifiers that begin with the same 9 characters.

CMPCPP-14660
:   Reported in version: 2022.12.0
:   Addressed an issue with the first line of the primary source file being ignored when using MS PCH files and pre-include options `/FI`. Ignoring the first line could cause capture errors.

CMPCPP-14954
:   Reported in version: 2024.12.0
:   Fixed an issue in the `-Wshadow` command line option in cov-internal-emit-clang that caused it to emit spurious warnings.

CMPCPP-14993
:   Reported in version: 2024.12.0
:   Fixed a stack overflow in the demangler when the mangled name contained a braced expression with a field access.

CMPCPP-15045
:   Reported in version: 2024.12.0
:   A problem replaying a Windows build on Linux (in Polaris) with "file not found" has been fixed.

CMPCPP-15073
:   Reported in version: 2024.12.0
:   Fixed failure to emit when using clang based compiler, --emit-complementary-info and a vector type with attribute **ext_vector_type** where either the base type and/or the number of element are template dependent.

CMPCPP-15097
:   Reported in version: 2024.12.0
:   Fixed an issue where the wrong C++ dialect would be specified for Xcode versions 10.0 and later.

CMPFG-1544
:   Reported in version: 2024.12.0
:   In the Kotlin Frontend, handle compile-time constant values containing errors

### Rapid Scan Static (Sigma engine) 2025.6.0

#### End-of-life products

SIGMACOV-725
:   The `--disable-sigma-telemetry` option to `cov-analyze` has been deprecated and removed.

#### Bug fixes

SIGMACOV-763
:   Reported in version: unspecified
:   Fixed an issue where Coverity may have had recoverable errors when analyzing an idir on a Windows virtual drive.

## Coverity Desktop 2025.6.0

This section provides release notes for Coverity Desktop components.

### Coverity Desktop for Eclipse 2025.6.0

#### End-of-life products

PRD-13203
:   Support for Eclipse 2021-12 has been removed as of 2025.6.0.

#### Deprecated products and features

PRD-13204
:   Support for Eclipse 2022-06 is deprecated as of 2025.6.0 and will be removed in a future release.

#### New or changed features

PRD-13200
:   Added support for Eclipse 2025-03.

### Coverity Desktop for Microsoft Visual Studio 2025.6.0

#### Bug fixes

PRD-13199
:   Reported in version: 2025.3.0
:   Fixes the Visual Studio macro "DevEnvDir" being "Undefined".

## Coverity Documentation 2025.6.0

This section provides release notes for Coverity Documentation components.

### Coverity Documentation 2025.6.0

#### Deprecated products and features

PRD-13196
:   The Win32 Coverity plugins are deprecated as of 2025.6.0 and will be removed in 2025.12.0.

#### Bug fixes

COVDOCS-1777
:   Reported in version: 2025.3.0
:   In the Coverity cloud deployment 2024.9.0 release, the Coverity Connect web app administrator default password was changed, and the 2024.9.0 release supports a new Web application administrator password feature that enables you to create and change the Web application administrator password. The *Coverity Cloud Administrator and User Guide* for the current 2025.6.0 release highly recommends that you change the password during initial deployment. Otherwise, to re-connect to the web app as administrator, you will need to manually create a password secret or contact Black Duck Software for the default password.
