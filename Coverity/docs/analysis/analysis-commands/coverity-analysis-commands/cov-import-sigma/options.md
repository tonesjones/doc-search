---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "5Vy7uoRuddjYKiuL5x5HsA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:27.988213+00:00"
---

# Options

--append
:   Append issues to any issues that exist in the intermediate directory.

    - If `--append` is absent, all of the issues in the
      intermediate directory are deleted before importing and analysis
      summaries will not be captured.
    - If `--append` is present, issues are not deleted.

    See also `--output-tag`.

--dir <dir_name>
:   The name of the folder where cov-import-sigma is going to
    create an intermediate directory for Sigma output. This intermediate
    directory will not be deleted because it will be used to commit results to
    Coverity Connect.

--sigma-result <sigma-output.json>
:   The name of the file holding Sigma output results. This file would have been
    created using the --format coverity option to the
    sigma analyze command to produce a format that can be
    consumed by Coverity Connect.

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
