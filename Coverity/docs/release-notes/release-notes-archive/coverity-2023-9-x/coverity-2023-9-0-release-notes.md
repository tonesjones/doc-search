---
title: "Coverity 2023.9.0 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2023.9.0-release-notes.html"
content_id: "2CwnITxaIaAoTZ9L5rbDXg"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:42.925207+00:00"
---

# Coverity 2023.9.0 Release Notes

## Important information for 2023.9.0

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

The Coverity 2023.9.0 release adds support for several new language versions, while simplifying cloud deployments and enhancing the user experience.

**Release highlights**

- Coverity cloud deployment supports Linux ARM64.
- Build capture is now supported on Apple silicon machines.
- Improved Issue query performance.
- Analysis details section of UI provides more details on key checkers:
  - Parse Warning (PW*) checkers
  - MISRA, CERT or other coding standard checkers
- Updated support for Java 20, Kotlin 1.9, and Python 3.11.
- PHP 8 support is now available through Rapid Scan Static (Sigma), bundled with Coverity. PHP quality checkers are no longer included.
- Addressed several false positive and false negative reports in the `PATH_MANIPULATION` checker.
- The Coverity CLI and Thin Client now support scanning Visual Basic projects.
- Coverity Point and Scan now supports scanning Git-based source code management repositiories.
- Coverity Point and Scan now supports Operating System-native notifications for when scans have completed for Windows, Linux, and macOS.

**Known issues**

- Customers might see a higher number of false positives than expected in certain PHP checkers due to a lack of models for some libraries.
  Customers using Coverity to scan PHP applications might want to consider waiting to upgrade until a fix is available.
  This is scheduled for the first 2023.9 minor release.

Please see below for full details of these and other enhancements included in this release.

## Coverity Platform 2023.9.0

This section provides release notes for Coverity Platform components.

### Coverity Connect 2023.9.0

#### Deprecated products and features

COVDOCS-1116
:   Support for Windows Server 2012 is deprecated and will be removed in a future release.

#### New or changed features

COVDOCS-1075
:   The `connect.enable.metrics` property is added to enable or disable publishing of application metrics to the `/metrics` endpoint. This is `false` by default. Customers who have been using metrics in prior releases must set this value to `true` in the 2023.9.0 release to be able to access metrics at the `/metrics` endpoint.

COVDOCS-1108
:   In the bundled software, Apache Tomcat has been updated to version 9.0.78 and OpenJDK has been updated to version 17.0.8.

IM-27512
:   A new REST API operation (`POST /files/search`) has been added for retrieving information on source code files and associated streams.

IM-29201
:   A new REST API operation (`GET /issues/sourceCodeInfo`) has been added for retrieving source code-related information for a specified issue.

IM-29824
:   Parse Warning (PW*) checkers are now listed in the "Enabled Checkers" section.

#### Bug fixes

COVDOCS-1115
:   Reported in version: 2023.6.0
:   Coverity Connect and Coverity Reports server platform support for Windows workstation releases 10 and higher was erroneously removed from the documentation in release 2022.12.0. This support has been reinstated to the documentation in this release.

IM-29477
:   Reported in version: 2022.9.0, 2022.12.0
:   Fixed issue where `cov-archive export-streams` gives a database error when defects in streams have SAML owners.

IM-29740
:   Reported in version: 2022.9.0, 2022.12.0, 2022.6.2, 2023.3.4
:   Fixed Coverity REST API V2 endpoint `PUT "/issues/triage"` to update the value of the "Ext. Reference" triage field correctly.

IM-29756
:   Reported in version: 2022.6.0
:   Fixed issue with access to unsaved view of `query/defects.htm?projectId=<valid project id>&snapshotId=<valid snapshot id>` .

IM-30020
:   Reported in version: 2022.12.1
:   Fixed timestamp inconsistency on snapshot view for Coverity Connect.

IM-30140
:   Reported in version: 2022.12.0, 2022.12.1
:   Timestamp in "Snapshots" |"All In Project" is now correct.

IM-30329
:   Reported in version: 2022.12.1
:   Vulnerable components in Coverity Connect have either been updated or removed.

IM-30488, IM-30499
:   Reported in version: 2023.3.0
:   Fixed CWE mapping issue between Connect UI and generated reports.

IM-30546
:   Reported in version: 2023.3.2
:   Fixed issues in the "Triage" panel in the GUI.

IM-30569
:   Reported in version: 2022.12.1, 2023.3.2
:   The **OK** button is now visible and clickable when selecting **Save a Copy** of a **Shared** view.

IM-30590
:   Reported in version: 2023.3.0
:   Correct issues are now shown after clicking on "View Issues" from "Hierarchies".

IM-30803
:   Reported in version: 2023.3.2
:   Fixed an issue with project/stream role assignment disappearance on subscriber after sync up with coordinator.

IM-30827
:   Reported in version: 2023.3.2
:   Hovering over an option in a menu highlights that option.

IM-30833
:   Reported in version: 2023.3.2, 2023.6.0
:   Fixed view rendering issues when using saved URLs from old Coverity Connect versions.

IM-30848
:   Reported in version: 2023.3.2
:   The Event descriptor text is rendered correctly when the SCM Author option is enabled.

IM-30901
:   Reported in version: 2023.3.2
:   Fixed issues with rendering of views.

IM-30947
:   Reported in version: 2023.6.0
:   Links from view notification emails no longer direct the user to views with issues in the UI.

### Coverity Report Generators 2023.9.0

#### Bug fixes

RG-1559, RG-1585, RG-1586, RG-1689, RG-1751, RG-1772, RG-1775, RG-1788, RG-1802
:   Reported in version: 2020.06-1 , 2020.12 , 2022.03, 2021.12.1, 2022.12.0, 2022.12.2, 2023.3.0, 2022.6.0, 2022.9.0, 2023.3.0
:   Fixed CWE mapping issue between Connect UI and generated reports.

RG-1784
:   Reported in version: 2023.3.0
:   For the Security Report, added configuration file option to hide or display the LOC (Lines of Code) metric from the report. The default is to show the LOC metric in the report.

## Coverity Analysis 2023.9.0

This section provides release notes for Coverity Analysis components.

### Coverity Analysis - General 2023.9.0

#### New or changed features

COVCLI-2679
:   The `cov-build` command option `--record-with-source` can now be used for Visual Basic. This change means that it is now possible to use the thin client to analyze Visual Basic source code where the thin client is intended for use with Coverity cloud deployments.

COVDOCS-1082
:   Added Coverity Thin Client on Linux, Windows, and macOS (Intel) support for Visual Basic (VB) in 2023.9.0.

COVGUI-931
:   The Point and Scan GUI will now be able to leverage the native notification systems of macOS, Windows, and Linux.
    The supported notifications will cover the cases when a scan has completed or when a scan has failed.

SAT-39906
:   Improved analysis performance, notably on C/C++ codebases.

SAT-43733
:   Improved `glib` APIs modelling by adding models for `g_list*`, `g_slist*` and `g_slice*` functions.

SAT-44523
:   Improved analysis performance, notably on large C++ codebases.

SAT-44578
:   Improved analysis performance, notably on large C++ codebases, when using the default set of checkers.

#### Bug fixes

SAT-44660
:   Reported in version: 2022.9.0
:   Made a change to improve analysis runtime when analyzing functions containing thousands of different clauses separated by `&&` operators within a single expression.

### Coverity Checkers 2023.9.0

For a summary of checkers that have been added or changed in this release, refer to the "Coverity Checker Change History" table in the *Coverity Checker Reference*.

#### Deprecated products and features

COVDOCS-1127
:   Support for Ruby in Coverity quality checkers is being deprecated as of Coverity 2023.9.0 and will be removed in a future release. Support for the Brakeman Pro analyzer, which runs as part of the Coverity Analysis suite, will continue. The following Coverity checkers for Ruby are affected:

    - CONSTANT_EXPRESSION_RESULT
    - COPY_PASTE_ERROR
    - DEADCODE
    - FORWARD_NULL
    - IDENTICAL_BRANCHES
    - NO_EFFECT
    - PARSE_ERROR
    - REVERSE_INULL
    - UNEXPECTED_CONTROL_FLOW
    - UNREACHABLE

#### New or changed features

SAT-29201
:   The `COPY_PASTE_ERROR` checker has been improved to consider code from simple `if`/`else` statements, where there is only one statement in both blocks of the `if`/`else`. All languages supported by `COPY_PASTE_ERROR` are affected by these changes.

SAT-39171
:   Improved the `UNLOCKED_ACCESS` checker for C/C++ to report on thread-unsafe functions such as `localtime`.

SAT-41210
:   Added option `not_zero_checked` to the `DIVIDE_BY_ZERO` checker for all supported languages except for Ruby.

SAT-41725
:   Improved handling of the C++ standard concurrency library, notably uses of `std::unique_lock`.

SAT-44463
:   Improved results of the `BAD_CHECK_OF_WAIT_COND` checker for all supported languages.

SAT-44637
:   Improved TEE APIs modelling by adding models for functions in the TEE core API.

SAT-44672
:   The `BUFFER_SIZE` checker now considers size function parameters when the `report_fixed_size_dest` option is set to `true`. All languages supported by `BUFFER_SIZE` are affected by these changes.

SATSEC-6394
:   The `SEALED_JAR_ESCAPE` Java checker now supports the `ignore_package` and `show_system_packages` options.

SATSEC-7069
:   The `PATH_MANIPULATION` checker for Java has been reworked to report defects at file system operations instead of at the creation of `File` and `Path` objects, eliminating certain classes of false positives.

SATW-5303
:   The `CERT DCL60-CPP` checker no longer reports defects on symbols with no definition. It only reports defects on symbols with more than one definition.

SIGMACOV-557
:   The `INSECURE_COMMUNICATION` Java and JavaScript checkers have been removed. The functionality is now covered by Sigma checkers. For details, see the "Upgrade considerations for 2023.9" section in the *Coverity Installation and Upgrade Guide*.

#### Bug fixes

SAT-16545
:   Reported in version: 7.0.3
:   The `COPY_PASTE_ERROR` checker now considers `constant` variables and `enum` tags while checking for defects. This behavior may result in either more defects or fewer defects, depending on the context. All languages that are supported by this checker are affected by this change.

SAT-38688
:   Reported in version: 2021.03
:   Fixed a false positive for the `UNINIT` checker on `std::optional` when initialized with `nullopt` (C++, CUDA, Objective-C++).

SAT-40309
:   Reported in version: 2021.9.0
:   The `COPY_PASTE_ERROR` checker now considers `constant` variables and `enum` tags while checking for defects. This behavior may result in either more defects or fewer defects, depending on the context.

SAT-43407, SAT-43569
:   Reported in version: 2022.3.0, 2022.9.0
:   Fixed a false positive for the `UNINIT` checker on `std::optional` when initialized with `nullopt`.

SAT-44420
:   Reported in version: 2023.6.0
:   Fixed a recoverable crash with message "It's illegal to commit the same error multiple times." in some cases involving the `VARARGS` checker.

SAT-44537
:   Reported in version: 2023.3.0
:   Improved `USE_AFTER_FREE` checker's handling of local linked lists (C/C++, CUDA, Objective-C/C++).

SAT-44666
:   Reported in version: 2023.3.0
:   Fixed an assertion failure in tainted checkers.

SAT-44747
:   Reported in version: 2022.12.0
:   Fixed a crash involving the `MISSING_PERMISSION_FOR_BROADCAST` checker.

SAT-44772
:   Reported in version: 2023.3.0
:   Fixed an issue that could prevent deviation annotations to apply to `MISRA C-2004 Rule 5.1` and `MISRA C-2012 Rule 5.1` reports when those reports involve multiple files.

SATSEC-15439
:   Reported in version: unspecified
:   Fixed issue for Apex language where the defect impact was not set appropriately.

SATSEC-6201
:   Reported in version: 2022.6.1
:   Fixed a crash when processing an XML configuration file which contains invalid characters.

SATW-5154
:   Reported in version: 2022.9.0
:   Fixed false positive related to "ambiguous essential type" for MISRA C-2012 Rule 10.5.

SATW-5251
:   Reported in version: 2022.12.0
:   Fixed false positive for MISRA-C 2012 Rule11.9, which was caused by an implicit `Null`.

SATW-5291
:   Reported in version: 2022.12.2
:   Fixed a false positive for the `MISRA-C-2012-Rule-15.7` checker.

### Coverity Commands 2023.9.0

#### New or changed features

CMPG-4331
:   For the `cov-emit-java` command, the `--use-fe` option has been deprecated. Already, specifying `--use-fe edg` has no effect and the Eclipse front end is used in every case.

    In a future release, `cov-emit-java` will no longer accept the `--use-fe` option.

COVCLI-2655
:   It is now possible to generate anaylsis results in a JSON file during commit. To do so, use the `coverity scan` or `coverity commit` commands with the `--local-format json --local <json_filename>` options.

SAT-13083
:   Added a new option to the `cov-run-desktop` command, `--report-rws [true|false]`. This option allows disabling mandatory reporting of recovery warnings; previously, recovery warnings would always be reported regardless of configuration.

SIGMACOV-296
:   SIGMA checks can now be enabled individually.

#### Bug fixes

SAT-44100
:   Reported in version: 2023.6.0
:   In the 2023.6.0 release, a communication error -- such as a connection timeout or invalid server certificate -- would cause the `cov-commit-defects` command to crash. This problem has been corrected; the utility now prints an error message instead.

SAT-44639
:   Reported in version: 2023.6.2
:   Fixed an issue when the current user name contains some special characters.

### Coverity Compilers and Capture 2023.9.0

#### End-of-life products

CMPG-4038
:   Support for Oracle/Open JDK 19 has been removed as of Coverity version 2023.9.0.

CMPG-4234
:   Support for Sony PS4 has been dropped as of 2023.9.0.

CMPG-4257
:   Support for IAR National CR16 has been removed as of 2023.9.0.

CMPG-4259
:   Support for IAR Freescale HCS12 has been removed as of 2023.9.0.

COVP-2567
:   Support for FreeBSD 13.1 has been removed as of 2023.9.0.

COVP-2573
:   Support for Perforce 2019.1 has been removed as of 2023.9.0.

#### Deprecated products and features

COVP-2572
:   Support for Perforce 2019.2 is deprecated as of 2023.9.0 and will be removed in a future release.

#### New or changed features

BLC-1247
:   `cov-capture` will no longer provide a copy of Maven and Gradle. Customers will now need to download their own Maven, Gradle, and JDK compatible with their chosen Gradle to capture their Java projects. Upgrade and workaround instructions can be found in the following linked article: <https://community.blackduck.com/s/article/Coverity-2023-9-0-Cov-Capture-Change>.

CAP-2166
:   Build capture using the `cov-build` command is now supported for macOS on Apple silicon.

CMPCPP-13001
:   The `--comptype` option for the `cov-configure` command now accepts the `ignore` and `exclude` values. The `--comptype ignore` option excludes binary, but does not exclude subprocesses. The `--comptype exclude option excludes both binary and subprocesses. This can be useful for ignoring compiler wrapper scripts that have similar names to compilers.

CMPFG-774
:   Support for Kotlin 1.9 has been added as of 2023.9.0

CMPG-4343
:   Support for GCC 13.1 is added in 2023.9.0.

CMPG-4344
:   Support for Python 3.11 has been added as of 2023.9.0

CMPG-4358
:   Support for Kotlin 1.7 has been dropped as of 2023.9.0. Support for Kotlin 1.8 has been deprecated and will be dropped in a future release.

CMPG-4360
:   The `cov-emit` command does no longer support `--ppp_translator cmd:` options.

CMPG-4362
:   The `cov-build` command option `--record-with-source` can now be used for Visual Basic.

CMPG-4384
:   Added support for the Sony PS5 SDK 4.000 compiler.

CMPJS-1106
:   The documentation has been updated to indicate added support for ECMAScript 13. This support was added in 2023.3.0, although the documentation was not updated in that release.

CMPPY-366
:   Support for Python 3.11 has been added as of 2023.9.0.

COVP-2570
:   Support for Git 2.38-2.40 has been added as of 2023.9.0.

COVP-2571
:   Support for Perforce 2023.1 has been added as of 2023.9.0.

#### Bug fixes

CAP-2138
:   Reported in version: 2023.3.0, 2023.6.0
:   The Coverity Bazel integration can now correctly capture compilations whose results are contained inside of a `filegroup` target.

CMPCPP-11007
:   Reported in version: 2020.03
:   Fixed `cov-emit` assertion failure `!v.is_deduced_class` when compiling C++17 source with class template argument deduction.

CMPCPP-11652
:   Reported in version: 2019.12
:   If a source file is included multiple times in the same translation unit (TU), we stop emitting some information about it after a few iterations. This is a heuristic to handle some special use cases that could lead to long compilation times. The `COVERITY_DEDUP_COMMENTS` environment variable is no longer needed to enable this feature and it has been removed.

CMPCPP-12357
:   Reported in version: 2021.12.0
:   Fixed issue where translation (compilation) units were recompiled unnecessarily when moving an intermediary directory from one system to another.

CMPCPP-12363
:   Reported in version: 2021.12.0
:   Improved performance of `cov-internal-emit-clang` when dealing with multiple redefined macros in deep include hierarchies.

CMPCPP-12371
:   Reported in version: 2021.12.0
:   Coverity Analysis now supports the `MSVC -external:I<directory>`option. In previous releases, only `MSVC -external:I <directory>` (with a space between the `I` switch and the directory name) was supported.

CMPCPP-12428
:   Reported in version: 2021.12.0
:   Fixed a crash in `cov-internal-emit-clang` when the left operand of a compound assignment is a pointer.

CMPCPP-12458
:   Reported in version: 2022.3.0
:   Fixes an issue for the `cov-internal-emit-clang` when using the `--preprocess-first` option.

CMPCPP-12462
:   Reported in version: 2021.12.0
:   Fixed an issue where Coverity annotation comments were not properly associated with inline functions that appeared in an included header file.

CMPCPP-13028
:   Reported in version: 2022.3.0
:   Fixed `cov-emit` crash when using Microsoft extensions with the GCC compiler.

CMPCPP-13066
:   Reported in version: 2022.12.0
:   Fixed performance issue for the `cov-internal-emit-clang` command when capture was very slow for files with the last line containing a lot of content to emit.

CMPCPP-13300
:   Reported in version: 2022.12.0
:   Inappropriate diagnostic `OOPS: unexpected TYPELOC 51` has been eliminated and the code construct is now handled.

CMPCPP-13325
:   Reported in version: 2022.9.0
:   When using either the `/QM` or `/QMM` option for the Intel **icx** compiler on Windows, the compilation will be skipped.

CMPCPP-13368
:   Reported in version: 2023.3.0
:   Fixed an issue regarding parse errors when using GCC with non-standard PCH names.

CMPCPP-13488
:   Reported in version: 2023.3.0
:   A problem with template meta-programming was resulting in an assertion in `record_substitution_for_type`. This has been fixed.

CMPCPP-13525
:   Reported in version: 2023.6.0, 2023.3.0
:   Fixed a crash for `cov-configure` when given malformed XML to the `--xml-option`.

CMPFG-566, CMPFG-622, CMPFG-677, CMPFG-693
:   Reported in version: 2022.3.0, 2022.6.0
:   The Coverity Kotlin frontend now uses the Kotlin IR compiler, which fixes several backend JVM errors.

CMPFG-633
:   Reported in version: unspecified
:   Fixed a defect in the Coverity Kotlin frontend, which could be encountered when emitting an `enumValues<T>()` expression.

CMPFG-760
:   Reported in version: 2023.3.0
:   Fixed analysis crash caused by improper handling of Kotlin file-level classes by `cov-emit-java`.

CMPFG-766
:   Reported in version: 2023.3.2
:   Fixed handling of Java 8 `unsigned int` and `unsigned long` types for Kotlin.

CMPFG-768
:   Reported in version: unspecified
:   Fixed handling of the Kotlin `-opt-in` option for multiple values. The `cov-emit-java` command now correctly handles all `-opt-in` values.

CMPGO-367
:   Reported in version: 2022.12.0
:   Fixed issue where `cov-build` hangs on a Go project when using the `itchyny/gojq` library.

CMPJ-1660
:   Reported in version: 2021.06
:   Fixed an issue in which Android ID integers could be conflated.

CMPJ-1671
:   Reported in version: 2021.9.3
:   Fixed a "Cannot find decl for class..." crash which could occur while analyzing Kotlin TUs.

CMPJ-2027
:   Reported in version: 2022.12.2
:   Fixed Coverity Java compiler handling of duplicate `--add-exports` options.

CMPVB-88
:   Reported in version: 2021.03
:   Addressed an issue in `cov-emit-vb` where the assertion "Strings are different" would be thrown when using a method from bytecode with a `varargs` list.

### Rapid Scan Static (Sigma engine) 2023.9.0

#### New or changed features

SIGMACOV-296
:   SIGMA checks can now be enabled individually.

## Coverity Desktop 2023.9.0

This section provides release notes for Coverity Desktop components.

### Coverity Desktop for Android Studio 2023.9.0

#### End-of-life products

PRD-12978
:   Support for Android Studio 4.2 has been removed as of 2023.9.0.

#### Deprecated products and features

PRD-12974
:   Support for Android Studio Arctic Fox (2020.3) is deprecated and will be removed in a future release.

#### New or changed features

PRD-12965
:   Added support for Android Studio Giraffe (2022.3).

### Coverity Desktop for Eclipse 2023.9.0

#### End-of-life products

PRD-12976
:   Support for Eclipse 4.17 (2020-03) has been removed as of 2023.9.0.

#### Deprecated products and features

PRD-12975
:   Support for Eclipse 4.17 (2020-09) is deprecated and will be removed in a future release.

#### New or changed features

PRD-12961
:   Added support for Eclipse 2023-06 (4.28).

PRD-12963
:   Added support for Eclipse 2023-09 (4.29).

### Coverity Desktop for Intellij IDEA 2023.9.0

#### End-of-life products

PRD-12977
:   Support for IntelliJ, PhpStorm, PyCharm, RubyMine, CLion and Webstorm 2021.12 has been removed as of 2023.9.0.

#### New or changed features

PRD-12967
:   Added support for IntelliJ 2023.2.

PRD-12968
:   Added support for PyCharm 2023.2.

PRD-12969
:   Added support for PhpStorm 2023.2.

PRD-12970
:   Added support for RubyMine 2023.2.

PRD-12971
:   Added support for WebStorm 2023.2.

## Coverity Documentation 2023.9.0

This section provides release notes for Coverity Documentation components.

### Coverity Documentation 2023.9.0

#### New or changed features

COVDOCS-1002
:   The *Release Notes* now show in which Coverity version a fixed bug was discovered.

COVDOCS-1090
:   Updated the *Coverity Command Reference* to describe the new `--report-rws` option for the `cov-run-desktop` command.

COVDOCS-1117
:   In the *Coverity Platform User and Administrator Guide*, added information on setting up a reverse proxy.

COVDOCS-1119
:   The minimum memory requirement for PHP analysis has been updated in section "6.2.1 Minimum requirements" of the *Coverity Installation and Upgrade Guide*.

COVDOCS-1146
:   Updated documentation for the `CONSTANT_EXPRESSION_RESULT` checker to provide a description for the `pointless_string_compare` event.

COVDOCS-1151
:   A new document, the *Simplified Analysis Guide,* describes the use of the Simplified Analysis features Point and Scan and the Coverity Command Line Interface (CLI).

SAT-44685
:   Improved one CodeXM pattern example.

#### Bug fixes

COVDOCS-1126
:   Reported in version: 2022.12.0
:   Corrected documentation for the `allow_array_of_uniform_structs` option of the `OVERRUN` checker.

COVDOCS-1155
:   Reported in version: 2023.6.0
:   Removed invalid reference from `custom.css` file used by HTML documentation.

COVDOCS-1161
:   Reported in version: 2023.6.0
:   Changed supported version of the DISA ASD STIG standard from version 4 to version 5. The updated text can be found in the "DISA Application Security and Development STIG standard" section of the *Coverity Checker Reference*.

SAT-44668
:   Reported in version: unspecified
:   Made a correction to the first code sample in "Writing your first CodeXM checker".

SAT-44726
:   Reported in version: 2022.12.2
:   Updated the descriptions of `arrayType` and `classType` for the CodeXM C/C++ library. The `sizeInBytes` field for both these types can return `null` if the size value is not known at runtime.
