---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "EN5vjdvp5rXDD7nDvWhYmQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:20.762990+00:00"
---

# Options

--append
:   Append issues to any issues that exist in the intermediate directory.

    - If `--append` is absent, all of the issues in the
      intermediate directory are deleted before importing and analysis
      summaries will not be captured.
    - If `--append` is present, issues are not deleted.

    See also `--output-tag`.

--dir <intermediate_directory>
:   Path name to an intermediate directory that is used to store the results of
    the build and analysis. This option is required.

--<lang>
:   The value for lang may be `cpp`, `cs`, `dart`,
    `java`, `javascript`,
    `objc`, `php`, `python3`,
    `ruby`, `rust`, `scala`,
    `swift`, `text-files`, or
    `vb`.

    This option sets the source language and analysis domain in the output
    `error.xml` file.

    - For `cpp`, `cs`, and `java`, the corresponding
      domain is `STATIC_C`, `STATIC_CS`,
      `STATIC_JAVA`, or
      `DYNAMIC_JAVA`.
    - For all other source languages, the domain is
      `OTHER`.

    You can only import results for one source language per invocation of
    `cov-import-results`. However, you can use the
    `--append` option to add results attributed to other
    source languages before committing the results to Coverity Connect.

    See also, `--output-tag`.

--no-banner
:   Hide the version of Coverity Analysis and build number.

--output-tag <name>
:   Specifies a non-default location within the intermediate directory for the
    results of one or more imports. The name can be anything you choose, using
    characters allowed in file names. When specified *without* the `--append` option, prior results
    found in this location are replaced. When specified *with*
    `--append`, new results are added to the result set.

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
