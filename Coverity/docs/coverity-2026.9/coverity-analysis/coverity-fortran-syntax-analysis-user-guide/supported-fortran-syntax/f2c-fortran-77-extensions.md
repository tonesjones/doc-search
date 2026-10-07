---
title: "F2c Fortran 77 extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/f2c-fortran-77-extensions.html"
content_id: "0gs4v19vZHyh84zifug0TA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:36.753772+00:00"
---

# F2c Fortran 77 extensions

- The tab is supported but does not imply the analysis of characters beyond column
  72.
- By default, f2c Fortran supports C-string backslash editing. This can be
  disabled using the compiler option `-!bs`. Coverity Fortran
  Syntax Analysis supports backslash editing if extension 42 has been enabled in
  the configuration file, which is the default for the f2c Fortran 77 compiler
  emulation.
