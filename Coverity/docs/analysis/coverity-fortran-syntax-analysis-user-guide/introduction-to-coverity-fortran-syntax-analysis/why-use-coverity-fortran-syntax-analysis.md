---
title: "Why Use Coverity Fortran Syntax Analysis?"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/why-use-coverity-fortran-syntax-analysis-.html"
content_id: "k6GObocjbRu5n6YJS2sw_A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:43.985615+00:00"
---

# Why Use Coverity Fortran Syntax Analysis?

Although your Fortran compiler verifies the syntax of the input source code, this check
is in general far from complete. Coverity Fortran Syntax Analysis, on the other hand,
performs this verification as completely as possible. More importantly, Coverity Fortran
Syntax Analysis verifies the program as a whole. Procedure types, argument lists and
common blocks are all verified for consistency program-wide.

In active development, Coverity Fortran Syntax Analysis can save time and annoyance
because coding errors are detected as early as possible. Coverity Fortran Syntax
Analysis is also very useful in porting efforts: Since it can emulate a variety of
target com­pilers, it can ensure compatibility with many compilers using a single
machine to run the analyses.

As an option, Coverity Fortran Syntax Analysis checks the conformance of your pro­gram to
the FORTRAN 77 [1], the Fortran 90 [2, 3], the Fortran 95 [4], the Fortran 2003 [5], the
Fortran 2008 [6], or the Fortran 2015 [7] standard. Although most compilers have an
option to reveal deviations from the standard, they generally perform this in a limited
way. Coverity Fortran Syntax Analysis, however, reveals almost all deviations which can
be detected during static analysis. This is of utmost value when developing software
that is intended to be portable.

In addition to the stream of defects that can be uploaded to a Coverity Platform
instance, Coverity Fortran Syntax Analysis produces auxiliary outputs that can be useful
for program analysis:

- an index of program units and module procedures,
- a reference structure (call tree) of all subprograms,
- a dependency tree of all modules, and
- cross-reference tables of procedures, common blocks, common-block objects, modules,
  public module data, external I/O and include files.

Coverity Fortran Syntax Analysis can emulate most language extensions supported across a
variety of compilers. When you tell Coverity Fortran Syntax Analysis to emulate the
compiler of the target system you can use it as a code conversion and porting aid.

The global information of the various program units can be stored in library files. You
can verify newly developed or changed program units in the context of the entire program
by specifying the library files containing the global program information without
analyzing all source code anew. In this way you can develop programs in a modular way
without the risk of creating inconsistencies in the subprogram interfaces.
