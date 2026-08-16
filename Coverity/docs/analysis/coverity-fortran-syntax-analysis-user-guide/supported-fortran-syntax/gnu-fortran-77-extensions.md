---
title: "GNU Fortran 77 extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/gnu-fortran-77-extensions.html"
content_id: "w2YdBPtbU~4aBpCPFKQK3Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:04.114019+00:00"
---

# GNU Fortran 77 extensions

The GNU Fortran 77 compiler has many options to enable or disable certain language
ex­tensions. The configuration file supplied should therefore be considered as a
skeleton. You can easily adapt this configuration file to your needs when using certain
optional extensions, when migrating to Fortran 90. The compiler is now succeeded by
gfortran.

- cpp preprocessing is supported.
- The tab is supported but does not imply the analysis of characters beyond column
  72.
- The length of symbolic names is unlimited in GNU Fortran 77. Coverity Fortran Syntax
  Analysis considers only the first 64 characters as significant.
- By default, GNU Fortran supports C-string backslash editing. This can be disabled
  using the compiler option `-!bs`. Coverity Fortran Syntax Analysis
  supports backslash editing if extension 42 has been enabled in the configuration
  file, which is the default for the GNU Fortran 77 compiler emulation.
- GNU Fortran accepts a statement label after a statement separator (;). Coverity
  Fortran Syntax Analysis does not support this feature.
- GNU Fortran accepts continuation lines of INCLUDE directives and more than one
  IN­CLUDE directive can be placed on a single line using statement separators (;).
  Coverity Fortran Syntax Analysis does not support these extensions.
