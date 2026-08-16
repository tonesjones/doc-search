---
title: "Fortran inputs"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/fortran-inputs.html"
content_id: "zoz__HL0~19PJIfBpb6Leg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:15.148344+00:00"
---

# Fortran inputs

Coverity Fortran Syntax Analysis analyzes the specified Fortran source files in two
phases, a local phase and a global phase. During the local phase, it analyzes each file
separately and emits defects as it finds them. It also collects symbol information to be
used during the global analysis phase. During the global phase, it uses the stored
information to report on issues that span program unit boundaries.

Coverity Fortran Syntax Analysis respects C-style preprocessor (i.e.
`cpp`) directives and `INCLUDE` statements to determine
when source code is being imported. Coverity Fortran Syntax Analysis emulates the target
compiler by importing those files in the expected manner. Coverity
Fortran Syntax Analysis resolves paths relative to the current working directory; thus, the environment
in which `cov-run-fortran` is run should mimic the actual compilation
environment as closely as possible.

Coverity Fortran Syntax Analysis also respects `USE` statements appearing
in the code and uses these to import symbols and interfaces from the modules so named.
Modules must be analyzed in a bottom-up order, so that types, symbols and interfaces
imported from a given module can be checked for consistency at their point of use.
Coverity Fortran Syntax Analysis automatically calculates and uses a bottom-up
processing order. However, it is still necessary to list in the
`cov-run-fortran` command the source files and/or library files
containing all of the modules used.

Coverity Fortran Syntax Analysis library files provide a summary of the interface information
extracted from module and non-module source files. They perform the dual purpose of
fulfilling module references and providing information about intrinsic or library
functions provided by the compilation environment (compiler and OS). Multiple library
files can be referenced in one `cov-run-fortran` invocation. See the
Coverity Fortran Syntax Analysis User Guide for more information on creating and
using libraries.

As with other Coverity analysis tools, `cov-run-fortran` will accept some or
all of its input from response files. Command line arguments of the form
`@@<response_file>` cause the command interpreter to read options
from the named response file.
