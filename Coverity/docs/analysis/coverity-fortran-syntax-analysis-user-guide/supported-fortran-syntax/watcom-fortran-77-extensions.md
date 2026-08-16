---
title: "Watcom Fortran 77 extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/watcom-fortran-77-extensions.html"
content_id: "niiBE_xkxgiVQUqZTjEb9g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:13.239821+00:00"
---

# Watcom Fortran 77 extensions

- The Watcom compiler interprets a as end of line comment in any column. Coverity
  Fortran Syntax Analysis interprets a in column 6 as a continuation character (as
  in Fortran 90).
- Coverity Fortran Syntax Analysis does not support the Watcom
  `*$include` compiler directive.
