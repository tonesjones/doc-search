---
title: "Intel Fortran extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/intel-fortran-extensions.html"
content_id: "1WyFpMfpvRLmLHy1EgCz0Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:06.731299+00:00"
---

# Intel Fortran extensions

- cpp preprocessing is supported (fpp).
- The compiler directive `OPTIONS` will be recognized but the
  specified options will have no effect.
- The keyword `VIRTUAL` is supported but the limitations in usage
  will not be checked.
- DEC FORTRAN 4+ synonyms for Fortran 77 keywords in `OPEN` and
  `CLOSE` are supported and are flagged.
- Type attributes are skipped, except for `ALLOCATABLE`, which is
  processed to allow for allocatable arrays. The limitations and consistency in
  usage of the attributes are not verified.
