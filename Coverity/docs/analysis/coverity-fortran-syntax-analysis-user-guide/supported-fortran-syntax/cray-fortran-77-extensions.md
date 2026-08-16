---
title: "Cray Fortran 77 extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cray-fortran-77-extensions.html"
content_id: "J_NyCE64l~Nr8Z_goWNoZQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:00.265063+00:00"
---

# Cray Fortran 77 extensions

- The Cray Fortran 77 compiler accepts type specifications with length modifiers but
  interprets `INTEGER*2`, `*4`, `*8` as
  64 bit integers, `LOGICAL*2`, `*4`, `*8` as 64 bit logicals, `REAL*4`, `*8` as 64 bit
  reals. They occupy a full 64 bit word. `REAL*16`, `COMPLEX*8` and `COMPLEX*16` data occupy two words (128 bits).
- The `CDIR$` directives are treated as comment and have no
  effect.
- Though Fortran 90 and Coverity Fortran Syntax Analysis do, Cray Fortran 77 does not
  allow an `ENDDO` statement to be labeled.
- Cray Fortran 77 allows recursion in subprograms either by using the prefix RECURSIVE
  in the subprogram header or by specifying the recursive option in the command line
  when compiling. In Coverity Fortran Syntax Analysis the RECURSIVE prefix is accepted
  for Cray Fortran 77 (extension 216). Recursive reference without the RECURSIVE
  prefix can be enabled by specifying extension 229 in the configuration file.
