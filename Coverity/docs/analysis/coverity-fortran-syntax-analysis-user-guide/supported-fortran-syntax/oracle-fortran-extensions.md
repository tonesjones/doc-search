---
title: "Oracle Fortran extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/oracle-fortran-extensions.html"
content_id: "5pRrK4PAPSB7yURvkuK9TQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:09.282515+00:00"
---

# Oracle Fortran extensions

- The Oracle compiler has a data type `UNSIGNED` and accompanying
  intrinsic functions. Coverity Fortran Syntax Analysis does not support
  this.
- The module `SUN IO HANDLERS` is not supplied and the usage of the
  Oracle I/O Error handling routines is not verified.
- The `!DIR$ FREE` and `!DIR$ FIXED` directives are
  supported.
