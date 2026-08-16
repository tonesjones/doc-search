---
title: "Verification of procedure entries"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/verification-of-procedure-entries.html"
content_id: "VVaUOweiNB1ta7Zwa0t3aA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:38.055058+00:00"
---

# Verification of procedure entries

Coverity Fortran Syntax Analysis verifies the dummy (formal) argument list of each
individual `ENTRY` statement of a procedure. Unreferenced dummy arguments
are flagged. If a dummy procedure name is used after an `ENTRY`
statement, it must be present in the argument list of that `ENTRY`
statement. Arguments that specify the dimensions of adjustable arrays must be present in
each `ENTRY` argument list in which the name of the adjustable array
occurs. After each `ENTRY` statement Coverity Fortran Syntax Analysis
will detect variables which are referenced before they are defined, as long as the
statements are executed sequentially or if the `-rigorous` option has
been enabled.

If the `-rigorous` option is in effect Coverity Fortran Syntax Analysis
informs you if the ”entry blocks” are not disjoint, that is to say if paths from one
`ENTRY` statement and another coincide. This is relaxed for an
`ENTRY` statement which follows the specification statements
immediately.
