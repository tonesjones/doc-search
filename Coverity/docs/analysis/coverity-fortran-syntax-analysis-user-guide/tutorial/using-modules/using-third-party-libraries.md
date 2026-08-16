---
title: "Using third-party libraries"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-third-party-libraries.html"
content_id: "ShNTIzLt8UInKCwOh4fHKQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:53.693468+00:00"
---

# Using third-party libraries

When referencing third-party modules, e.g. supplied by the compiler vendor, Coverity
Fortran Syntax Analysis needs the interfaces to perform the analysis.

Coverity Fortran Syntax Analysis cannot read the .mod files as
supplied by the vendor because they are proprietary binary files. If the source code
with the interfaces is supplied by the vendor you can generate a Coverity Fortran Syntax
Analysis library file containing the interfaces. See Coverity Fortran Syntax Analysis library files on how to generate the
library file.

If the interface is not supplied in source code, you can compose it from the
documentation as described in Specification of procedure interfaces.
