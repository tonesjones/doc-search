---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "CI62EEmmztUGAXXAWAfsWQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:54.482658+00:00"
---

# Options

--dir <intermediate_directory>
:   Path name to an intermediate directory that is used to store the results of
    the build and analysis. This option is required.

--emacs-style
:   Print a short version of the defect event with line numbers to
    `stdout`, formatted as gcc compiler warnings. This option
    is useful for integration into an editor such as Emacs.

    This option is equivalent to `--text-output-style
    multiline`.

--exclude-files <regex>
:   Omit defects from files that are in paths that match the specified regular
    expression. You cannot use this option multiple times in the same command
    line. You can use it with the `--include-files` option. If
    you use both options together, `--exclude-files` takes
    precedence over `--include-files`. For example, defects from
    a given file are excluded from the output in the case that the regular
    expressions both include and exclude the file.

    Example that excludes paths that contain both `/bar/` and
    `.c`:

    ```
    --exclude-files '/bar/.*\.c$'
    ```

    The example excludes the following file:

    `/foo/bar/test.c`

    The example does not exclude the following files:

    `/foo/test.c`

    `/foo/bar/test.cc`

    Note: The example above uses single quotes around the
    string value. However, your command interpreter might require double quotes
    (for example, `"/bar/.*\.c$"`).

--file <filename>
:   Only generate pages for errors in files containing
    `<filename>` as a substring of the full pathname.

--filesort
:   Sort rows by filename.

--function <func>
:   Only generate pages for errors in function `<func>`.

--functionsort
:   Sort rows by function name.

--html-output <directory>
:   Write the HTML results to the specified directory, and create this directory
    first if it does not exist.

    You must either specify a directory previously written by
    `cov-format-errors`, or a directory that is empty, or
    that does not yet exist.

--include-files <regex>
:   Use defects only from files that are in paths that match the specified
    regular expression. You cannot use this option multiple times in the same
    command line. You can use it with the `--exclude-files`
    option. If you use both options together, `--exclude-files`
    takes precedence over `--include-files`. For example, defects
    from a given file are excluded from the output in the case that the regular
    expressions both include and exclude the file.

    Example that includes `/foo/`:

    ```
    --include-files '/foo/'
    ```

    The example includes the following file:

    `/bar/foo/test.c`

    The example excludes the following file:

    `/bar/test.c`

    Note: The example above uses single quotes around the
    string value. However, your command interpreter might require double quotes
    (for example, `"/foo/"`).

--json-output-v10 <filename>
:   Writes `cov-format-errors` output to the specified file in JSON format (see "Desktop
    Analysis JSON output syntax" in the Coverity
    Desktop Analysis
    2026.6.0 User Guide). You can include either an
    absolute path or a path relative to the location in which you execute the
    command. If you want the file name to end in `.json`, you
    must include '`.json`' at the end of the filename string.

    The `--json-output-v10` option is the recommended JSON output
    option because it contains the most complete information. The
    `json-output-v1` through `json-output-v9`
    options are supported for backward compatibility.

--lang <language>
:   Write event messages in the specified language. Currently, the supported values are
    `en` (for English), `ja` (for Japanese),
    `ko` (for Korean), and `zh-cn` (for
    Simplified Chinese). The default language is English (`en`).

--misra-only
:   [Deprecated in 8.0] Using this option will result in an error.

--noX
:   Do not build cross-reference information. Normally, cross-reference
    information is built if the `-x` option is specified.

--output-tag <name>
:   Use this option if you used it when generating analysis results. See the
    --output-tag option to
    `cov-analyze`.

--preview-report <file>
:   Use this option to give triage information to `cov-format-errors`.
    This is reflected in the JSON output and can be used for filtering.
    The `<file>` parameter can be obtained by running
    `cov-commit-defects` with the
    `--preview-report-v2` option.

    --preview-report works for report versions 2 and higher.

--security-file <license file>

-sf <license file>
:   Path to a valid Coverity Analysis license file. If not specified, this path is given by the
    `security_file` tag in the Coverity configuration or by
    license.dat (located in the Coverity Analysis
    <install_dir>/bin directory). A valid license
    file is required to run the analysis.

--sort <sort_spec>
:   Specifies the sort order for text output. The `<sort-spec>` accepts the
    values listed below. To sort on more than one attribute, you can use a
    non-empty, comma-separated list of values. Additionally, to specify
    ascending or descending sort order for any attribute, you can add
    `:a` or `:d` (respectively) directly after
    the attribute name. All attributes, except `cid`, are ordered
    in ascending order by default.

    The available sort attributes are:

    - `cid`: ID number assigned by Coverity Connect to each
      issue.
    - `occurrence`: The number of the occurrence among all
      those in the output set that have the same merge key.
    - `occurrences`: The total number of issue
      occurrences.
    - `mergeKey`: An internal identifier used to assign CIDs
      to issues. This is mainly useful when the CID is missing, either
      because the command is in disconnected mode or because the Coverity
      Connect server is a subscriber that is disconnected from its
      coordinator.
    - `checker`: The name of the checker that found this
      issue.
    - `file`: The complete path to the file that contains
      the issue.
    - `line`: The file's line number where the issue is
      located.
    - `function`: The name of the function that contains the
      issue.
    - `impact`: The issue's impact, as determined by
      Coverity Connect: High, Medium, or Low
    - `category`: Description of the nature of the software
      issue.
    - `subcategory`: The sub-category of the defect reported
      by `<checker>`.
    - `present`: True if the issue is present in the
      specified snapshot, otherwise false.
    - `ownerLdapServerName`: The LDAP server of the defect
      owner.
    - `component`: The name of the component that contains
      this issue.
    - `firstDetected`: The date and time in which the issue
      was first detected by the analysis.
    - `classification`: The value of the issue's
      classification attribute.
    - `action`: The specified action to be taken on the
      issue.
    - `fixTarget`: Target milestone for fixing an issue.
    - `severity`: The value of the issue's severity
      attribute.
    - `legacy`: True if the issue is marked as a
      `legacy` issue, otherwise false.
    - `MISRACategory`: MISRA categories are sorted in order
      from least to most stringent: Advisory, Required, Mandatory. If this
      option is not specified, MISRA defects are not sorted by category.
    - `owner`: The user assigned to the issue.
    - `externalReference`: An internal identifier used by
      your company to track the issue.
    - `customTriage[<attribute>]`: The
      value of any custom triage attributes. Within the bracket-enclosed
      `<attribute>` name, use two consecutive right
      brackets (`]]`) to encode a single right bracket
      (`]`).

    For example, `--sort file,classification:d` will order the
    results first by ascending file name, then descending Classification.

--strip-path <path>

-s <path>
:   Strips leading directory names from file paths that
    appear in error messages and in references to your source files.

    The leading portion of the path is omitted if it matches a value
    specified by this option. For example, if the actual full path name of a
    file is /test/me/sourceFile.c, and
    `--strip-path /test` is specified, then the name
    attribute for the file becomes
    /me/sourceFile.c.

    The `--strip-path string` can include more than one
    directory name. Also, you can specify the `--strip-path`
    option multiple times. If more than one `--strip-path` is
    present, Coverity uses the longest of these. (Coverity does not attempt
    to use more than one of the specified path prefixes.)

    For example, suppose that you specify the following:

    ```
    --strip-path /a --strip-path /b --strip-path /b/c
    ```

    ... then `--strip-path` would condense paths in the
    following way:

    Table 1. Results of using `--strip-path`

    | Original path | Stripped path | Notes |
    | --- | --- | --- |
    | a/fname | /fname |  |
    | a/b/fname | /b/fname | In this case, /b was not a leading directory name in the path. |
    | b/fname | /fname |  |
    | b/c/fname | /fname |  |

    Important: We recommend using this option for a number of
    reasons:

    - Failure to use this option can result in poor Coverity Connect
      performance, triage issues related to component maps, an
      unnecessary increase the size of the Coverity Connect database,
      and even incorrect LOC counts.
    - This option shortens paths that Coverity Connect displays. It
      also allows your deployment to be more portable if you need to
      move it to a new machine in the future.
    - In addition, using this option during the analysis, rather than
      when committing the analysis results to Coverity Connect, can
      enhance end-to-end performance of the path stripping process
      itself.

    The `--strip-path` is available for several commands.

--text-output-style <style>
:   Prints a short version of the defect event with line numbers to
    `stdout`, formatted using the given style. There are
    several accepted styles:

    - `oneline` - Each occurrence and event is written as a
      single line of output. This format works best with vi type
      editors.
    - `multiline` - Each occurrence and event is split
      across multiple lines. This format works best with Emacs
      editors.
    - `msvs` - Similar to `multiline`, but
      prints locations as `<file(line)>` instead of
      `<file:line>`; for use with Visual Studio.

--title <title>
:   Specify a title for the generated index pages.

-X
:   Run the `cov-internal-build-xrefs` command first. Without this
    option, the identifiers in the source code will not be hyperlinked. When
    this has been done once on an intermediate directory, it does not need to be
    done again until the intermediate data changes. `-x`
    automatically implies `-X` unless `--noX` is
    also specified.

-x
:   Use cross-reference information when building static pages. Without this
    flag, the identifiers in the source code will not be hyperlinked. This
    option needs to be specified every time you want the generated pages to have
    cross-reference information.

## Filtering options

--category-regex <regex>
:   Filters the list of returned issues to include only those whose
    `checkerProperties` is not `null`, and
    where `checkerProperties.category` matches the specified
    regular expression. See the "CheckerProperties" section in the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

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

--impact-regex <regex>
:   Filters the list of returned issues to include only those whose
    `checkerProperties` is not `null`, and
    where `checkerProperties.impact` matches the specified
    regular expression. See the "CheckerProperties" section in the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

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

--occurrences <range>
:   When there are multiple occurrences for a given defect, each instance is
    given an occurrence number, O, from 1 to *N*. The
    `--occurrences <range>` option, specifies the
    valid values for O.

    Ranges are as described for the `--cid` option.

--ownerLdapServerName-regex <regex>
:   Filters the list of returned issues to include only those whose `stateOnServer` is
    `null`, or whose `ownerLdapServerName`
    matches the specified regular expression. See the "StateOnServer" section in
    the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

--subcategory-regex <regex>
:   Filters the list of returned issues to include only those whose
    `checkerProperties` is not `null`, and
    where `checkerProperties.subcategoryShortDescription` matches
    the specified regular expression. See the "CheckerProperties" section in the Coverity
    Desktop Analysis
    2026.6.0 User Guide.

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

## Shared options

--debug

-g
:   Turn on basic debugging output.

--ident
:   Displays the version of Coverity Analysis and build number.

--info
:   Displays certain internal information (useful for debugging), including the
    temporary directory, user name and host name, and process ID.

--tmpdir <tmp>

-t <tmp>
:   Specifies the temporary directory to use.

    - On UNIX, the default is `$TMPDIR`, or
      `/tmp` if that variable does not exist.
    - On Windows, the default is to use the temporary directory specified
      by the operating system.

--verbose <0, 1, 2, 3, 4>

-V <0, 1, 2, 3, 4>
:   Set the detail level of command messages. Higher is more verbose (more
    messages). Defaults to 1.
