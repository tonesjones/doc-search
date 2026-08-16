---
title: "Program-unit analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/program-unit-analysis.html"
content_id: "9BZMc845Bm0TPjVpoqkz~Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:14.272115+00:00"
---

# Program-unit analysis

Program-unit analysis options affect the analysis that can be applied to individual
program units, These are generally termed "intraprocedural" analyses, even though
Fortran contains some program-unit types that are not executable. Program-unit analysis
options can be specified with per-file granularity.

Options which are specified before any source file are global and in effect for the entire
analysis. Options appearing within the source file list are local and affect only the
analysis of the next file. Local options override the global options temporarily. After
the analysis of that file completes, all options revert to their global values. See
The usage of analysis options.

`-allc`
:   Analyze all columns of the source input records. If negated and the
    `-ff` option is not in effect, only columns 1 to 72
    (after expansion of tabs) will be analyzed. See also the sections Interpretation of source code records and Lay-out of source code listing in the Analysis chapter. Default:
    `-nallc`.

`-acqintf`
:   Use the interface of the previously analyzed subprogram with an implicit
    interface, if present, to verify the references during subprogram analysis.
    If negated the actual argument lists of the references in the various
    subprograms will only be verified during global program analysis. You need
    to specify this option if you analyse an unrelated set of program units, or
    if you have modified interfaces and have not yet updated the Coverity
    Fortran Syntax Analysis libraries containing the interfaces. Default:
    `/nacqintf`.

`-cntl` *C*
:   Allow a maximum of *C* continuation lines in a statement. The value of
    *C* must be less than

    or equal to 999. The default depends on the compiler emulation
    chosen.

`-cpp`
:   For files with a filename extension starting with .F, the default is
    `/cpp`. For all other files, the

    default is `/ncpp`.

`-cond`
:   Process debug (`D`) lines. Default:
    `-ncond`.

`-declare`
:   Present a warning for all variables that have not been explicitly declared in
    a type statement. Default: `-ndeclare`.

`-dp`
:   Map all default reals to double precision and double precision to REAL(16).
    Map all default complex objects to double complex and all double complex to
    COMPLEX(16). See also `-r8`. Default:
    `-ndp`.

`-externals`
:   Flag referenced external procedures which have not been declared external.
    Default: `-nexternals`.

`-f77`
:   Validate the syntax for conformance to the FORTRAN 77 standard. All
    nonstandard syntax will be flagged. Note that this option does not enable
    FORTRAN 77 syntax by itself. To en­able FORTRAN 77 syntax a configuration
    file of a FORTRAN 77 compiler must be selected. Default:
    `-nf77`.

`-f90`
:   Validate the syntax for conformance to the Fortran 90 standard. All
    nonstandard syntax will be flagged. Note that this option does not enable
    Fortran 90 syntax by itself. To enable Fortran 90 syntax a configuration
    file of a Fortran 90 compiler must be selected. Default:
    `-nf90`.

`-f95`
:   Validate the syntax for conformance to the Fortran 95 standard. All
    nonstandard syntax will be flagged. Note that this option does not enable
    Fortran 95 syntax by itself. To enable Fortran 95 syntax a configuration
    file of a Fortran 95 compiler must be selected. Default:
    `-nf95`.

`-f03`
:   Validate the syntax for conformance to the Fortran 2003 standard. All
    nonstandard syntax will be flagged. Note that this option does not enable
    Fortran 2003 syntax by itself. To en­able Fortran 2003 syntax a
    configuration file of a Fortran 2003 compiler must be selected. Default:
    `-nf03`.

`-f08`
:   Validate the syntax for conformance to the Fortran 2008 standard. All
    nonstandard syntax will be flagged. Note that this option does not enable
    Fortran 2008 syntax by itself. To en­able Fortran 2008 syntax a
    configuration file of a Fortran 2008 compiler must be selected. Default:
    `-nf08`.

`-f15`
:   Validate the syntax for conformance to the Fortran 2015 standard. All
    nonstandard syntax will be flagged. Note that this option does not enable
    Fortran 2015 syntax by itself. To en­able Fortran 2015 syntax a
    configuration file of a Fortran 2015 compiler must be selected. Default:
    `-nf15`.

`-ff`
:   Source code input is in free source form. The interpretation depends on the compiler emulation
    chosen and the specification of the `-f90`,
    `-f95`, or `-f03` option. For files with a
    filename extension of .f90, .f95,
    .f03, .f2003,
    .f08, f2008,
    F90, F95,
    F03, F2003,
    F08 or F2008 the default is
    `-ff`. For all other files the default is
    `-nff`.

`-i2`
:   Default integers occupy 2 bytes by default. The length of logicals will
    depend on the compiler emulated.

`-i4`
:   Default integers and logicals occupy 4 bytes by default.

`-i8`
:   Default integers and logicals occupy 8 bytes by default.

`-intent`
:   Flag dummy arguments for which no INTENT attribute has been specified.
    Default: `-nintent`.

`-intrinsic`
:   Flag referenced intrinsic procedures which have not been declared intrinsic. Default:
    `-nintrinsic`.

`-obsolescent`
:   Flag all syntax features which are marked as obsolescent in the Fortran
    standard which is in effect. Default:
    `-nobsolescent`.

`-r8`
:   Map all default reals to double precision. Map all default complex objects
    to double complex. See also `-dp`. Default:
    `-nr8`.

`-relax`
:   Relax type checking on integers, logicals and Holleriths. No messages will be
    produced for type conflicts between logicals and integers, for the usage of
    relational operators on logicals and for the usage of logical operators on
    integers. Hollerith constants can be used in expressions and mixed with
    logicals, integers and reals. Default: `-nrelax`.

`-save`
:   Save all variables by default. Default: `-nsave`.

`-specific`
:   Flag all referenced specific intrinsic procedures. Default:
    `-nspecific`.

`-standard`
:   Validate the syntax for conformance to the Fortran standard of the level that
    is in effect. All nonstandard syntax will be flagged. The effective level is
    determined by the compiler emulation chosen. Default:
    `-nstandard`.
