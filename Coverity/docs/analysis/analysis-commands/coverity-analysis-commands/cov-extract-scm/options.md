---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "U66hhzQqq6JNpdObKcbjHQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:45.256303+00:00"
---

# Options

--error-threshold <percentage>
:   Sets the percentage of successful extractions required for
    `cov-extract-scm` to exit with a success return code
    (`0`). If the extraction rate is below this threshold,
    `cov-extract-scm` will print a warning and exit with
    return code `8`. The default percentage is
    `80`.

--get-baseline-code-version
:   (Code version mode only)

    This switch indicates that instead of performing its usual function of
    querying the SCM for "annotate" information, the tool shall write to its
    `--output` file some information about the code version
    that the user has most recently checked out, updated from, or pulled.

    The output shall be a JSON file using ASCII character encoding and
    platform-native line endings. It consists of a single JSON object with a
    single attribute called "date" using `YYYY-MM-DDThh:mmZ`
    syntax.

    Example output file:

    ```
    {
      date: "2013-12-18T15:34Z"
    }
    ```

--get-modified-files
:   (Code version mode only)

    This switch also indicates to suppress normal processing and instead retrieve
    the set of files with unpublished local changes. These are the files with
    differences relative to the version of the code indicated by
    `--get-baseline-code-version`.

    The output shall be written to the `--output` file as JSON
    using ASCII character encoding and "\u" escapes in strings as needed to
    represent non-ASCII characters. The output is a single JSON object with two
    attributes, "`modified_files`" and
    "`untracked_files`". The former are files that the SCM
    knows about and have been modified from their baseline version. The latter
    are files that are not checked in to the SCM and are also not excluded by
    SCM "ignore" filtering (like `.gitignore`). Each is an array
    of strings representing the file names. File names have their letter case
    preserved and use the platform native syntax for file names and directory
    separators. The file names shall be relative to the repository root, which
    is assumed to be the current directory unless a different root is specified
    as a command line option with `--scm-project-root`.

    Example output file (using Windows separators):

    ```
    {
      modified_files: [
        "utilities\\cov-format-errors\\cov-format-errors.cpp",
        "Makefile"
      ],
      untracked_files: [
        "analysis\\cov-run-desktop\\some-new-file.cpp",
        "analysis\\cov-run-desktop\\some-new-file.hpp",
        "name with \u1234 non-ASCII character"
      ]
    }
    ```

--input <input_file>
:   (Annotate mode only)

    Specifies the path to a file that contains information about the files that
    gather last modified dates. The format of this file is the same as the
    output of the `list-scm-unknown` option of
    `cov-manage-emit`.

--log <log_path>
:   Specifies the path to a file to which output from the
    `cov-extract-scm --scm-tool` executable and other
    recoverable errors are written.

--ms-delay <int>
:   Specifies a delay in milliseconds between calls to the underlying SCM. This
    is useful for preventing a denial of service situation.

--output <output_path>
:   Specifies the path to a file to which the output data is written to. The format of this output
    (in Annotate mode) is used as input to the
    `add-scm-annotations` subcommand for
    `cov-manage-emit`. See
    `--get-baseline-code-version` and
    `--get-modified-files` for the format of this output in
    Code version mode.

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

--scm-command-arg <command_arg>
:   (Annotate mode only)

    This option has been deprecated. Instead of
    using `--scm-command-arg arg1`, use `--scm-param
    annotate_arg=arg1`. Specifies additional arguments that are
    passed to the command that retrieves the last modified dates. The arguments
    are placed after the command and before the target file. This option can be
    specified multiple times.

--scm-param
:   Specifies additional arguments that are passed to the SCM tool in a
    context-aware manner. The value passed to `--scm-param` must
    have the format `key=arg`; the key specifies what the arg is
    to be used for. For example, `--scm-param tool_arg=--foo`
    causes the argument `--foo` to be added to the
    `<tool-args>` list, and `--scm-param
    annotate_arg=--bar` causes the argument `--bar`
    to be added to the `<command-args>` list. Specific SCMs
    may accept other keys, if they require more information.

--scm-project-root <root_path>
:   Specifies a path that represents the root of the source control
    repository.

    In Code version mode, this option allows `cov-extract-scm`
    to run from a directory other than the root of the source control
    repository. All filenames returned by `--get-modified-files`
    are relative to this path.

--scm-tool <tool_path>
:   Specifies the path to an executable that interacts with the source control
    repository. If the executable name is given, it is assumed that it can be
    found in the path environment variable. If not provided, the command uses
    the default tool for the specified `--scm` system.

    For usage information, see `cov-extract-scm`.

--scm-tool-arg <tool_args>
:   This option has been deprecated. Instead of using `--scm-tool-arg
    arg1`, use `--scm-param tool_arg=arg1`. Specifies
    additional arguments that are passed to the SCM tool, specified in the
    `--scm-tool` option, that gathers the last modified
    dates. The arguments are placed before the command and after the tool. This
    option can be specified multiple times.

    For usage information, see `cov-extract-scm`.

## Shared options

--debug

-g
:   Turn on basic debugging output.

--ident
:   Displays the version of Coverity Analysis and build number.

--verbose <0, 1, 2, 3, 4>

-V <0, 1, 2, 3, 4>
:   Set the detail level of command messages. Higher is more verbose (more
    messages). Defaults to 1.
