---
title: "Coverity 2024.6.0 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2024.6.0-release-notes.html"
content_id: "Evr~s~sU78fjS0imU8Ztsw"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:30.839439+00:00"
---

# Coverity 2024.6.0 Release Notes

## Important information for 2024.6.0

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

If you are upgrading a Coverity cloud deployment, refer to [Upgrading a Coverity cloud deployment](https://documentation.blackduck.com/bundle/coverity-docs/page/cnc/topics/upgrade-coverity.html) in the Coverity Cloud Deployment Administrator and User Guide. This document provides important information for administrators who are deploying or upgrading Coverity in a Kubernetes container environment.

The Coverity 2024.6.0 release introduces support for MISRA C 2023 standards, more robust Coverity Connect deployments, and support for several new programming language versions.

**Special announcement**

Starting next year, the number of Coverity Connect installer releases will be reduced as we
focus on Coverity Connect in the Coverity cloud deployment. There will be no change to
the Coverity Analysis or the Coverity cloud deployment release cadence.

The Coverity 2025.3 release will not include a Coverity Connect installer and there will be no
more minor releases that include a Coverity Connect installer, except in cases where
there are critical security issues.

In 2025, there will only be 2 major releases that include the Coverity Connect installer: the 2025.6 release and the 2025.12 release.

**Release highlights**

- Added support for MISRA C 2023, so that customers can track and manage their compliance with the latest version of this standard.
- Added the ability to run Coverity Connect as a highly available web application. Multiple Connect web UIs can now be run simultaneously in a single Kubernetes cluster to prevent outages and improve the performance of the Connect application.
- Coverity's Bazel support is now much simpler to configure, but any customers currently using
  it will need to make a simple one-time adjustment to their Coverity scans. More
  information is available in the [Upgrade considerations for 2024.6](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/upgrade_considerations_for_2024_6.html) section of the *Coverity 2024.6.0
  Installation and Upgrade Guide*.
- Java 22 and Go 1.22 are now supported.
- Initial support for C# support has been added to the Rapid Scan Static (Sigma) engine.​
- For C#, Java, and Visual Basic customers, a new security checker,
  `MASS_ASSIGNMENT`, is now available.​
- Improved accuracy and language support for the `OVERRUN`,
  `DIVIDE_BY_ZERO`, and `XML_EXTERNAL_ENTITY`
  checkers.​

**Known issues**

- The AIX Coverity Analysis binary will not be available in this release.

Please see below for full details of these and other enhancements included in this release.

## Coverity Platform 2024.6.0

This section provides release notes for Coverity Platform components.

### Coverity Connect 2024.6.0

#### New or changed features

CNC-701
:   Added the ability to download Coverity Analysis binaries from the download page in a Coverity cloud deployment, similar to Coverity Connect.

COVDOCS-1402
:   New application metrics have been added to track maximum database connections, active database connections, and number of commits queued for a stream (`max_db_connections`, `active_db_connections`, `no_of_commits_queued_for_a_stream`). Additionally, a new Coverity Connect property has been introduced to enable logging on some relevant application metrics to help with debugging (`connect.enable.logging.metrics`).

IM-30854
:   The operation `POST {viewType}/content` has been added to the Coverity Connect API. This new operation retrieves data for the specified `viewType`. For more information, refer to the API reference documentation at `<scheme>://<my_connect_host>:<port>/swagger/cim/index.html` (where `<scheme>` is either `http` or `https`, depending how you configured your Coverity Connect server, and `<my_connect_host>:<port>` are the host and port of your Coverity Connect server) and the section "Retrieve data for the specified view type" in the *Coverity Platform 2024.6.0 REST Web Services API Guide*.

IM-30926
:   Added a new built-in standard, MISRA C 2023. All operations supported for other built-in standards, such as **Filtering**, **group-by**, and so on, are also supported for MISRA C 2023.

IM-31297
:   Changed the response for the `GET /api/v2/snapshots/{id}` API call to include the snapshot's associated stream ID (`streamId`).

IM-31685
:   The operation `GET {viewType}/columns` has been added to the Coverity Connect API. This new operation retrieves the set of column keys and associated display names applicable to the specified `viewType`. For more information, refer to the API reference documentation at `<scheme>://<my_connect_host>:<port>/swagger/cim/index.html` (where `<scheme>` is either `http` or `https`, depending how you configured your Coverity Connect server, and `<my_connect_host>:<port>` are the host and port of your Coverity Connect server) and the section "Retrieve column keys for the specified view type" in the *Coverity Platform 2024.6.0 REST Web Services API Guide*.

#### Bug fixes

CNC-2801
:   Reported in version: 2023.12.3
:   Improved the performance of loading the **Configuration > Users & Groups** view.

IM-25951
:   Reported in version: 2021.03
:   Fixed issue with view links in emails for hierarchy views.

IM-29356
:   Reported in version: 2022.9.1
:   Fixed a role-based access control issue where a confusing warning message was printed to the console while running `cov-run-desktop` or `cov-commit-defects` with the `--preview-report` option for users having only 'Preview Commit' permission, and not 'Commit to a Stream' permission.

IM-31405
:   Reported in version: 2023.9.0, 2023.6.2
:   Fixed an issue where users could not set the same role on two triage stores back to back.

IM-31501
:   Reported in version: 2023.6.2
:   Stream filtering auto complete suggestions are now limited to 200.

IM-31548
:   Reported in version: 2023.12.0
:   Fixed issue with user group relationship during LDAP refresh.

IM-31646
:   Reported in version: 2023.3.2
:   Fixed an issue where large snapshots (snapshots with more than 65,535 stream files) could not be deleted.

IM-31669
:   Reported in version: 2023.9.2
:   Added a loading indicator when adding file rules to a Component Map.

IM-31675
:   Reported in version: 2024.3.0
:   Improved performance of the Coverity Connect application when applying role-based access control rules.

IM-31709
:   Reported in version: 2023.3.2, 2023.12.0
:   Fixed an issue with HikariPool configuration and statistics logging. Relevant information for HikariPool will be available in Coverity Connect logs as expected.

IM-31800
:   Reported in version: 2023.12.3
:   Fix errors during LDAP group refresh.

#### Known issues and solutions

COVDOCS-1413
:   Synopsys recommends that customers use HTTPS in production to provide secure communication to Coverity Connect.

COVDOCS-1461
:   The Export Defect Handler that enables non-Jira external bug tracking system integration is broken in Coverity Connect 2024.6.0. If you are using the Export Defect Handler, Synopsys recommends to not upgrade to 2024.6.0 until this issue is resolved.

### Coverity Report Generators 2024.6.0

#### New or changed features

RG-1812
:   Added support for the MISRA C:2023 standard in Coverity reports.

#### Bug fixes

RG-1853, RG-1871
:   Reported in version: 2023.12.2, 2023.9.0
:   Fixed issues where a stream with 100 snapshots or more was causing out of memory errors during identification of the latest snapshot details.

SAT-45466
:   Reported in version: 2023.9.0
:   Fixed an issue that could cause parse-warning checkers (`PW.*`) to appear multiple times in a Connect view or cause unenabled parse-warning checkers to appear as enabled.

## Coverity Analysis 2024.6.0

This section provides release notes for Coverity Analysis components.

### Coverity Analysis - General 2024.6.0

#### New or changed features

COVDOCS-1372
:   Support has been added for the frameworks Azure OpenAI client library (Azure SDK) for .NET (C#/Visual Basic) and Azure OpenAI client library for Java (Azure SDK).

COVGUI-2534
:   A new checkbox in the Point and Scan login page allows users to use 2-step SSO authentication (via the default browser) to complete the SSO login for Coverity Connect version 2023.12.0 or newer.

    To use 2-step SSO authentication (via the default browser) with Coverity Connect version 2023.12.0 or newer, select the checkbox.
    To use the legacy SSO login (within Point and Scan), keep the checkbox clear. This works with all supported Coverity Connect versions.

SAT-45046
:   When `--aggressiveness-level` is set to `high`, Coverity Analysis now reports `OVERRUN` and `CHECKED_RETURN` defects that were previously suppressed in the presence of enumerators containing "count" in the enumerator name.

SAT-45658
:   Added a new code pattern, `enumeratorLiteral`, to the CodeXM C/C++ library.

SATSEC-15571
:   Coverity now detects insecure JSON serialization defects in .NET through Rapid Scan Static (Sigma)

SATSEC-15728
:   Coverity now detects 'password' keywords for C# through the Sigma engine. The recognition of the keyword happens with or without its usage.

SATSEC-15733
:   The `es5-ext` module for Node.js, delivered with Coverity Analysis, has been upgraded to version 0.10.64. This resolves security vulnerability CV-2024-27088.

SATSEC-15794
:   In Coverity 2024.6.0, Ruby has been upgraded to version 3.3.1 on all supported platforms except for Windows 64-bit.

#### Bug fixes

CMPCPP-13841
:   Reported in version: 2023.9.0
:   Fixed a recoverable error in `cov-analyze` caused by an invalid mangled name.

CMPCPP-13857
:   Reported in version: 2022.12.0
:   Fixed a false positive in the AUTOSAR C++14 A7-1-9 checker when a member with `enum` type appeared within a class template.

CMPCPP-13983
:   Reported in version: 2022.9.2
:   Fixed issue resulting in `cov-configure` crashing when using really long command lines with the Yocto toolchain.

CMPJS-1152
:   Reported in version: 2023.12.0
:   Fixed issue that was introduced into `cov-internal-js-fe` in the Coverity 2023.12.0 release, which would sometimes cause crashes in `cov-analyze`.

SAT-45585
:   Reported in version: 2023.12.0
:   Fixed a suppressible assertion when `cov-analyze` generates metrics with `--generate-function-metrics` and functions have whitespace in their names.

SAT-45717
:   Reported in version: 2024.6.0
:   Fixed an analysis performance issue in some cases involving classes with lots of fields.

SATSEC-15573
:   Reported in version: 2023.9.0
:   Corrected behavior of the `sanitizer_for_checker` directive so that it now matches the documented semantics. [C#, Java, Visual Basic]

### Coverity CLI 2024.6.0

#### New or changed features

COVCLI-2377
:   Reduced the verbosity of the Coverity CLI output to improve readability. Verbose output can be enabled by specifying the `--verbose` argument.

COVCLI-2867
:   It is now possible to configure the collection of scan transparency data using the Coverity CLI configuration file for build capture, `cov-translate` capture, and analysis.

COVCLI-3055
:   Coverity CLI will now log output from the `coverity capture`, `coverity analyze`, `coverity commit` and `coverity scan` commands to the file `<idir>/coverity-cli/coverity-cli-log.txt`.

COVCLI-3069
:   The Coverity CLI now supports HFI (High Fidelity Incremental) analysis, allowing analysis to be limited to only specifically selected files.

COVCLI-3199
:   The Coverity CLI has added support for a new comparison report format.

COVDOCS-1381
:   The Coverity CLI has added options for saving defects to a local file system.

#### Bug fixes

COVCLI-3245
:   Reported in version: 2024.3.0
:   Fixed a performance issue in Coverity CLI buildless capture that caused excessive run time for projects with a large number of modules and a highly connected dependency tree. This issue impacted buildless capture for Java, C# and Go.

COVCLI-3250
:   Reported in version: 2024.3.0
:   Fixed issue where the `--language configuration` option for the `coverity capture` command only works when used in conjunction with the `--language <scripting_language>` option.

COVCLI-3279
:   Reported in version: 2024.6.0
:   Coverity CLI C# buildless capture will now capture and analyze C# files where the project directory only contains a solution (`.sln`) file. Previously, when capturing a project using buildless capture, C# files would only be captured and analyzed using buildless capture if the project directory contained a C# project (`.csproj`) file or no known project files.

### Coverity Checkers 2024.6.0

For a summary of checkers that have been added or changed in this release, refer to the "Coverity Checker Change History" table in the *Coverity Checker Reference*.

#### New or changed features

SAT-39700, SAT-45239
:   The `DIVIDE_BY_ZERO` checker has been improved for finding defects on floating-point types. [All languages supported by the checker]

SAT-43999
:   Added support for MISRA-C: 2012 Amendment 3 and Amendment 4 rules, completing support for MISRA-C:2023.

SAT-45210
:   Reduce false positive reports for the `INTEGER_OVERFLOW` checker when analyzing code which uses a retry loop to write or read data in a buffer.

SAT-45476
:   Improved detection of some `errno`-setting functions that are sometimes defined as macros for the purpose of MISRA C:2012 Rules 22.8, 22.9, and 22.10.

SAT-45501
:   The `UNINIT` checker was improved to report cases where a jump went past a declaration in C++.

SATSEC-3176
:   Brakeman Pro for Ruby on Rails security analysis has been upgraded to version 6.1.2.

SATSEC-6535
:   The `SENSITIVE_DATA_LEAK` checker now also reports on sensitive data being stored in an environment variable, in support of CWE-526. [C, C++, C#, Go, Java, JavaScript, Kotlin, Python, TypeScript, Visual Basic]

SATSEC-6924
:   Enhanced defect events for the `XML_EXTERNAL_ENTITY` checker. [C#, Java, Visual Basic]

SATSEC-15598
:   Added new checker `MASS_ASSIGNMENT` for C#, Java, and Visual Basic.

SATSEC-15728
:   Coverity now detects 'password' keywords for C# through the Sigma engine. The recognition of the keyword happens with or without its usage.

SATSEC-15743
:   The Node.js runtime has been upgraded to version 18.19.1.

SATSEC-15864
:   Added new checker option `report_allow_anonymous` for the `MISSING_AUTHZ` checker. [C#]

SATW-5382
:   Added support for MISRA C 2023 standard.

#### Bug fixes

CMPCPP-13928
:   Reported in version: 2022.12.0
:   Fixes an issue in the AUTOSAR C++14 M0-1-3 checker related to global variables defined within a namespace.

SAT-2999
:   Reported in version: 4.3.0
:   Fixed some false positives and false negatives for the `NULL_RETURNS` checker. [All languages supported by the checker]

SAT-30793
:   Reported in version: 2019.06
:   Fixed a false positive for the `DIVIDE_BY_ZERO` checker when `System.Math.Sign` is used. [C#]

SAT-31156, SAT-34362, SAT-43132, SAT-43142
:   Reported in version: 2019.03 , 2019.12 , 2022.9.0
:   Fixed a source of false positives for the `OVERRUN` checker. [All languages supported by the checker]

SAT-41893, SAT-42260, SAT-43716
:   Reported in version: 2021.12.0, 2022.03, 2021.12.0, 2022.12.0
:   Fixed an issue where the AUTOSAR C++14 A2-10-4 checker would report violations for multiple specializations of the same templated function.

SAT-45217
:   Reported in version: 2023.9.0
:   Fixed a source of false positives for the `UNINIT` checker when using the `readdir_r` function. [All languages supported by the checker]

SAT-45347
:   Reported in version: 2023.12.0
:   Fixed a source of false positives for the `RESOURCE_LEAK` checker, related to `TEE_AllocateOperation`.

SAT-45351
:   Reported in version: 2023.3.0, 2023.12.0
:   Fixed an issue where MISRA C:2012 Rule 8.6 reports would incorrectly refer to a global variable as a function.

SAT-45390
:   Reported in version: 2023.12.0
:   Fixed a source of false positives for AUTOSAR C++14 Rule A3-1-1 and MISRA C++:2008 Rule 3-1-1 with C++17 inline variables.

SAT-45398
:   Reported in version: 2024.3.0
:   Improved reference counting detection heuristics.

SAT-45425, SAT-45450
:   Reported in version: 2023.12.0
:   Fixed false positives for the `REVERSE_INULL` and `FORWARD_NULL` checkers, related to `TEE_SetOperationKey`.

SAT-45433
:   Reported in version: 2023.12.0
:   Fixed a source of false positives for the `UNLOCKED_ACCESS` checker related to constant string literals.

SAT-45504, SAT-45663
:   Reported in version: 2023.12.2, 2024.3.1
:   Fixed a crash in the `COPY_PASTE_ERROR` checker for anonymous functions in JavaScript.

SAT-45583, SAT-45619
:   Reported in version: 2023.12.0
:   Fixed a false positive for the `UNINIT_CTOR` checker related to lambda constructors. [C++, CUDA, Objective-C++]

SAT-45584
:   Reported in version: 2023.12.0
:   Fixed an issue where the AUTOSAR C++14 rule A2-10-4 would report violations for multiple specializations of the same templated function.

SAT-45644
:   Reported in version: 2023.12.0
:   Fixed a `NULL_RETURNS` false positive involving Java's `Optional.orElseGet()`. [Java]

SAT-45670
:   Reported in version: 2023.12.0
:   Fixed a recoverable error when using the `RegexExtended` CodeXM pattern and performing a regex replacement that did not actually modify the string.

SATSEC-6880
:   Reported in version: 2023.3.0
:   Corrected behavior of the `sanitizer_for_checker` directive so that now it matches the documented semantics. [C#, Java, Visual Basic]

SATSEC-15591
:   Reported in version: 2023.12.0
:   In some cases, a `CSRF` defect was reported where the SpringBoot framework automatically protects against `CSRF`. The false positive was caused by a failure to propagate HTTP method information through the implementation (Java) class hierarchy. This problem has been corrected. [Java]

SATSEC-15643
:   Reported in version: 2023.6.2
:   Fixed a false negative for the `MISSING_AUTHZ` checker. [C#]

SATSEC-15651
:   Reported in version: 2023.9.2
:   Fixed a recoverable analysis crash with the `CSRF` checker. [Java]

SATSEC-15697
:   Reported in version: 2024.3.0
:   Fixed a false positive for the `PATH_MANIPULATION` checker, where it would report a defect if a field (attribute) of a tainted object was passed to a method considered to be a sink (consumer) of that tainted data, even if that same field was passed to a method in a parameter labelled as a sanitizer using a `sanitizer_for_checker` directive. [C#, Java, Visual Basic]

SATSEC-15722
:   Reported in version: 2023.12.1
:   The `IDENTICAL_BRANCHES` checker was reporting a false positive when one branch contained `yield <expr>` and the other contained `yield from <expr>`. The `IDENTICAL_BRANCHES` checker now considers the two expressions to be distinct. [Python]

SATSEC-15739
:   Reported in version: 2024.3.0
:   Fixed a bug that caused the option `SQLI:report_nosink_errors` to be ignored when the `SQL_NOT_CONSTANT` checker was enabled. [C#, Java, Visual Basic]

SATSEC-15753
:   Reported in version: 2023.12.0
:   Fixed a false negative for the `SQLI` checker. [C#]

SATSEC-15777
:   Reported in version: 2024.6.0
:   Fixed a bug that could cause a crash in the `UNSAFE_DESERIALIZATION` checker. [Java]

SATSEC-15810
:   Reported in version: 2023.9.2
:   Fixed a recoverable crash for the `XSS` checker. [Java]

SATW-5408
:   Reported in version: 2023.9.2
:   Fixed a source of false positives in AUTOSAR C++14 Rule A15-4-4 where constructors were incorrectly considered to never throw an exception.

### Coverity Commands 2024.6.0

#### Deprecated products and features

COVCLI-3202
:   The `fs_capture_build_options` setting has been deprecated, and support for it will be discontinued in a future release of Coverity Analysis.

#### New or changed features

SAT-45566
:   The `cov-commit-defect` command now returns a success code instead of a failure when it detects recoverable errors.

#### Bug fixes

SAT-45728
:   Reported in version: 2024.6.0
:   Fixed security issue CVE-2020-14315 in the packaged third-party `bsdiff` program, used during Coverity upgrades.

#### Known issues and solutions

COVDOCS-1411
:   `cov-manage-findings` (findings report) doesn’t have support for MISRA C 2023 category.

### Coverity Compilers and Capture 2024.6.0

#### End-of-life products

CMPCPP-14183
:   Support for LLVM Clang version 8.x has been removed as of 2024.6.0.

CMPGO-453
:   Support for Go 1.20 has been removed as of 2024.6.0.

CMPJ-2198
:   Support for Oracle/Open JDK 11 has been removed as of 2024.6.0.

COVP-2608
:   Support for FreeBSD 12 has been removed as of 2024.6.0.

COVP-2612
:   Support for .NET 7 has been removed as of 2024.6.0.

#### Deprecated products and features

CMPCPP-14451
:   Support for LLVM Clang 9.0 is deprecated as of 2024.6.0 and will be removed in a future release.

CMPGO-452
:   Support for Go 1.21 is deprecated as of 2024.6.0 and will be removed in a future release.

COVP-2607
:   Support for macOS 12 is deprecated as of 2024.6.0 and will be removed in a future release.

#### New or changed features

CAP-1900
:   The `cov-build --bazel` command now accepts any valid Bazel target format including multi-target options.

CAP-2294
:   The rule-based Bazel integration has been removed. See the *Coverity Analysis User and Administrator Guide* for instructions on how to set up a new Bazel build with Coverity, or the *Coverity Installation and Upgrade Guide* for information on what changes to make to capture an existing build.

CMPCPP-14069
:   Support for Clang 18.1.0 and Xcode 15.3 has been added as of 2024.6.0.

CMPCPP-14188
:   Extended support for CUDA version 12.4 with GCC and MSVC as host compilers.

CMPGO-451
:   Support has been added for Go 1.22.

CMPJ-2200
:   Support for Oracle/Open JDK 22 has been added as of 2024.6.0.

CMPJ-2231
:   Updated Tomcat to version 9.0.89.

#### Bug fixes

CAP-1985
:   Reported in version: 2021.12.0, 2022.3.0
:   The environment variable `COVERITY_CMPG3856_WORKAROUND` no longer needs to be set to work around certain edge cases with running builds with `cov-build --bazel` and `cov-manage-emit replay-from-script`, and now has no effect.

CAP-2269
:   Reported in version: 2024.6.0
:   The `cov-build` command will not serialize builds that use Gradle to launch processes (e.g. Gradle builds using the `cpp-library` plugin).

CAP-2274
:   Reported in version: 2023.12.0
:   Fixed an issue where `cov-build` could cause a crash when running Mono on macOS.

CAP-2298
:   Reported in version: 2024.3.0
:   Bazel execution root path replacement will now work for source files in nested directories.

CMPCPP-13004
:   Reported in version: 2022.9.2
:   Fixed a crash in `cov-internal-emit-clang` when a coroutine contains a `co_return` statement with a braced-enclosed initializer list.

CMPCPP-13564
:   Reported in version: 2023.3.2
:   Fixed an issue where using `typedef` for floating point types in constant expressions caused an assertion failure in template instantiation context.

CMPCPP-13982
:   Reported in version: 2023.9.0
:   Fixed spurious diagnostic output for Clang compilers when using the `--debug` option.

CMPCPP-13983
:   Reported in version: 2022.9.2
:   Fixed issue resulting in `cov-configure` crashing when using really long command lines with the Yocto toolchain.

CMPCPP-13986
:   Reported in version: 2023.9.0
:   Fixed a bug in `cov-internal-emit-clang` where deviations were not properly used.

CMPCPP-14090
:   Reported in version: 2023.12.1
:   Fixed handling of legacy Windows 8.3-style paths in the `record-with-source` workflow for Clang-based compilers.

CMPCPP-14259
:   Reported in version: 2023.3.0
:   Fixed an issue where defects were produced for internal compatibility headers when performing a cross-platform replay.

CMPCPP-14399
:   Reported in version: 2023.6.0
:   Fixed an assertion in `cov-emit` when a multiline string was expanded as part of a macro with a variadic parameter list.

CMPCSH-2008
:   Reported in version: 2023.12.1
:   Addressed an issue with `dotnet` Razor code generation in "record with source" workflows.

CMPFG-1062
:   Reported in version: 2023.12.2, 2024.3.1
:   Fixed an issue in incremental capture scenarios where `cov-emit-text` was skipping the emit of files that had changed since the initial capture.

CMPGO-393, CMPGO-467
:   Reported in version: 2023.12.0, 2023.6.0
:   Resolved an issue where `cov-analyze` could crash due to `cov-emit-go` generating an incorrect size for some types.

CMPGO-442, CMPGO-444
:   Reported in version: 2023.12.0, 2024.3.0
:   Fixed an issue in `cov-emit-go` where generic types could cause analysis to crash with missing declaration errors.

CMPJ-1719
:   Reported in version: 2021.12.2
:   Tomcat `jar` files used by `cov-internal-emit-java-webapp` have been updated to address CVE-2022-23181.

CMPJ-2171
:   Reported in version: 2023.9.1
:   Fixed handling of `--add-exports` when using duplicate packages in the Java front end.

    Fixed handling of `--module-source-path` when using wildcard paths and overrides in the Java front end.

CMPJS-1144, CMPJS-1151, CMPJS-1153, CMPJS-1160, CMPJS-1166, CMPJS-1178
:   Reported in version: 2023.12.0
:   A defect in the Coverity frontend for TypeScript, when processing ECMAScript decorators, could sometimes cause `cov-analyze` to crash with a diagnostic about "no function named...". This defect has been fixed.

CMPJS-1167
:   Reported in version: 2022.6.1
:   Fixed an issue where JavaScript files with paths that contained non-ASCII characters were not properly recorded in a record with source build.

CMPJS-1207
:   Reported in version: 2024.3.0
:   Fixed issue in the Coverity TypeScript frontend which could cause it to take excessive amounts of time to process large binary expressions.

SATSEC-15727
:   Reported in version: 2023.9.2
:   On projects containing `AndroidManifest.xml files`, the `cov-run-desktop` command was not including those files among the translation units (TUs) to be analyzed when **Analyze Entire Scope** is selected. Some checkers depend on the Android manifest file for taint-source information, hence related defects were missing in comparison with a central analysis run. Now, `cov-run-desktop` includes `AndroidManifest.xml` files in the list of files to be analyzed.

### Coverity Point and Scan 2024.6.0

#### New or changed features

COVGUI-2534
:   A new checkbox in the Point and Scan login page allows users to use 2-step SSO authentication (via the default browser) to complete the SSO login for Coverity Connect version 2023.12.0 or newer.

    To use 2-step SSO authentication (via the default browser) with Coverity Connect version 2023.12.0 or newer, select the checkbox.
    To use the legacy SSO login (within Point and Scan), keep the checkbox clear. This works with all supported Coverity Connect versions.

### Rapid Scan Static (Sigma engine) 2024.6.0

#### New or changed features

SATSEC-15571
:   Coverity now detects insecure JSON serialization defects in .NET through Rapid Scan Static (Sigma)

SIGMACOV-643
:   When Coverity has information about a project's root directory, this is now passed to Rapid Scan Static (Sigma) so it can be used to generate more stable defect merge keys.

#### Bug fixes

SIGMACOV-649
:   Reported in version: 2023.9.2
:   Fixed a bug where certain Rapid Scan Static (Sigma) defects would close and re-open when a codebase was analyzed in different directories.

## Coverity Desktop 2024.6.0

This section provides release notes for Coverity Desktop components.

### Coverity Desktop for Android Studio 2024.6.0

#### End-of-life products

PRD-13081
:   Support for Android Studio 2021.1 has been removed as of 2024.6.0.

#### Deprecated products and features

PRD-13080
:   Support for Android Studio 2021.2 and 2021.3 is deprecated as of 2024.6.0 and will be removed in a future release.

#### New or changed features

PRD-13070
:   Added support for Android Studio 2023.2.0.

### Coverity Desktop for Eclipse 2024.6.0

#### End-of-life products

PRD-13076
:   Support for Eclipse 2020-12 has been removed as of 2024.6.0.

#### Deprecated products and features

PRD-13077
:   Support for Eclipse 2021-06 is deprecated as of 2024.6.0 and will be removed in a future release.

#### New or changed features

PRD-13063
:   Added support for Eclipse 2024-03.

### Coverity Desktop for Intellij IDEA 2024.6.0

#### End-of-life products

PRD-13078
:   Support for IntelliJ 2022.1 has been removed as of 2024.6.0.

#### Deprecated products and features

PRD-13079
:   Support for IntelliJ 2022.3 is deprecated as of 2024.6.0 and will be removed in a future release.

#### New or changed features

PRD-13064
:   Added support for IntelliJ 2024.1.0.

PRD-13065
:   Added support for CLion 2024.1.0.

PRD-13066
:   Added support for WebStorm 2024.1.0.

PRD-13067
:   Added support for RubyMine 2024.1.0.

PRD-13068
:   Added support for PhpStorm 2024.1.0.

PRD-13069
:   Added support for PyCharm 2024.1.0.

## Coverity Documentation 2024.6.0

This section provides release notes for Coverity Documentation components.

### Coverity Documentation 2024.6.0

#### New or changed features

COVDOCS-1355
:   Updated the documentation for the Synopsys Software Integrity Report in the *Configuring and Generating Coverity Reports* document to include the `include-false-positive` option.

COVDOCS-1365
:   The AUTOSAR, MISRA, SEI CERT, and HYUNDAI tables in the *Coverity Checker Reference* now show the following extra information for each rule: impact, checker type, related CWE types, and whether the rule is in the CWE top 25.

COVDOCS-1380
:   Updated the *Coverity Command Reference* document for the `cov-analyze --webapp-security-aggressiveness-level` option, specifying which checkers are affected by this option. The description for each of these checkers in the *Coverity Checker Reference* document has also been updated with details regarding the effects of the various levels supported by the `--webapp-security-aggressiveness-level` option.

COVDOCS-1386
:   The *Coverity CodeXM Checkers Development Guide* now documents the `enumeratorLiteral` pattern for the C/C++ library.

#### Bug fixes

COVDOCS-1067
:   Reported in version: 2023.12.0
:   Table 9 "Support by language" in the *Coverity Analysis User and Administrator Guide* has been updated with the addition of rows for the Docker and Terraform languages (which includes information on how to capture code written in these languages). The table in section 3.4.1.2 "The capture: Build options by language" has also been updated with information for Docker, Terraform, and HTML.

COVDOCS-1217
:   Reported in version: 2023.6.1
:   Added a section to help resolve a Coverity cloud deployment Ingress issue where the SAML URL uses `http` instead of `https`. An Ingress annotation is defined for GCP, and X-Forwarded-proto is defined for NGINX. See the section "Ingress: the SAML URL uses http instead of https" in the "Troubleshooting" chapter in the *Coverity Cloud Deployment Administrator and User Guide*.

COVDOCS-1324
:   Reported in version: 2023.9.2
:   Fixed the OpenShift route parameters configured in the OpenShift UI to create routes. Refer to section "OpenShift route - exposing the Coverity cloud instance outside an OpenShift cluster" in the *Coverity Cloud Deployment Administrator and User Guide*.

COVDOCS-1339
:   Reported in version: 2023.12.0
:   Documented how to generate and configure TLS/SSL CA-signed certificates. Refer to section "Generating Connect Certificates" in the *Coverity Cloud Deployment Administrator and User Guide*.

COVDOCS-1354
:   Reported in version: 2023.12.0
:   In the "Software issues and impacts by checker" table in `coverity-checker-coverage.html`, corrected hyperlinks for `JSHINT` checkers.

COVDOCS-1357
:   Reported in version: 2024.3.0
:   Updated documentation for "Coverity OWASP Top 10 Mobile: Android".

COVDOCS-1367
:   Reported in version: 2023.12.0
:   Updated documentation for the `cov-build` command to indicate platform specific options.

COVDOCS-1383
:   Reported in version: 2024.3.0
:   The `cov-commit-defects` command provides the option of committing analysis data over HTTPS using a WebSocket connection.

    Section 4.4 "Testing WebSocket connectivity" has been added to the *Coverity Platform User and Administrator Guide* to document how to test the WebSocket connection.

COVDOCS-1384
:   Reported in version: 2023.12.0
:   Section 3.1.2 "Triage attributes" in the *Configuring and Generating Coverity Reports* book has been updated to improve the explanation of how to create and configure the custom triage attributes known as CVSS attributes before running the CVSS Report Generator.

COVDOCS-1412
:   Reported in version: 2024.3.0
:   In the *CodeXM Guide,* the description of `RegexExtended()` has been updated to correctly describe this function's behavior.
