---
title: "Apollo/Domain Fortran extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/apollo/domain-fortran-extensions.html"
content_id: "zPPJuTbV8bAp_ULM5ZxQTQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:58.302895+00:00"
---

# Apollo/Domain Fortran extensions

- The Apollo/Domain compiler can read source records up to 1023 characters in free-form mode,
  Coverity Fortran Syntax Analysis reads a maximum of 512 characters.
- The number of continuation lines is unlimited for the Apollo/Domain compiler,
  Coverity Fortran Syntax Analysis can read a maximum of 999 continuation lines.
- The Apollo/Domain SR10 Fortran compiler accept names up to 4096 significant characters,
  Coverity Fortran Syntax Analysis considers only the first 64 characters as
  significant.
- The Apollo/Domain compiler accepts by default in-line comment between curly brackets ({ }).
  Coverity Fortran Syntax Analysis no longer supports this form of comment. For the
  Apollo/Domain compiler you can specify the in-line comment character using the
  `-inline` option. In Coverity Fortran Syntax Analysis you can
  enable the exclamation mark as the start of in-line comment by enabling extension 6
  in the configuration file.
- Apollo Domain Fortran supports C-string backslash editing when the `-uc`
  compiler option has been enabled. Coverity Fortran Syntax Analysis supports
  backslash editing if extension 42 has been enabled in the configuration file.

- The `INCLUDE` line and the compiler directives
  `%include`, `%eject`, `%list`,
  `%nolist` are supported.
- Conditional source input lines can be specified starting with ”`D`”,
  or ”`Debug`”.
