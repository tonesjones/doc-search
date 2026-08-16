---
title: "Tutorial"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tutorial.html"
content_id: "pBGjIvM9LLmbMqVR8kEpwg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:45.913756+00:00"
---

# Tutorial

Coverity Fortran Syntax Analysis is a sophisticated tool that permits fine-grained
control of its Fortran source code analysis through configuration files and command line
arguments. This chapter presents an overview of its operation using the
`cov-run-fortran` command.

The behavior of Coverity Fortran Syntax Analysis is governed in detail by its
configuration file. These behaviors include: the compiler emulation and enabled language
extensions, data sizes, standards conformance, which checks are performed and which
defects are issued.

Coverity Fortran Syntax Analysis currently provides over 70 compiler emulations in
pre-written configuration files, and supports easy selection among these through its
configuration selection options. Advanced users can also create a custom configuration
files and select one explicitly.

For a complete description of the user interface, see Operation. For
a precise clarification of the analysis, see Analysis.
