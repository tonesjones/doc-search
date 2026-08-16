---
title: "Options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/options.html"
content_id: "guUhFur5ilGoFphxpwMXMw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:49.418353+00:00"
---

# Options

--dir <intermediate_directory>
:   Path name to an intermediate directory that is used to store the results of
    the build and analysis. This option is required.

--no-triage-filters
:   Calculate owner assignment for all defects whose merge key is present in
    the preview report, regardless of the triage values. By default, owner
    assignment is only calculated for defects whose current triage values
    satisfy the following conditions:

    - The Owner attribute is unset
    - The Classification attribute is Unclassified, Pending, Bug, or
      Untested.

    This option is useful, for example, to calculate owner assignment for
    comparison with owner assignments that have already been made manually
    in Coverity Connect to evaluate the accuracy of the owner assignment
    rules. In this case, you must use the
    `--no-triage-filters` option.

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

--owner-assignment-rules <RULE1>[,<RULE2>,...,<RULEn>]
:   Determines an owner by consulting history from the SCM system. If this
    option is specified, you must include at least one rule. Multiple rule
    options must be comma-separated. If this option is not specified, then
    all rules are applied. In the descriptions below, main event refers the
    event that Coverity Connect first highlights when the user clicks on the
    defect in the defects list.

    The rules are:

    - `file` - Queries the SCM for the person that most
      recently modified the file containing the main event, and that
      SCM user is the chosen owner.
    - `line` - Queries the SCM for the person that most
      recently modified the particular line of code that has the main
      event.
    - `function` - If there is a function associated
      with the main event, then `cov-blame` queries
      the SCM for the person who most recently modified that function.
      Otherwise, this rule acts the same as the file rule.
    - `top_events` - Retrieves all of the lines of code
      that contain a non-interprocedural defect event in the issue,
      then returns the person that most recently modified any of those
      lines.
    - `all_events` - Similar to the
      `top_events` rule, except that it also
      considers all interprocedural defect events.
    - `all_functions` - Combines the
      `function` and
      `all_events` rules to query for the person
      who most recently modified the functions associated with all the
      defect events. If there are no functions at all, this rule
      behaves like the `all_files` rule.
    - `all_files` - Combines the
      `file` rule with the
      `all_events` rule to query for the person
      who most recently modified the files containing all of the
      defect events.
    - `default_component_owner` - Reports the issue's
      owner as the designated default owner for the component in
      Coverity Connect. The output of this rule, unlike all of the
      other rules, is a Coverity Connect user, and not an SCM user.
      This rule can yield no assignment if a component does not have a
      default owner.

--preview-report <filename>
:   Specifies the path and name of the preview report generated by
    `cov-commit-defects
    --preview-report-v2` or
    `cov-commit-defects
    --preview-report-v3`. This option is
    required.

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
    When this is used, all file paths that are used to gather information are
    interpreted as relative to this project-root path.

    For usage information, see `cov-extract-scm`.

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

--stop-after <limit>
:   Stops computing owner assignments after a certain number of defects, as
    specified in `<limit>`. This allows you to quickly
    experiment with rules without waiting for a long time for each defect to
    be assigned an owner.

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
