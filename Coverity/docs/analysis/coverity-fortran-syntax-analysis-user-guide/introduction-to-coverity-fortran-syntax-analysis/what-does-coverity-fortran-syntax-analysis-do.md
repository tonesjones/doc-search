---
title: "What does Coverity Fortran Syntax Analysis do?"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/what-does-coverity-fortran-syntax-analysis-do-.html"
content_id: "DNIerR_rv56fpUMZxM12hA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:43.344607+00:00"
---

# What does Coverity Fortran Syntax Analysis do?

Coverity Fortran Syntax Analysis verifies syntax by parsing the source program. This is
done as precisely as possible for the selected compiler emulation. The full Fortran 2015
syntax (which includes the Fortran 2008, Fortran 2003, Fortran 95, Fortran 90 and
FORTRAN 77 syn­tax) is supported. Many Fortran 2015 features are also supported.
Moreover most language extensions of many compilers are accepted. As an option, the
syntax can be verified for strict conformance to the FORTRAN 77, Fortran 90, Fortran 95,
Fortran 2003, Fortran 2008, or Fortran 2015 standard.

Cross-reference tables of all objects within program units are composed. Information and
warnings concerning the usage of all objects are provided.

The reference structure (call tree) of the program can be analyzed and presented.
Recursive references are traced and verified. The persistence of common-block objects
and global module data is verified.

The consistency of the entire program is verified by checking the category and type of
the procedures and the argument lists of all procedure references. Length, type and
structure of the common blocks specified in the various program units are compared.

Cross-reference tables of all procedures, common blocks, common-block objects, modules,
public module data, external I/O and include files over the program are composed.

Coverity Fortran Syntax Analysis can emulate a specific compiler by reading a
configuration file in which all types and language extensions to be supported are
enumerated. The `cov-run-fortran` command can be used to list the
available configurations; it provides guidance for selecting among them.

The global information of each program unit can be stored in library files. These can be
referenced and updated in subsequent Coverity Fortran Syntax Analysis runs. Using
libraries provides the means to test a subset of program units in the context of the
entire program. In this way, the code under active development can be analyzed more
rapidly while preserving the accuracy of the analysis.
