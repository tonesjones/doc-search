---
title: "Microsoft Fortran extensions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/microsoft-fortran-extensions.html"
content_id: "RnJonn7ax~0HuLZFyUJO~g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:07.996220+00:00"
---

# Microsoft Fortran extensions

The syntax extensions listed apply for both Microsoft Fortran V5.1 and Microsoft Fortran
PowerStation V1.0

- The compiler directives are supported.
- Type attributes are skipped, except for ALLOCATABLE, which is processed to allow for
  allocatable arrays. The limitations and consistency in usage of the attributes are
  not verified.

Most extensions of Microsoft Fortran PowerStation V4.0 are supported. However, only
simple logical expressions (name oper const) in the `if` and
`elsif` directives are supported.
