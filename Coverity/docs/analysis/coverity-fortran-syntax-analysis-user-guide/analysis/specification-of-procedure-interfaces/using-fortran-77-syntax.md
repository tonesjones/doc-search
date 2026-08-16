---
title: "Using FORTRAN 77 syntax"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-fortran-77-syntax.html"
content_id: "PGFK_sAz8DU57Qm40qDwVQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:52.349104+00:00"
---

# Using FORTRAN 77 syntax

You can use FORTRAN 77 syntax to specify a procedure interface by constructing a template
for the procedure. Just specify the appropriate procedure statement
(`FUNCTION` or `SUBROUTINE`) with the dummy argument
list, a type specification statement for the result in case of a
`FUNCTION` procedure and a type specification for each of the dummy
arguments. If an argument is an input argument, reference it, if it is an output
argument provide an assignment statement to define it, and if it is an input/output
argument reference it first and define it later on. Conclude the template procedure with
an `END` statement. For example:

```
	FUNCTION MYFUN(ARG1) 
	REAL MYFUN, ARG1
	MYFUN=ARG1
	END
```

Include the templates in the Coverity Fortran Syntax Analysis analysis by specifying them
as an input source file or place the Coverity Fortran Syntax Analysis analysis result in
a Coverity Fortran Syntax Analysis library file.
