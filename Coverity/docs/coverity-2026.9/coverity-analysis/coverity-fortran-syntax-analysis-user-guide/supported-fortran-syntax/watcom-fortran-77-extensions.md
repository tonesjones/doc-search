---
title: "Watcom Fortran 77 extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/watcom-fortran-77-extensions.html"
content_id: "niiBE_xkxgiVQUqZTjEb9g"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:37.326412+00:00"
---

# Watcom Fortran 77 extensions

- The Watcom compiler interprets a as end of line comment in any column. Coverity
  Fortran Syntax Analysis interprets a in column 6 as a continuation character (as
  in Fortran 90).
- Coverity Fortran Syntax Analysis does not support the Watcom
  `*$include` compiler directive.
