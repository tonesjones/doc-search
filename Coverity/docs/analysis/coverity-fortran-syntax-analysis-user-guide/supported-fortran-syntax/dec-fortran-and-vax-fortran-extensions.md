---
title: "DEC FORTRAN and VAX Fortran extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/dec-fortran-and-vax-fortran-extensions.html"
content_id: "uiZUTCbJ8RZG5ckTKelWEQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:02.209190+00:00"
---

# DEC FORTRAN and VAX Fortran extensions

- VAX Fortran accepts more than 19 continuation lines as long as the records fit
  in the statement buffer. Only when the statement buffer becomes full you have to
  specify the `/CONTINUATIONS` qualifier. Coverity Fortran Syntax
  Analysis accepts a maximum of 999 continuation lines for the VAX Fortran
  emulation. You can specify the `/CONTINUATIONS` qualifier to
  change this number, or use the `/F77` qualifier to allow 19
  continuation lines.
- The compiler directive `OPTIONS` will be recognized but the
  specified qualifiers will have no effect.
- The keyword `VIRTUAL` is supported but the limitations in usage
  will not be checked.
- DEC FORTRAN 4+ synonyms for Fortran 77 keywords in `OPEN` and
  `CLOSE` are supported, and are flagged.
