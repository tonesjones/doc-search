---
title: "Analyzing a single source file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analyzing-a-single-source-file.html"
content_id: "RmHDS7naDKa7aHg9Bkz67A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:47.207298+00:00"
---

# Analyzing a single source file

It is advisable to start simply by analyzing a single source file. Choose a source file
containing a program unit that does not use modules, or one that contains all the
referenced modules. In this way you can verify the settings and experiment using some of
the options.

When using Coverity Fortran Syntax Analysis in command line mode an example of the
analysis of a single source file is:

```
cov-run-fortran --dir idir -- test
```

The default filename extension is .f.

You may need to specify some analysis options to indicate the source form and specify the
path of the include files (if these are not in the path of the source file) before you
get the results you expect. These options are:

-allc
:   Analyze all columns of the source input records (beyond column 72 for fixed source
    form).

-cntl *c*
:   Allow a maximum of *c* continuation lines in a statement (beyond 19 for fixed source
    form).

-ff
:   Source code input is in free source form. (This is the default for source
    files with a filename extension of .f90, .f95, .f03, or f08.)

-define
:   Define meta symbols for conditional compilation. The specified symbols must
    be separated by a ”`;`”.

-I
:   Set directories of include files. The items in the list must be separated by a
    ”`;`”.

These options must be specified before the source file they are intended to affect. If
specified before the first in a list of source files, they affect all source files
(globally). For example:

```
cov-run-fortran --dir idir -- -allc -cntl 100 -ff -define x86 source.f
```

The negative form of an option is the option preceded by an `n`, e.g.
`-nff` indicates fixed form.

If the source file contains more than one program unit, they are analyzed in the order in
which they appear, and a global analysis is performed in addition to the program unit
analysis.
