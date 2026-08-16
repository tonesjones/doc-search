---
title: "Absoft Fortran 77 extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/absoft-fortran-77-extensions.html"
content_id: "FMHmr9i7eYize8tx~SN16Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:57.661276+00:00"
---

# Absoft Fortran 77 extensions

- Coverity Fortran Syntax Analysis folds all input to uppercase. The Absoft compiler
  supports folding to uppercase, to lowercase or treat input case sensitive.
- Absoft has compiler options to specify the kind of free form source code. Coverity
  Fortran Syntax Analysis also supports various kinds of free form input but you have
  to specify this in the configuration file. Default is the Fortran 90 format.
- Absoft has a compiler option to support C-string backslash editing. For Coverity
  Fortran Syntax Analysis you have to enable extension 42 in the configuration
  file.
- Absoft has compiler options to support conditional compilation lines beginning with
  ’D’,... ’d’, ’X’, or ’x’. In the supplied configuration file for Coverity Fortran
  Syntax Analysis only conditional lines beginning with ’D’, or ’d’ are enabled. To
  accept also lines beginning with ’X’, or ’x’ you must enable extension 3 in the
  configuration file which, however, accepts conditional lines beginning with any
  letter.
- Coverity Fortran Syntax Analysis supports `DO WHILE`..
  `ENDDO`, but not `WHILE`..
  `ENDDO`.

- Coverity Fortran Syntax Analysis does not support the following keywords:
  `GLOBAL`, `INLINE`, `VALUE`,
  `GLOBAL DEFINE`, `REPEAT`.
