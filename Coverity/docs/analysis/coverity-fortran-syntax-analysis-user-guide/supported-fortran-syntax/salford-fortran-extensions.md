---
title: "Salford Fortran extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/salford-fortran-extensions.html"
content_id: "mYsb0ToGEN1kwWFSBnsj4g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:10.599844+00:00"
---

# Salford Fortran extensions

Most FTN77/386 extensions are supported, but a number of the newer FTN extensions are
not.

- Though the maximum number of continuation lines supported is 19 for fixed format and
  39 for free format, the FTN compilers allow more continuation lines depending of the
  length of the lines. FTN95 allows 19 in fixed format, 39 in free format and 99 in
  free format in .NET configuration or if the Fortran 2003 switch /F03 has been
  specified.
- The compiler directive `OPTIONS` will be recognized but the specified
  qualifiers will have no effect.
- Internal procedures are not supported.

- `INTERRUPT SUBROUTINE`, `SPECIAL SUBROUTINE` and
  `SPECIAL ENTRY` are not supported.
- Conditional compilation (`CIF`, `CELSE`,
  `CENDIF`) is not supported.
- The `%` prefix to denote an address in a `DATA`
  statement is not supported.
- Business editing is not supported.
