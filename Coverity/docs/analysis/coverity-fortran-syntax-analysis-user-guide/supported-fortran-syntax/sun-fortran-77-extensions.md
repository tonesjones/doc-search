---
title: "Sun Fortran 77 extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sun-fortran-77-extensions.html"
content_id: "EQRBzGCPo0i1VDqUZZ3WRA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:11.924381+00:00"
---

# Sun Fortran 77 extensions

- cpp preprocessing is supported.
- The tab is supported but does not imply the analysis of characters beyond column
  72.
- The default maximum number of continuation lines for the Sun compiler is 19.
  This maximum can be increased using the `-Nln` option. Coverity
  Fortran Syntax Analysis also allows a maximum of 19 continuation lines by
  default. Coverity Fortran Syntax Analysis' maximum can be increased up to 999,
  using the `-cont n` option.
- By default Sun Fortran supports C-string backslash editing. This can be disabled
  using the compiler option `-xl`. Coverity Fortran Syntax Analysis
  supports backslash editing if extension 42 has been enabled in the configuration
  file, which is the default for the SUN compiler emulation.
