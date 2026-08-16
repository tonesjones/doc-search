---
title: "Intrinsic procedures"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/intrinsic-procedures.html"
content_id: "jC1ASF1ovEWJiDVJMl3Ctw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:38.688754+00:00"
---

# Intrinsic procedures

For each invocation of a Fortran intrinsic generic function, Coverity Fortran Syntax
Analysis generates a specific function according to the data type and data-type kind and
length of the arguments. The name of the generated specific function is inserted in the
cross-reference table of referenced procedures.

Coverity Fortran Syntax Analysis does not need to recognize all specific functions of
every compiler because you should use preferably the appropriate generic function. Only
for type conversion of actual arguments you may need specific functions, which are
supplied.

Coverity Fortran Syntax Analysis can flag each intrinsic function which has not been
declared intrinsic by specifying the `-intrinsic` option. By specifying
the `-specific` option you can flag each specific intrinsic function
used.
