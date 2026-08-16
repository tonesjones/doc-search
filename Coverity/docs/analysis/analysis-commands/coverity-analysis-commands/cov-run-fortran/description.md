---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "w4Z4IV2sek8~a1lVDSEgxw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:14.511476+00:00"
---

# Description

The `cov-run-fortran` command runs the Coverity Fortran Syntax Analysis tool
on user's code and puts the output into a form compatible with Coverity Connect. The
`cov-commit-defects` command can then be used to upload the results
to Coverity Connect. The options described in this command reference are of two kinds:
Control and Analysis. Control options are interpreted by the
`cov-run-fortran` command and used to control Coverity Fortran Syntax Analysis
and the subsequent translation. Analysis options are passed through to
Coverity Fortran Syntax Analysis verbatim. This command reference provides an overview
of the analysis options. Refer to the Coverity Fortran Syntax Analysis User Guide for
additional details.

Coverity Fortran Syntax Analysis is a static analysis tool designed to give detailed
feedback on syntax and usage that is not compatible with the selected compiler and
language level. Coverity Fortran Syntax Analysis supports many current and legacy
configurations through pre-written compiler configuration files. It is especially useful
for porting and regularization efforts, since compiler incompatibilities can be
discovered by selecting the target compiler's configuration file.

The control options simplify the selection of a configuration file, and specify the
directories where the intermediate and output files are to be stored. The analysis
options indicate which source and library files to process and control other features of
the Coverity Fortran Syntax Analysis tool.

The main output of `cov-run-fortran` is the file
FC.errors.xml, which is written into the
output section of the intermediate directory specified by the
`--dir` option. The emit-db is updated with
filename and error summary information.

The exit code of `cov-run-fortran` is 0 when the analysis completes
successfully and 2 or greater if there is an error.
