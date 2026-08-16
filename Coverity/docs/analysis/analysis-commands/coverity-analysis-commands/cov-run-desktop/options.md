---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "UGy4BCmG~cv_dM2LVClSKQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:11.260644+00:00"
---

# Options

--add-ignore-modified-file-regex `<regex>`
:   Specify a `<regex>` to ignore in addition to what is
    specified by `--ignore-modified-file-regex` and the
    `coverity.conf` file.

--add-restrict-modified-file-regex `<regex>`
:   Specify a `<regex>` to add to those specified by
    `--restrict-modified-file-regex` and the
    `coverity.conf` file. This means that filtered
    translation units must match both regular expressions specified by
    `--add-restrict-modified-file-regex` and
    `--restrict-modified-file-regex`.

--all-security
:   Enables all security checkers.
    This includes the Security, Android Security, and Web App Security categories, and other security checkers that
    require explicit enablement. It also includes the default set of Sigma checkers.
    It *does not include* the audit security checkers (which are enabled by --enable-audit-checkers).

    You can view the list of checkers that the --all-security option has enabled
    by invoking `cov-analyze` with the --list-checkers option.

--allow-suffix-match
:   Restores backward compatibility (pre-8.7) in specifying files to analyze on
    the command line. Specifically, this option allows specifying files for
    analysis using any unique path suffix already captured in the emit. Normally
    (without this option), the specified path must exist relative to the current
    working directory or as an absolute path, as one would expect from a command
    line command, so this option is only recommended for backward
    compatibility.

    This functionality can be made more permanent through a `coverity.conf`
    setting. See Coverity
    Desktop Analysis
    2026.6.0 User Guide for details.

--analyze-captured-source
:   Selects for analysis all files previously captured. This option is an
    alternative to listing files for analysis on the
    `cov-run-desktop` command line.

--analyze-scm-modified
:   Specifies the translation units to be analyzed as those that have been
    modified locally, as referenced against your Source Code Management (SCM)
    system. When `--analyze-scm-modified` is passed, you must
    also pass the `--scm` option, or,
    preferably, set "`settings.scm.scm`" in
    `coverity.conf`. This option is an alternative to listing
    files for analysis on the `cov-run-desktop` command line.

--analyze-untracked-files <boolean>
:   When true, files reported as untracked by the SCM will be analyzed.
    This option is false by default.

--auth-key-file <keyfile>
:   Specify the location of a previously created authentication key file, used for connecting to the
    Coverity Connect server. Authentication keys can be registered with a
    Coverity Connect instance and used for authentication in place of the
    `--user` and `--password` options. See
    "Working
    with authentication keys" in Coverity Platform 2026.6.0 User and Administrator Guide.

--build
:   Runs the build command specified in the `coverity.conf` file
    under `cov-build`. This is necessary so the Coverity tools
    know how to compile all of the source files in your project.
    If you add new source files or change how they are compiled, you need to re-run `cov-run-desktop --build`.
    The build command will automatically configure compilers (`cov-run-desktop --configure`) if they have not been configured yet.
    If you change a command line, you should also delete the contents of the intermediate directory, idir/, before you
    re-run `cov-run-desktop --build`.

--category-regex <regex>
:   Filters the list of returned issues to include only those whose
    `checkerProperties` is not `null`, and
    where `checkerProperties.category` matches the specified
    regular expression. See the "CheckerProperties" section in the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

--certs <filename>
:   In addition to CA certificates obtained from other truststores, use the CA certificates in the
    given `filename`. This file is in PEM format. For information on the TLS/SSL certificate
    management functionality, please see Coverity Platform 2026.6.0 User and Administrator Guide.

--checker-regex <regex>
:   Filters the list of returned issues to include only those whose `checkerName`
    matches the specified regular expression. See `checkerName`
    in the "IssueOccurrence"
    section in the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

--cid <rangeFilter>
:   Filters the list of returned issues to include only those whose `stateOnServer` is
    not `null` (see the "StateOnServer" section in the Coverity
    Desktop Analysis
    2026.6.0 User Guide for details), and whose
    `stateOnServer.cid` is not `null` and
    matches the range filter. The range filter should match one of the following
    formats:

    `<int>`
    :   A single CID matching the value in
        `<int>`.

    `<int>"-"`
    :   A range of CIDs including `<int>` and all
        greater values.

    `"-"<int>`
    :   A range of CIDs including `<int>` and all
        lower values.

    `<int1>"-"<int2>`
    :   A range of CIDs including `<int1>`,
        `<int2>`, and all CID values in
        between.

--clean
:   Runs the clean command specified in the `coverity.conf` file.

--code-base-dir <code_base_dir>
:   Specifies the value of the "`code_base_dir`" variable. This is
    the directory that contains the `coverity.conf` file, and
    will generally be your SCM project root directory.

    By default, `cov-run-desktop` searches upward in the file tree
    from where it is invoked to find a `coverity.conf` file. If
    one is found, then the directory containing that file is the
    `code_base_dir`. Otherwise, the invocation directory is
    the `code_base_dir`.

--component-not-regex <regex>
:   Filters the list of returned issues to include only those whose `stateOnServer` is
    `null` or for those which have no component names that
    match the specified regular expression. See the "StateOnServer" section in the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

--component-regex <regex>
:   Filters the list of returned issues to include only those whose `stateOnServer` is
    `null` or for which at least one component name matches
    the specified regular expression. See the "StateOnServer" section in the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

--config <cov_config_file>
:   The name of the file where the compiler configuration information will be
    stored. By default, this is the value of the
    `compiler_config_file` in
    `coverity.conf`.

--configure
:   When this option is specified, `cov-run-desktop` invokes
    `cov-configure` on each of the
    `CompilerConfiguration` elements in the
    `coverity.conf` file.

--confine-to-scope <boolean>
:   Filters the list of returned issues to include only those whose
    `mainEventFilePathname` (see `mainEventFilePathname`
    in the "IssueOccurrence" section
    in Coverity
    Desktop Analysis
    2026.6.0 User Guide) is one of the "analysis scope"
    files. This means that any defects found in files outside of the analysis
    scope will not be returned. When false, no such filtering is done.

    For example, the command line `cov-run-desktop test.c`
    reports defects in `test.c` but not in the headers it might
    include. The command line `cov-run-desktop --confine-to-scope false
    test.c` reports defects in `test.c`
    *and in* its headers.

    This option is `true` by default

    Note:
    For information on how analysis scope is defined, see
    the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

--connect-timeout <timeout>
:   Allows users to change (in seconds) the connection timeout to the given
    duration. The default connection timeout is set to 60 seconds.

--cov-user-dir <cov_user_dir>
:   Specifies the value of the "`cov_user_dir`" variable. This
    corresponds to a directory where user-specific and application-specific
    settings are stored. By default, this is
    "`%APPDATA%/Coverity`" on Windows and
    "`$HOME/.coverity`" on Unix.

--create-auth-key
:   Creates an authentication key file and writes it to the
    `auth_key_file` location specified in
    `coverity.conf`.

--custom-triage-attribute-not-regex <attrName> <regex>
:   Filters the list of returned issues to include only those whose `stateOnServer` is
    `null`, or whose `CustomTriage` does not
    contain a key equal to the specified attribute name, or that does contain
    such a key but with a corresponding value that does not match the specified
    regular expression. See the "StateOnServer" section in the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

    For example, `--custom-triage-attribute-not-regex "customAttr"
    "customVal"` will return only those issues that *do
    not* have a custom attribute named "customAttr" with a value
    containing "customVal" as a substring.

--custom-triage-attribute-regex <attrName> <regex>
:   Filters the list of returned issues to include only those whose `stateOnServer` is
    `null`, or whose `CustomTriage` contains a
    key exactly equal to the specified attribute name and for which the
    corresponding value matches the specified regular expression. See the "StateOnServer" section in
    the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

    For example, `--custom-triage-attribute-regex "customAttr"
    "customVal"` will return only those issues that have a
    custom attribute named "customAttr" with a value containing "customVal"
    as a substring.

--cwe-category-regex <regex>
:   Filters issues whose CWE category matches the given `<regex>` (using partial
    match). Issues that do not have a CWE category will match "none".

    For example, `--cwe-category-regex
    '^(none|762)$'` will match all the issues that either do not
    have a CWE category or have a category of 762. Note the need for "^" and
    "$" for partial regex matches.

--data-dir
:   Specifies the directory in which `cov-run-desktop` stores its
    data. The default value is `$(code_base_dir)/data-coverity`.
    The value is stored in a variable, `$(data_dir)`.

    Note:
    You must use `coverity.conf` 6 or above to use the
    `data_dir` option.

--dir <intermediate_dir>
:   Specifies the intermediate directory. Required if no
    `coverity.conf` file is present.

    Note:
    Desktop Analysis can only be run on an intermediate directory
    created on the same machine, and in the same source code directory, as the
    analysis will take place (i.e. the build and analysis processes must take
    place on the same machine and directory, and the intermediate directory must
    not be moved).

--disable-misra
:   Ignores any MISRA analysis configuration when
    `cov-run-desktop` uses analysis settings from the chosen
    reference snapshot. This is useful when the reference snapshot includes
    unwanted or unnecessary MISRA analysis results, but you still want to use
    the same settings for local analysis.

--disconnected
:   When specified, `cov-run-desktop` operates in "disconnected"
    mode. Related options will be accepted but ignored while disconnected.

--enable-audit-mode
:   Enables audit mode analysis, which is intended to expose more potential
    security vulnerabilities by considering additional potential data sources
    that could be used in an exploit.

    Using this option usually reports more defects that are less likely to
    represent true vulnerabilities. Audit mode analysis will take noticeably
    longer to complete: It analyzes all functions that are present in the
    source, not just those that are present in the call tree. This level of
    testing can be useful for auditors and for any users who want to see the
    maximum number of defects.

    The `--enable-audit-mode` option has the following effects:

    - It enables additional audit mode checkers that normally are off by
      default: for example, SQL_NOT_CONSTANT and INSECURE_COOKIE.

      For a list of all audit mode checkers, see the "Checker Enablement and Option Defaults by
      Language" table in the Coverity 2026.6.0 Checker Reference (HTML only).
    - It sets the `--webapp-security-aggressiveness-level`
      to `high`.
    - It sets `--distrust-all`.
    - For tainted dataflow security checkers, it introduces additional
      audit mode sources of untrusted (tainted) data, in order to model
      potential attacks. Such sources include all function parameters, and
      the return value from external functions (those that are not visible
      in the source code or bytecode, and for which no model exists).

--exit1-if-defects <boolean>
:   When true, `cov-run-desktop` exits with code 1 when defects
    are present in the analysis, as long as there are no errors present that
    cause a higher exit code. This option is false by default.

--extend-checker <executable>
:   This option will cause the specified `executable` to be
    invoked as an additional checker for Desktop Analysis. The executable can be
    either an absolute or relative path.

    This option can be specified more than once to enable multiple Extend checkers.

--extend-checker-option <executable> <checker_name>:<option>[:<option_value>]
:   Passes a checker option for an Extend checker, which must be specified with
    `--extend-checker`. The specified
    `executable` must exactly match the
    `executable` passed to `--extend-checker`.

    Example:

    ```
    > cov-run-desktop [options] --extend-checker MY_CHECKER.exe --extend-checker-option MY_CHECKER.exe MY_CHECKER:option_a:true
    ```

--file-not-regex
:   Filters the list of returned issues to *not* include those whose
    `mainEventFilePathname` matches the specified regular
    expression. See `mainEventFilePathname` in the "IssueOccurrence" section
    in the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

--file-regex <regex>
:   Filters the list of returned issues to include only those whose
    `mainEventFilePathname` matches the specified regular
    expression. See `mainEventFilePathname` in the "IssueOccurrence" section
    in the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

--first-detected-after <date>
:   Filters the list of returned issues to include only those that were first detected after the
    specified date. The value of `<date>` must follow one
    of the following formats:

    - `YYYY-MM-DD`: Specifies a year
      (`YYYY`), month (`MM`), and
      day (`DD`). Note that midnight in the local time
      zone (that is, `T00:00<local>`) is
      implicit.
    - `YYYY-MM-DD[ T]hh:mm(:ss)`: Specifies a time of
      day along with the date. The time format accepts hours
      (`hh`), minutes (`mm`), and
      seconds (`ss`). Note that the local time zone is
      implicit.
    - `YYYY-MM-DD[ T]hh:mm(:ss)Z`: Specifies the
      Greenwich Mean Time (GMT) zone for the specified time and date.
      Here, `Z` refers to "Zulu", which signifies
      GMT.
    - `YYYY-MM-DD[ T]hh:mm(:ss)[+-]hh:mm`: Specifies the
      date along with an offset (`[+-]`) to the
      specified local time of day.

--first-detected-before <date>
:   Filters the list of returned issues to include only those that were first
    detected before the specified date. For the date format, see the `--first-detected-after` option.

--function-regex <regex>
:   Filters the list of returned issues to include only those whose
    `functionDisplayName` matches the specified regular
    expression. See `functionDisplayName` in the "IssueOccurrence" section
    in the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

--host <hostname>
:   Specifies the DNS hostname or IP address of the machine where Coverity Connect is running. This option is required, or must be specified in
    `coverity.conf`, unless operating in "disconnected" mode. If
    disconnected, this option has no effect. This option is deprecated.

--ignore-all-files-regex <regex>
:   When specified, any file whose name matches `<regex>` will be ignored by analysis.
    This option may only be specified once, but `<regex>` may use the "|" operator to ignore
    multiple files.
    See Translation unit selection for more information.

--ignore-deviated-findings
:   Set this option to prevent reporting defects that are deviated with annotations.

    Any defects or false positives annotated using the `#pragma` Coverity
    compliance directive will be suppressed and will not be reported by Coverity Connect.
    *All* recorded deviations in the current project version are
    then written to a CSV file.
    For more information see "Annotating compliance deviations"
    in the Customizing Coverity book.

--ignore-modified-file-regex <regex>
:   When specified, any file whose name matches `<regex>` will be treated as not modified.
    This option may only be specified once, but `<regex>` may use the "|" operator to ignore
    multiple files.
    See Translation unit selection for more information.

--ignore-modified-non-psf <boolean>
:   When specified as true, a translation unit will be considered modified only
    if its primary source file is modified. This option is false by default.

--ignore-uncapturable-inputs <boolean>
:   When `true`, allows analysis to proceed even if Coverity is unable to process some
    input files for analysis. Specifically, if some file has not been in a
    captured a compilation and no automatic way of capturing it is configured
    (for example, buildless capture), the file will be ignored if this option
    is `true`. If `false`, such input files will
    cause an error. Although this option can be used as a crude alternative to
    the "modified file" regex options, it is not recommended for that purpose.
    Although not recommended, this functionality can be made more permanent
    through a `coverity.conf` setting.
    See Coverity
    Desktop Analysis
    2026.6.0 User Guide for details.

--ignore-untracked-file-regex <regex>
:   Untracked files are ignored if they match the <regex>.

--impact-regex <regex>
:   Filters the list of returned issues to include only those whose
    `checkerProperties` is not `null`, and
    where `checkerProperties.impact` matches the specified
    regular expression. See the "CheckerProperties" section in the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

--include-missing-locally <boolean>
:   When this option is set to `true`, the list of returned issues
    includes issues that are missing in the local analysis but present in the
    reference snapshot; that is, their local status is "missing". Defaults to
    `--include-missing-locally false`.

--json-output-v10 <filename>
:   When present, `cov-run-desktop`'s output is written to the specified file in JSON
    output (see "Desktop Analysis JSON output syntax"
    in the Coverity
    Desktop Analysis
    2026.6.0 User Guide).
    You can include either an absolute path or a path relative to the location in which you execute the
    command. If you want the file name to end in `.json`, you
    must include it in the `<filename>`.

    `--json-output-v10` is the recommended JSON output option, as
    it contains the most complete set of information. Earlier versions, v1
    through v9, are supported for backward compatibility.

--kind-regex <regex>
:   Filters the list of returned issues to include only those whose
    `checkerProperties` is not `null`, and
    where the `issueKinds` value matches the specified regular
    expression. See the "CheckerProperties" section in the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

    Matching is done using a single string, which is a comma-separated
    concatenation of all the `issueKinds`, in alphabetical
    order. For example, "`QUALITY,SECURITY`".

--language-regex <regex>
:   Filters the list of returned issues to include only those whose
    `language` matches the specified regular
    expression.

--lang <language>
:   Write event messages in the specified language. Currently, the supported
    values are `en` (for English), `ja` (for
    Japanese), and `zh-cn` (for Simplified Chinese). The default
    language is English (`en`).

--lang-regex <language>
:   This option specifies a regex and matches it against the defect's language.
    These languages include the following: C, C++, C#, CUDA, Fortran, Java,
    JavaScript, Objective-C, Objective-C++, PHP, Python, Ruby, Scala, Text, and
    VisualBasic.

--local-status-not-regex <local status>
:   This option can be used only when `--include-missing-locally` is set to
    `true`. Filters the list of returned issues to exclude
    those issues whose local status matches the specified regular expression.
    The valid values for the local status are as follows:

    `local`
    :   The issue's CID is present in a recent run, but not present on
        the server.

    `missing`
    :   The issue's CID is present on the server, but not in a recent run.

    `present`
    :   The issue's CID is present in both a recent run and on the server.

    Here is an example of using `--local-status-not-regex`:

    ```
    cov-run-desktop --include-missing-locally true --local-status-not-regex present <analysis options
    ```

--local-status-regex <local status>
:   This option can be used only when `--include-missing-locally` is set to
    `true`. Filters the list of returned issues to include
    only those issues whose local status matches the specified regular
    expression. The valid values for the local status are as follows:

    `local`
    :   The issue's CID is present in a recent run, but not present on
        the server.

    `missing`
    :   The issue's CID is present on the server, but not in a recent run.

    `present`
    :   The issue's CID is present in both a recent run and on the server.

    Here is an example of using `--local-status-regex`:

    ```
    cov-run-desktop --include-missing-locally true --local-status-regex missing <analysis options>
    ```

--mark-fp <cid> <explanation>
:   Sets the Classification of the specified CID to "False Positive". The value
    of `<cid>` is the defect's CID, and
    `<explanation>` is a string which explains why this
    defect is a False Positive.

--mark-int <cid> <explanation>
:   Sets the Classification of the specified CID to "Intentional". The value of
    `<cid>` is the defect's CID, and
    `<explanation>` is a string which explains why this
    defect is Intentional.

--merge-key-regex <regex>
:   Filters the list of returned issues to include only those whose `mergeKey` matches
    the specified regular expression. See `mergeKey` in the "IssueOccurrence" section
    in the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

--MISRA-category-regex <regex>
:   Filters defects that have a MISRA category which matches the specified
    `<regex>`. Possible categories are
    `Advisory`, `Required`, and
    `Mandatory`.

--modification-date-threshold <date_time>
:   Specifies the modification date threshold to use instead of the default. Only
    those files modified on or after the specified date will be included in the
    analysis. The value of `<date_time>` should match the
    `YYYY-MM-DD[ T]hh:mm(:ss)` format, where date and time
    are separated by a space or `T`. The time, specified by
    `hh:mm:ss`, is optional, and seconds
    (`:ss`) are not required. If time is not specified, the
    default value is midnight (00:00) of the specified date.

--no-default-triage-filters
:   By default, there are three active issue filters, which have the effect
    of suppressing issues triaged as uninteresting, or in a component named
    to hold third-party code:

    - ```
      --component-not-regex "[Tt]hird.*[Pp]arty"
      ```
    - ```
      --triage-attribute-not-regex "classification" \
      									"False Positive|Intentional|No Test Needed|Tested Elsewhere"
      ```
    - ```
      --triage-attribute-not-regex "action" "Ignore"
      ```

    If `--no-default-triage-filters` is specified, then
    all three of these filters are deactivated.

    If `--component-regex` or
    `--component-not-regex` is specified, then the first
    filter is deactivated.

    If `--triage-attribute-regex` or
    `--triage-attribute-not-regex` is specified for
    "classification" or "action", then the respective filter for that
    attribute is deactivated.

--no-text-output
:   When present, `cov-run-desktop` does not print the
    compiler-like textual output.

--occurrences <range>
:   When there are multiple occurrences for a given defect, each instance is
    given an occurrence number, O, from 1 to *N*. The
    `--occurrences <range>` option, specifies the
    valid values for O.

    Ranges are as described for the `--cid` option.

--on-new-cert <trust | distrust>
:   Indicates whether to trust (with trust-first-time) self-signed certificates, presented by the
    server, that the application has not seen before. Default is `distrust`. If
    `distrust` and the certificate is self-signed, the connect attempt will fail.
    For information on the new TLS/SSL certificate management functionality, please
    see Coverity Platform 2026.6.0 User and Administrator Guide.

    CAUTION:

    Setting `on-new-cert` to
    `trust` does not currently work with Coverity Analysis and
    Black Duck® Bridge. The workaround is to manually
    add the self-signed certificate to your operating system's
    certificate store. This will tell the operating system that it can
    trust this certificate, and should allow you to continue.

--ownerLdapServerName-regex <regex>
:   Filters the list of returned issues to include only those whose `stateOnServer` is
    `null`, or whose `ownerLdapServerName`
    matches the specified regular expression. See the "StateOnServer" section in
    the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

--password <password>, -pa <password>
:   Specifies the password for connecting to the Coverity Connect server.

--port <port_number>
:   Specifies the HTTP or HTTPS port of the Coverity Connect server. The default
    value is 8080. If `--ssl` is present, the default value is
    8443. This option has no effect in disconnected mode. This option is
    deprecated.

--present-in-reference <boolean>
:   Filters the list of returned issues to include only those whose `stateOnServer`
    (see the "StateOnServer"
    section in the Coverity
    Desktop Analysis
    2026.6.0 User Guide for details) is
    `null`, or whose value for
    `presentInReferenceSnapshot` is equal to the specified
    boolean.

--print-path-events <boolean>
:   When true, path events are printed in the text output. When false, path
    events are not printed. This option is true by default.

--reference-snapshot <specification>
:   Specifies how `cov-run-desktop` should select a reference
    snapshot from the selected "stream." The
    `<specification>` must be one of the following values:

    id:<ID>
    :   Use the snapshot with the matching `<ID>`.
        `--reference-snapshot` will return an error
        if the ID is invalid or if it is not in the selected stream.

    date:<date_time>
    :   Use the snapshot that was created closest to, but not after, the
        specified `<date_time>`. The value of
        `<date_time>` should match the
        `YYYY-MM-DD[ T]hh:mm(:ss)` format, where date
        and time are separated by a space or `T`. The
        time, specified by `hh:mm:ss`, is optional, and
        seconds (`:ss`) are not required.

        `--reference-snapshot` will return an error if
        there is no snapshot with summary data that was created before
        the specified `<date_time>`.

    latest
    :   Use the snapshot with the latest code-version date (that also
        contains summary data) in the specified stream.

        Note:
        This is not necessarily the most recently committed snapshot,
        since it is possible to commit a snapshot with an arbitrary code
        version date.

    idir-date
    :   Use the snapshot created closest to, but not after, the creation
        date of the intermediate directory.

        This is the default option.

    scm
    :   This option will query the SCM to determine the version that was
        most recently checked out or updated, and then use the closest
        snapshot.

        The `--scm` option, or
        the "`settings.scm.scm`" attribute in
        `coverity.conf`, is required when using this
        specification.

--relative-paths <boolean>
:   When true, compiler-like output paths are printed as relative paths, relative
    to the directory specified by `--relative-to`. If
    `--relative-to` is not specified, the current working
    directory is used.

--relative-to <path>
:   When `--relative-paths` is true, compiler-like output paths
    are printed relative to the specified `<path>`. If not
    specified, the current working directory is used.

--report-rws {true|false}
:   Default=`true`.

    When `true`, recovery warnings are always reported, regardless of other settings.
    This setting can be useful during interactive development, when code might not have been checked by the native compiler and can contain parse errors.

    When `false`, recovery warnings are reported only if otherwise enabled by the configuration.
    This setting is more useful for a case like CI/CD, when the native compiler is assumed to have been run, and it is more important to maintain
    consistency of results with central analysis.

@@<response_file>
:   Specify a response file that contains a list of additional command line
    arguments, such as a list of files for analysis. Each line in the file is
    treated as one argument, regardless of spaces, quotes, etc. The file is read
    using the platform default character encoding. Using a response file is
    recommended when the list of input XML files is long or automatically
    generated.

    Optionally, you can choose a different encoding, by specifying it after the
    first "@". For example:

    ```
    cov-run-desktop [OPTIONS] @UTF-16@my_response_file.txt
    ```

    You must use a supported Coverity encoding, listed under the
    `cov-build --encoding` option.

--restrict-all-files-regex `<regex>`>
:   When specified, any file whose name does not match `<regex>` will be ignored by analysis.
    This option may only be specified once, but `<regex>` may use the "|" operator to include multiple files.

    Note:
    `--ignore-all-files-regex` takes
    precedence if used in tandem with `--restrict-all-files-regex`.

--restrict-modified-file-regex `<regex>`>
:   When specified, only files whose name matches
    `<regex>` (and whose timestamp satisfies the
    modification date threshold) will be included in the analysis. This option
    may only be specified once, but `<regex>` may use the "|"
    operator to include multiple files.

    Note:
    `--ignore-modified-file-regex` takes
    precedence if used in tandem with `--restrict-modified-file-regex`.

--restrict-untracked-file-regex `<regex>`
:   Only untracked files that match the
    `<regex>`, and do not match
    `--ignore-untracked-file-regex`, will be analyzed.

--scm <scm_type>
:   Specifies the name of the source control management system. For this option to
    function correctly, your source files must remain in their usual locations in the
    checked-out source tree. If the files are copied to a different location after
    checkout, the SCM query will not work.

    Possible `scm_type` values:

    - GIT: `git`
    - Perforce: `perforce`
    - Plastic: `<plastic|plastic-distributed>`.

      Use `plastic` when working in a non- or partially-distributed Plastic
      configuration. Use `plastic-distributed` when working in
      a fully-distributed Plastic configuration.
    - SVN: `svn`

    For usage
    information for the `--scm` option, run `cov-extract-scm
    --help`.

    Note: The following commands or setup utilities must be run beforehand in order to
    successfully communicate with the SCM server:

    - `perforce`

      The environment variable `P4PORT` should be set to the
      value expected by the p4 tool.

--scm-param
:   Specify extra arguments to be passed to the SCM tool in a context-aware
    manner. For usage information of the `--scm` option, see
    `cov-extract-scm`.

--scm-project-root <scm_root_path>
:   Specifies a path that represents the root of the source control repository.
    Use this option when `cov-run-desktop` is being run from a
    directory other than the root of the source control repository. All paths
    returned by `--get-modified-files` will be relative to this
    path.

    This option behaves the same as `cov-extract-scm --scm-project-root`.
    See `cov-extract-scm` for additional details.

--scm-tool <scm_tool_path>
:   Specifies the path to an executable that interacts with the source control
    repository. If the executable name is given, it is assumed that it can be
    found in the path environment variable. If not provided, the command uses
    the default tool for the specified `--scm` system.

    This option behaves the same as `cov-extract-scm --scm-tool`.
    See `cov-extract-scm`
    for additional details.

--scm-tool-arg <scm_root_path>
:   This option has been deprecated. Instead of using `--scm-tool-arg
    arg1`, use `--scm-param tool_arg=arg1`.Specifies
    additional arguments that are passed to the SCM tool, specified in the
    `--scm-tool` option, that gathers the last modified
    dates. The arguments are placed before the command and after the tool. This
    option can be specified multiple times.

    This option behaves the same as `cov-extract-scm --scm-tool-arg`.
    See `cov-extract-scm` for additional details.

--set-new-defect-owner <boolean>
:   When true, and in connected mode, sets the owner for newly detected defects
    that exist locally as the current user. True by default.

    See also, `--set-new-defect-owner-limit`.

--set-new-defect-owner-limit <limit>
:   Set the limit on the number of defects to assign to the current user. If the
    number of discovered defects is more than the limit, then skip the
    assignment. The default limit is 100.

    Note:
    `--set-new-defect-owner` and
    `--set-new-defect-owner-limit` have no effect on the
    following platforms:

    - FreeBSD
    - Itanium

--set-new-defect-owner-to <user>
:   When used with `--set-new-defect-owner`, this specifies the
    user to whom any new defects will be assigned. The default is the current user.

    The specified `<user>` must already exist in the
    Coverity Connect database.

--setup
:   This option is intended as a single step to get a new user ready for Desktop Analysis.
    It creates an authentication key (if one has not already been
    created), runs the clean command, if applicable, and then captures a full
    build, if applicable. No build is captured if the
    `--skip-build` option is used with
    `--setup` or if the configured build command in
    `coverity.conf` is empty. The clean command, if
    configured, is only executed if a build is to be captured. Since it is
    common to capture a build, it is an error to leave the build command
    unspecified and run `--setup` without
    `--skip-build`.

--skip-build
:   Used only with `--setup` to omit capturing a build, even if one is specified in
    coverity.conf. This can be useful if your project contains compiled and
    interpreted code, but you intend only to analyze interpreted (buildless
    capture) code. This functionality can be made more permanent by specifying
    an empty build command in coverity.conf.
    See Coverity
    Desktop Analysis
    2026.6.0 User Guide for usage.

--sort <sort_spec>
:   Specifies the sort order for text output. The `<sort-spec>`
    accepts the values listed below. To sort on more than one attribute, you can
    use a non-empty, comma-separated list of values. Additionally, to specify
    ascending or descending sort order for any attribute, you can add
    `:a` or `:d` (respectively) directly after
    the attribute name. All attributes, except `cid`, are ordered
    in ascending order by default.

    The available sort attributes are:

    - `cid`: ID number assigned by Coverity Connect to each issue.
    - `occurrence`: The number of the occurrence among all
      those in the output set that have the same merge key.
    - `occurrences`: The total number of issue
      occurrences.
    - `mergeKey`: An internal identifier used to assign CIDs
      to issues. This is mainly useful when the CID is missing, either
      because the command is in disconnected mode or because the Coverity Connect
      server is a subscriber that is disconnected from its
      coordinator.
    - `checker`: The name of the checker that found this issue.
    - `file`: The complete path to the file that contains
      the issue.
    - `line`: The file's line number where the issue is located.
    - `function`: The name of the function that contains the issue.
    - `impact`: The issue's impact, as determined by
      Coverity Connect: High, Medium, or Low.
    - `category`: Description of the nature of the software issue.
    - `subcategory`: The sub-category of the defect reported
      by `<checker>`.
    - `present`: True if the issue is present in the
      specified snapshot, otherwise false.
    - `ownerLdapServerName`: The LDAP server of the defect owner.
    - `component`: The name of the component that contains this issue.
    - `firstDetected`: The date and time in which the issue
      was first detected by the analysis.
    - `classification`: The value of the issue's
      classification attribute.
    - `action`: The specified action to be taken on the issue.
    - `fixTarget`: Target milestone for fixing an issue.
    - `severity`: The value of the issue's severity attribute.
    - `legacy`: True if the issue is marked as a
      `legacy` issue, otherwise false.
    - `MISRACategory`: MISRA categories are sorted in order
      from least to most stringent: Advisory, Required, Mandatory. If this
      option is not specified, MISRA defects are not sorted by category.
    - `owner`: The user assigned to the issue.
    - `externalReference`: An internal identifier used by
      your company to track the issue.
    - `customTriage[<attribute>]`:
      The value of any custom triage attributes. Within the bracket-enclosed
      `<attribute>` name, use two consecutive right
      brackets (`]]`) to encode a single right bracket
      (`]`).

    For example, `--sort file,classification:d` will order the
    results first by ascending file name, then descending Classification.

--ssl
:   When present, use TLS/SSL encryption for all communication with Coverity Connect
    .
    This option has no effect in disconnected mode. This option is deprecated.

--stream <stream_name>
:   Specifies the Coverity Connect
    stream which contains the relevant snapshot
    and triage information. This option has no effect in disconnected mode.

--subcategory-regex <regex>
:   Filters the list of returned issues to include only those whose
    `checkerProperties` is not `null`, and
    where `checkerProperties.subcategoryShortDescription` matches
    the specified regular expression. See the "CheckerProperties" section in the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

--text-output <filename>
:   Write the text output to the specified file rather than writing it to the console.

--text-output-style <style>
:   Specifies the style of the text output. There are several accepted styles:

    - `oneline` - Each occurrence and event is written as a
      single line of output. This format works best with vi type
      editors.
    - `multiline` - Each occurrence and event is split
      across multiple lines. This format works best with Emacs editors.
    - `msvs` - Similar to `multiline`, but
      prints locations as `<file(line)>` instead of
      `<file:line>`; for use with Visual Studio.

    If unspecified, the `multiline` style is used by default.

--triage-attribute-not-regex <attrName> <regex>
:   Filters the list of returned issues to include only those whose `stateOnServer` is
    `null`, or whose `Triage` does not contain
    a key equal to the specified attribute name, or that does contain such a key
    but with a corresponding value that does not match the specified regular
    expression. See the "StateOnServer" section in the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

    For example, `--triage-attribute-not-regex "severity"
    "Minor"` will return only those issues that *do not*
    have a "severity" attribute with a value containing "Minor" as a
    substring.

--triage-attribute-regex <attrName> <regex>
:   Filters the list of returned issues to include only those whose `stateOnServer` is
    `null`, or whose `Triage` contains a key
    exactly equal to the specified attribute name and for which the
    corresponding value matches the specified regular expression. See the
    "StateOnServer" section in
    the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

    For example, `--triage-attribute-regex "classification" "Bug"`
    will return only those issues that have a "classification" attribute with the value, "Bug" (or containing the
    substring "Bug").

    The valid triage attributes are as follows:

    - `"action"`
    - `"classification"`
    - `"externalReference"`
    - `"fixTarget"`
    - `"legacy"`
    - `"owner"`
    - `"severity"`

--tu-pattern <pattern>
:   When specified, only those translation units which match
    `<pattern>` will be present in the analysis.

--upgrade <version>
:   Launches an assisted upgrade of Coverity Analysis to the version specified.
    The value of `<version>` should be the desired Coverity Analysis version number (2022.6.0 for example).
    This will download the required installer from Coverity Connect, run it, and provide instructions
    to invoke the new version. The existing installation with *not* be overwritten.

--url <path>
:   Allows you to connect to a Coverity Connect instance that has a context path in its
    HTTP(S) URL. You can use this option instead of the `--host`,
    or `--port` options. The `--url` option is
    provided to accommodate the use of a context path and to deal with setting
    up Coverity Connect behind a reverse proxy.

    Use HTTPS or HTTP to connect to a Coverity Connect HTTPS or HTTP port. For
    `http`, the default port is 80; for
    `https`, the default port is 443. For example:

    ```
    https://example.com/coverity
    ```

    ```
    https://cimpop:8008
    ```

    ```
    http://cim.example.com:8080
    ```

    Note: You may not use the commit:// scheme in the URL.

--use-reference-settings <boolean>
:   If true, `cov-run-desktop` will use the analysis settings
    downloaded from the reference snapshot. True by default.

--user <user_name>
:   Specifies the Coverity Connect user name.
    If unspecified, the default is the
    value for the environment variable, `COV_USER`, `USER`, or `USERNAME`, if
    specified. If none of these is specified, and
    "`settings.server.username`" is not specified in the
    `coverity.conf` file, then the `--user`
    option is required.

    This option has no effect in disconnected mode.

--whole-program
:   Some checkers, such as Application Security checkers and IDENTIFIER_TYPO, are
    only effective when analyzing all source files in the program. By default,
    these "whole-program" checkers are not available to
    `cov-run-desktop`.

    Specifying `--whole-program` allows
    `cov-run-desktop` to run whole-program checkers.

## Example 1

```
> cov-run-desktop file1.c file2.c
```

This will analyze file1.c and file2.c,
assuming a compilation of those files has previously been captured using
`cov-build`.

## Example 2

```
> cov-run-desktop file1.js
```

This will analyze file1.js.

## Example 3

```
> cov-run-desktop --analyze-scm-modified
```

This will query your SCM to find out which files have been modified locally and
analyze those.

## Example 4

```
> cov-run-desktop --dir idir --url http://my_server:8080 
                  --auth-key-file keyfile --stream my_stream \
                  --triage-attribute-regex Owner user1 \
                  --text-output-style oneline \
                  file1.c file2.c
```

This example analyzes both file1.c and
file2.c, obtains a reference snapshot from the
"`my_stream`" stream on `my_server:8080`,
authenticates using "keyfile" (which must have been previously
created using `cov-run-desktop`), filters the results for those
assigned to `user1`, and writes the defects to the console in the
`oneline` format, which uses one line of text for each defect and
event. Notice that many of the options specified here could instead have been put
into a coverity.conf file for convenience.
