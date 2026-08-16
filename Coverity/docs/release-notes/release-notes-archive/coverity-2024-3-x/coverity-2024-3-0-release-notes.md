---
title: "Coverity 2024.3.0 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2024.3.0-release-notes.html"
content_id: "vKme2Wb15mt_ynUUypEcIA"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:34.323746+00:00"
---

# Coverity 2024.3.0 Release Notes

## Important information for 2024.3.0

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

The Coverity 2024.3.0 release includes new support for .NET 8 and several improvements to the Coverity CLI and user experience.

**Special announcement**

Starting this year, the number of Coverity Connect installer releases will be reduced as we focus on Coverity Connect
in the Coverity cloud deployment. There will be no change to the Coverity Analysis or the Coverity cloud deployment release cadence.

The Coverity 2024.9 release will not include a Coverity Connect installer and there will be no more minor releases that include a Coverity Connect
installer, except in cases where there are critical security issues.

In 2025, there will only be 2 major releases that include the Coverity Connect installer: the 2025.6 release and the 2025.12 release.

**Release highlights**

- Improved visibility into completed scans, including new details about what was scanned, how comprehensive the scan was, and areas of code that were unreachable.
- The Coverity CLI now supports Coverity's Bazel integration.
- Updated support for .NET 8.
- Added support for Large Language Models (LLMs) to protect against insecure output handling.
- Reduced false positive and false negative rates for the `COPY_PASTE_ERROR`, `INFINITE_LOOP`, and `RESOURCE_LEAK` checkers​

**Known issues**

- The AIX Coverity Analysis binary will not be available in this release.

Please see below for full details of these and other enhancements included in this release.

## Coverity Platform 2024.3.0

This section provides release notes for Coverity Platform components.

### Coverity Connect 2024.3.0

#### End-of-life products

COVDOCS-1266
:   Support for PostgreSQL 11 has been discontinued.

#### Deprecated products and features

COVDOCS-1337
:   The SOAP API is deprecated in 2024.3 and will be removed in a later release. Please switch to the equivalent REST API, which is the solution going forward.

IM-31252
:   The REST`api/v2/healthcheck/download` endpoint is deprecated in 2024.3 and will be removed in 2024.6. This endpoint is no longer relevant because, starting with 2024.3, the health check report will be saved to the database instead of the file system.

#### New or changed features

IM-28400
:   When any user is locked or disabled, all of the user's login sessions will be timeout.

IM-30312
:   The new Scan Transparency Data feature provides additional details on each analysis scan through the Coverity Connect GUI and API. Metrics are provided for all snapshots and whole data are provided for the latest snapshot of the stream. You enable this feature by setting the property `scan.transparency.enabled` to `true` in the Connect server's `cim.properties` file. For more information, refer to the section "Enabling collection of scan transparency data" in the *Coverity Platform 2024.3.0 User and Administrator Guide*.

IM-31120
:   TLS v1.3 is now enabled by default in Coverity Connect along with TLS v1.2.

IM-31128
:   To change the timezone of the `http-access.log` file, users can modify their `config/server.properties` file as follows:

    Set either `java_opts_pre` or `java_opts_post` to `-Duser.timezone={desired_timezone}`. For example: `java_opts_pre=-Duser.timezone=MST`

    Please be aware that making this change will impact other functionality in Coverity Connect as well. For instance, cron jobs, SCM modification dates, snapshot creation dates, and so on, will all happen with respect to the newly configured timezone.

IM-31397
:   The operation `GET /streams/{name}/scantransparency` has been added to the Coverity Connect API. This new operation retrieves JSON-formatted scan transparency data associated with the latest snapshot of the specified stream. For more information, refer to the API reference documentation at `<scheme>://<my_connect_host>:<port>/swagger/cim/index.html` (where `<scheme>` is either `http` or `https`, depending how you configured your Coverity Connect server, and `<my_connect_host>:<port>` are the host and port of your Coverity Connect server) and the section "Retrieve scan transparency data" in the *Coverity Platform 2024.3.0 REST Web Services API Guide*.

IM-31566
:   The version of Apache Tomcat bundled with Coverity Connect has been upgraded to 9.0.86.

#### Bug fixes

CNC-2585
:   Reported in version: 2023.12.0
:   Customers can now successfully deploy Coverity in the cloud on ARM64 machines.

IM-27613
:   Reported in version: 2021.12.0
:   Fixed an issue where in some projects the "functionMergeName" field was incorrect and the wrong merge name from the previous commit was being used.

IM-30875
:   Reported in version: 2023.3.0
:   Fixed an issue with the `/api/v2/snapshots/<snapshotID>` endpoint, whose response did not match the SOAP operation response. This endpoint now returns the correct response.

IM-30878
:   Reported in version: 2022.12.2, 2023.6.0, 2023.9.0
:   Fixed an issue with JIRA integration, where a field mapping with constant templated static field `<component>` will now show up the right value after exporting the defect.

#### Known issues and solutions

COVDOCS-1348
:   Test Advisor metrics, along with all other legacy Test Advisor data, have been removed from the application and the underlying database. If you have custom trend records calculated off of legacy Test Advisor data, you will need to rebuild these trend records manually to ensure that Test Advisor metrics no longer contribute to these values. See the "Managing daily trend records at the project level" section of the *Coverity Platform User and Administrator Guide* for instructions as to how to do this.

COVDOCS-1356
:   The `cov-commit-defects` command hangs when used with the `--dataport` option or with the `--url commit://` option to specify the commit port on Coverity Connect. Both these options are deprecated. For alternative options, see the `cov-commit-defects` command in the *Coverity Command Reference*.

## Coverity Analysis 2024.3.0

This section provides release notes for Coverity Analysis components.

### Coverity Analysis - General 2024.3.0

#### New or changed features

COVDOCS-1313
:   The `cov-analyze` and `cov-build` commands have new options for disabling or enabling *scan transparency*.

COVDOCS-1334
:   As of Coverity 2024.3, client-side cache invalidation is only allowed for administrative users.

COVGUI-2510
:   SSO 2-Step Verification is now supported on Debian (Linux). The SAML IdP Authorization step now redirects to the system's default browser and, after a successful login, it redirects back to Point and Scan to complete the login process.

    **Known Issue:** If the browser is not re-directing to the application, run the command `update-desktop-database ~/.local/share/applications` in the terminal to update the mime handler databases.

COVP-2601
:   New information about the comprehensiveness of Coverity scans in the form of captured source files, analyzed functions, number of annotations, and number of customer models can now be found in the **Snapshot** details of Coverity Connect. This information is disabled by default in Coverity Connect, but it can be enabled by setting the `scan.transparency.enabled` property to `true` in the `cim.properties` file.

SAT-45026
:   Duplicate file detection in JavaScript has changed such that the first file in alphabetical order will be selected for analysis. This might cause some triage to be lost.

SAT-45563
:   The version of Tomcat bundled in `cov-analysis` was upgraded to 9.0.85.0 in the 2024.3.0 release.

SATSEC-15536
:   Coverity now supports the Large Language Model (LLM) taint type to track taints from LLM APIs.

SIGMACOV-613
:   The `--sigma-enable-check-set <sigma-check-set(s)>` option for the `cov-analyze` command can now be used to bulk-enable Sigma check sets, as specified by the `<sigma-check-set(s)>` parameter.

#### Bug fixes

CMPCPP-14006, CMPCPP-14016, CMPCPP-14031, CMPCPP-14033
:   Reported in version: 2023.12.0, 2023.6.2
:   Fixed a source of analysis recoverable errors with message "assertion failed: object" when using clang-based compilers.

INS-3392
:   Reported in version: 2022.3.0, 2022.12.0, 2023.3.0, 2023.3.2, 2023.6.0, 2023.6.1, 2023.9.2
:   Fixed issue where SLF4J warnings were shown when Coverity Desktop was used to assign new defects.

SAT-45223, SAT-45467
:   Reported in version: 2022.12.0
:   Fixed an unrecoverable analysis crash in some cases involving compliance checkers (CERT and MISRA), notably on very large codebases.

SAT-45255
:   Reported in version: 2023.12.0
:   Fixed issues in coding standard configuration files such as missing deviation entries for CERT-C CON43-C, CERT-C MSC41-C, CERT-C WIN30-C, and MISRA-C2012 Rule 2.8 rules.

SAT-45282
:   Reported in version: 2023.9.0
:   Fixed an issue that could cause the analysis to run out of memory.

SATSEC-15631
:   Reported in version: 2023.12.0
:   A ReDoS issue was discovered in versions of the Ruby URI extension preceding 0.12.2. Although the URI extension is not used by Coverity analysis, it is included in the Ruby runtime distributed with Coverity. This represents a potential security issue if other software happened to use Coverity's Ruby runtime. In this release, the URI extension has been upgraded to version 0.13.0, which resolves the ReDoS issue.

SATSEC-15676
:   Reported in version: 2023.12.0
:   Fixed a false negative related to command line taints from the Python `argparse` module.

#### Known issues and solutions

COVDOCS-1343
:   With the introduction of 2-step authentication, the browser needs to be opened to complete the SSO authentication. Using the `coverity scan` command directly may cause an issue on Linux ARM machines as the scan may not get triggered immediately after completing SSO sign-in due to Wayland protocol error. However, the authentication process will be completed successfully.

### Coverity CLI 2024.3.0

#### Deprecated products and features

COVCLI-2570
:   Buildless capture (the `cov-capture` command) is now deprecated and will be removed in a future release. The Coverity CLI (using the the `coverity` command set) can be used in place of buildless capture. Please see the section "Moving from buildless capture to the Coverity CLI" in the *Coverity Analysis User and Administrator Guide* for more information.

#### New or changed features

COVCLI-2066
:   The Coverity CLI will now automatically disable progress ticker output if it detects that stdout is not connected to a terminal.

COVCLI-2877
:   On Windows, if the clean or build command begins with `dotnet`, `dotnet.exe`, `msbuild`, or `msbuild.exe` (case insensitive), then an attempt will be made to use `vswhere` to find the location of the `dotnet` or `msbuild` command. If `vswhere` cannot be found, then an error will occur.

COVCLI-3007
:   Support for Bazel capture has been added to the Coverity CLI. Refer to section "Building with Bazel" of the *Coverity Analysis User and Administrator Guide* and section "Bazel support" of the *Guide to the Coverity Point and Scan UI and the Coverity CLI* for details.

COVCLI-3047
:   The Coverity CLI will now no longer do dependency resolution in cases where it is not needed, for example when a build command is provided.

COVCLI-3048
:   During buildless capture, if dependency resolution fails, the Coverity CLI will now continue the capture process on a best effort basis. Previously, some errors in dependency resolution would cause a catastrophic capture failure.

COVDOCS-1304
:   The Coverity CLI has added options for saving defects to a local file system.

SIGMACOV-613
:   The `--sigma-enable-check-set <sigma-check-set(s)>` option for the `cov-analyze` command can now be used to bulk-enable Sigma check sets, as specified by the `<sigma-check-set(s)>` parameter.

### Coverity Checkers 2024.3.0

For a summary of checkers that have been added or changed in this release, refer to the "Coverity Checker Change History" table in the *Coverity Checker Reference*.

#### New or changed features

CCK-2510
:   Added support for MISRA C:2012 Amendment 3 Rule 18.9.

CCK-2517
:   Added support for MISRA C:2012 Amendment 3 Rule 23.4.

CCK-2522
:   Added support for MISRA C:2012 Amendment 3, Directive 4.6.

CCK-2542
:   Added new checker for HYUNDAI C MC-EXP-007.

CCK-2583
:   Added support for MISRA C:2012 Amendment 4 Rule 11.10.

CCK-2587
:   Added support for MISRA C:2012 Amendment 4 Rule 21.26.

CCK-2589
:   Added support for MISRA C:2012 Amendment 4 Rule 22.12.

CCK-2590
:   Added support for MISRA C:2012 Amendment 4 Rule 22.13.

CCK-2600
:   Added support for MISRA C:2012 Amendment 4 Rule 13.2.

CCK-2616
:   Added new checker for HYUNDAI C MC-ARR-008.

CCK-2622
:   Added support for MISRA C:2012 Amendment 3 Rule 23.6.

COVDOCS-1296
:   For CodeXM checkers that evaluate C/C++ source code, a `language` field now allows a CodeXM checker to analyze only a particular language; for example, C++ only, Objective-C++ only, CUDA (Host), CUDA (Device) and so on.

COVDOCS-1299
:   For CodeXM checkers that evaluate C/C++ source code, the `macrosExpandedFrom` and `macroExpansionsPresent` fields now allow testers to view the macros, if any, used to build the current abstract syntax tree (AST) and the current node in that tree.

SAT-3934
:   Improved the accuracy of the `track_fields` option to the `RESOURCE_LEAK` checker. This option is now enabled by default. [C/C++]

SAT-10264
:   Improved handling of the "placement new" operator in the `OVERRUN` checker. [C++, CUDA, Objective-C++]

SAT-17994
:   Improved handling of "try-lock" functions for the `LOCK`, `ORDER_REVERSAL` and `LOCK_INVERSION` checkers; these functions are now understood as not causing lock inversion defects, while potentially causing issues if called on a locked mutex. [C/C++, C#, Java]

SAT-40518
:   Improved handling of the "placement new" operator in the `USE_AFTER_FREE` checker. [C/C++, CUDA, Objective-C/C++]

SAT-44129
:   Suppress some `COPY_INSTEAD_OF_MOVE` defects on structures that are inexpensive to copy, or for which a move is not different from a copy. [All languages]

SAT-44317
:   A change has been made to the `AUTO_CAUSES_COPY` checker so that it does not report a defect when the copy is inexpensive to generate. [All languages]

SAT-44424
:   Improved handling of the "placement new" operator in the `UNINIT` checker. [C++, CUDA, Objective-C++]

SAT-44586
:   Updated the `COPY_INSTEAD_OF_MOVE` checker to eliminate defect reports when a copy and a move are the same operation.[C++, CUDA, Objective-C++]

SAT-44705
:   Added new checker for HYUNDAI C MC-EXP-004.

SAT-44710
:   Added new checker for HYUNDAI C MC-MSC-009.

SAT-44880
:   Added support for MISRA C:2012 Amendment 3, Directive 4.11.

SAT-44883
:   The event text for MISRA-C 2012 Rule 2.2 has been updated to match the preferred wording listed in MISRA-C 2012 Amendment 4.

SAT-44893
:   Added support for MISRA C:2012 Amendment 4, Rule 2.8.

SAT-44952
:   Improved handling of the `std::nullptr_t` type, which can appear in template specializations; this allows the analysis to detecting some null checks that it previously could not. [C++]

SAT-45203
:   A new `trace_update_reachability` option has been added to the `INFINITE_LOOP` checker. When this option is enabed, the checker will report a defect when none of the statements updating the loop conditions are reachable. The option is `false` by default and has to be set explicitly. [C, C++]

SAT-45299
:   The `INFINITE_LOOP` checker now reports cases when the loop condition is a function call that always returns the same value throughout the loop. [All languages]

SATSEC-15559
:   The `SCRIPT_CODE_INJECTION` checker now supports Go.

SATW-5351
:   Added new checker for HYUNDAI MC-MSC-018.

SATW-5353
:   Added new checker for HYUNDAI MC-POS-010.

SATW-5362
:   Added new checker for HYUNDAI MC-MSC-001.

SATW-5366
:   Added support for MISRA C:2012 Amendment 3 Rule 17.9.

SATW-5368
:   Added support for MISRA C:2012 Amendment 3 Rule 23.1.

SATW-5376
:   Added support for MISRA C:2012 Amendment 4 Rule 9.6.

SATW-5411
:   Added support for MISRA C:2012 Amendment 3 Rule 21.11.

SATW-5437
:   Added support for MISRA C:2012 Amendment 3 Rule 21.10.

SATW-5438
:   Added support for MISRA C:2012 Amendment 3 Rule 17.1.

SATW-5439
:   Added support for MISRA C:2012 Amendment 3 Rule 21.12.

SATW-5450
:   Updated checker for MISRA C:2012 Rule 21.4 and MISRA C:2012 Rule 21.5. The checker will now run faster as the new implementation does not require checks while compiling code.

SATW-5468
:   Added support for MISRA C:2012 Amendment 3 Rule 8.16.

SATW-5479
:   Added support for MISRA C:2012 Amendment 3 Rule 7.5.

SATW-5486
:   Added new checker for HYUNDAI C MC-ARR-009.

SATW-5503
:   Added support for MISRA C:2012 Amendment 3 Rule 8.17.

SATW-5504
:   Added support for MISRA C:2012 Amendment 3 Rule 17.13.

#### Bug fixes

SAT-14504
:   Reported in version: 7.5.1
:   Fixed a source of false positives for the `RESOURCE_LEAK` checker when an allocated pointer was freed or saved through the value of a `++` or `--` expression. [C/C++, CUDA, Objective-C/C++]

SAT-32940
:   Reported in version: 2019.06
:   Fixed a false negative for the `OVERRUN` checker related to values returned from functions. [All languages]

SAT-37375
:   Reported in version: 2020.09
:   The `COPY_PASTE_ERROR` checker has been improved to reduce false positives around `if` statements with similar patterns. [All languages]

SAT-38885
:   Reported in version: 2020.12
:   Fixed an issue related to detecting overflows when an offset was computed as the lower of two values, which resulted in a false positive for the `OVERRUN` checker. [All languages]

SAT-40794
:   Reported in version: 2021.09
:   Fixed a source of false positives for the `OVERRUN` checker by improving the handling of range bounds when an operation different than "==" is encountered. [All languages]

SAT-43764
:   Reported in version: 2021.12.0
:   Fixed a false positive for the `UNINIT` checker related to the `boost::optional` constructor. [C++, CUDA, Objective-C++]

SAT-43896
:   Reported in version: 2022.3.0
:   Fixed a source of false positives for the `LOCK` checker when using the `mtx_lock` function. [C/C++, CUDA, Objective-C/C++]

SAT-43965
:   Reported in version: 2022.12.1
:   The `USE_AFTER_FREE` checker recognizes more reference counting patterns. [All languages]

SAT-45054, SAT-45380
:   Reported in version: 2023.12.0
:   Fixed a false positive for the `UNINIT` checker when using `std::unique_lock`. [C++, CUDA, Objective-C++]

SAT-45064
:   Reported in version: 2023.6.0
:   Updated the CWE coverage for the `SIZEOF_MISMATCH` checker to cover CWE 131 and CWE 468 instead of CWE 569.

SAT-45154
:   Reported in version: 2023.3.2
:   Fixed an issue where the `STRING_NULL` checker would fail to notice `null`-termination when taking the address of an array element. [All languages]

SAT-45160
:   Reported in version: 2023.12.0
:   Fixed a source of false positives with various checkers in C++ when passing `nullptr` as an argument to template functions, notably some assertions seen in GoogleTest. [C++]

SAT-45199
:   Reported in version: 2023.6.2
:   Fixed an issue that could cause checkers that look for C++ one-definition rule violations (`ODR_VIOLATION`, MISRA C++-2008 Rule 3-2-2, AUTOSAR C++14 Rule M3-2-2, CERT DCL60-CPP, HYUNDAI MP-DCL-011) to take very long, potentially being mistaken for a deadlock, causing the analysis to crash. [C++]

SAT-45229
:   Reported in version: 2023.12.0
:   Fixed a source of recoverable crashes with message `assertion failed: Index out of range` when analyzing with compliance checkers (CERT and MISRA). [C/C++]

SAT-45230
:   Reported in version: 2023.12.0
:   Fixed a source of analysis recoverable errors.

SAT-45287
:   Reported in version: 2023.12.0
:   Updated the `COPY_INSTEAD_OF_MOVE` checker so that it handles correctly constructs such as `do{...} while(false);`. [All languages]

SAT-45355
:   Reported in version: 2023.12.0
:   Fixed a recoverable analysis failure with the `RETURN_LOCAL` checker and message "`error->has_main_event()`". [All languages]

SAT-45372
:   Reported in version: 2024.3.0
:   Fixed a recoverable error in the `INTEGER_OVERFLOW` checker when dealing with `std::nullptr_t()`. [C++, CUDA, Objective-C++]

SATSEC-6759
:   Reported in version: 2022.3.0
:   Fixed a false negative with compliance checkers. [Java]

SATSEC-15568
:   Reported in version: 2023.3.0
:   Fixed a false positive for the `PATH_MANIPULATION` checker, where it would report a defect if a field (attribute) of a tainted object was passed to a method considered to be a sink (consumer) of that tainted data, even if that same field was passed to a method in a parameter labelled as a sanitizer using a `sanitizer_for_checker` directive. [C#, Java, Visual Basic]

SATSEC-15572
:   Reported in version: 2023.3.0
:   Fixed a false positive for the `PATH_MANIPULATION` checker when a tainted return value was assigned to a local variable and this variable was later passed to a method in a parameter that was labelled as sanitized using a `sanitizer_for_checker directive`. [C#, Java, Visual Basic]

SATSEC-15670
:   Reported in version: unspecified
:   Fixed a false positive for the `INSECURE_FILE_PERMISSIONS` checker related to the Go `os.OpenFile` API when `os.O_CREATE` is not specified. [Go]

SATW-1937
:   Reported in version: 2017.07-hotfix
:   Fixed a false positive for the MISRA C++:2008 Rule 4-10-2 when macro defined `NULL` is used.

SATW-2988
:   Reported in version: 2018.12
:   Fixed a false positive for the MISRA C:2012 Rule 11.9 checker.

SATW-5100
:   Reported in version: 2022.6.0
:   Fixed a false positive in the MISRA C++:2008 Rule 4-10-2 checker.

SATW-5341
:   Reported in version: 2023.6.0
:   Fixed a false positive for the AUTOSAR C++ A10-1-1 checker.

SATW-5731
:   Reported in version: 2023.12.0
:   Fixed a false positive for the `AUTOSAR A10-1-1` checker.

### Coverity Commands 2024.3.0

#### New or changed features

CMPJ-2153
:   The following options have been removed from `cov-emit-java`: `--enable-java-parse-error-recovery`, `--enable-java-per-class-error-recovery`, and `--enable-java-per-file-error-recovery`. These options have had no effect since 2023.9 and can be safely removed from any `cov-emit-java` command lines.

#### Bug fixes

SAT-45189
:   Reported in version: 2023.9.2
:   Fixed an issue that caused `cov-commit-defects` to trust self-signed certificates by default when using an `https` URL.

### Coverity Compilers and Capture 2024.3.0

#### End-of-life products

CAP-2244
:   Support for Bazel 4 has been removed as of 2024.3.0.

COVP-2595
:   Support for Windows Server 2019 has been removed as of Coverity 2024.3.0.

#### Deprecated products and features

COVP-2599
:   Support for Oracle/Open JDK 11 is deprecated as of 2024.3.0 and will be removed in a future release.

COVP-2600
:   Support for FreeBSD 12 is deprecated as of 2024.3.0 and will be removed in a future release.

#### New or changed features

CAP-1881
:   Support for using the Bazel build system with the Thin Client has been added as of 2024.3.0

CAP-2157
:   The syntax for enabling link-unit capture for Bazel has been made redundant; the old syntax will continue to work, but is no longer necessary as link-unit capture is now automatically enabled for Bazel when the `cov-build` command is passed both the `--bazel` and `--emit-link-units` flags in the same invocation.

CAP-2211
:   Added support for Bazel 7.

CAP-2224
:   Translation units (TUs) captured from the Bazel build system using `cov-build --bazel` will now be emitted with paths relative to the Bazel workspace, not the Bazel execution root.

CAP-2226
:   The `cov-build --bazel` command now implies the `-j auto` option, unless otherwise specified.

CMPCPP-13915
:   Added support for TI Arm Clang compilers up to version 2.1.3.LTS.

CMPCPP-13974
:   Added support for Xtensa xt-clang RI-2022.9 compiler.

CMPCSH-1949
:   Added support for C# 12.

CMPG-4441
:   In previous releases, when invoking `cov-configure` without the `--template` option, if the required command line options did not match the actual configuration of a translation unit (TU), that would cause Coverity Analysis to skip the TU and add a message about this to the build log. As of Coverity 2024.3.0, Coverity Analysis would capture the TU and save it in the intermediate directory as a failed TU.

COVP-2565
:   Added support for FreeBSD 14.0.

COVP-2598
:   Added support for .NET 8.

#### Bug fixes

CAP-2199
:   Reported in version: 2023.6.0
:   When using the `cov-build --bazel` command, the `--emit-complementary-info` option now works as expected.

CAP-2261
:   Reported in version: 2023.12.0
:   The Coverity-Bazel integration will now correctly capture dependencies included in `cc_library` targets through the `implementation_deps` attribute.

CMPCPP-11759
:   Reported in version: 2021.06
:   Fixed `cov-emit` crash with `EXCEPTION_STACK_OVERFLOW` error when instantiating template code with deep recursion.

CMPCPP-12788
:   Reported in version: 2021.06
:   Fixed a `cov-internal-emit-clang` crash caused by the `alignas` specifier in C++ templates.

CMPCPP-12841
:   Reported in version: 2020.09
:   Fixed an issue where using an unsupported option caused the filename given as parameter to certain commands such as `cov-build` to not be recorded.

CMPCPP-13374
:   Reported in version: 2023.3.0
:   Thread-local storage use in the `armv7-apple-darwin` platform no longer issues an error.

CMPCPP-14019
:   Reported in version: 2022.12.0
:   Fixed an issue for the `cov-translate` command when using the `-V 0` verbose option, where spurious lines were inserted on the `stdout`.

CMPG-4426
:   Reported in version: 2022.12.1
:   Fixed issue where a crash in `cov-emit-java` for buildless capture scenarios did not record failures in the intermediate directory, causing incorrect success rates to be reported to users.

CMPJ-2164
:   Reported in version: 2023.6.0
:   Fixed internal compiler error in `cov-emit-java` encountered when targeting older Java release versions.

### Coverity Point and Scan 2024.3.0

#### New or changed features

COVGUI-2510
:   SSO 2-Step Verification is now supported on Debian (Linux). The SAML IdP Authorization step now redirects to the system's default browser and, after a successful login, it redirects back to Point and Scan to complete the login process.

    **Known Issue:** If the browser is not re-directing to the application, run the command `update-desktop-database ~/.local/share/applications` in the terminal to update the mime handler databases.

#### Known issues and solutions

COVDOCS-1343
:   With the introduction of 2-step authentication, the browser needs to be opened to complete the SSO authentication. Using the `coverity scan` command directly may cause an issue on Linux ARM machines as the scan may not get triggered immediately after completing SSO sign-in due to Wayland protocol error. However, the authentication process will be completed successfully.

## Coverity Desktop 2024.3.0

This section provides release notes for Coverity Desktop components.

### Coverity Desktop for Android Studio 2024.3.0

#### End-of-life products

PRD-13037
:   Support for Android Studio 2020.3 has been removed as of 2024.3.0.

#### Deprecated products and features

PRD-13040
:   Support for Android Studio 2021.1 is deprecated as of 2024.3.0 and will be removed in a future release.

#### New or changed features

PRD-13027
:   Added support for Android 2023.1.1.

PRD-13033
:   Added support for macOS ARM 12–14.

### Coverity Desktop for Eclipse 2024.3.0

#### End-of-life products

PRD-13038
:   Support for Eclipse 2020-06 and 2020-09 has been removed as of 2024.3.0.

#### Deprecated products and features

PRD-13041
:   Support for Eclipse 2020-12 and 2021-03 is deprecated as of 2024.3.0 and will be removed in a future release.

#### New or changed features

PRD-13004
:   Added supported for Eclipse 2023-12.

PRD-13033
:   Added support for macOS ARM 12–14.

#### Known issues and solutions

COVDOCS-1349
:   Coverity Desktop plugin users are not able to view remote issues from Coverity Connect version 2023.3 or higher. This is due to a change in Coverity Connect that was made to address a security issue. This issue affects all Coverity Desktop plugins.

    **Workaround:** You may workaround this issue by elevating the permissions for plugin users to **Manage user and groups** in Coverity Connect so they can see the remote issues. *Note that this is "admin-like" access and should be used where admin permissions would, otherwise, be appropriate.*

### Coverity Desktop for Intellij IDEA 2024.3.0

#### End-of-life products

PRD-13039
:   Support for IntelliJ 2021.3 has been removed as of 2024.3.0.

#### Deprecated products and features

PRD-13026
:   Support for IntelliJ 2022.1 and 2022.2 is deprecated as of 2024.3.0 and will be removed in a future release.

#### New or changed features

PRD-13006
:   Added support for IntelliJ 2023.3.0.

PRD-13008
:   Added support for CLion 2023.3.0.

PRD-13010
:   Added support for WebStorm 2023.3.0.

PRD-13011
:   Added support for RubyMine 2023.3.0.

PRD-13012
:   Added support for PhpStorm 2023.3.0.

PRD-13013
:   Added support for PyCharm 2023.3.0.

PRD-13033
:   Added support for macOS ARM 12–14.

#### Known issues and solutions

COVDOCS-1349
:   Coverity Desktop plugin users are not able to view remote issues from Coverity Connect version 2023.3 or higher. This is due to a change in Coverity Connect that was made to address a security issue. This issue affects all Coverity Desktop plugins.

    **Workaround:** You may workaround this issue by elevating the permissions for plugin users to **Manage user and groups** in Coverity Connect so they can see the remote issues. *Note that this is "admin-like" access and should be used where admin permissions would, otherwise, be appropriate.*

### Coverity Desktop for Microsoft Visual Studio 2024.3.0

#### Known issues and solutions

COVDOCS-1349
:   Coverity Desktop plugin users are not able to view remote issues from Coverity Connect version 2023.3 or higher. This is due to a change in Coverity Connect that was made to address a security issue. This issue affects all Coverity Desktop plugins.

    **Workaround:** You may workaround this issue by elevating the permissions for plugin users to **Manage user and groups** in Coverity Connect so they can see the remote issues. *Note that this is "admin-like" access and should be used where admin permissions would, otherwise, be appropriate.*

## Coverity Documentation 2024.3.0

This section provides release notes for Coverity Documentation components.

### Coverity Documentation 2024.3.0

#### New or changed features

COVDOCS-1259
:   Improved description for the `relaxed_operator_context` option of the `OVERFLOW_BEFORE_WIDEN` checker in the *Coverity Checker Reference*.

COVDOCS-1284
:   Added example for the `allow_negative_unsigned_returns_from_functions` option of the `INTEGER_OVERFLOW` checker in the *Coverity Checker Reference*.

COVDOCS-1315
:   In the *Coverity CodeXM Checkers Development Guide*, the descriptions of the `parent` field in "astnode" sections for the language libraries have been updated to improve clarity.

COVDOCS-1319
:   The documentation has been updated to clarify that the Coverity Connect API supports authentication using an authentication key as an alternative to using a password.

COVDOCS-1346
:   In [Getting started with Coverity Analysis](https://documentation.blackduck.com/bundle/coverity-docs/page/help-center/topics/getting_started_with_coverity_analysis.html), updated the list of languages that Coverity supports.

#### Bug fixes

COVDOCS-1264
:   Reported in version: 2023.12.0
:   Fixed a typo in the "SIG Docker registries" table, in the *Coverity Cloud Deployment Administrator and User Guide*. The SIG private Docker registry URL is `sig-repo.coverity.com`, not `sig.repo.coverity.com`.

COVDOCS-1270
:   Reported in version: 2023.12.0
:   Added a note to the "Coverity container images" section in the *Coverity Cloud Administrator and User Guide* that all container images work with both ARM64 and Intel/AMD.

COVDOCS-1289
:   Reported in version: 2023.12.0
:   In the *Coverity Cloud Deployment Administrator and User Guide*, for the `cim.ingress.path` Helm key, added the following statement for an AWS ALB ingress path: 'You might need to set this to "/*" for AWS ALB ingress controllers.'.

COVDOCS-1314
:   Reported in version: 2023.12.0
:   Fixed localization issue in `coverity-checker-coverage.html`.
