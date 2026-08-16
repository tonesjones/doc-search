---
title: "Generating Fortran 90 interfaces"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/generating-fortran-90-interfaces.html"
content_id: "VMxdKKfvExWu7JBkfeblJA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:25.032816+00:00"
---

# Generating Fortran 90 interfaces

The unsupported utility `interf` takes a Coverity Fortran Syntax Analysis
library file as input and produces a Fortran 90 module with an interface body for each
of the subprograms in the library file. The output is in Fortran 90 free source
form.

This can be useful when converting from FORTRAN 77 to Fortran 90 and to examine the
properties of the subprograms as contained in the library file. By specifying the module
in the program units which references these subprograms the interfaces of the
subprograms become explicit and both the compiler and Coverity Fortran Syntax Analysis
can now verify the references while compiling or analyzing the program unit.
