---
title: "Compaq Fortran extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/compaq-fortran-extensions.html"
content_id: "iWfnIZswjM7vwM3W5BSAgg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:58.971516+00:00"
---

# Compaq Fortran extensions

Compaq Visual Fortran, formally Digital Visual Fortran, supports most DEC Fortran and Microsoft
Fortran PowerStation Fortran extensions.

- The compiler directive `OPTIONS` will be recognized but the specified
  qualifiers will have no effect.
- cpp preprocessing is supported.
- The keyword `VIRTUAL` is supported but the limitations in usage will
  not be checked.
- DEC FORTRAN 4+ synonyms for Fortran 77 keywords in `OPEN` and
  `CLOSE` are supported, and are flagged.
- Type attributes are skipped, except for `ALLOCATABLE`, which is
  processed to allow for allocatable arrays. The limitations and consistency in usage
  of the attributes are not verified.
