---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "_ry6tUkpTWRvcdsginJ28A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:30.716997+00:00"
---

# Description

The `cov-analyze` command runs checkers on captured code in an
intermediate directory and stores analysis results in that directory, which is specified
with `--dir`. This command typically follows 
`cov-build`
 and precedes 
`cov-commit-defects`
 invocations on the same intermediate directory. Though
`cov-analyze` does not report defects in Java and .NET bytecode,
nor in some forms of source code not written by a person, the command does run an
analysis of them for the benefit of finding interprocedural defects in editable source
code.

A log file (analysis-log.txt) with information about the checkers
used in the analysis, including notices of crashes, is located in the following
directory: <intermediate_directory>/output

Note:

If you get a fatal `No license
found` error when you attempt to run this command, you need to make sure
that license.dat was copied correctly to <install_dir>/bin.

On some Windows platforms, you might need to use
administrative privileges when you copy the Coverity license to
<install_dir>/bin. Due to file
virtualization in some versions of Windows, it might look like
license.dat is in <install_dir>/bin when it is not.

Typically, you can set the administrative permission
through an option in the right-click menu of the executable for the command interpreter
(for example, Cmd.exe or Cygwin) or Windows Explorer.
