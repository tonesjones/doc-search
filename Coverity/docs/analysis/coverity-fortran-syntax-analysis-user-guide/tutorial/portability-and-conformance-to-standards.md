---
title: "Portability and conformance to standards"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/portability-and-conformance-to-standards.html"
content_id: "Oim2ZsznbQIGRy58inh7_A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:54.330390+00:00"
---

# Portability and conformance to standards

To verify if a program is portable, you can instruct Coverity Fortran Syntax Analysis to
verify if it is standard conforming. See Standard conformance.

To make your program suitable for the next Fortran level, you can let Coverity Fortran
Syntax Analysis flag the presence of obsolescent syntax (`-obsolescent`
option). It is also possible to instruct Coverity Fortran Syntax Analysis to accept only
those language extensions of a compiler that are available in another Fortran language
level. This is elucidated in Compiler emulation.
