---
title: "Basic Operation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/basic-operation.html"
content_id: "Gx0Jkgxp8rNYhBjiEl1ITg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:46.558980+00:00"
---

# Basic Operation

Coverity Fortran Syntax Analysis requires three pieces of information to run
correctly:

1. where to write the results;
2. which configuration (compiler emulation) to use; and
3. the names of one or more files to analyze.

Coverity Fortran Syntax Analysis results are written to the intermediate directory
specified by the `--dir` option.

The configuration is determined by specifying configuration options
(`--platform`, `--vendor`, `--version`,
`--level`) sufficient to identify the desired one uniquely. If the
choice is not unique, the first candidate in the list is used, but a warning message is
printed. If no configuration options are specified at all, then the generic
configuration file “f95” is used by default. If no choices match the configuration
selection criteria, then an error is issued.

The name of the desired configuration file can also be specified explicitly using the
`--configuration` option. This option makes it possible to use custom
configuration files.

The names of files to be analyzed are simply listed on the command line. Analysis options
and filenames must follow control options on the command line. The command parser can
usually determine where the list of control options ends and the list of analysis
options and filenames begins. However, since some cases are ambiguous, it is recommended
practice to always place the `--` delimiter between the list of control
options and the list of analysis options and filenames.

A minimal command line to run `cov-run-fortran` looks like:

```
cov-run-fortran --dir idir -- test.f
```

assuming that `test.f` exists in the current working directory. The
corresonding output is

```
Coverity Fortran Syntax Analysis version 2018.01 on Linux 3.13.0-133-generic x86_64
[STATUS] Reading Fortran configuration files.
[STATUS] Selecting configuration file.
[WARNING] No configuration specified.
  Using generic configuration f95
[STATUS] Running Fortran analysis
[STATUS] Converting results
[STATUS] Importing to intermediate directory
test.f
Successfully imported 1 source files.
[STATUS] cov-run-fortran finished
```

indicating that `cov-run-fortran` ran successfully and imported the
defects from one source file.
