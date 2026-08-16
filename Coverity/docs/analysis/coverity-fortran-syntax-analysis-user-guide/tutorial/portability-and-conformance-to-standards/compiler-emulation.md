---
title: "Compiler emulation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/compiler-emulation.html"
content_id: "Mb~5XT5QtFEruEVAiUw0xA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:55.629447+00:00"
---

# Compiler emulation

By choosing the appropriate configuration file, the correct language level is chosen and
the supported language extensions are enabled. If you want only those language
extensions to be accepted that are in the next Fortran level, you can specify one of the
specific conformance options. E.g. if you use `gfortran` emulation and
allow all extensions which are in the Fortran 2003 standard, you specify the
`-f03` option.
