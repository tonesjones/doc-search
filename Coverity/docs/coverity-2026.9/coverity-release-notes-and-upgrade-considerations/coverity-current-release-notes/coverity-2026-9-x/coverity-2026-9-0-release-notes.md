---
title: "Coverity 2026.9.0 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/coverity-2026.9.0-release-notes.html"
content_id: "KFHd6nsj5sbjH~Qw_oEiLQ"
version: "2026.9"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-10-04T23:39:43.176896+00:00"
---

# Coverity 2026.9.0 Release Notes

## Important information for 2026.9.0

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://docs.blackduck.com/r/coverity/latest/coverity-documentation/coverity-upgrade-considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

If you are upgrading a Coverity cloud deployment, refer to [Upgrading a Coverity cloud deployment](https://docs.blackduck.com/r/coverity/latest/coverity-documentation/upgrading-a-coverity-cloud-deployment.html) in the Coverity Cloud Deployment Administrator and User Guide. This document provides important information for administrators who are deploying or upgrading Coverity in a Kubernetes container environment.

## Coverity Platform 2026.9.0

This section provides release notes for Coverity Platform components.

### Coverity Connect 2026.9.0

#### New or changed features

COVCLI-4497
:   Coverity AI triage is now compatible with systems with glibc 2.28 and newer.

COVDOCS-2222
:   Added Coverity Checker Policy Enforcement (CEP). CEP gives administrators a centralized way to define and enforce analysis configuration requirements across teams and projects. Administrators create YAML or JSON policy files that specify required checkers, checker sets, coding standards, and analysis settings, and apply them at the global or project level. At commit time, Coverity Connect checks whether the scan configuration satisfies the effective policy and can reject or warn on non-compliant scans.

COVDOCS-2244
:   The Modern UI introduces a redesigned Projects Landing Page as the default view after login. Projects are displayed as cards that surface key health indicators, including Security Impact and Quality Impact summaries, giving users an at-a-glance status of each project. Users can search, filter, and sort projects to quickly locate the project they need.

COVDOCS-2245
:   The Modern UI now includes a Streams View, accessible from the new Projects Landing Page. This view presents all streams within a project in the Coverity hierarchy, providing an at-a-glance status of each stream. Users can search, filter, and sort the stream list.

#### Bug fixes

COVCLI-4637
:   Reported in version: 2026.6.0
:   Fix issue where AI triage did not work correctly with Open AI models.

COVGUI-2704
:   Reported in version: 2026.3.0
:   Previously, when a user attempted to scan a new project on a Coverity Connect account containing more than 200 projects, the scan setup could fail with the error:

    A filter for one of the following attributes is required: 'name' or 'project-name'

    This occurred because the UI fetched only the first page of Connect projects when resolving a project by ID. If the target project fell beyond the default page limit, the lookup returned no result, causing the subsequent stream search to be issued without a required filter parameter.

    The UI now paginates through all available Connect projects when resolving a project by ID, ensuring projects are found regardless of their position in a large account.

## Coverity Analysis 2026.9.0

This section provides release notes for Coverity Analysis components.

### Coverity Analysis - General 2026.9.0

#### Deprecated products and features

COVDOCS-2224
:   The following JavaScript/TypeScript security checkers are deprecated as of Coverity 2026.9.0 and will be removed in a future release:

    - ANGULAR_EXPRESSION_INJECTION
    - ANGULAR_SCE_DISABLED
    - CONFIG.ENABLED_DEBUG_MODE
    - CONFIG.HANA_XS_PREVENT_XSRF_DISABLED
    - CONFIG.HARDCODED_CREDENTIALS_AUDIT
    - CONFIG.HARDCODED_TOKEN
    - CONFIG.VUE_ROUTER_PARAMS_EXPOSED_TO_PROPS
    - CSRF
    - DF.CUSTOM_CHECKER
    - DNS_PREFETCHING
    - EXPRESS_WINSTON_SENSITIVE_LOGGING
    - LOCALSTORAGE_WRITE
    - MISSING_AUTHZ
    - UNLESS_CASE_SENSITIVE_ROUTE_MATCHING
    - XML_EXTERNAL_ENTITY

COVDOCS-2243
:   The XML_INJECTION checker is deprecated for the Python language. Python support will be removed in a future release.

#### New or changed features

COVDOCS-2214
:   Groovy support is now available through Rapid Scan Static (Sigma), bundled with Coverity.

COVDOCS-2238
:   Starting in Coverity 2026.9, the Issues View (Modern UI) displays a notification when LLM errors occur during analysis of AI-augmented SAST checkers.

SAT-47388
:   Upgraded Flexnet support on Windows. It will require the `lmgrd` server to be upgraded, otherwise you may get "Bad message command" errors.

SAT-48178
:   Added models for std::filesystem::path.

SATSEC-16658
:   Added support for the DGS framework [Java].

SIGMACOV-911
:   The --sigma-config-file option has been removed from cov-analyze. Users should specify sigma configuration options via the coverity.yml config file instead.

#### Bug fixes

SAT-48228
:   Reported in version: 2026.3.0, 2025.6.2
:   Fixed a bug in which cov-analyze would incorrectly treat a non-pointer type as a pointer type while processing Java array types, causing an assertion failure and crash.

SAT-48249
:   Reported in version: 2025.9.0, 2025.12.0
:   Fixed issues that could occur when analysing extremely large IDIRs.

SATSEC-16716
:   Reported in version: unspecified
:   The builtin `URLSearchParams` is now a recognized dataflow passthrough in JavaScript.

SATW-7250
:   Reported in version: unspecified
:   Standardised capitalization across MISRA C++ 2023 checker subcategory descriptions for improved consistency and readability.

### Coverity CLI 2026.9.0

#### New or changed features

COVCLI-4290
:   The `coverity verify-compliance` command can be used to verify that a proposed analysis complies with the effective checker policy in Coverity Connect.

COVCLI-4403, COVDOCS-2186
:   The Coverity CLI now recognizes {{groovy}} as a supported language for buildless capture. {{groovy}} files can be included or excluded using {{groovy}} as the language key — for example, {{capture.languages.include: [groovy]}} in {{coverity.yaml}}, or {{--language groovy}} on the command line.

COVCLI-4546
:   The Coverity CLI now recognizes {{rust}} as a supported language for build capture. {{rust}} files can be included or excluded using {{rust}} as the language key — for example, {{capture.languages.include: [rust]}} in {{coverity.yaml}}, or {{--language rust}} on the command line.

COVDOCS-2257
:   (See COVCLI-4546)

### Coverity Checkers 2026.9.0

For a summary of checkers that have been added or changed in this release, refer to the "Coverity Checker Change History" table in the *Coverity Checker Reference*.

#### New or changed features

COVDOCS-2263, SAT-47742
:   CONSTANT_EXPRESSION_RESULT checker will now report scenarios where a bit-wise `&` was used and resulted in 0, suggesting that the wrong operation was done.
    By default, it only considers statements with enumerator operands, but all integrals will be considered if the checker flag `report_any_constant_int_bitwise_and_is_zero` is enabled.
    Masking macros and byte-reordering macros are excluded from this defect reporting.

SAT-44759
:   Added new option `report_on_negative_constant` for `NEGATIVE_RETURNS` (defaults to false) which determines whether or not the checker reports when using negative constants as a parameter. The checker will also no longer report on iterator arithmetic.

SAT-47402
:   The NON_POD_BYTE_ACCESS checker detects cases where the memory of variables that are not Plain Old Data (POD) types is accessed directly. This checker applies to C++ code.

    Non-POD types include any `class` or `struct` that has one or more of the following characteristics:

    1. A non-default constructor or destructor
    2. Private members or member functions
    3. Virtual functions
    4. Inherits from another class or struct
    5. Contains non-POD members
    6. Is templated or contains templated member functions

SAT-48058
:   Added a new checker, WRITE_IMMUTABLE, which detects cases where an immutable reference in Rust may be written to.

SAT-48062
:   Created a new overflow sink for Rust. When a C function is called from an unsafe Rust block and its parameters are cast to narrower types than the original Rust types from which they originated, a defect is now reported.

SAT-48075
:   Checkers CHECKED_RETURN and NULL_RETURNS now support Rust, including when calling C function via Rust ffi.

SAT-48385
:   The HARDCODED_SECRET checker may be enabled via the `--security` or the `--all-security` options for C/C++, CUDA and Objective C/C++.

SATW-7100
:   Added securityImpact for compliance standards: MISRA C-2012, MISRA C-2023, MISRA C-2025, CERT C, CERT CPP , CERT C-Recommendation and CERT Java. The securityImpact field is set for rules which are supported.

#### Bug fixes

SAT-43812, SAT-47946
:   Reported in version: 2022.12.1
:   Fixed a source of false positives for the UNINIT and UNINIT_CTOR checkers that occurred when member initialization was performed through a downcast, most commonly in code using the Curiously Recurring Template Pattern (CRTP).

SAT-47521
:   Reported in version: unspecified
:   Fixed a false positive in MISRA C-2023 Rule 9.1 involving padding being considered uninitialized for compilers using versions after C99 and C++03.

SAT-47532
:   Reported in version: 2025.9.0
:   Fixed a false positive in FORWARD_NULL that could occur when accessing an element of a vector that was initially created empty and populated later.

SAT-47563
:   Reported in version: 2025.12.0
:   The HARDCODED_SECRET checker now reports defects when std::string_view objects are compared with string literals in C++.

SAT-47649
:   Reported in version: 2025.12.0
:   The HARDCODED_SECRET checker no longer reports false positive defects for strings that use C-style or Rust-style format specifiers. It also suppresses false positives for strings that resemble XML namespaces and other patterns that are clearly not secrets.

SAT-48097
:   Reported in version: 2025.9.0
:   Fixed an issue in `INCOMPLETE_DEALLOCATOR` that could cause it to fail to recognize certain deallocations when followed by NULL reassignments.

SAT-48325
:   Reported in version: 2026.6.0
:   Reporting class member functions that should be made `const` per MISRA C-2004 Rule 16.7 and CERT DCL13-C has been restored.

SAT-48365
:   Reported in version: 2026.6.0
:   Fixed a bug where the checker option RULE_OF_ZERO_THREE_FIVE:ignore_virtual_dtor could not be turned off with high aggressiveness.

SAT-48386
:   Reported in version: 2026.6.0
:   Fixed an issue where conflicting sub-categories occurred when BAD_EXIT or INSECURE_COOKIE defects were committed using `cov-commit-defects`.

SAT-48387
:   Reported in version: 2026.6.0
:   Fixed a false positive for UNCAUGHT_EXCEPT on std::format().

SAT-48390
:   Reported in version: 2026.3.0
:   Fixed an analysis recoverable crash with message "construction from null is not valid" in some cases involving the UNNECESSARY_STRING_COPY checker and unnamed types.

SAT-48426
:   Reported in version: 2026.9.0
:   The HARDCODED_SECRET checker now ignores dummy credentials that are used in a string representing a URI (ex: `htttps://username:password@myexample.com`).

SAT-48436
:   Reported in version: 2026.9.0
:   The HARDCODED_SECRET checker has been improved by removing false positives where secrets are not returned by function calls in some contexts.

SAT-48465
:   Reported in version: 2026.6.0
:   Fixed a recoverable analysis crash involving the UNNECESSARY_STRING_COPY checker and function pointers.

### Coverity Commands 2026.9.0

#### New or changed features

SAT-48104
:   The `cov-format-errors` command can now generate a new version of JSON defects, which includes a `securiyImpact` value.

#### Bug fixes

SAT-46793
:   Reported in version: 2024.12.0
:   Added a new option enable/disable-receiver-interface-escape for cov-analyze (enabled by default) that suppresses RESOURCE_LEAK defects in C# involving unresolvable receiver objects.

### Coverity Compilers and Capture 2026.9.0

#### End-of-life products

CMPJ-2542
:   Support for Oracle/Open JDK 17 has been removed as of 2026.9.0.

#### Deprecated products and features

CAP-2702
:   Support for Oracle/Open JDK 1.8 is deprecated as of 2026.9.0 and will be removed in a future release.

CMPCPP-15609
:   ARM and Keil 5.x have been deprecated.

CMPCSH-2189
:   Support for .NET 9 is deprecated as of 2026.9.0 and will be removed in a future release.

CMPCSH-2194
:   Support for .NET 8 is deprecated as of 2026.9.0 and will be removed in a future release.

CMPJ-2541
:   Support for Oracle/Open JDK 26 is deprecated as of 2026.9.0 and will be removed in a future release.

#### New or changed features

CAP-2648
:   Capture of Bazel projects using the `--bazel` option to `cov-build` has been improved to better handle unusual dependency types automatically, so passing `--bazel-extra-dep-type` is no longer necessary or useful in any situation.

CMPCPP-15308
:   Added support for GCC 16 in 2026.9.

CMPCPP-15614
:   The latest HighTec compiler is now Clang-based and uses the compiler type hightec:clang.

CMPCPP-15616
:   We now support Microchip XC32 up to 5.1.

CMPCPP-15617
:   We now support Microchip XC8 up to 3.10.

CMPCPP-15676
:   Added support for Analog SHARC 9.0.4.0.

CMPCPP-15759
:   Support for C++23 coroutines has been improved.

CMPCPP-16028
:   Limited support has been added for NonStop HPE C/C++ Cross Compiler. If you are interested, contact support.

COVDOCS-2275
:   Support added for ECMAScript 16 (JavaScript 2025).

COVDOCS-2276
:   Support for TypeScript 5.3 to 6.0 has been added as of 2026.9.0.

#### Bug fixes

CAP-2617
:   Reported in version: 2024.12.0
:   Unconfigured compiler detection will no longer cause cov-build to fail when an unreadable binary is executed during the build.

CAP-2646
:   Reported in version: 2024.9.0
:   Unconfigured compiler detection will no longer cause cov-build to fail if a build tries to execute a directory.

CAP-2669
:   Reported in version: 2025.12.0, 2026.3.0
:   The Coverity Bazel integration now properly handles the presence of a `--` argument in Bazel commands.

CAP-2681
:   Reported in version: 2026.3.0
:   The Coverity Bazel installation now works correctly when Coverity is installed to a directory that has spaces in its path.

CAP-2683
:   Reported in version: 2025.12.0
:   Capture will no longer cause builds to intermittently fail with permission errors if there are elements in the PATH environment variable that are not readable by the user.

CAP-2704
:   Reported in version: 2026.3.0
:   Capture will no longer routinely cause a segfault when capturing some programs built against Qt 6.4 or 6.5 using Qt's QProcess class to launch subprocesses on Linux.

CMPCPP-15251
:   Reported in version: 2025.3.0
:   Fixed an issue with GCC compilers prior to version 12 where redeclaring a name in an anonymous namespace could cause recoverable errors.

CMPCPP-15837
:   Reported in version: unspecified
:   The use of some C++23 in `chrono` and `format` system headers are now recognized by cov-emit.

CMPCPP-16001
:   Reported in version: 2026.6.0
:   Eliminated the following assertion in Clang support:

    `Assertion failed: (!isNull() && "Cannot retrieve a NULL type pointer"),`

CMPCSH-2195
:   Reported in version: unspecified
:   Coverity C# analysis no longer fails to translate methods that use C# 12 primary constructors with nested local functions or lambdas.

## Coverity Desktop 2026.9.0

This section provides release notes for Coverity Desktop components.

### Coverity Desktop for Eclipse 2026.9.0

#### End-of-life products

PRD-13256
:   Support for Eclipse 2023-03 has been removed as of 2026.9.0.

#### Deprecated products and features

PRD-13257
:   Support for Eclipse 2023-09 is deprecated as of 2026.9.0 and will be removed in a future release.

#### New or changed features

PRD-13254
:   Added support for Eclipse 2026-06.
