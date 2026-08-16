---
title: "Introduction to Coverity Fortran Syntax Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/introduction-to-coverity-fortran-syntax-analysis.html"
content_id: "3ktzvDhKIrKGP66GuWkQDw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:42.682874+00:00"
---

# Introduction to Coverity Fortran Syntax Analysis

Coverity Fortran Syntax Analysis is a Fortran program development, conversion,
maintenance, verification and documentation tool. It parses Fortran programs, verifies
the syntax and composes cross-reference tables. It analyzes separate program units as
well as the program as a whole.

Coverity Fortran Syntax Analysis has been integrated into the Coverity Analysis
work­flow, permitting the coding errors it detects to be managed and displayed through a
Coverity Platform instance.

In that workflow, the Fortran sources constituting a program are analyzed using

`cov-run-fortran` and written to the specified intermediate directory.
Following that, the analysis results may be uploaded to Coverity Platform using
`cov-commit-defects`.

Coverity Fortran Syntax Analysis does not use `cov-build`; therefore it
does not perform a build capture, nor does it perform a filesystem capture. It is
necessary to specify the files to be analyzed explicitly on the command line.
