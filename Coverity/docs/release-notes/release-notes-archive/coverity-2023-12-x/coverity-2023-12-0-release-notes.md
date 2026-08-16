---
title: "Coverity 2023.12.0 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2023.12.0-release-notes.html"
content_id: "sI_fZFr3EMYq2cMxMo8rHg"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:38.737697+00:00"
---

# Coverity 2023.12.0 Release Notes

## Important information for 2023.12.0

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

The Coverity 2023.12.0 release adds support for several new language versions, while simplifying cloud deployments and enhancing the user experience.

**Release highlights**

- Coverity cloud deployment adds support for forward compatibility to the Scan Service.
- Coverity cloud deployment adds the ability to cancel a job in the Scan Service.
- Coverity Connect now supports CWE Top 25 2023.
- Coverity Connect now supports PostgreSQL version 15.
- Coverity Analysis now supports macOS 14.
- Updated support for C++ 23, Java 21, Go 1.21, Ruby 3, and TypeScript/ECMAScript 2023.
- Updated support for Clang 17, Xcode 15, and Android NDK R26.
- Dart/Flutter support is now available through Rapid Scan Static (Sigma), bundled with Coverity.
- PHP Symfony and Laravel support is now available through Rapid Scan Static (Sigma), bundled with Coverity.
- New hardcoded secrets checkers have been added for Java and JavaScript/TypeScript.
- Addressed several false positive and false negative reports in the `COPY_PASTE_ERROR`, `INFINITE_LOOP`, and `INTEGER_OVERFLOW` checkers.
- Coverity Point and Scan's user interface has been redesigned to align with other Synopsys Application Security products.
- Coverity Point and Scan will now surface more information about the defects that it found after a scan has completed.
- Coverity Point and Scan has a new option that allows users to easily export all relevant Coverity scan logs.

**Known issues**

- Solaris and AIX Coverity Analysis binaries will not be available in this release and will be delayed to a minor release of 2023.12

Please see below for full details of these and other enhancements included in this release.

## Coverity Platform 2023.12.0

This section provides release notes for Coverity Platform components.

### Coverity Connect 2023.12.0

#### Deprecated products and features

COVDOCS-1205
:   Support for Coverity Connect integration with Jira Server is deprecated as of 2023.12.0 and will be removed in a future release.

#### New or changed features

COVDOCS-1183
:   Coverity Connect has upgraded its external database support to PostgreSQL 11–15 (including all minor releases). The embedded database has been upgraded to PostgreSQL 15.4.

COVDOCS-1232
:   In the bundled software, Apache Tomcat has been updated to version 9.0.82 and OpenJDK has been updated to version 17.0.9.

IM-28458
:   Use the cim property `cim.authkey.expiration.duration` to set the expiration duration of auth keys in hours, days, months or years in the format <durationValue><unit>, for example 10h. Accepted units are hours (h/H), days (d/D), months (m/M) and years (y/Y). The default value is 30Y (30 years).

IM-30019
:   Two new operations have been added to the Coverity Connect REST API:

    - The `GET /healthcheck/data` operation retrieves the user's most recently generated health check report as a JSON response.
    - The `DELETE /healthcheck/stopGeneration` operation aborts the generation of an in-progress health check report.

IM-30370
:   The user will see the message "Password has been used recently. Please choose a different one.", when trying to reset the password (from the login page) or trying to change the password from the user preferences menu, and the new password matches the password history.

IM-30532
:   To retain local groups associations for the user when SAML Groups is enabled, set the `saml.user.local.groups.removal` property in the `cim.properties` file to `false`. The default value for this property is `true`, which means users will be removed from local group when SAML Groups is enabled.

IM-30939
:   New attributes have been added to the response of the `GET /issues/sourceCodeInfo` operation of the Coverity Connect REST API:

    - The new `issueOccurrences.eLearningCweUrl` attribute contains the URL for the Common Weakness Enumeration (CWE) documentation related to the issue.
    - The new `issueOccurrences.secureCodeWarrior.learningVideoUrls` attribute contains an array of URLs for Secure Code Warrior learning videos related to the issue.
    - The new `issueOccurrences.secureCodeWarrior.portalUrl` attribute contains the URL for the Secure Code Warrior portal.

IM-31222
:   A new property, `udc.data.collection.disable`, has been added to `cim.properties`. To disable the collection of use and compliance data (UDC), set `udc.data.collection.disable` to `true`.

#### Bug fixes

CNC-2322
:   Reported in version: 2023.3.2, 2023.6.0
:   Fixed a performance issue in the `/api/v2/issues/search` and `/api/v2/issueOccurrences/search` REST API operations that occurred when the request body contained thousands of matchers per filter.

CNC-2431
:   Reported in version: 2023.9.0
:   Corrected documentation link in the **Maintenance** tab.

IM-26726
:   Reported in version: 2021.06, 2021.12
:   Fixed a bug where report generation from the **Health Check** menu would fail when projects in the report cumulatively had more than 65,535 snapshots.

IM-28390
:   Reported in version: 2022.03
:   Fixed output of `GET <server>/api/v2/projects` to return only those projects for which the user has access.

IM-29339
:   Reported in version: 2022.9.0, 2022.9.2
:   Improved load performance in the "All Projects" view.

IM-30357
:   Reported in version: 2022.12.0, 2023.3.0
:   Fixed an issue where the user's details were not being saved when switching the account type from LDAP to local.

IM-30395
:   Reported in version: 2023.3.0
:   Event markers are now being correctly updated.

IM-30640
:   Reported in version: 2023.3.0
:   Fixed an issue where Coverity Connect didn't start as a service on a Windows machine without manual intervention.

IM-30932
:   Reported in version: 2023.3.4
:   Improved load performance when selecting all columns in the "All Projects" view.

IM-31046
:   Reported in version: 2023.6.0
:   Fixed source code management (SCM) annotations to now show all annotations, as expected.

IM-31086
:   Reported in version: 2023.6.1
:   Fixed issue with inaccessible **Edit** button on **Projects & Streams** when the Triage Store name is long.

IM-31101
:   Reported in version: 2023.6.0
:   Fixed a bug where upgrade was failing when using an external Microsoft Azure database with the maximum ratio between `work_mem` and `maintenance_work_mem` exceeding 2GB and the `shared_buffers` value also exceeding 2GB.

IM-31130
:   Reported in version: 2023.6.1
:   Coverity Connect now shows the correct line of code when selecting a specific issue in a view.

IM-31161
:   Reported in version: 2023.9.0
:   Various fixes relating to source browser event markers.

IM-31187
:   Reported in version: 2023.9.0
:   **Banner Type** effect fixed for different locales.

IM-31263
:   Reported in version: 2023.6.0, 2023.9.0
:   Fixed the add/edit SAML user functionalities to no longer expect a user to provide or confirm a password.

### Coverity Report Generators 2023.12.0

#### New or changed features

RG-1786
:   'Issue Kind' information is now shown in the Coverity Security Report.

#### Bug fixes

RG-1818
:   Reported in version: 2023.6.0
:   Fixed 'issueImpact' typo in JSON output as part of the Coverity Security Report.

## Coverity Analysis 2023.12.0

This section provides release notes for Coverity Analysis components.

### Coverity Analysis - General 2023.12.0

#### New or changed features

SAT-43712
:   Added models for the `libical` library.

SATSEC-3190
:   Ruby analysis using Brakeman Pro has been upgraded to Brakeman version 6.0.1.

#### Bug fixes

RELENG-7567
:   Reported in version: 2023.3.2
:   Updated the Coverity installer builds to sign Coverity DLL files and added signature checks for DLL files to the automated test suites.

SAT-44825
:   Reported in version: 2023.6.0
:   Fixed a recoverable crash with message "assertion failed: !edge->from->ast_nodes.empty()" in some cases involving Java `switch` expressions.

SAT-44953
:   Reported in version: 2023.9.0
:   Fixed a `cov-analyze` command crash with message "assertion failed: Invalid type" when exporting summaries in some C++ cases.

SAT-45027
:   Reported in version: 2023.9.0
:   Fixed an issue that could cause the `deviation-warnings.txt` files not to appear if all deviations were unused.

### Coverity CLI 2023.12.0

#### New or changed features

COVCLI-2469
:   Support for use of a forward proxy to communicate with Coverity Connect has been added to Coverity CLI.

### Coverity Checkers 2023.12.0

For a summary of checkers that have been added or changed in this release, refer to the "Coverity Checker Change History" table in the *Coverity Checker Reference*.

#### New or changed features

SAT-19934
:   The `INFINITE_LOOP` checker now has a new heuristic that reports a defect if a change to the loop condition is not reachable. [All languages]

SAT-29768, SAT-40674
:   A new heuristic has been added to the `COPY_PASTE_ERROR` checker to consider candidates where the replacement of two objects may have different class types, or derived class types (for example, a pointer to a class). [C/C+, C#, CUDA, Java, Objective-C/C+, Scala]

SAT-44236
:   The `INTEGER_OVERFLOW` checker has been redesigned. It can now also be enabled by the `--security` option. [All languages]

SAT-44457
:   The new `POINTER_NONDETERMINISM` checker reports on non-deterministic program behavior arising from pointer comparisons. [C/C++, CUDA, Objective-C/C++]

SAT-44607
:   The `CONSTANT_EXPR_RESULT` checker now reports a defect when, in a loop condition test, the loop index is compared with a value outside of the bounds of the loop index's data type. [All languages]

SAT-44714
:   Added support for Hyundai code compliance checker `MC-MSC-013`.

SAT-44794
:   Improved results for the `LOCK` checker, particularly for the Go language. [Go]

SATSEC-11947
:   Fixed false positives for the `SQLI` checker related to using the Java `StringWriter` class. [Java]

SATSEC-15481
:   Fixed false positives for the `SQLI` checker related to `MyBatis`. [Java]

SATSEC-15540
:   Fixed a false positive for the `HARDCODED_CREDENTIALS` C# checker. [C#]

SATSEC-15543
:   Fixed a false positive for the `INSECURE_COMMUNICATION` C# checker. [C#]

SATSEC-15551
:   The SpotBugs integration has been updated to version 4.8.0.

SATSEC-15554
:   The `SCRIPT_CODE_INJECTION` checker now supports Kotlin.

SATSEC-15565
:   Fixed a false positive for the `SQLI` checker. [C#]

SATSEC-3201
:   The `BAD_CERT_VERIFICATION` checker now supports C# and Visual Basic.

SATSEC-3238
:   The `REGEX_INJECTION` checker now supports Go.

SATW-5303
:   The `CERT DCL60-CPP` checker no longer reports defects on symbols with no definition. It only reports defects on symbols with more than one definition.

#### Bug fixes

SAT-14423, SAT-16314, SAT-38431, SAT-41048, SAT-5996, SAT-6966
:   Reported in version: 2021.06, 2021.12.0, 5.5.1, 5.5.3, 7.5.1 , 8.0.0
:   Rewrote the `INTEGER_OVERFLOW` checker.

SAT-41525, SAT-44343
:   Reported in version: 2021.09
:   Fixed a source of false positives for the `CERT STR31-C` checker where we claimed an index could be negative when in fact it could not.

SAT-42975
:   Reported in version: 2022.9.0
:   Fixed a false positive for the `FORWARD_NULL` checker involving `std::exchange`.[C++]

SAT-43224
:   Reported in version: 2022.12.0
:   Fixed a false positive for the `DEADCODE` Kotlin checker when using the `let` function inside a loop. [Kotlin]

SAT-44700
:   Reported in version: 2023.3.0
:   The `RULE_OF_ZERO_THREE_FIVE` checker now considers special functions declared with `=delete` as being user-defined. [C++, CUDA]

SAT-44725
:   Reported in version: 2022.9.1
:   Fixed an issue for the `COPY_PASTE_ERROR` checker where it can run for a very long time when the analyzed function has too many similar expressions or statements. [C, C++, C#]

SAT-44744
:   Reported in version: 2023.9.0
:   The `COPY_PASTE_ERROR` checker has been improved to reduce false positives around simple `if` statements, `const` variables and `enum` tags. [All languages]

SAT-44779
:   Reported in version: 2023.9.0
:   Fixed a source of false positives for the `UNLOCKED_ACCESS` Java checker when using `ThreadLocal`. [Java]

SAT-44790
:   Reported in version: 2023.9.0
:   Fixed a source of false positives for the `FORWARD_NULL` Go checker when checked downcasts are used. [Go]

SAT-44796
:   Reported in version: 2023.9.0
:   Fixed a source of false positives in concurrency checkers such as `LOCK` for Go code where we would sometimes see a lock but not the matching unlock. [Go]

SAT-44811
:   Reported in version: 2023.6.0
:   Fixed an issue where implicit returns were ignored for the `HIS_RETURN` metric, which could prevent reporting some HIS metric violations.

SAT-44834
:   Reported in version: 2023.9.0
:   Fixed an issue where some compliance defects could be non-deterministically suppressed if they appeared in code that's sometimes compiled as a system header and sometimes as a user header. [C, C++, CUDA]

SAT-44856
:   Reported in version: 2023.6.0
:   Fixed a source of concurrency false positives for the `LOCK_EVASION` C++ checker when using semaphores. [C++]

SAT-44917
:   Reported in version: 2023.9.0
:   Fixed a false positive for the `OVERRUN` checker when a variable is assigned and compared against a constant inside a conditional statement (for example, an `if` statement). [All languages]

SAT-44956
:   Reported in version: 2022.12.0
:   Fixed an issue for the `UNINIT` and `AUTOSAR C++ A8-5-0` checkers where we would incorrectly claim that objects of type `std::mutex` where not initialized. [C++, CUDA, Objective-C++]

SAT-44971
:   Reported in version: 2023.9.0
:   Fixed a false positive for the `PRINTF_ARGS` checker, where we incorrectly claimed that the `'` flag did not apply to `%u`. [C/C++, CUDA, Objective-C/C++]

SAT-44998
:   Reported in version: 2023.6.0
:   The `GLOBAL_INIT_ORDERING` checker no longer considers the presence of a particular global variable as potentially conflicting if it was defined with a `constexpr` constructor. [C++, CUDA, Objective-C++]

SAT-9560
:   Reported in version: 6.5.3
:   The `COPY_PASTE_ERROR` checker now finds defects inside expressions such as `!(expr1) && !(expr2)`. [All languages]

SATSEC-15567
:   Reported in version: 2023.6.0
:   Fixed a false negative for the `SQLI` checker when using the Express framework. [JavaScript]

SATW-5163, SATW-5357
:   Reported in version: 2023.6.0
:   Fixed a false positive for the MISRA C-2004 Rule 13.1 checker.

SATW-5244
:   Reported in version: 2022.12.0
:   Fixed false positive for the AUTOSAR C++ A5-1-1 checker when an `enum` value is used in a `case` condition inside a `switch` block.

SATW-5288
:   Reported in version: 2023.12.0
:   Fixed false positive for the AUTOSAR C++ A18-5-2 checker related to the `reset()` method of `std::unique_ptr` and `std::shared_ptr`.

SATW-5320
:   Reported in version: 2022.12.0
:   Fixed false positive for AUTOSAR C++ A8-4-9 checker when passing a function as parameter and there is no modification (reference to function).

SATW-5336
:   Reported in version: 2023.6.0
:   Fixed a false positive (DCL01-J violation) caused by the `Utils`, `Utility` and `StringUtils` libraries, which are not a part of the Java Standard library.

### Coverity Compilers and Capture 2023.12.0

#### End-of-life products

CMPG-4035
:   Support for LLVM Clang version 7.x has been removed as of 2023.12.0.

CMPGO-407
:   Support for Go 1.19 has been removed as of 2023.12.0.

COVP-2580
:   Support for macOS 11 has been removed as of 2023.12.0.

#### Deprecated products and features

CMPG-4045
:   Support for LLVM Clang 8.0 is deprecated as of 2023.12.0 and will be removed in a future release.

CMPG-4435
:   Support for Go 1.20 is deprecated as of 2023.12.0 and will be removed in a future release.

CMPG-4446
:   Support for Oracle/Open JDK 20 is deprecated as of 2023.12.0 and will be removed in a future release.

COVP-2583
:   Support for Windows Server 2019 is deprecated as of 2023.12.0 and will be removed in a future release.

COVP-2586
:   Support for .NET 7 is deprecated as of 2023.12.0 and will be removed in a future release.

#### New or changed features

CMPCPP-12794
:   Support for Clang 17.0.1, Xcode 15.0, and Android NDK r26a has been added as of 2023.12.0.

CMPCPP-13253
:   The Clang compiler now accepts the `-mgeneral-regs-only` option.

CMPCPP-3880
:   The `--record-with-source` option is now supported for **Clang** based compilers.

CMPG-4437
:   Support for TypeScript 5.0, 5.1, and 5.2 has been added as of 2023.12.0.

CMPG-4438
:   Support added for ECMAScript 14 (JavaScript 2023).

CMPG-4447
:   Support for Oracle/Open JDK 21 has been added as of 2023.12.0.

    Usage of Java 21 preview features are not supported at this time. To avoid issues, ensure error recovery is enabled when using preview features.

CMPG-4449
:   Support for Xtensa `xt-clang` Linux compiler version RI-2022.10 has been added as of 2023.12.0.

CMPGO-402
:   Support for Go 1.21 has been added as of 2023.12.0.

CMPJS-1103
:   Significantly improved performance of JavaScript capture when large sourcemaps are present.

COVP-2578
:   Support for macOS 14 has been added as of 2023.12.0.

#### Bug fixes

CAP-1790
:   Reported in version: 2020.09
:   When running `cmake` on macOS under `cov-build` you may encounter a "No Files Emitted" warning. If you have validated that (a) your compilers are properly configured and (b) your build is actually compiling source code, then set the environment variable `COVERITY_MACOS_PROBLEM_EXES=cmake` before running `cov-build`; this should allow your build to be properly captured.

CAP-2170
:   Reported in version: 2023.3.0
:   Fixed race condition issue for the `cov-build` command, which could cause the build to fail with the message: `[ERROR] capture: cannot update build log: Bad file descriptor`.

CAP-2204
:   Reported in version: 2023.9.0
:   Fixed issue for Kotlin where `cov-build` running with Gradle 8.1 or newer could miss compilations if a previous Kotlin daemon was running.

CMPCPP-12137
:   Reported in version: 2021.12.0
:   Fixes an issue in `cov-emit` for template pack expansion.

CMPCPP-12739
:   Reported in version: 2021.12.1
:   Fixes an issue in pre-processor of `cov-emit` for string literals.

CMPCPP-13282
:   Reported in version: 2022.3.0
:   Changed the Compiler Integration Toolkit (CIT) configuration for Tasking Tricore to look in the current directory.

CMPCPP-13311
:   Reported in version: 2023.6.0, 2023.3.0, 2023.9.0
:   Fixes an issue in `cov-emit` where passing multiple string arguments to the GCC target pragma had caused the command to hang.

CMPCPP-13569
:   Reported in version: 2022.6.0
:   Fixed the handling of the `-e` option for Clang.

CMPCPP-13656
:   Reported in version: unspecified
:   Precompiled header files (PCH) larger than 4GB are now supported.

CMPCPP-13674
:   Reported in version: 2023.6.0
:   Fixed some C/C++ missing library linkage information needed by Black Duck.

CMPCPP-13764
:   Reported in version: 2023.3.2
:   A fix has been added to the C/C++ compiler to avoid Coverity Connect errors such as:

    `Caused by: org.postgresql.util.PSQLException: ERROR: index row size 3568 exceeds btree version 3 maximum 2712 for index "uk_2ypxjm2ayrneyrjikigvmvq24"`

CMPCPP-13765
:   Reported in version: 2023.6.0, 2022.9.1
:   Fixed issue where `__STRICT_ANSI__` was getting defined incorrectly while using the Green Hills compiler.

CMPCPP-13819
:   Reported in version: 2023.6.0
:   Fixed `cov-internal-emit-clang` crash with assertion failed: "Do not have dependent type kind for this kind of `UnaryTransformType`".

CMPG-4011
:   Reported in version: 2022.6.0
:   `cov-configure --help` no longer erroneously claims support for the `--set-instrument-var` option.

CMPGO-432
:   Reported in version: 2023.6.0
:   The `cov-emit-go` command no longer sets the value of `GO111MODULE` to `auto` if it is already set to a different value.

CMPJ-2080
:   Reported in version: 2022.12.1
:   Fixed crash for the `cov-emit-java` command when the `--handle-missing-types` option is enabled for invalid Java code with improper usages of labeled `continue` statements.

CMPJ-2129
:   Reported in version: 2023.6.0
:   Fixed crash in `cov-format-errors` caused by `cov-emit-java` failing to strip ignorable characters from Java identifiers.

CMPJ-2130
:   Reported in version: 2023.9.0
:   Fixed `cov-analyze` crash with message "assertion failed: No function named com.google.common.collect.Comparators.least(int, java.util.Comparator)java.util.stream.Collector".

### Coverity Dynamic Analysis 2023.12.0

#### Bug fixes

CMPRB-131
:   Reported in version: 2023.3.0, 2023.6.0
:   The Ruby runtime has been upgraded to version 3.2.2 of the Brakeman Pro Ruby analyzer, which removes the following vulnerabilities:

    - High-impact vulnerabilities removed: CVE-2020-25613, CVE-2021-41819, CVE-2020-5247, CVE-2022-28739, CVE-2023-28756, CVE-2021-28965, CVE-2019-16201, CVE-2019-16255, CVE-2021-28966.
    - Medium-impact vulnerabilities removed: CVE-2019-15845, CVE-2019-16254, CVE-2020-10933, CVE-2021-31810.

### Coverity Point and Scan 2023.12.0

#### New or changed features

COVGUI-2362
:   A new **Zip All** button has been added in the **Log Viewer** panel in the Coverity Point and Scan GUI. This button enables downloading a ZIP file containing all of the log files currently displayed in the **Log Viewer**.

COVGUI-2382
:   In the Coverity Point and Scan GUI, a new **Defects Summary** panel has been added under the **Scan Details** page, where you can view a summary of defects reported by checkers. In the new **Defects Details** tab, you can view details of the defects.

#### Bug fixes

IM-30948
:   Reported in version: unspecified
:   Added support for SSO 2-Step Verification. The SAML IdP Authorization step now redirects to the system's default browser and, after a successful login, it redirects back to Point and Scan to complete the login process.

### Rapid Scan Static (Sigma engine) 2023.12.0

#### New or changed features

SIGMACOV-591
:   Dart support is now available through Rapid Scan Static (Sigma), bundled with Coverity.

#### Bug fixes

SIGMACOV-549
:   Reported in version: 2023.3.0
:   Fixed a hardcoded secret false negative by enabling the `SIGMA.hardcoded_secret` checker for Java, JavaScript and TypeScript.

## Coverity Documentation 2023.12.0

This section provides release notes for Coverity Documentation components.

### Coverity Documentation 2023.12.0

#### New or changed features

COVDOCS-1193
:   In the *Platform Administration Guide* and in the "Coverity glossary" (shared among various documents), added notes to remind users that the names of streams in a source-code project are case sensitive.

COVDOCS-1206
:   Updated the "Coverity language support" table in the Coverity documentation to clarify that the support for Dart, PHP and Swift is version agnostic.

#### Bug fixes

COVDOCS-1181
:   Reported in version: 2023.6.0
:   Updated the *CodeXM Guide* to correct some missing or misleading information about certain object types; in particular, `characterLiteral`, `functionDefinition`, and `globalVariableDefinition`.

COVDOCS-1200
:   Reported in version: 2023.9.0
:   Corrected documentation for the `STRING_NULL:report_string_copy_output` aggressiveness level.

COVDOCS-1228, COVDOCS-1229
:   Reported in version: 2023.6.0, 2023.9.0
:   Corrected inconsistencies regarding aggresiveness level for several checkers in the *Coverity Command Reference* and *Coverity Checker Reference* documents.

COVDOCS-1230
:   Reported in version: 2023.9.0
:   Corrected inconsistency in documentation about license region options for the Coverity Silent Installer.

COVDOCS-1241
:   Reported in version: 2023.6.0
:   Corrected description for the `cov-admin-db psql` command in the *Coverity Command Reference*, removing "external" from the supported database types. This command only works with embedded databases.
