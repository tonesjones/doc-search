---
title: "NDP Fortran extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/ndp-fortran-extensions.html"
content_id: "b8oqjlv02B4EjcQew3hoPA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:37.054801+00:00"
---

# NDP Fortran extensions

- The NDP compiler can read source records up to 132 characters in fixed-form mode
  and 13200 in free-form mode, Coverity Fortran Syntax Analysis only reads a
  maximum of 512 characters.
- NDP Fortran supports C-string backslash editing if the compiler option
  `-f6` is specified. Coverity Fortran Syntax Analysis can
  support backslash editing by enabling extension number 42 in the configuration
  file.
