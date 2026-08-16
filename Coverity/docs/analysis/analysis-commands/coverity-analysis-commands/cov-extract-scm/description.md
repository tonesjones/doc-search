---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "turnFuGBgdw_cRTJtWU86w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:44.619410+00:00"
---

# Description

Queries an SCM system for information of use to Coverity, Automatic Owner Assignment and
Fast Desktop. `cov-extract-scm` operates in one of two modes:
"Annotate" (the default mode) or "Code version".

Annotate mode
:   Retrieves the change data for each line of a file from the SCM system.
    This is the default mode.

Code version mode
:   Retrieves information regarding the code version the user has most
    recently checked out, updated from, or pulled. The information is either
    about the code version itself or the unpublished changes since the code
    version. (See 
    `cov-run-desktop`
    .)

    This mode is activated by the
    `--get-baseline-code-version` or
    `--get-modified-files` options.

**Using SCM argument tags**

`cov-extract-scm` issues a call to the SCM system to get information
about last modified dates for each line in a source file. On most systems, this command
is either "blame" or "annotate". For example:

```
git blame foo.c
```

In some cases, SCM systems have additional items that need to be specified in the command
to allow Coverity to get the appropriate information from the system. The
`--scm-param` option (as well as the deprecated
`--scm-tool-arg` and `--scm-command-arg` options)
allow for this functionality. Furthermore, the `--scm-tool` allows you to
specify an SCM tool that is non-standard or provides command output in a format that is
not easily parsed by Coverity. For example:

```
<tool> <tool-args> <command> <command-args> <coverity-mandated-flags> <target-file>
```

- `<tool>` is from the `--scm-tool` argument. If it is not
  specified, an appropriate default is used for the specified SCM type.
- `<tool-args>` and `<command-args>` are, respectively,
  lists of values associated with the `tool_arg` and
  `annotate_arg` keys passed to
  `--scm-param`.
- `<command>` is specific to each source control management system and can not
  be modified; typically a variation of blame or annotate. If the command is not
  specified, Coverity uses the appropriate command for the specified SCM type.
- `<coverity-mandated-flags>` are also specific to each source control
  management system and can not be modified.
- `<target-file>` is generated from the data passed in the
  `--input` option.

The `<command>` and `<coverity-mandated-flags>`
syntax for each supported SCM is as follows:

- `git`:

  `<tool-args> blame <command-args> -p <file>`
- `perforce`:
  1. `<tool-args> changes <command-args> -t -i
     <file>`
  2. `<tool-args> annotate <command-args> -q -I
     <file>#have`

  Any `<tool-args>`/`<command-args>` are passed to both
  commands.
- `plastic`:

  `<tool-args> annotate <command-args> <file>
  --format={owner}|{date}|{rev}`
- `plastic-distributed`:

  `<tool-args> annotate <command-args> <file>
  --format={owner}|{date}|{rev}`
- `svn`:

  `<tool-args> blame <command-args> -xml
  <file>`

## A note on Git superprojects

Git superprojects are unsupported by `cov-extract-scm`'s code
version mode (activated by the `--get-baseline-code-version` and
`--get-modified-files` options).

You might be able to work around this issue by creating a script to access
Git using submodules, and specify that script with the `--scm-tool`
option. This is an advanced use case, and should only be attempted by experienced
users.
