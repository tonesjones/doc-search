---
title: "Coverity 2025.9.0 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2025.9.0-release-notes.html"
content_id: "qDQBRf_zxxZ50hWLfwFkdA"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:16.927630+00:00"
---

# Coverity 2025.9.0 Release Notes

## Important information for 2025.9.0

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

If you are upgrading a Coverity cloud deployment, refer to [Upgrading a Coverity cloud deployment](https://documentation.blackduck.com/bundle/coverity-docs/page/cnc/topics/upgrade-coverity.html) in the Coverity Cloud Deployment Administrator and User Guide. This document provides important information for administrators who are deploying or upgrading Coverity in a Kubernetes container environment.

**Release Highlights**

·     Python 3.13 is now supported

·     Added a new checker for C++: UNNECESSARY_STRING_COPY that reports the inefficient use of std::string.

·     Now enables the C++ checker INCOMPLETE_DEALLOCATOR by default. This checker reports resource leaks in pairs of allocation and deallocation functions linked to structures.

·     Added a REST API to enable users to retrieve information about their usage of the Coverity scan service. This API lets users check the status of a scan job, cancel a scan job, and see a list of scans in the queue.

·     Added the option to limit output files to Logs Only in order to simplify troubleshooting in the event that large intermediate directories (idirs) fail to upload.

## Coverity Platform 2025.9.0

This section provides release notes for Coverity Platform components.

### Coverity Connect 2025.9.0

#### New or changed features

COVDOCS-1804
:   In Coverity cloud deployments, with the Helm key `scan-service.jobRunner.uploadArtifacts` set to `"logsOnly"`, the Scan Service artifacts job runner now uploads analysis results in addition to logs to storage service storage (bucket, blob). This is true for successful and failed scans. For further information, refer to the document *Coverity Cloud Deployment Administrator and User Guide*

COVDOCS-1838
:   For Coverity cloud deployments. this release establishes allowable units of measure for the NGINX HTTP gateway timeout configuration values when changing the values. These units apply whether creating annotations, configuring nginxConfig keys in the cnc Helm chart, or editing the NGINX ConfigMap. For further information, refer to the *Coverity Cloud Deployment Administrator and User Guide*.

COVDOCS-1849
:   For Coverity cloud deployments, this release introduces a new set of cache-service environment variables in the `scan-services` Helm subchart, designed to address requirements for S3-compatible storage in a Dell ECS deployment.

COVDOCS-1856
:   For Coverity cloud deployments, this release introduces a new Coverity Connect property that you must provide when using custom domains for storage service configurations. For further information, refer to the *Coverity Cloud Deployment Administrator and User Guide*.

IM-33097
:   We have delivered tomcat version to 10.1.42.

#### Bug fixes

CNC-3849
:   Reported in version: unspecified
:   In Coverity cloud, in the cnc chart, these Helm keys address the need for helm overrides for the `cim-nginx-config` to allow configuration changes without manual edits.

CNC-4047
:   Reported in version: 2024.9.0
:   There is no change in the application features.

CNC-4064
:   Reported in version: 2024.9.0
:   Fixed performance issues of the updateUser API.

CNC-4146
:   Reported in version: 2025.6.0
:   Fixed an issue where the CNC REST API failed to process requests containing square brackets. As of 2025.9.0, the API processes square brackets in payloads correctly.

IM-32089
:   Reported in version: 2023.12.2
:   Fixed issues with source code display after XREF linksets was enabled.

IM-32118
:   Reported in version: 2024.6.0
:   CC is now able to fetch all projects from Jira Cloud instances when we have product_discovery type Projects in the Jira instances.

IM-32478
:   Reported in version: 2024.6.1
:   Able to navigate to the defect from search box.

IM-32579
:   Reported in version: 2024.12.0
:   Fixed an issue where the "View Issues" link on the Coverity Connect Trends dashboard fails to work when certain segmentations are applied.

IM-32609
:   Reported in version: 2024.12.0
:   Fixed an issue causing JIRA export failures due to incomplete field retrieval from JIRA’s API.

IM-32636
:   Reported in version: 2024.6.0
:   Fixed a bug where Coverity Connect was unable to fetch projects from Jira Cloud due to a Product Discovery project type issue.

IM-32735
:   Reported in version: 2024.6.0, 2024.9.0, 2024.12.0
:   Fixed a Coverity Connect UI bug where issue details were omitted after switching many pages.

IM-32832
:   Reported in version: 2024.9.0
:   Able to run parallel preview commits without the error log.

IM-32883
:   Reported in version: 2024.9.0
:   Fixed a Coverity Connect bug where the UI returned all streams when trying to view the last stream.

#### Known issues and solutions

COVDOCS-1860
:   Using special characters within a Coverity Connect project name or stream name can cause a failure. In Coverity Connect, for both projects and streams, do not use the following special characters: ``` \ / : `` ````` ` ' “ * ``. This restriction applies to the user interface, REST API, and Web service calls, including `cov-manage-im`.

COVDOCS-1869
:   In the Coverity Connect UI, the new default `Function` view `With Outstanding Issues` has a known issue where it does not provide translations for the user's locale.

## Coverity Analysis 2025.9.0

This section provides release notes for Coverity Analysis components.

### Coverity Analysis - General 2025.9.0

#### New or changed features

COVCLI-3975
:   It is possible to specify a proxy server to use to connect to Coverity Connect using the environment variables `HTTP_PROXY` and `HTTPS_PROXY`. It is also possible to use a proxy server that uses the `http` scheme in the proxy server URL in `commit.connect.proxy-url` and `analyze.connect.proxy-url`.

COVDOCS-1754
:   In the *Command Reference,* the description of `cov-manage-emit` now includes an entry for the translation-unit option, `--tu-pattern 'had_recoverable_errors("true")' list`. The *Safety Manual* now mentions this option as well, along with a recommendation for how to run `cov-manage-emit` to ensure the customer's code base causes no recovery or emit errors.

SATSEC-16347
:   In the RISKY_CRYPTO checker, re-enabled the `usage_report` option for JavaScript and TypeScript.

#### Bug fixes

CMPCPP-14503
:   Reported in version: 2024.6.0
:   Fixed FP for MISRA C++ 2008 Rule 0-1-3, AUTOSAR C++ Rule M0-1-9 where objects are not used but contain a user-defined constructor or destructor.

CMPCPP-15129
:   Reported in version: 2024.12.0
:   Fixed a Coverity Analysis issue where the `cov-configure` command did not support the GCC/Clang `_FILE_NAME_` macro.

CMPCPP-15238
:   Reported in version: 2025.3.0
:   Fixed a Coverity Analysis issue where the `cov-build` command failed to compile one file during a build.

COVDOCS-1785
:   Reported in version: unspecified
:   In the *Installation and Upgrade Guide,* information about supported versions of PostgreSQL has been corrected.

COVDOCS-1794
:   Reported in version: unspecified
:   Misleading pages about out-of-date versions of the Coverity Jenkins plug-in have now been removed.

SAT-14337
:   Reported in version: 7.6.0
:   An underrun issue related to non-const index expressions was not reported by mistake. The issue has been fixed.

SAT-46141
:   Reported in version: 2024.6.0
:   A bug with CUDA.SHARE_FUNCTION was fixed where certain built-in CUDA functions were mistakenly considered host-only functions, causing FPs.

SAT-47087
:   Reported in version: 2024.12.0
:   Fixed an issue with the tracking of constant values in INTEGER_OVERFLOW.

SATSEC-16156
:   Reported in version: unspecified
:   Fixed a class of SQLI false negatives related to the Django REST Framework.

SATSEC-16330
:   Reported in version: unspecified
:   Fixed an XML_EXTERNAL_ENTITY false positive when running with high webapp-security aggressiveness.

SATW-6474
:   Reported in version: 2024.12.0
:   Fixed a Coverity Analysis issue where, in C++, the Connect AUTOSAR checker did not detect the omission of either an `override` or `final` tag in an AUTOSAR rule A10-3-2 implicit destructor.

### Coverity CLI 2025.9.0

#### New or changed features

COVCLI-3228
:   The Coverity CLI supports a new configuration setting, commit.connect.target, which specifies a target platform for the committed snapshot.

COVCLI-3749
:   The Coverity CLI supports a new configuration setting, capture.build.propagate-build-failure-status, which specifies whether the Coverity CLI should exit with the same status as the build command when the build fails.

COVCLI-3918
:   The Coverity CLI now exposes the Sigma `base-check-set` configuration as a first-class setting in the configuration file. This can now be configured using `analyze.sigma.base-check-set`.

COVCLI-3928
:   It is now possible to provide a parse warnings configuration to the Coverity CLI to configure the parse warnings checkers. The configuration can be supplied in a configuration file or in-line in the configuration.

COVCLI-3937
:   The `files` section of the Coverity CLI configuration will now also influence which files are captured by build capture. Specifically, files captured by build capture that should not be included in the scan based on the `files` configuration will be removed from the intermediate directory at the end of the capture step. This also means that by default, files in hidden directories, i.e. directories that start with a "." or files in "vendor" directories, will also be removed from the intermediate directory unless they are explicitly included.

COVDOCS-1802
:   (See COVCLI-3937.)

#### Bug fixes

COVCLI-3914
:   Reported in version: 2024.12.0
:   In the auth key file created by the Coverity CLI, the "ssl" value in the "comments" section is now quoted correctly.

### Coverity Checkers 2025.9.0

For a summary of checkers that have been added or changed in this release, refer to the "Coverity Checker Change History" table in the *Coverity Checker Reference*.

#### Deprecated products and features

COVDOCS-1840
:   Support for Scala in Coverity Quality checkers has been deprecated, and will be removed in a future release of Coverity Analysis.

#### New or changed features

COVDOCS-1770
:   In the *Checker Reference,* updated the description of PRINTF_ARGS to be clearer and more correct.

COVDOCS-1778
:   In the CodeXM C/C++ library description table of `intLiteral` values, the name of the `llsuffix` field has been updated to `llzsuffix`.

COVDOCS-1793
:   In the *Checker Reference,* the description of INCOMPLETE_DEALLOCATOR has been updated to describe the new options `custom_allocators` and `custom_deallocators`, along with the case for their use.

COVDOCS-1798
:   (See SAT-46170.)

COVDOCS-1825
:   (See SAT-46842.)

COVDOCS-1835
:   (See SAT-46005.)

SAT-43447
:   `BUFFER_SIZE` reports interprocedural defects.

SAT-46005, SAT-47079
:   A new option was added for the REVERSE_INULL checker: `report_asserts_regex`. It can be used to check inside macros. The user can use `report_asserts_regex:fatal_if|fatal` to check inside their macros and find these cases. See documentation for a more detailed explanation.

SAT-46099
:   The `UNLOCKED_ACCESS` now always considers static initializers to be thread-safe.

SAT-46170
:   Added a checker option to INTEGER_OVERFLOW to allow the customer to suppress defect reports involving unsigned values being cast to signed values of the same size when the value itself does not fit in the signed type. This invokes implementation-defined behavior.

SAT-46646
:   Improved the `OVERRUN` checker to avoid false positives when using the linux `for_each_cpu` macro.

SAT-46842
:   A new checker, UNNECESSARY_STRING_COPY, detects inefficiencies in the use of C++ `std::string` objects. It locates inefficient patterns and suggests changes to improve efficiency. The defects reported by this checker do not address program correctness, only inefficient use of resources.

SAT-46921
:   Added support for erase through iterator's value such as map::erase(it->second) in the INVALIDATE_ITERATOR checker.

SAT-46980
:   Triage information for `MISRA C-2012` checkers is also inherited by equivalent `MISRA C-2023` checkers.

SAT-47114
:   Added a new property to CodeXM tokens that allows finding matches for a particular regex in the token's text.

SATSEC-3229
:   The `XML_INJECTION` checker now supports Go and Kotlin.

SATSEC-16283
:   The `SQL_NOT_CONSTANT` checker now supports Kotlin.

SATSEC-16326
:   The SSRF checker is now enabled with `--webapp-security`. [Java]

#### Bug fixes

SAT-45774
:   Reported in version: 2024.6.0
:   For the MISRA C-2012 Rule 22.7, do not generate a defect when the `EOF` value is cast to a type that is exactly compatible with `int`.

SAT-45980
:   Reported in version: 2024.6.0
:   Fixed a source of `RESOURCE_LEAK` false positives when using the `WRDE_REUSE` flag to glibc `wordexp`.

SAT-46017
:   Reported in version: 2024.6.0
:   Fixed an assertion failure involving the constraint FPP.

SAT-46179
:   Reported in version: 2023.12.0, 2024.6.0
:   General improvements to INTEGER_OVERFLOW.

SAT-46191
:   Reported in version: 2024.6.0
:   An issue with RESOURCE_LEAK related to TEE library function `TEE_AllocatePropertyEnumerator` is fixed.

SAT-46192
:   Reported in version: 2024.6.0
:   Created a built-in model for `socketpair(2)`.

SAT-46354
:   Reported in version: 2024.6.1
:   Improved the built-in model for `recvmsg(2)`.

SAT-46580, SAT-46838
:   Reported in version: 2024.12.0, 2024.9.0
:   `BUFFER_SIZE` reports a defect when using the source buffer's length as a parameter in size buffer functions and interprocedural defects generally.

SAT-46687
:   Reported in version: 2024.6.0
:   Fixed an issue that could cause `RESOURCE_LEAK` false positives when using pointer arithmetic and the `?:` operator.

SAT-46799
:   Reported in version: 2025.3.0
:   Improvements to the way we track values in ternary expressions found inside macros.

SAT-46895
:   Reported in version: 2024.12.0
:   Fixed a crash in ANONYMOUS_DB_CONNECTION for Golang.

SAT-46951
:   Reported in version: 2025.3.0
:   Fixed an issue where range-based 'for' loop would incorrectly add a level of nesting to `HIS_LEVEL`.

SAT-47028
:   Reported in version: 2023.6.2
:   A `NULL_RETURNS` FN issue with the Java Collection classes is fixed.

SAT-47122
:   Reported in version: 2025.6.0
:   Improved `BUFFER_SIZE`'s ability to understand array and pointer offsets.

SAT-47210
:   Reported in version: 2025.6.0
:   Fixed a source of false positives for `UNUSED_VALUE` and similar MISRA rules such as MISRA C++ 2023 Rule 0.1.1 when using `constexpr auto` variables.

SAT-47213
:   Reported in version: 2025.9.0
:   Fixed an issue in INCOMPLETE_DEALLOCATOR when a linked list is built through multiple layers of nested structs.

SAT-47214
:   Reported in version: 2025.9.0
:   Fixed an issue related to locating allocators for the INCOMPLETE_DEALLOCATOR checker.

SAT-47259
:   Reported in version: 2025.9.0
:   Fixed a source of `NO_EFFECT` false positives when accessing a static object through an instance, when using a clang-based compiler.

SAT-47270
:   Reported in version: 2025.3.0
:   Fixed an issue where the `DIVIDE_BY_ZERO` checker could cause significant performance degradation in the presence of `nan` values in the code.

SATSEC-16248
:   Reported in version: unspecified
:   Fixed a bug with the `XSS` checker leading to a recoverable error.

SATW-5326
:   Reported in version: 2022.12.0, 2023.6.0
:   Fixed False Positive for Autosar C++14 rule M8-5-2.

SATW-5692
:   Reported in version: 2023.12.0
:   Fixed False Positive for AUTOSAR C++14 M5-2-10.

SATW-6133
:   Reported in version: 2023.6.0
:   Fixed False positive for AUTOSAR C++14 A12-1-5.

SATW-6283
:   Reported in version: 2024.6.0
:   Fixed False Positive for AUTOSAR C++-14 A13-5-2.

SATW-6293
:   Reported in version: 2024.6.0
:   Fixed False positive for AUTOSAR C++14 M5-3-1.

SATW-6500
:   Reported in version: unspecified
:   Fixed False Positive for CERT LCK08-J.

SATW-6516
:   Reported in version: 2024.12.0
:   Fixed FNs in MISRA C++-2023 Rule 9.2.1 for expression initializers.

SATW-6601
:   Reported in version: 2024.12.0
:   Fixed the false negative issue related to MISRA C++ 2023 Rule 21.6.2 for the global variables.

SATW-6629
:   Reported in version: 2025.3.0
:   Fixed FP for Autosar C++14 A5-2-2, for direct (brace) initialization.

### Coverity Commands 2025.9.0

#### New or changed features

SAT-43409
:   Added support for FlexNet licensing to the macos-arm platform. For compatibility reasons, the `flexlm` server needs to also run on macos-arm.

SAT-47085
:   Improved handling of the `--file-regex` and `--file-not-regex` options to `cov-run-desktop` and `cov-format-errors` on Windows. They will now accept either `\` or `/` as a path separator.

#### Bug fixes

SAT-45545
:   Reported in version: 2023.12.0
:   Fixed an unrecoverable analysis crash with message "tuinfo.cpp:411: allowExternalClassMembers" in some cases involving error recovery and Java nested classes.

SAT-47224
:   Reported in version: 2024.12.0
:   Fixed an unrecoverable analysis crash with message `virtuallinker.cpp:276: assertion failed: rv != NULL` in some cases involving C++ nested classes.

SAT-47279
:   Reported in version: 2025.6.0
:   Fixed an issue that could cause analysis to stall at the "computing links" phase when using `--emit-complementary-info`.

### Coverity Compilers and Capture 2025.9.0

#### End-of-life products

CAP-2417
:   `cov-setup-bazel-registry` is no longer required and has been removed as of 2025.9.0. Please see the "Building with Bazel" section of the Coverity Analysis User and Administrator Guide for more details on how to integrate with Bazel.

CMPCPP-15100
:   Support for Android NDK r21e and earlier has been EOLed.

#### Deprecated products and features

CAP-2424
:   The `cov-build` option `--bazel-provide-empty-cpp-toolchain` is deprecated and no longer has any effect. It will be removed in a future release.

CMPJ-2411
:   Support for Oracle/Open JDK 24 is deprecated as of 2025.9.0 and will be removed in a future release.

#### New or changed features

CMPFG-1555
:   Support for Python 3.12 has been added as of 2024.9.0.

#### Bug fixes

CAP-2446
:   Reported in version: 2024.6.0
:   Capture performance for very large Bazel builds with a large number of targets supplied in the build command has been significantly improved.

CAP-2449
:   Reported in version: 2024.6.0, 2024.9.0, 2024.12.0, 2025.6.0
:   `cov-build --bazel` will now respect any "startup" arguments (arguments between `bazel` and the action) passed with the bazel command when it runs derived `bazel info` commands

CAP-2476
:   Reported in version: 2025.6.0
:   `cov-build` in `--instrument` mode on Windows no longer causes C/C++ compilations to fail when using Visual Studio 2022 versions newer than 17.6.

CCK-2841
:   Reported in version: 2022.9.0
:   Added Support for -Qoption,c and -Qoption,cpp for Intel Oneapi compiler.

CMPCPP-13208
:   Reported in version: 2022.9.0
:   Fixed a crash in cov-internal-emit-clang when a __uuidof expression was used in a constexpr context.

CMPCPP-14271
:   Reported in version: 2023.9.0
:   Error with cov-manage-emit add "Invalid row detected in translation unit row <N>: No row <M> in table CompilationArtifact" has been fixed.

CMPCPP-14481
:   Reported in version: 2023.12.0
:   Fixed a crash when using templates defined in pch files while using Microsoft mode.

CMPCPP-14738
:   Reported in version: 2024.3.1
:   Fixed a parse error in cov-emit due to a GNU emulation issue.

CMPCPP-15092
:   Reported in version: 2025.3.0
:   Fixed an error when using a 3-way operator (<=>) in c++20 mode.

CMPCPP-15166
:   Reported in version: 2024.12.0
:   Long relative paths using ".." were exceeding the max path limit. These paths are now normalized to be shorter.

CMPCPP-15207
:   Reported in version: 2025.3.0
:   Fixed an assertion failure in cov-emit involving `requires` clauses.

CMPCPP-15239
:   Reported in version: 2025.6.0
:   Fixed a compilation error in cov-emit when using the flag /utf-8 with MSVC mode.

CMPCPP-15309
:   Reported in version: 2025.6.0
:   Assertion or catastrophic on template specialization has been fixed.

CMPFG-1573
:   Reported in version: 2024.6.0
:   In the Kotlin Frontend, fixed handling of valueOf() calls for nullable primitive arrays.

CMPGO-558
:   Reported in version: 2024.12.0
:   Fixed an issue in Go variadic argument.

CMPJ-2210
:   Reported in version: 2023.12.0
:   Fixed a Java inner class crash.

CMPJ-2401
:   Reported in version: 2025.6.0
:   Resolved an issue which could cause scan failures while processing JSP files.

CMPJ-2429
:   Reported in version: 2025.3.0
:   Improved handling of unknown types used for generic methods during error recovery in the Java front-end.

## Coverity Desktop 2025.9.0

This section provides release notes for Coverity Desktop components.

### Coverity Desktop for Eclipse 2025.9.0

#### End-of-life products

PRD-13214
:   Support for Eclipse 2022-03 has been removed as of 2025.9.0.

#### Deprecated products and features

PRD-13215
:   Support for Eclipse 2022-09 is deprecated as of 2025.9.0 and will be removed in a future release.

#### New or changed features

PRD-13211
:   Added support for Eclipse 2025-06.

## Coverity Documentation 2025.9.0

This section provides release notes for Coverity Documentation components.

### Coverity Documentation 2025.9.0

#### New or changed features

COVDOCS-1799
:   In the *Checker Reference,* we have updated the description of CSRF to clarify that this checker is enabled by default for Ruby code.

COVDOCS-1801
:   In the *Guide to the Coverity Point and Scan UI and the Coverity CLI,* updated the "Web app security configuration" page to more clearly show the context of these options in a YAML configuration file.

COVDOCS-1819
:   (See COVCLI-3918.)

COVDOCS-1829
:   We reorganized the table of contents to make some things easier to find by navigating. Analysis and Connect documentation have discrete chapters containing everything relevant, including installation, upgrade, and support information. An Integrations chapter contains the Coverity CLI, Point and Scan, and Coverity Desktop.

#### Bug fixes

COVDOCS-1747
:   Reported in version: unspecified
:   In the *Coverity Cloud Deployment Administrator and User Guide*, improved LDAP descriptions, emphasized the need to use the Connect UI to configure LDAP for the first time, described how to change LDAP configuration values using Helm keys, and documented the LDAP Helm keys.

COVDOCS-1809
:   Reported in version: 2024.12.1
:   In the *Coverity Cloud Deployment Administrator and User Guide*, organized documentation of scan services Helm keys into platform-specific sections, providing better guidance for each deployment platform, and linked the keys to the infrastructure creation and configuration.

COVDOCS-1818
:   Reported in version: unspecified
:   Information about Kotlin support in the *Analysis Administration Guide* has been corrected.

COVDOCS-1820
:   Reported in version: 2025.9.0
:   Information about the "Web and mobile application security" option `--recommended-security-checkers` has been added to the *Command Reference* description of `cov-analyze`.

COVDOCS-1831
:   Reported in version: unspecified
:   In the *Checker Reference,* the sample code for the "Models and Annotations" >"C/C++ Models" section of the NULL_RETURNS description has been updated and corrected.

COVDOCS-1842
:   Reported in version: 2025.6.0, 2025.6.1, 2025.6.2
:   Fixed an issue with the Japanese translation for the Checker Enablement and Option Defaults page.

COVDOCS-1843
:   Reported in version: 2025.6.0
:   In the *Coverity Analysis User and Administrator Guide* and the _Guide to the Coverity Point and Scan UI and the Coverity CLI, added disclaimers to notify users that building with Bazel does not support caching.

COVDOCS-1848
:   Reported in version: 2025.6.0
:   In the Coverity Cloud Admin Guide, the steps to reset the Coverity Connect password have been updated.
