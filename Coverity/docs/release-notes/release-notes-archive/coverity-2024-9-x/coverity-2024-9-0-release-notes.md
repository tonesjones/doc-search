---
title: "Coverity 2024.9.0 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2024.9.0-release-notes.html"
content_id: "iWynJBTrCw_rsp_XIlF3ww"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:28.015225+00:00"
---

# Coverity 2024.9.0 Release Notes

## Important information for 2024.9.0

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

- Added Amazon S3 Express storage support for environments that require high-performance access to Coverity scan data.
- Kotlin 2.0 and Python 3.12 are now supported.
- Added Kotlin and Python support to Rapid Scan Static (the Sigma engine) for API safety and hardcoded secret checks.
- Added C# and Visual Basic support to the `SESSION_FIXATION` checker.
- Added support for Unity version 2022.3.0 on Windows operating systems.
- Added support for Wind River DIAB 7.0.5.
- Added support for ARM Embedded FuSa 6.16.2 Toolchain on Linux.
- Android NDK r27 is now supported.
- The Coverity CLI will automatically run all security checkers by default when scanning.

Please see below for full details of these and other enhancements included in this release.

## Coverity Platform 2024.9.0

This section provides release notes for Coverity Platform components.

### Coverity Connect 2024.9.0

#### Deprecated products and features

COVDOCS-1488
:   Support for glibc 2.17 has been deprecated in Coverity Connect 2024.9.0 and will be removed in the 2024.12.0 version.

#### New or changed features

CNC-1596
:   The Coverity cloud deployment 2024.9.0 release supports a new Coverity Connect Web application administrator password feature that enables an administrator to create and change the administrator password. For information on creating and managing this password, refer to the document, *Coverity Cloud Deployment Administrator and User Guide*.

CNC-2638
:   In a Coverity cloud deployment, storage service and scan-service migration jobs that fail have not provided logs for you to download. The 2024.9.0 release makes these job logs available, even if the jobs fail, making it easier to troubleshoot issues.

CNC-2785
:   In a Coverity cloud deployment within Amazon AWS, the storage service supports S3 general purpose storage buckets. In the 2024.9.0 release, the storage service additionally supports S3 Express One Zone directory storage buckets. For installation and configuration of these storage buckets, refer to the document, *Coverity Cloud Deployment Administrator and User Guide*.

COVDOCS-1428
:   Coverity Connect has upgraded its external database support to PostgreSQL 12–16 (including all minor releases). The embedded database has been upgraded to PostgreSQL 15.7.

IM-31484
:   Inserting a file rule in Component Maps will now add it below the currently selected location.

IM-32122
:   Added a new built-in standard in Coverity Connect, MISRA C++ 2023. All operations supported for other built-in standards, such as **Filtering**, **group-by**, and so on, are also supported for MISRA C++ 2023. Note that full support for MISRA C++ 2023 will be available in a future release.

#### Bug fixes

CNC-2807
:   Reported in version: 2023.3.5, 2023.12.3
:   All users with "Server Admin" role are now able to correctly see whether other users have been temporarily locked out.

IM-31791
:   Reported in version: 2023.12.2
:   All users with "Server Admin" role are able to access/invoke the "Users & Groups" URL, irrespective of the name of the user.

IM-32010
:   Reported in version: 2024.3.0
:   Fixed the following security vulnerabilities: CVE-2022-21724, CVE-2023-5869 and CVE-2024-0985.

IM-32024
:   Reported in version: 2022.9.0
:   Fixed Coverity Connect login loophole for locked accounts, following 5 unsuccessful logins.

IM-32034
:   Reported in version: 2022.9.0
:   Added Content-Security-Policy response header to the Coverity Connect login page

IM-32082
:   Reported in version: 2024.6.0
:   Fixed Standard mappings for Visual Basic code.

IM-32098
:   Reported in version: 2024.6.0
:   Fixed **Groups** synchronization issue, where subscriber wasn't showing up the updates made on coordinator for the group. **Note:** Subscriber must be updated to Coverity 2024.9.0 in order to see the fix applied.

### Coverity Report Generators 2024.9.0

#### New or changed features

RG-1896
:   The Coverity MISRA report now includes supported MISRA C++ 2023 rules. Note that full support for MISRA C++ 2023 will be available in a future release.

## Coverity Analysis 2024.9.0

This section provides release notes for Coverity Analysis components.

### Coverity Analysis - General 2024.9.0

#### New or changed features

SAT-45392
:   Added models for `scandir` and `scandirat` functions to address false negatives for the `RESOURCE_LEAK` checker. [C, C++]

SAT-45876
:   Improved the error message when unrecognized rules were present in the deviations list of a coding standard configuration file.

SATSEC-15728
:   Coverity now detects 'password' keywords for C# through the Sigma engine. The recognition of the keyword happens with or without its usage. [C#]

SATSEC-15834
:   In Coverity 2024.9.0, Ruby has been upgraded to version 3.3.1 on Windows 64-bit.

#### Bug fixes

SAT-45356
:   Reported in version: 2023.12.0
:   Fixed a recoverable analysis error with message `No class named __coverity_gnu_vector_int_4`.

SAT-45784
:   Reported in version: 2024.6.0
:   Fixed an issue in the CodeXM `RegexExtended` pattern where setting `multiline` or `singleline` to `false` could have no effect.

SAT-45862
:   Reported in version: 2024.3.1
:   Fixed an assertion failure in the pointer solver.

SAT-45892
:   Reported in version: 2024.3.1
:   Fixed an issue when uploading results to Polaris when a defect is detected in the `main` function in a top-level file at the root of the directory tree, after path stripping.

SAT-46021
:   Reported in version: 2024.6.0, 2024.3.1
:   Fixed a recoverable error with message "Expected a value to be present for optional integer" when using desktop analysis.

SAT-46043
:   Reported in version: 2024.6.0
:   Fixed an unrecoverable crash caused by large Java annotation chains.

### Coverity CLI 2024.9.0

#### New or changed features

COVCLI-3216
:   Coverity CLI accepts a new capture configuration setting called `import-scm`, which causes `cov-import-scm` to be invoked at the end of the capture phase so that customers can see "blame" information in Coverity Connect.

COVCLI-3378
:   Coverity CLI accepts a new capture configuration setting called `failure-threshold-percent`, which sets the minimum percentage of files that must be captured in order to proceed with the analysis. Files which are ignored because they have been excluded by the configuration or are not supported are not included in the capture rate calculation.

### Coverity Checkers 2024.9.0

For a summary of checkers that have been added or changed in this release, refer to the "Coverity Checker Change History" table in the *Coverity Checker Reference*.

#### New or changed features

SAT-41321
:   The `OVERRUN` checker now reports cases when a receiving buffer of a `scanf`-type function could be overrun. [C, C++]

SAT-44573, SAT-45992
:   The new `report_bitand` option of the `OVERRUN` checker reports a defect if the index expression used in an array access is the result of a bitwise AND operation and the value of the mask used in the bitwise AND operation indicates the index may be out of bounds. [All languages]

SAT-44822
:   The `OVERRUN` checker now reports fewer false positives related to `strlen` function calls. [C, C++]

SAT-45494, SAT-45615
:   Added a new `OVERRUN` checker option, `untrusted_function_parameters`, which reports defects by assuming function parameters can be any value that fits within the type. [All languages]

SAT-45579
:   Added support for `std::rend` in the `INVALIDATE_ITERATOR` checker. [C++]

SAT-45623
:   Updated the `OVERRUN` checker to report when a call to `scanf` contains a width specifier that might cause an overrun of the destination buffer. [C, C++]

SAT-45702
:   CodeXM now offers token patterns in its C/C++ library. Among other capabilities, users can now match preprocessor directives.

SAT-45916, SAT-45919
:   It is now possible to gather HIS metrics using the MISRA C-2023 and C++-2023 standards.

SAT-45956
:   The `USE_AFTER_MOVE` checker was improved to report cases where a function returns after moving a reference parameter. Those reports can be disabled with the new `report_reference_parameter` option. [C, C++]

SATSEC-3211, SATSEC-15875
:   The `SESSION_FIXATION` checker now supports C# and Visual Basic.

SATSEC-15728
:   Coverity now detects 'password' keywords for C# through the Sigma engine. The recognition of the keyword happens with or without its usage. [C#]

SATSEC-15937
:   The `SESSION_FIXATION` checker now supports Go.

#### Bug fixes

SAT-24532, SAT-38048
:   Reported in version: 2017.07-SP2-1 , 2020.12
:   Fixed a false positive for the `OVERRUN` checker by improving interval tracking through modulo conditions. [C, C++]

SAT-37489, SAT-39902
:   Reported in version: 2020.09 , 2021.06
:   Fixed a false positive for the `DEADCODE` checker when a nullable type can also be zero. For instance, this could apply to a nullable enum in which one enumeration value is zero. The analysis previously interpreted evidence of non-nullness as evidence that a value was non-zero. [C#]

SAT-40741
:   Reported in version: 2021.09
:   The `OVERRUN` checker can now find more defects related to the format string for `sprintf`. [C, C++]

SAT-45394
:   Reported in version: 2024.3.0
:   Fixed a source of `RESOURCE_LEAK` false positives when a function allocates memory into a field of a parameter and also returns that memory. [C, C++]

SAT-45395
:   Reported in version: 2024.3.0
:   Fixed a source of `RESOURCE_LEAK` false positives when using the zlib `deflateInit` function. [C, C++]

SAT-45427
:   Reported in version: 2022.12.0
:   Fixed deadlock issues for the `MISRA-C 2012 Rule 17.2` checker on large projects. [C]

SAT-45512
:   Reported in version: 2023.12.0
:   Fixed an `INVALIDATE_ITERATOR` crash that occurred with specific cases using `std::end`. [C++]

SAT-45675, SAT-45895
:   Reported in version: 2023.6.0, 2023.12.0
:   Reduce false positive reports for the `INTEGER_OVERFLOW` checker when analyzing code which uses a retry loop to write or read data in a buffer. [All languages]

SAT-45676, SAT-45952, SAT-46056
:   Reported in version: 2023.12.0, 2024.3.0, 2024.6.0
:   Fixed a false positive for the `INTEGER_OVERFLOW` checker related to unsigned values in comparison operations. [C, C++]

SAT-45677
:   Reported in version: 2024.3.0
:   Suppress `Y2K38_SAFETY` reports for declarations within system header files. [C, C++]

SAT-45682, SAT-45777
:   Reported in version: 2024.6.0
:   Fixed a false positive in the `INTEGER_OVERFLOW` checker when a value is erroneously tracked to a negative one. [All languages]

SAT-45799
:   Reported in version: 2024.3.0
:   Fixed an issue for the `AUDIT.SPECULATIVE_EXECUTION_DATA_LEAK` checker where the `lfence` function was not recognized in some compilation settings. [C++]

SAT-45861
:   Reported in version: 2023.12.0
:   Fixed an issue that could cause `cov-analyze` to crash when analyzing Java projects making use of annotations.

SAT-45981
:   Reported in version: 2024.6.0
:   Fixed a crash involving the `NULL_RETURNS` checker. [C#]

SAT-45987
:   Reported in version: 2024.6.0
:   Fixed a recoverable error with message "Setting issue type after issue taxonomy was set directly" when using the `CHECKED_RETURN` checker. [C, C++]

SATSEC-15848, SATSEC-15849
:   Reported in version: 2024.3.0
:   Added models for the Python `mysql.connector module` to address false negatives for the `HARDCODED_CREDENTIALS` checker related to environment variables. [Python]

SATSEC-15964
:   Reported in version: 2024.6.0
:   Fixed an issue in the `MASS_ASSIGNMENT` checker that caused analysis to crash. [C#, Java, Visual Basic]

### Coverity Commands 2024.9.0

#### New or changed features

CNC-2729
:   Coverity Analysis uploads a zip of the analyzed intermediate directory (IDIR), analysis output, and execution logs (execLog) to the storage bucket. This increases significantly the scan duration and uses a lot of storage. A new Helm key (`scan-service.​jobRunner.uploadArtifacts`) is available, allowing the customer to opt out of uploading the artifacts after a scan.

### Coverity Compilers and Capture 2024.9.0

#### End-of-life products

CMPFG-1163
:   Support for Kotlin 1.8 has been removed as of 2024.9.0

#### Deprecated products and features

CMPCSH-1846
:   macOS (Intel) support for C# is deprecated as of 2024.9 and will be removed in a future release.

CMPFG-1164
:   Support for Kotlin 1.9 is deprecated as of 2024.9.0 and will be removed in a future release.

CMPJ-2237
:   Support for Oracle/Open JDK 22 is deprecated as of 2024.9.0 and will be removed in a future release.

COVP-2618
:   Support for .NET 6 is deprecated as of 2024.9.0 and will be removed in a future release.

#### New or changed features

CCK-2649
:   Added support for the ARM Embedded FuSa compiler version 6.16.2.

CCK-2660
:   Added support for Wind River Diab compiler version 7.0.5.

CMPCPP-14110
:   Added support for HighTec TriCore 4.9.4.1 compiler on Linux platforms.

CMPCPP-14202
:   Support for Android NDK r27a has been added as of 2024.9.0.

CMPCSH-2044
:   Support for Unity 2022.3 on Windows 64-bit has been added as of 2024.9.0.

CMPFG-799
:   Support for Kotlin 2.0 has been added.

CMPFG-870
:   Support for Python 3.12 has been added as of 2024.9.0.

#### Bug fixes

CAP-2296
:   Reported in version: 2023.12.0
:   `cov-build` can now successfully capture builds that use Xcode 15.3 or newer.

CAP-2316
:   Reported in version: 2023.12.0, 2024.3.0
:   The error given by the `cov-build` command for invalid versions of Xcode now matches the documented versions.

CMPCPP-12709
:   Reported in version: 2021.12.1
:   Fixed an issue with Microsoft Visual Studio's `/permissive` flag, which caused builds to hang.

CMPCPP-12995
:   Reported in version: 2022.9.0
:   Fixed lookup rules and reference type deduction used in `range-v3`.

CMPCPP-13096
:   Reported in version: 2022.12.1
:   Fixed a recoverable error that affected constraints using parentheses.

CMPCPP-14065
:   Reported in version: 2023.6.0
:   Fixed an issue where the `-fno-exceptions` option for QNX compilers was not properly handled .

CMPCPP-14424
:   Reported in version: 2024.3.0
:   When using LLVM compilation database with `cov-manage-emit replay-from-script`, the current environment variables will be inherited during the replay.

CMPCPP-14545
:   Reported in version: 2023.12.0
:   Fixed an issue in `clang` compatibility header for SVE builtins.

CMPJ-2079
:   Reported in version: 2022.6.2
:   A defect in the Coverity frontend for Java which could manifest as `cov-analyze` crashing with a diagnostic about "Cannot find class decl for..." has been fixed.

CMPJ-2203
:   Reported in version: 2023.9.0, 2023.12.0
:   In the Java front-end, fixed handling of nested `instanceof` declarations with the same name.

CMPJ-2240
:   Reported in version: unspecified
:   Fixed an issue related to recording command lines where the letter case for an argument was different than the filesystem on Windows.

CMPJ-2243
:   Reported in version: 2024.3.0
:   Improved handling of unknown types used for generics during error recovery in the Java front-end.

CMPJ-2289
:   Reported in version: 2024.6.0
:   Fixed an issue in the Kotlin front-end where symbol names with special characters such as ' ', ',' ')' and ')' would trigger an assert.

## Coverity Desktop 2024.9.0

This section provides release notes for Coverity Desktop components.

### Coverity Desktop for Android Studio 2024.9.0

#### Deprecated products and features

PRD-13127
:   Support for Android Studio 2022.1 is deprecated as of 2024.9.0 and will be removed in a future release.

#### New or changed features

PRD-13128
:   Added support for Android Studio 2023.3.

### Coverity Desktop for Eclipse 2024.9.0

#### End-of-life products

PRD-13114
:   Support for Eclipse 2021-03 has been removed as of 2024.9.0.

#### Deprecated products and features

PRD-13115
:   Support for Eclipse 2021-09 is deprecated as of 2024.9.0 and will be removed in a future release.

#### New or changed features

PRD-13116
:   Added support for Eclipse 2024-06.

### Coverity Desktop for Intellij IDEA 2024.9.0

#### End-of-life products

PRD-13118
:   Support for IntelliJ 2022.2 has been removed as of 2024.9.0.

## Coverity Documentation 2024.9.0

This section provides release notes for Coverity Documentation components.

### Coverity Documentation 2024.9.0

#### New or changed features

COVDOCS-1328
:   A new section in the *Coverity Command Reference* describes the exit codes for Coverity Connect commands.

COVDOCS-1416
:   In the *Coverity CodeXM Checkers Development Guide*, added a new "referenceType" section for C++.

COVDOCS-1422
:   In the *Coverity Command Reference*, updated the description of the `-webapp-security-aggressiveness-level` option for `cov-analyze` to include a reminder that setting `--webapp-security--agressiveness-level` to `high` includes the effect of setting `--distrust-all`.

COVDOCS-1449
:   In the “C/C++ code-line annotations” section of *Customizing Coverity*, improved unclear annotation description.

COVDOCS-1450
:   In the *Customizing Coverity* document, added descriptions of C/C++ primitives to model `printf()` behavior.

COVDOCS-1474
:   In the *Coverity Checker Reference*, added information about supported sanitizers for the `LDAP_INJECTION` checker in the "Security reference" > "Coverity Web application security" > "Technologies and remediation" > "LDAP sanitizers - Java, C#" section.

SAT-44685
:   Improved one CodeXM pattern example.

#### Bug fixes

COVDOCS-1432
:   Reported in version: 2024.3.1
:   In the `INTEGER_OVERFLOW` description in the *Coverity Checker Reference*, removed statement saying that the `INTEGER_OVERFLOW` checker cannot be enabled with the `-all` option. Starting with the Coverity 2023.12 release, this checker will be enabled when using the `-all` option for `cov-analyze`.

COVDOCS-1435
:   Reported in version: 2024.6.0
:   In the "defineIssueType()" section of the *Coverity CodeXM Checkers Development Guide,* the parameter descriptions have been corrected.

COVDOCS-1441
:   Reported in version: 2024.3
:   Updated description for the `--enable-callgraph-metrics` option for `cov-analyze` in the *Coverity Command Reference* document, as well as the "Determining which functions are analyzed and called" section in the *Coverity Analysis User and Administrator Guide*, which relates to this option.

COVDOCS-1500
:   Reported in version: 2024.3.1
:   Fixed an issue where the documentation used a single secret to support access for both container image pulls and scan tool synchronization. The *Coverity Cloud Deployment Administrator and User Guide* now describes how to create a container image pull secret and a scan tool synchronization secret, then how to configure the Helm keys to use these secrets.

COVDOCS-1519
:   Reported in version: 2024.6.0
:   Updated the description for the `--on-new-cert trust` argument in the *Coverity Command Reference*, *Guide to the Coverity Point and Scan UI and the Coverity CLI*, and *Configuring and Generating Coverity Reports* documents. The updated description consists of the following: "Setting `on-new-cert` to `trust` does not currently work with Coverity Analysis and Synopsys Bridge. The workaround is to manually add the self-signed certificate to your operating system's certificate store. This will tell the operating system that it can trust this certificate, and should allow you to continue. "

COVDOCS-1523
:   Reported in version: 2024.6.0
:   Updated the following statement "The free space should be roughly 3x the size of the database, as determined by the size of the <cc_install_dir>/<database> directory’s contents." in the *Coverity Installation and Upgrade Guide* by changing the recommendation from 3x to 4x the size of the database.
