---
title: "Coverity 2026.6.0 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2026.6.0-release-notes.html"
content_id: "RDHCk5F_XkFkzSlyoXSKMA"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:08.026742+00:00"
---

# Coverity 2026.6.0 Release Notes

## Important information for 2026.6.0

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://docs.blackduck.com/r/coverity/latest/coverity-documentation/coverity-upgrade-considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

If you are upgrading a Coverity cloud deployment, refer to [Upgrading a Coverity cloud deployment](https://docs.blackduck.com/r/coverity/latest/coverity-documentation/upgrading-a-coverity-cloud-deployment.html) in the Coverity Cloud Deployment Administrator and User Guide. This document provides important information for administrators who are deploying or upgrading Coverity in a Kubernetes container environment.

**Release highlights**

- Hyundai 4.1 coding standards for C, C++, and Java are now supported.
- Java 26 is now supported.
- Go 1.26 is now supported.
- Visual Studio 2026 is now supported.
- The Rust language is now supported as a beta feature.
- Clang compilers versions 21 and 22 are now supported.

Please see below for full details of these and other enhancements included in this release.

## Coverity Platform 2026.6.0

This section provides release notes for Coverity Platform components.

### Coverity Connect 2026.6.0

#### New or changed features

IM-30951
:   The new API is an upgrade to the get snapshots for a stream as they result in the latest snapshot delivery

#### Bug fixes

IM-33787
:   Reported in version: unspecified
:   Fixed a thread-safety issue in Coverity commit preview / cov-run-desktop that could cause a ConcurrentModificationException during parallel preview commits when logging was enabled.

IM-34080
:   Reported in version: 2025.6.0
:   Fixed an issue where the admin user could be removed from the Administrators group via the Users tab (Configuration → Users & Groups → Users). The Remove button is now disabled for the admin user in the Administrators group, ensuring consistent behavior across both the Users and Groups management interfaces.

IM-34203
:   Reported in version: unspecified
:   Fixed a NullPointerException in Coordinator CIM synced-history processing caused by merged defects with missing accretion_id.

IM-34221
:   Reported in version: 2025.12.0
:   Resolved an issue where the Trends view was visible to users without the "View project history and dashboard" permission. The Trends and Snapshot views are now correctly hidden for users who lack this permission.

IM-34280
:   Reported in version: unspecified
:   Eliminated a continuous refresh issue in the "Snapshots | All In Project" view of the Connect UI, which could be triggered by rapid snapshot selection. This fix prevents unintended page reload loops and URL toggling, resulting in a more stable and responsive user experience.

IM-34285
:   Reported in version: unspecified
:   Fixed a `cov-commit` failure due to OutOfMemory error on `xref_symbolset` query.

IM-34323
:   Reported in version: 2026.3.0, 2025.6.2
:   Upgraded the bundled Apache Tomcat from version 10.1.52 to 10.1.55 to address security vulnerabilities CVE-2026-29145 and CVE-2026-29146.

IM-34440
:   Reported in version: 2026.3.0
:   Performance issues were identified in the API due to N+1 query patterns across multiple execution paths, particularly impacting customers with a large number of roles configured. The APIs have now been optimised to eliminate these N+1 queries, resulting in improved scalability and significantly better performance for high-volume role setups.

### Coverity Report Generators 2026.6.0

#### Bug fixes

IM-34322
:   Reported in version: 2026.3.0, 2025.6.2
:   Upgraded the bundled Apache Log4j library from version 2.17.1 to 2.25.3 in Report Generation to address security vulnerability CVE-2025-68161.

RG-1941
:   Reported in version: 2024.6.0, 2025.6.0, 2025.9.0
:   Fixed an issue where the Coverity Security Report generator GUI tool failed to import all values from a YAML configuration file. The tool now correctly populates all configuration fields when loading a saved configuration.

RG-1950
:   Reported in version: 2024.12.0
:   Fixed an issue where cov-generate-misra-report failed to generate a MISRA report when the snapshot contained no MISRA violations. The tool now correctly generates a report even when zero violations are found.

RG-1984
:   Reported in version: unspecified
:   Fixed data inconsistencies between the Coverity Integrity Report and Security Report for the CWE/SANS Top 40 list so that counts now match across both reports.

RG-2016
:   Reported in version: 2025.12.2
:   Fixed issue with MISRA rule descriptions containing unwanted tags.

## Coverity Analysis 2026.6.0

This section provides release notes for Coverity Analysis components.

### Coverity Analysis - General 2026.6.0

#### Deprecated products and features

COVDOCS-2127
:   Support for the following frameworks will be removed in a future release: Apache Struts 1, Struts 1 XML, Apache Axis 1, Direct Web Remoting (DWR), Apache Tiles, Terasoluna BLogic, and ASP.NET Web Forms.

COVDOCS-2128
:   Support for the following frameworks will be removed in a future version: Apache Struts 1, Apache Flex/BlazeDS, Apache iBATIS, Apache Axis 1, Apache Xindice, Castor XML/ORM, jCouchDB, and Netscape LDAP SDK.

COVDOCS-2129
:   Support for the following frameworks will be removed in a future release: AngularJS (Angular 1.x) and Angular platform-webworker.

COVDOCS-2130
:   Support for the following frameworks will be removed in a future release: ASP.NET Core, ASP.NET Web Forms, and Noesis.Javascript.

COVDOCS-2131
:   Support for the following Python 2-specific modules and frameworks will be removed in a future release: cPickle, cStringIO, urllib2, urlparse, mimetools, rfc822, strop, cookielib, httplib, httplib2, Fabric v1, and legacy Django APIs.

COVDOCS-2132
:   Support for ASP.NET Web Forms and ASPX page analysis will be removed in a future release. This includes Web Forms entry point detection, Web Forms-specific directives, and the CONFIG.ASP_VIEWSTATE_MAC and CONFIG.DEAD_AUTHORIZATION_RULE checkers. Customers using ASP.NET Web Forms should plan to migrate to Blazor, Razor Pages, or ASP.NET Core MVC.

COVDOCS-2133
:   The XML_EXTERNAL_ENTITY checker for Go and Kotlin is deprecated as of 2026.6.

COVDOCS-2134
:   Python support for the MISSING_AUTHZ checker is deprecated and will be removed in a future release.

COVDOCS-2135
:   Python support for the CSRF checker is deprecated as of 2026.6.0.

COVDOCS-2161
:   Support for updating the Sigma binary used by `cov-analyze` through the `--update-sigma-binary` or `--use-sigma-binary` options has been deprecated and will be removed in a later release.

COVDOCS-2175
:   Support for Hyundai C 4.0, Hyundai C++ 4.0, and Hyundai Java 4.0 will be removed in 2026.9.0.

#### New or changed features

COVCLI-4510
:   In the 2026.6.0 release, a new Coverity MCP Server is available that can be used to scan code for issues using a coding agent with MCP server support.

COVCLI-4513
:   The AI-assisted triage service requires either Anthropic Claude Sonnet 4.6 or OpenAI ChatGPT 5.4. Other LLM models are not currently supported.

COVDOCS-2064
:   Added support for Hyundai C 4.1, Hyundai C++ 4.1, and Hyundai Java 4.1 in the Connect UI and Report Generator.

COVDOCS-2145
:   Added beta support for Rust. Rust projects built with cargo can now be captured using cov-configure --rust and cov-build. Supported on Linux (64-bit and ARM64), macOS (Apple Silicon), and Windows (64-bit).

SAT-47280
:   Assigning to `*this` while returning it in the `return` statement of the `operator=` member function is no longer reported as a defect.

SAT-48005
:   Added MISRA C-2025 support to HIS metric analysis.

SAT-48036
:   Added a new option to `cov-analyze`, `--cra`, to enable checkers relevant to the EU Cyber Resilience Act.

#### Bug fixes

CMPCPP-15667
:   Reported in version: 2025.12.0, 2025.9.0
:   Fixed merge of emits with precompiled headers.

SAT-47967
:   Reported in version: 2025.12.0
:   Improved the error message when the stream language doesn't match the source code language to be more readable.

SAT-48137
:   Reported in version: 2026.6.0
:   Fixed a behavior that might allow the `--output-tag` option to create new directories, possibly even outside of the intermediate directory. Output tags are now forbidden from containing directory separator characters.

### Coverity CLI 2026.6.0

#### New or changed features

COVCLI-3689
:   The Coverity CLI now automatically configures sccache as a prefix compiler for build capture, enabling C/C++ analysis for projects that use sccache as a compiler cache without requiring manual cov-configure invocations.

COVCLI-4193
:   Added SQL as a supported language for buildless capture in the Coverity CLI. SQL files can be included or excluded using `sql` as the language key — for example, `capture.languages.include: [sql]` in `coverity.yaml` or `--language sql` on the command line.

COVCLI-4287
:   Added support for three new coding standards in the Coverity CLI: Hyundai C 4.1 (hyundai-c-4.1), Hyundai C++ 4.1 (hyundai-cpp-4.1), and Hyundai Java 4.1 (hyundai-java-4.1). Each standard supports the `all` and `all-deviations` pre-canned configurations.

COVCLI-4336
:   The Coverity CLI supports a new boolean configuration setting, `analyze.checkers.cra`, and a corresponding `--cra` CLI flag, which enables EU Cyber Resilience Act (CRA) analysis mode.

#### Bug fixes

COVCLI-4355
:   Reported in version: unspecified
:   Thin client HFI analysis with caching disabled could previously fail when TUs changed due to replay. This has now been fixed.

### Coverity Checkers 2026.6.0

For a summary of checkers that have been added or changed in this release, refer to the "Coverity Checker Change History" table in the *Coverity Checker Reference*.

#### Deprecated products and features

COVDOCS-2045
:   The SIZECHECK checker is deprecated. As of release 2026.6, we recommend using
    BUFFER_SIZE, SIZEOF_MISMATCH, or STRING_NULL instead.

COVDOCS-2121
:   The `--enable-callgraph-metrics` option has been deprecated for Kotlin, Go, Python, and JS/TS.

COVDOCS-2166
:   The `check_ssl_session` checker option has been removed from the BAD_CERT_VERIFICATION checker.

#### New or changed features

COVDOCS-2080, SAT-47212
:   Constants whose value is known at compile-time will no longer be reported as unused for MISRA C++ 2023 Rule 0.1.1 or when UNUSED_VALUE checker configuration would previously have reported it.
    To restore, use medium or above aggresiveness or enable "report_unused_constant_variables" checker flag.

COVDOCS-2112
:   A new Rust checker UNNECESSARY_PANIC has been added.

COVDOCS-2144
:   The new BAD_EXIT checker finds instances where the program exits and returns a non-portable exit code.

COVDOCS-2154
:   Added support for all Hard Coded Secrets (HSS) checkers across all languages in the AI-Assisted Triage Plug-in. The following checkers are now supported: HARDCODED_CREDENTIALS, HARDCODED_SECRET, and SIGMA.hardcoded_secret.

SAT-46755
:   The WRAPPER_ESCAPE checker will look for uses of a C++ shallow container (string_view or span) where the container outlives the owner of the data.

SAT-47215
:   MISRA C++ 2023 Rule 10.1.1 checker no longer considers the implicit `this` parameter for whether the function should be marked `const` or not.

SAT-47353
:   The following checkers are supported for Rust (beta version): BAD_EXIT, BAD_SHIFT, COPY_PASTE_ERROR, DIVIDE_BY_ZERO, HARDCODED_SECRET, INSECURE_COOKIE, INTEGER_OVERFLOW, SECURE_TEMP, SWAPPED_ARGUMENTS, TAINTED_STRING, USELESS_CALL.

    Also, a new Rust-specific checker is available: UNNECESSARY_PANIC.

    For the Rust beta release, all these checkers are enabled by default.

SAT-47460
:   MISRA C++ 2023 Rule 10.1.1 checker will no longer report class member functions that can be made `const`.

SAT-47809
:   The RESOURCE_LEAK checker will now report on certain patterns when a pointer is assigned a NULL value and that pointer is later freed without being reassigned to a non-NULL value on any path.

SATSEC-16560
:   Brakeman Pro for Ruby on Rails security analysis has been upgraded to version 8.0.3.

SATW-6772
:   New Risk assessment values have been supported in language standards for Hyundai 4.1.

SATW-6875
:   Added support for Hyundai version 4.1 language standards for C, C++, and Java.

#### Bug fixes

COVDOCS-2162
:   Reported in version: 2026.3.0
:   The default value of INTEGER_OVERFLOW:report_unsigned_underflow_cast_to_signed is true and is not affected by aggressiveness.

SAT-24659, SAT-46219, SAT-47569
:   Reported in version: 2017.07 , 2024.6.0, 2025.9.0
:   Fixed a source of UNINIT false positives when using value-initialization syntax in the presence of a non-user-provided constructor, such as when using `= default` or non-static data member initializers.

SAT-44166
:   Reported in version: 2022.12.0
:   Fixed a source of USE_AFTER_MOVE false positives when using `move` within an `initializer_list`.

SAT-45938, SAT-46120, SAT-46197, SAT-46624, SAT-46828, SAT-46917, SAT-47187, SAT-47714
:   Reported in version: 2024.12.0, 2024.6.0, 2024.6.1, 2025.6.0
:   Added a handling for the case where a `unique_lock` is explicitly unlocked before its destructor is called. Fixing a LOCK double unlock false positives.

SAT-46531
:   Reported in version: 2024.12.0
:   Fixed an issue where the OVERRUN checker was unable to track `strlen` values when used under `+=`.

SAT-46628
:   Reported in version: 2024.6.0
:   Fixed the handling of `static constexpr` objects when applying the One Definition Rule.

SAT-46802
:   Reported in version: 2024.9.0, 2024.12.0
:   Fixed a bug in OVERRUN's `aggressive_intervals_in_callees` option that would cause the checker to lose track of the value of parameters used in array access.

SAT-47084
:   Reported in version: 2025.3.0
:   NULL_RETURNS now recognizes C# unit assertions such as `Is.Not.Null`. Certain FPs due to failure to consider such assertions are now eliminated.

SAT-47236
:   Reported in version: 2024.9.0
:   Added handling for increment and decrement operators on floating-point numbers in the DIVIDE_BY_ZERO checker.

SAT-47449
:   Reported in version: 2025.6.2
:   Fixed an issue that could cause OVERRUN false positives where the claimed access index was incorrect.

SAT-47605
:   Reported in version: 2025.9.0
:   Fixed a source of OVERRUN false positives at high aggressiveness level (`aggressive_intervals_in_callees` option) when a function checks a fixed bound on one of its parameters. In that case, we could incorrectly infer that the bound was reached even if the corresponding argument is a known constant.

SAT-47993, SAT-47994
:   Reported in version: 2025.12.0, 2026.3.0
:   Fixed an UNNECESSARY_STRING_COPY false positive related to the creation of temporary strings that are later moved.

SAT-48021
:   Reported in version: 2026.3.0
:   HARDCODED_SECRET has been improved for finding secrets through data-flow (ex: with assignments).

    For example:

    const char *s = "Cov3r!tY";

    const char *passwd = s;

SAT-48033
:   Reported in version: 2025.12.1
:   Fixed a crash in UNNECESSARY_STRING_COPY when encountering an anonymous variable.

SAT-48094
:   Reported in version: 2025.9.0, 2025.12.0
:   Fixed a crash in UNNECESSARY_STRING_COPY when strings were passed to varargs functions.

SATSEC-16522
:   Reported in version: unspecified
:   Fixed a false negative for SQL_NOT_CONSTANT. [Java/C#]

SATSEC-16530
:   Reported in version: unspecified
:   Improved dataflow handling of the SQLI checker when audit mode is turned on.

SATSEC-16605
:   Reported in version: unspecified
:   Fixed a crash with the framework analyzer.

SATSEC-16642
:   Reported in version: unspecified
:   Fixed a false positive in SENSITIVE_DATA_LEAK where cryptographic IVs and nonces were incorrectly treated as sensitive data.

SATSEC-16643
:   Reported in version: unspecified
:   Fixed a false positive in HARDCODED_CREDENTIALS where a character-pool string accessed via charAt with a runtime index was incorrectly reported as a hardcoded password.

SATW-4986
:   Reported in version: 2022.3.1
:   Fixed False Positive for CERT C Rule INT30-C.

SATW-5126, SATW-5127, SATW-5131, SATW-6382, SATW-6537, SATW-6658
:   Reported in version: 2022.3.1, 2022.6.0, 2024.12.0, 2024.12.0, 2025.6.0, 2024.9.0
:   Fixed False Positive for CERT C Rule INT31-C.

SATW-5358, SATW-5750
:   Reported in version: 2023.6.0, 2023.6.0, 2023.12.0
:   Fixed False Positive for CERT CPP Rule CTR50-CPP.

SATW-5498
:   Reported in version: unspecified
:   Fixed False Positive for CERT-C++ DCL51-CPP.

SATW-6872
:   Reported in version: 2025.12.0
:   Fixed False Positive case related to enum type for MISRA C++-2023 Rule 10.2.3.

SATW-6980
:   Reported in version: unspecified
:   Fixed False Positives for MISRA C++-2023 Rule 7.0.2 where contextual conversions of std::atomic<bool> to bool were incorrectly flagged.

SATW-7068
:   Reported in version: unspecified
:   Fixed False Negatives for CERT SEC03-J when endorsed types were accessed via factory methods or when the untrusted class loader was set rather than retrieved.

### Coverity Commands 2026.6.0

#### New or changed features

SAT-45263, SAT-47044
:   `cov-run-desktop` results will now include the effects of issue categorization maps.

#### Bug fixes

IM-30146
:   Reported in version: 2022.12.1
:   As of this release, Cov-archive does not migrate priority filters which uses LOBs. This is in the roadmap and planned for upcoming releases.

### Coverity Compilers and Capture 2026.6.0

#### End-of-life products

CMPGO-567
:   Support for Go 1.24 has been removed as of 2026.6.0.

COVP-2673
:   Support for FreeBSD 13 has been removed as of 2026.6.0.

#### Deprecated products and features

CMPGO-566
:   Support for Go 1.25 is deprecated as of 2026.6.0 and will be removed in a future release.

CMPJ-2525
:   Support for Oracle/Open JDK 17 is deprecated as of 2026.6.0 and will be removed in a future release.

COVP-2671
:   Support for macOS 14 is deprecated as of 2026.6.0 and will be removed in a future release.

#### New or changed features

CAP-2513
:   `cov-build` on macOS no longer requires Xcode to be installed when running in `--bazel` mode.

CMPCPP-15391
:   Added support for Clang 20.1, 21.1, and 22.1.

CMPCPP-15593
:   TI CL2000 (TMS320C2000) now supports up to 25.11.0 on Windows.

CMPCPP-15594
:   TI ARMCL now supports up to 20.2.7.

CMPCPP-15603
:   Added support to Code Warrior m56800e for the use of environment variable in response files.

CMPCPP-15670
:   Better support for CodeWarrior m56800e support.

CMPCPP-15703
:   Added switches for CodeWarrior Compiler.

CMPGO-619
:   Added support for Go version 1.26.

CMPJ-2523
:   Support for Oracle/Open JDK 26 has been added as of 2026.6.0.

COVP-2668
:   Support for Visual Studio 2026 has been added as of 2026.6.0.

#### Bug fixes

CMPCPP-14692
:   Reported in version: 2023.12.0
:   Fixed an issue affecting EDG compilers when using empty enums.

CMPCPP-15260
:   Reported in version: unspecified
:   Fixed a crash in clang when structure bound array passed to lambda.

CMPCPP-15281
:   Reported in version: 2025.6.0
:   Fixed missing built-in types and functions related to ARM64 NEON. Also, fixed catastrophic error related to GNU #pragma GCC target and assignment operator class member functions.

CMPCPP-15314
:   Reported in version: 2025.6.0
:   Fixed recoverable error during analysis due to missing source file and location info when the same header was included more than once with different paths.

CMPCPP-15412
:   Reported in version: 2025.6.0
:   Supported bug _BitInt(N) for clang.

CMPCPP-15460
:   Reported in version: 2025.3.0
:   Fixed the modeling of the `_SVFloat` family of built-in types for the ARM64 architecture, specifically those used in the `arm_neon.h` system header file.

CMPCPP-15548
:   Reported in version: 2026.3.0
:   Fixed an issue when using many libraries with `--emit-link-units` where `cov-emit-link` would fail to run due to excessive command line length.

CMPCPP-15556
:   Reported in version: 2025.12.0
:   Fixed the modelling of built-in types and functions for ARM 64 architecture and specifically those used in the "arm_neon.h" system header file.

CMPCPP-15600
:   Reported in version: 2025.3.0
:   Fixed missing aarch64 builtin functions when compiling using QNX 7.1 compiler targeting ARM architecture.

CMPCPP-15601
:   Reported in version: 2025.6.0
:   Support for Code Warrior m56800e -ir option added.

CMPCPP-15681
:   Reported in version: 2025.12.0
:   Fixed failure on constrained partial specialization templates.

CMPCPP-15706
:   Reported in version: 2025.12.0
:   Added the --emit_system_include_comments option to retain comments from system includes, enabling annotations in system includes. For Clang, this option translates to -fretain-comments-from-system-headers.

CMPCPP-15755
:   Reported in version: 2025.3.1
:   Fixed a crash where both overriding and base methods have default value list initialization.

CMPCPP-15811
:   Reported in version: 2026.3.0
:   With IAR ARM and RX compilers, in class specialization is now permitted and __root keyword is now only enabled with "-e" option.

CMPCPP-15812
:   Reported in version: 2026.3.0
:   For IAR ARM, char8_t is no longer incorrectly enabled and a few intrinsics have been corrected.

CMPCSH-2173, CMPCSH-2179
:   Reported in version: unspecified
:   Resolved an issue where defects in some C# web applications were not mapped correctly to their source code.

CMPCSH-2182
:   Reported in version: 2025.12.0
:   Fixed a C# cross-scope local function delegate crash.

CMPCSH-2184
:   Reported in version: unspecified
:   Fixed an issue preventing C# from replaying in hardened containers.

CMPFG-2047
:   Reported in version: unspecified
:   Fixed an issue where `cov-build --replay` also replayed C# source files.

CMPJ-2403
:   Reported in version: unspecified
:   Fixed an out-of-memory problem for Java F-bounded generic type hierarchies.

CMPJ-2517
:   Reported in version: unspecified
:   Fixed crash during coverity analyze for Java projects containing jimage modules files.

### Coverity Point and Scan 2026.6.0

#### Bug fixes

COVGUI-2681
:   Reported in version: 2025.12.0, 2026.3.0, 2026.6.0
:   Fixed a regression introduced in 2025.12 where Point & Scan was committing two snapshots to Coverity Connect per scan. The local commit task was incorrectly running cov-commit-defects against the server instead of writing local JSON output. The local commit task is now correctly configured with commit.local-only=true, ensuring only a single snapshot is committed per scan.

## Coverity Desktop 2026.6.0

This section provides release notes for Coverity Desktop components.

### Coverity Desktop for Eclipse 2026.6.0

#### End-of-life products

PRD-13249
:   Support for Eclipse 2022-09 has been removed as of 2026.3.0.

#### Deprecated products and features

PRD-13250
:   Support for Eclipse 2023-03 is deprecated as of 2026.3.0 and will be removed in a future release.

#### New or changed features

PRD-13247
:   Added support for Eclipse 2025-09.

## Coverity Documentation 2026.6.0

This section provides release notes for Coverity Documentation components.

### Coverity Documentation 2026.6.0

#### New or changed features

COVDOCS-2012
:   Coverity now supports the Hyundai 4.1 compliance standards for Hyundai C 4.1, Hyundai C++ 4.1, and Hyundai Java 4.1.

SATSEC-16562
:   Documented allow-listing examples of URL_MANIPULATION checker for each language.
