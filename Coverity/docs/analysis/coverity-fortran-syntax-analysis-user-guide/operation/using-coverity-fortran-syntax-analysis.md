---
title: "Using Coverity Fortran Syntax Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-coverity-fortran-syntax-analysis.html"
content_id: "VoTb9x7b65VDi0pplnBO4g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:59.462210+00:00"
---

# Using Coverity Fortran Syntax Analysis

The Coverity Fortran Syntax Analysis analyzer can be started in a command shell by typing
the

```
cov-run-fortran
```

command
with options, source and library filenames. The command line has the following form

```
cov-run-fortran [control options] – [global options] file [[local options] file ...]
```

where `file` is the name of a Fortran source file or Coverity Fortran
Syntax Analysis library file to be analyzed. All source files must be specified before
any library file. Wild cards can be used in the filename specifications.

Analysis options specified before the first source filename are global and apply to the
whole analysis. Options specified within the list of source files are local and apply to
the next source file only. See The usage of analysis options.
Filenames must be separated by blanks. By default, a file is assumed to be a source
input file.

When a filename is preceded by the `-l` option, and the filename does not
have the suffix of a source or library file, it is considered to be a list file. If a
filename has a `.flb` suffix or it is preceded by one of the library
options, it is considered to be a Coverity Fortran Syntax Analysis library file. See
Specifying a list file and Specifying a library file for more information.

Default suffixes:

- `.f` for a source input file
- `.lst` for a list file
- `.flb` for a library file

The default suffixes for source input and include files depend on the compiler emulation
chosen. See the sections on compiler emulations and supported Fortran syntax for more
information.
