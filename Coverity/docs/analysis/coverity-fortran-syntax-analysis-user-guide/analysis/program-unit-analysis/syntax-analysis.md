---
title: "Syntax analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/syntax-analysis.html"
content_id: "kzskFtTnq4Qw5yCTb3L8IQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:36.102617+00:00"
---

# Syntax analysis

Coverity Fortran Syntax Analysis verifies the syntax of each program unit. If the
`-standard` option is in effect then the syntax will be verified for
conformance to the Fortran standard of the level that is currently in effect. If the
`-f77`, `-f90`, `-f95`,
`-f03`, `-f08` or `-f15` option is in
effect, the syntax will be verified for conformance to the FORTRAN 77, Fortran 90,
Fortran 95, Fortran 2003, Fortran 2008, or Fortran 2015 standard respectively, as
closely as possible during static analysis. For Fortran 90 and up, most constraints — as
specified in the standard — are verified. If the `-obsolescent` option
specified, Coverity Fortran Syntax Analysis flags all obsolescent features as specified
in the Fortran standard which is in effect.

You can also instruct Coverity Fortran Syntax Analysis to accept certain vendor-specific
Fortran language extensions. Fortran 77 language extensions table and
Fortran 90/95/2003/2008/2015 language extensions table describe
all language extensions supported. By default Coverity Fortran Syntax Analysis accepts
common extensions of the default compiler of the system on which Coverity Fortran Syntax
Analysis operates. To emulate a different compiler or to enable a different set of
language extensions, see The usage of language extensions.

Beside performing a lexical analysis and parsing the syntax, Coverity Fortran Syntax
Analysis performs limited semantic analyses. Coverity Fortran Syntax Analysis presents a
message if a variable is referenced without being defined. Unless the
`-rigorous` option has been enabled this is limited to statements
which are certainly executed sequentially.

Loop structures, `IF-THEN-ELSE` blocks and `CASE`
constructs are verified. Because of this, extended `DO` loops (though
this is a language extension of some compilers) will always be flagged as an error by
Coverity Fortran Syntax Analysis.
