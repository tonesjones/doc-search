---
title: "Running Fortran Syntax Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-fortran-syntax-analysis.html"
content_id: "DNFTiuVWfUbxMR4hMq6jhg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:12.384381+00:00"
---

# Running Fortran Syntax Analysis

Coverity Fortran Syntax Analysis provides Fortran syntax analysis and portability
checking. It can emulate the parsing behavior of many current and legacy compilers. In
addition, it can verify compliance of the source code with supported Fortran language
standards.

Coverity Fortran Syntax Analysis is a standalone tool that performs the file capture and analysis
in one step. Source files to be analyzed, include paths and symbol definitions must be
listed on the `cov-run-fortran` command line. The analysis expands
`INCLUDE` statements and performs limited C preprocessor
`cpp` emulation to interpret the sources.

Note: Keep the following in mind:

- Coverity
  Fortran Syntax Analysis will attempt to analyze all of the files
  listed as sources on the command line. Only valid Fortran sources should be
  listed.
- Coverity
  Fortran Syntax Analysis is sensitive to the compiler emulation and
  language level chosen. Make sure to select these appropriately. Valid syntax may
  be flagged as invalid if either the free-form `-ff` option or
  fixed-form `-nff` option is specified incorrectly.

Once the Fortran syntax analysis has completed, you can upload the results to Coverity Connect,
using the `cov-commit-defects` command.

For more information, see the `cov-run-fortran`
command entry in the Coverity 2026.6.0 Command Reference.

**Fortran analysis workflow example**

- Analyze all files in the current working
  directory:

  ```
  > cov-run-fortran --dir=idir --vendor=intel --version=14 -- *.f
  > cov-commit-defects --dir=idir ...
  ```
