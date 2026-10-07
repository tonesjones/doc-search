---
title: "Coverity 2026.3.0 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/coverity-2026.3.0-release-notes.html"
content_id: "J42XIYrf~zUWmaXuZcBxCg"
version: "2026.9"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-10-04T23:39:43.642782+00:00"
---

# Coverity 2026.3.0 Release Notes

## Important information for 2026.3.0

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://docs.blackduck.com/r/coverity/latest/coverity-documentation/coverity-upgrade-considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

If you are upgrading a Coverity cloud deployment, refer to [Upgrading a Coverity cloud deployment](https://docs.blackduck.com/r/coverity/latest/coverity-documentation/upgrading-a-coverity-cloud-deployment.html) in the Coverity Cloud Deployment Administrator and User Guide. This document provides important information for administrators who are deploying or upgrading Coverity in a Kubernetes container environment.

**Release Highlights**

·     A new, refreshed user interface is now available for login, projects, and triage workflows in Coverity Connect. This is opt-in and users may continue to use the previous UI without any loss of functionality.

·     C# 14 and .NET 10 are now supported.

·     Windows Server 2025 is now supported.

·     Coverity analysis now supports FreeBSD 15.

·     Added a new checker, SESSION_MANIPULATION, for Java.

·     The C/C++ checker, INCONSISTENT_UNION_ACCESS, is now enabled by default.

·     New, easy-to-use deployment scripts for Cloud Native Coverity.

## Coverity Platform 2026.3.0

This section provides release notes for Coverity Platform components.

### Coverity Connect 2026.3.0

#### Bug fixes

CNC-4410
:   Reported in version: 2026.3.0
:   Fixed a Coverity cloud/container issue where a customer was unable to pull container images for any Coverity version from the Black Duck registry.

IM-30717
:   Reported in version: 2026.3.0
:   Fixed an issue where the /api/v2/views REST endpoint failed when any Coverity Connect view was shared with a group.

IM-30882
:   Reported in version: 2026.3.0, 2026.3.0
:   Removed a redundant RBAC check on user-creation limits in the flow, since the creation method already performs the same license/RBAC validation both via AOP and explicitly in its own logic.

IM-31687
:   Reported in version: 2026.3.0, 2026.3.0
:   During the Angular migration, only one file instance ID was passed to display the file tree. The issue is fixed by passing all file instance IDs to show the complete file tree.

IM-32781
:   Reported in version: 2026.3.0
:   Fixed the issue - now we are getting streams after the project search.

IM-32893
:   Reported in version: 2026.3.0
:   Due to changes in SAML and modern browser behavior introducing stricter validation over time, SAML logins could fail when the original authentication request was not retained for verification. Connect now uses a SAML authentication request repository to reliably store and validate SAML requests and responses, improving compatibility and preventing these authentication failures.

IM-33100
:   Reported in version: unspecified
:   Implemented v3 Stream API endpoints with stream name as query parameter instead of path parameter.

    Changes

    Added 6 new REST API endpoints under {{/api/v3}}:

    Get Stream

    curl 'http://localhost:8080/api/v3/stream?name=test_stream'
    --user admin:password

    Update Stream

    curl --location --request PUT 'https://local.connect.example.com/api/v3/stream?name=test_stream'
    --header 'Content-Type: application/json'
    --header 'Accept: application/json'
    --header 'Authorization: Basic YWRtaW46QzB2ZXIxdHkh'
    --data '{
    "description": "Description Updated testing"
    }'

    Delete Stream

    curl -X DELETE 'http://localhost:8080/api/v3/stream?name=test_stream'
    --user admin:password

    Get Stream UUID

    curl 'https://local.connect.example.com/api/v3/stream/uuid?name=test_stream' --header 'Authorization: Basic YWRtaW46QzB2ZXIxdHkh'

    Download Scan Transparency Data

    curl 'http://localhost:8080/api/v3/stream/scantransparency?name=test_stream'
    --user admin:password

    Copy Stream

    curl -X POST 'http://localhost:8080/api/v3/stream?name=test_stream&projectName=TestProject'
    --header 'Content-Type: application/json'
    --user admin:password

    Key Differences from v2

    - Stream name passed as query parameter ({{?name=stream_name}}) instead of path parameter ({{/streams/{name}}})
    - Base path: {{/api/v3}} vs {{/api/v2}}
    - All other functionality and responses identical to v2

IM-33430
:   Reported in version: 2026.3.0
:   The inconsistent SAML login failures related issue has been fixed.

IM-33500
:   Reported in version: 2026.3.0
:   Fixed the multiple SCW logs.

IM-33600
:   Reported in version: 2026.3.0
:   The CIM UI now sanitizes invisible Unicode characters (such as Zero Width Spaces) from function names when copying, preventing API failures when pasted into Swagger or curl.

IM-33616
:   Reported in version: 2026.3.0
:   Fixed an issue where Coverity xref migration is failing due to invalid memory alloc request size.

#### Known issues and solutions

CNC-4435
:   In Coverity cloud, the `triage-suggestion-service...` container images are not available as `-ubi` images in the Coverity 2026.3.0 release. The Coverity 2026.3.0 release does not support AI-Assisted Triage on Red Hat OpenShift.

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

### Coverity Report Generators 2026.3.0

#### New or changed features

RG-1968
:   Added support for OWASP Mobile Top Ten 2024 in the Report Generator. Configure the desired OWASP Mobile version by setting the owasp-version field in the config.yaml file under the mobile-wasp-report section; the selected version will be reflected in generated OWASP Mobile reports.

#### Bug fixes

IM-33858
:   Reported in version: 2026.3.0
:   Fixed an issue where the Security Report Generator 2026.3.0 failed with a Duplicate key 25 error when generating a Security report configured for SANS 2023. Reports now generate successfully with SANS 2023 selected.

RG-1991
:   Reported in version: 2026.3.0
:   Fixed Mobile OWASP report data inconsistencies with Connect Server.

## Coverity Analysis 2026.3.0

This section provides release notes for Coverity Analysis components.

### Coverity Analysis - General 2026.3.0

#### End-of-life products

SATSEC-16408
:   Support for SpotBugs and Detekt has been removed in Coverity 2026.3.0.

#### Deprecated products and features

COVDOCS-1997
:   CodeXM for Go, Python, and JavaScript is deprecated and will be removed in a future release.

COVDOCS-1999
:   User written models for Go and Kotlin are deprecated. A future release will remove support for running `cov-make-library` to customize analysis of Go or Kotlin code.

COVDOCS-2029
:   Kotlin quality checkers are disabled by default as of 2026.3.0 and will be removed in a future version.

COVDOCS-2079
:   Support for checker options for trust and distrust settings has been deprecated as of 2026.3.0 and will be removed in a future version.

#### New or changed features

COVDOCS-2035
:   Coverity Analysis hardware requires a minimum of 3GB of memory.

IM-33228
:   This release addresses critical accessibility (a11y) issues identified in Lighthouse audits, ensuring WCAG 2.1 compliance and improving the user experience for users with disabilities.

    New Features

    Accessibility Enhancements
    Keyboard Navigation (WCAG 2.1 - Bypass Blocks)
    - Added skip links on login and main pages allowing keyboard users to bypass navigation and jump directly to main content
    - Skip links are visually hidden until focused, appearing at the top-left on keyboard focus

    ARIA Compliance
    - Fixed ARIA parent-child role relationships in data grid components (data-table.component.ts:460-517)
    - Added proper `role="row"` attributes to header containers
    - Added `role="grid"` and `aria-label` attributes to grid elements
    - Enhanced menu elements with proper `aria-label` attributes

    Semantic HTML
    - Wrapped main content areas in `<main>` elements with `aria-label` for screen reader navigation
    - Fixed improper list nesting (converted `<div>` to `<li>` elements where appropriate)
    - Corrected HTML structure in login forms and modal components

    Visual & Interactive Improvements
    - Added descriptive `alt` text to all images, particularly the Black Duck logo
    - Optimized data table row heights for better readability. Header row height: 28px and Data row height: 24px
    - New accessibility-click-targets.css ensuring minimum 48x48px touch/click targets
    - Enhanced skip link styling with high-contrast focus indicators

    Files Modified
    Angular Components (57 files)
    - Login, header, sidebar, and alert components
    - Configuration management components (groups, users, streams, hierarchies)
    - Modal dialogs and dropdowns across features
    - Data table components with ARIA fixes
    - Diagnostic and project view components

    Backend Templates (10 JSP files)
    - Login pages and password recovery forms
    - Error pages and license upload templates
    - Source browser templates (triage, xrefs)

    Stylesheets (5 files)
    - styles.less: Skip link global styles
    - New accessibility-click-targets.css: Click target size compliance
    - header.less, tableview.less: Layout adjustments
    - login.css: Enhanced login page accessibility

    Impact
    - Compliance: Addresses Lighthouse accessibility audit failures
    - User Experience: Improved navigation for keyboard users and screen reader users
    - Standards: WCAG 2.1 Level AA compliance for affected components
    - Maintainability: Comprehensive documentation added for developers

    Testing Recommendations
    - Run Lighthouse accessibility audits to verify score improvements
    - Test keyboard navigation using Tab/Shift+Tab and verify skip links appear on focus
    - Verify screen reader compatibility (NVDA, JAWS, VoiceOver)
    - Validate all interactive elements meet minimum 48x48px touch target requirements
    - Test color contrast ratios meet WCAG AA standards (4.5:1 for normal text)

SAT-47220
:   Code-line annotations, used to modify how Coverity Analysis reports and triages defects, are now case-insensitive with respect to the checker name and the event tag.

SAT-47233
:   Improved function pointer resolution when using `--enable-fnptr` to avoid incorrect resolutions in cases involving function pointers passed as arguments to functions taking `...`, such as `printf`.

SAT-47290
:   Upgraded Flexnet support on linux64. It will require the `lmgrd` server to be upgraded, otherwise you may get "Bad message command" errors.

SAT-47589
:   FLEXNET licensing now supports IPv6 networks on Linux platforms.

#### Bug fixes

COVCLI-4216
:   Reported in version: 2026.3.0
:   Previously, HFI analysis would fail to analyze configuration files if capture configuration included a languages setting. These files are now analyzed correctly.

IM-33227
:   Reported in version: 2026.3.0
:   Upon snapshot deletion triggered via REST API, correct status is shown of the process.

SAT-46741
:   Reported in version: 2026.3.0
:   Added models for `mutex_lock` and `mutex_unlock` causing LOCK to analyze them properly.

SAT-47833
:   Reported in version: 2026.3.0
:   Fixed an issue in DEADCODE that could cause JavaScript work units to fail if they contained anonymous variables.

### Coverity CLI 2026.3.0

#### New or changed features

COVCLI-3584
:   The Coverity CLI now supports a new configuration setting, `analyze.enable-check-set`, which provides easy analysis for OWASP Top 10 and CWE Top 25.

COVCLI-4065
:   It is now possible to force defect results to be committed to the local file system only. A new option, `--local-only`, has been added to the `commit` and `scan` commands, as well as a configuration-file setting `commit.local-only=true`, to force the commit to the file system only.

COVCLI-4125
:   The Coverity CLI has added a new configuration setting and command-line argument to allow a pool size to be specified for analysis in Connect.

COVCLI-4128
:   It is now possible to to skip emitting JavaScript files inside web application archives during capture using a new configuration setting `capture.files.webapp-archives.exclude-js=true`. This setting is configured per webapp archive in the `capture.files.webapp-archives` array and defaults to false to maintain backward compatibility.

COVCLI-4129
:   It is now possible to skip capturing all webapp archives files using a new configuration-file setting `capture.files.exclude-all-webapp-archives=true`.

COVDOCS-1987
:   (See [COVCLI-4065].)

COVDOCS-2018
:   (See [COVCLI-4129].)

#### Bug fixes

COVCLI-4177
:   Reported in version: 2026.3.0
:   An initial scan which failed due to invalid authentication could prevent later scans from succeeding with the same intermediate directory. This has now been fixed.

COVCLI-4259
:   Reported in version: 2026.3.0
:   In previous releases, some source files under a `vendor` directory were omitted from capture, despite a configuration setting of `capture.files.include-dirs=vendor`. This has now been fixed.

### Coverity Checkers 2026.3.0

For a summary of checkers that have been added or changed in this release, refer to the "Coverity Checker Change History" table in the *Coverity Checker Reference*.

#### Deprecated products and features

SAT-47726
:   Kotlin quality checkers are disabled by default in 2026.3.0 and will be removed in a future version.

#### New or changed features

SAT-424, SAT-44648, SAT-47747, SAT-47832
:   Improved the `RESOURCE_LEAK` checker to report cases where an allocated object with allocated fields is returned from a function, then freed without freeing some of the fields.

SAT-46333
:   Enhanced the `PRECEDENCE_ERROR` checker to handle unexpected binding of expressions outside of macro expansions to expressions within the macro expansions.

SAT-46473
:   Updated the `DIVIDE_BY_ZERO` checker to deduce bounds for variables in loop conditions involving "not equals to (!=)" operator.

SAT-46962
:   The Linux scandir() and scandirat() built-in models have been enhanced to no longer require the "namelist" parameter to be initialized, better matching these functions' behavior.

SAT-47156
:   Checker `READONLY_BUFFER` is now documented.

SAT-47295
:   Improved the event messages in `INCOMPLETE_DEALLOCATOR` when allocations happened in called functions.

SATSEC-16021
:   The `SESSION_MANIPULATION` checker now supports Java.

SATSEC-16243
:   The `MASS_ASSIGNMENT` checker options now supports regular expressions.

SATSEC-16461
:   The `MASS_ASSIGNMENT` checker options now supports class-qualified field names for Java and C#.

SATSEC-16527
:   The `MASS_ASSIGNMENT` checker now respects allow‑listing and will no longer report defects on protected types and parameters.

SATW-6800
:   Fixed incorrect reporting of MISRA C 2023 Rule 2.1 / MISRA C++ 2023 Rule 0.0.1 for unreachable statements.

#### Bug fixes

SAT-42223, SAT-42953, SAT-47450
:   Reported in version: 2022.03, 2026.3.0, 2026.3.0
:   Fixed a `RETURN_LOCAL` FP involving `weak_ptr.lock()`.

SAT-43357
:   Reported in version: 2026.3.0
:   A model is added for linux function filp_open to catch potential RESOURCE_LEAK defects.

SAT-43977
:   Reported in version: 2026.3.0
:   Getting the size of a variable's type using the sizeof() operator will no longer be treated as accessing the variable's value in the `EVALUATION_ORDER` checker.

SAT-44268
:   Reported in version: 2026.3.0
:   Fixed an issue that could case `FORWARD_NULL` false positives when using the `instanceof` pattern in Java.

SAT-45099, SAT-45906
:   Reported in version: 2026.3.0, 2026.3.0
:   Fixed a MISRA C-2012 Rule 5.9 false positive that could occur when an inline static function in a header file contained different macro expansions when included from different files.

SAT-46632
:   Reported in version: 2026.3.0
:   Fixed an issue that could prevent code compliance deviations from being applied to defects that are located at the beginning of the file.

SAT-46739
:   Reported in version: 2026.3.0
:   Fixed `MISSING_RETURN` false positive reports in C++ coroutines.

SAT-46856
:   Reported in version: 2026.3.0, 2026.3.0
:   Improved the handling of the case where a called function modifies fields in an unnamed structure.

SAT-46918
:   Reported in version: 2026.3.0
:   Fixed an issue in which the `INTEGER_OVERFLOW` checker might not properly track values of references in structured bindings.

SAT-46960
:   Reported in version: 2026.3.0
:   Fixed a bug in `POINTER_NONDETERMINISM` where an assignment event was located on the incorrect line.

SAT-46992
:   Reported in version: 2026.3.0
:   Fixed some One Definition Rule false negatives resulting from conflicts involving compiler-generated functions.

SAT-47075
:   Reported in version: 2026.3.0
:   In `INTEGER_OVERFLOW`, improve the handling of values that might be negative, but are later tested to ensure they are non-negative.

SAT-47174
:   Reported in version: 2026.3.0
:   MISRA C++ 2023 Rule 0.1.1 checker now correctly reports unused value for cases involving self-updates in a loop.

SAT-47211
:   Reported in version: 2026.3.0
:   Fixed a false positive in the `UNUSED_VALUE` and `MISRA C++-2023 Rule 0.1.1` checkers related to structure fields which are written individually, and not individually used, but the structure is used as a whole object.

SAT-47325
:   Reported in version: 2026.3.0
:   Fixed an issue in `INCOMPLETE_DEALLOCATOR` which could cause it not to recognize when a single allocation was assigned to multiple fields within the same structure.

SAT-47330
:   Reported in version: 2026.3.0
:   Models are added to Linux/Android functions to eliminate certain RESOURCE_LEAK FPs.

SAT-47741
:   Reported in version: 2026.3.0
:   Fixed a recoverable analysis error with message "No ODR diff found" in some cases when analyzing C++ code compiled in both 32 bit and 64 bit mode.

SAT-47915, SAT-47919
:   Reported in version: 2026.3.0, 2026.3.0
:   Fixed an issue in the way the control buffer in the `recvmsg()` function is handled.

SATSEC-16307
:   Reported in version: unspecified
:   Fixed a false positive for the `CSRF` checker. [Java]

SATSEC-16506
:   Reported in version: unspecified
:   Addressed `REGEX_INJECTION` false positives by adding a sanitizer for the .NET `Regex.Escape` method.

SATSEC-16541
:   Reported in version: unspecified
:   Fixed a false negative for the `SQLI` checker. [C#]

SATSEC-16547
:   Reported in version: unspecified
:   Fixed a false positive pattern for the `XML_EXTERNAL_ENTITY` checker. [C#]

SATW-5739
:   Reported in version: 2026.3.0
:   Fixed false positive for CERT MEM52-CPP.

SATW-6402
:   Reported in version: 2026.3.0
:   Fixed False Positive for AUTOSAR C++ 14 A7-1-7.

SATW-6518
:   Reported in version: 2026.3.0
:   Fixed False Positives for MISRA C-2023 Rule 22.12.

SATW-6531
:   Reported in version: 2026.3.0
:   Fixed False Positive for CERT ERR33-C/POS54-C.

SATW-6685, SATW-6686
:   Reported in version: 2026.3.0
:   Fixed false positive for AUTOSAR C++14 A5-1-1.

SATW-6710
:   Reported in version: 2026.3.0
:   Fixed False Positive for AUTOSAR C++ 14 A7-1-2.

SATW-6716
:   Reported in version: unspecified
:   Fixed regex failure for CERT C Rule PRE10-C.

SATW-6748, SATW-6749
:   Reported in version: unspecified
:   Fixed False Negatives for Rule Misra C++-2023 Rule 6.8.2.

SATW-6796
:   Reported in version: 2026.3.0
:   Fixed False Positive for MISRA C++-2008 Rule 8-4-4.

SATW-6873
:   Reported in version: 2026.3.0
:   Fixed False Positive for MISRA C++ 2023 Rule 15.1.4.

SATW-6874
:   Reported in version: 2026.3.0
:   Fixed False Positive for MISRA C++ 2023 19.0.2.

### Coverity Commands 2026.3.0

#### Deprecated products and features

SAT-47497
:   The `cov-link` binary has been deprecated and will be removed in a later release.

#### New or changed features

SATSEC-16416
:   `cov-analyze` now supports enabling checkers for specific vulnerability lists with the `--enable-check-set` option.

### Coverity Compilers and Capture 2026.3.0

#### End-of-life products

CAP-2581
:   Support for Bazel 6 has been removed as of 2026.3.0.

#### Deprecated products and features

CMPCSH-2141
:   Support for .NET 9 is deprecated as of 2026.3.0 and will be removed in a future release.

COVP-2662
:   Support for FreeBSD 13 is deprecated as of 2026.3.0 and will be removed in a future release.

#### New or changed features

CAP-2523
:   Added support for FreeBSD 15.0.

CAP-2585
:   Support for Bazel 9 has been added as of 2026.3.0.

CMPCPP-14556
:   Native compiler are usually probed in a temporary directory, but if the command line has relative paths on the command line, this can break. For some compilers, we will automatically probe in the current directory if probing in the temp directory fails.

CMPCPP-15612
:   IAR ARM 9.70 is now supported.

CMPCPP-15634
:   Added support for ARM FuSa 6.22.2.

CMPCPP-15635
:   SONY PS5 SDK 12.000 is now supported.

CMPCSH-2147
:   Added support for C# 14.

COVP-2660
:   Support for .NET 10 has been added as of 2026.3.0.

COVP-2663
:   Support for Windows Server 2025 has been added as of 2026.3.0.

#### Bug fixes

CAP-1241
:   Reported in version: 2018.01
:   Compilations launched from statically linked binaries will no longer be missed by capture, provided that:
    - The compiler itself is dynamically linked
    - The statically linked processes in the build do not clear any of the environment variables that Coverity sets
    - `cov-build` is not called with the `--original-capture` argument

CAP-2570
:   Reported in version: 2026.3.0
:   Users no longer need to set `ALLOW_NINJA_ENV` while building Android; Coverity now automatically sets that variable when it detects that Android is being built in a way that would require that to be set.

CAP-2597
:   Reported in version: 2026.3.0
:   Bazel arguments that include multiple `=` characters will no longer be parsed incorrectly when running `cov-build` with the `--bazel` argument.

CAP-2604
:   Reported in version: 2026.3.0
:   The `pseudo` tool will no longer cause capture to fail when running builds with the bitbake build system under new capture.

CAP-2605
:   Reported in version: 2026.3.0
:   Builds using the bitbake build system will no longer crash on a `getcwd` call when run under new capture.

CAP-2612
:   Reported in version: 2026.3.0
:   Bazel builds making use of the `copy_file` rule will now be captured properly.

CAP-2627
:   Reported in version: 2026.3.0
:   New capture will no longer treat a directory with a name matching the binary that we're attempting to run with `execvp` or `posix_spawnp` as a potentially executable file.

CMPCPP-13168
:   Reported in version: 2026.3.0
:   Fixed the Intel OneAPI CIT configuration redirect on Windows accidentally choosing Linux configuration.

CMPCPP-13250
:   Reported in version: 2026.3.0
:   `__float128` type is now recognized on Windows for Intel OneAPI compiler as well as `_Quad` type when Intel's undocumented `--extended_float_types` flag is used.

CMPCPP-15279
:   Reported in version: 2026.3.0
:   Fixed an issue where Apple Clang language version was not being set by default.

CMPCPP-15298
:   Reported in version: 2026.3.0
:   Fixed an issue where linker instrumentation for GNU ld would prefer shared libraries in system directories over static libraries in user-specified directories.

CMPCPP-15426
:   Reported in version: 2026.3.0
:   Coverity compiler was not permitting specializations of nested classes. A new `cov-emit` option `--allow_in_class_specializations` was added and used by default with IAR ARM compilers.

CMPCPP-15428
:   Reported in version: 2026.3.0, 2026.3.0, 2026.3.0, 2026.3.0, 2026.3.0, 2026.3.0
:   Updates to compiler compatibility header add missing scalable vector types and other vector types fix errors reporting undefined identifier of the form "__SV...._t"

CMPCPP-15490
:   Reported in version: 2026.3.0
:   Make sure __restrict is recognized in MSVC mode.

CMPCPP-15517
:   Reported in version: 2026.3.0
:   Diagnostics related to link units will only be displayed if link units are being emitted.

CMPCPP-15549
:   Reported in version: 2026.3.0
:   Fixed the handling of `-Qoption` handling for Intel OneAPI compiler.

CMPCPP-15591
:   Reported in version: 2026.3.0
:   Xtensa compiler configuration was failing when certain environment variables were set. This has been fixed and logging has been enhanced to better identify problems.

CMPCPP-15641
:   Reported in version: 2026.3.0
:   The Chess compiler is unsupported. A prototype is included in the product for investigation purposes only. The cov-configure help has been updated to indicated this status. Please contact support before using it.

CMPCPP-15711
:   Reported in version: 2026.3.0
:   Spurious defects were being reported in our compiler compatibility headers for the Xtensa compiler. These have been eliminated.

CMPCSH-2167
:   Reported in version: 2026.3.0
:   Resolved an issue with `cov-manage-emit` where merging two intermediate directories (iDir) could result in an invalid merged iDir.

CMPGO-593
:   Reported in version: 2026.3.0
:   Fixed the Go analysis crash when handling `map[string]interface{}`.

CMPGO-604
:   Reported in version: 2026.3.0
:   Added an opt-in compatibility mode for buildless capture with cgo.

COVCLI-4246
:   Reported in version: 2026.3.0
:   In the previous release, specifying files to be excluded from capture (e.g., with the Coverity CLI configuration setting `capture.files.exclude-regex`) did not exclude files which were generated by the analysis phase during replay. This has now been fixed, and translation units for all such files are now removed from the intermediate directory.

## Coverity Desktop 2026.3.0

This section provides release notes for Coverity Desktop components.

### Coverity Desktop for Eclipse 2026.3.0

#### End-of-life products

PRD-13238
:   Support for Eclipse 2022-09 has been removed as of 2026.3.0.

#### Deprecated products and features

PRD-13239
:   Support for Eclipse 2023-03 is deprecated as of 2026.3.0 and will be removed in a future release.

#### New or changed features

PRD-13236
:   Added support for Eclipse 2025-09.

## Coverity Documentation 2026.3.0

This section provides release notes for Coverity Documentation components.

### Coverity Documentation 2026.3.0

#### New or changed features

COVDOCS-1969
:   New REST APIs include purge_snapshots, clear_stream_role_assignments, and run_etl_process.

COVDOCS-2026
:   AI-Assisted Triage (Beta) uses Large Language Models to automatically analyze Coverity issues and suggest classifications.

COVDOCS-2028
:   Modern UI (Beta)

    The modern UI introduces an updated interface with improved navigation, faster performance, and streamlined workflows.

    This release includes the issue triage workflow. Additional features will be available in future releases.

    What's new:

    • Redesigned Projects and Issues pages with enhanced filtering and sorting capabilities
    • Full-page issue detail view with dedicated split-pane layout replacing side panels
    • AI-assisted triage suggestions (beta) to help identify false positives and classify issues

    For details, see the Coverity Platform User and Administrator Guide.

#### Bug fixes

COVDOCS-1789
:   Reported in version: unspecified
:   The section "Checker enablement and option defaults by language" is available in Japanese as of 2026.3.0.

COVDOCS-1956
:   Reported in version: 2026.3.0, 2026.3.0
:   Fixed Report Generator documentation showing incorrect BDSIR report information.

COVDOCS-1994
:   Reported in version: 2026.3.0
:   In the checker coverage documentation, the `STACK_USE` checker now displays a "yes" under the SANS/CWE Top 25 column.

COVDOCS-2049
:   Reported in version: 2026.3.0
:   Fixed supporting languages list for the --replay-from-emit, -rpfe option.
