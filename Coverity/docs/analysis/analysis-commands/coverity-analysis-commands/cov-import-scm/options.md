---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "Pmz~6HYIMFT7npXqcagw0g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:24.050411+00:00"
---

# Options

--dir <intermediate_directory>
:   Specifies the intermediate directory that is used to store the emit
    repository.

--error-threshold <percentage>
:   Sets a threshold for the percentage of successful extractions (from
    `cov-extract-scm`) below which this import command
    (`cov-import-scm`) will display a warning, indicating
    the need to check for a potential problem. Note, however, that
    `cov-import-scm` will attempt to add all successful
    extractions to the emit. The default percentage is `80`.

--filename-regex <regex>
:   Allows finer control over SCM information gathering. Information is gathered
    only for filenames that match the regex. Any files that do not match are
    skipped. This is beneficial when there are specific locations where code is
    known to exist under SCM control and other locations where it is not (such
    as system headers).

--log <log_path>
:   Specifies the path to a file to which output from the
    `cov-extract-scm --scm-tool` executable and other
    recoverable errors are written.

--ms-delay <int>
:   Specifies a delay in milliseconds between calls to the underlying SCM. This
    is useful for preventing a denial of service situation.

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
:   This option has been deprecated. Instead of
    using `--scm-command-arg arg1`, use `--scm-param
    annotate_arg=arg1`. Specifies additional arguments that are
    passed to the command that retrieves the last modified dates. The arguments
    are placed after the command and before the target file. This option can be
    specified multiple times.

    For usage information, see `cov-extract-scm`.

--scm-param
:   Specifies additional arguments that are passed to the SCM tool in a
    context-aware manner.

    For usage information, see `cov-extract-scm`.

--scm-project-root <root_path>
:   Specifies a path that represents the root of the source control repository.
    When this used, all file paths that are used to gather information are
    interpreted as relative to this project-root path. For usage information,
    see
    `cov-extract-scm`.

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
