---
title: "Miscellaneous"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/miscellaneous.html"
content_id: "un1GO4BLOwPRIOyH2A0sWQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:16.849273+00:00"
---

# Miscellaneous

`-batch`
:   Exit if error during command processing. Default:
    `-nbatch`.

`-define`
:   Define meta symbols for conditional compilation. Default:
    `-ndefine`.

`-help`
:   Present help information on screen. Default: `-nhelp`.

`-key`
:   A security key used internally for license authentication between Coverity
    and Coverity Fortran Syntax Analysis.

    To run Coverity Fortran Syntax Analysis either a valid Coverity Fortran
    Syntax Analysis license or a valid security key is required.

    Default: (none).

`-I`
:   Set directories of include files. When the first character is a
    ”`,`” or ”`:`” the current directory is
    also searched. Default: `-nI`.

`-idep` *d*
:   Generate a file with all referenced include files. Default:
    `-nidep`.

`-informative`
:   Show informative messages. Default: `-informative`.

`-log`
:   Show defines and undefines of meta variables. Default:
    `-nlog`.

`-report` *r*
:   Generate a report file *r*. If no filename is specified the filename is
    fck.rep. Default: `-nreport`.

`-rigorous`
:   Flag less robust and less portable code at the cost of more informative
    messages. Do not limit the number of messages for a statement or argument
    list. This option is useful when developing new code and to improve the
    quality of existing code. Do not use this option when analysing a project
    for the first time. See Syntax analysis, Verification of argument lists, and Verification of common blocks. Default:
    `-nrigorous`.

`-truncate`
:   Truncate names to 6 significant characters. Default:
    `-ntruncate`.

`-warnings`
:   Show warnings. Default: `-warnings`.

    Most of the miscellaneous options are global only and must be specified
    before the file-

    name of any source or library file. The `-informative` and
    `-warnings` options can also be

    specified locally to override the global setting. See The usage of analysis options.
