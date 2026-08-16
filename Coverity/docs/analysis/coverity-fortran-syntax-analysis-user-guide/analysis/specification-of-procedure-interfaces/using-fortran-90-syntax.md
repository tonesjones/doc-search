---
title: "Using Fortran 90 syntax"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-fortran-90-syntax.html"
content_id: "TXtv6TPbH7RhArjvJwx4_w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:53.005025+00:00"
---

# Using Fortran 90 syntax

Fortran 90 and up provide the appropriate syntax to specify a procedure interface. You create a
module and define an interface block. In this interface block you create one or more
interface bodies to define the interfaces of procedures. Each interface body should
consist of the appropriate procedure statement (`FUNCTION` or
`SUBROUTINE`) with the dummy argument list, a type specification
statement for the result in case of a `FUNCTION` procedure and a type
specification for each of the dummy arguments. If an argument is an input argument,
supply the `INTENT(IN)` attribute, if it is an output argument supply the
`INTENT(OUT)` attribute, and if it is an input/output argument supply
the `INTENT(INOUT)` attribute, which is the default. For optional
arguments specify the `OPTIONAL` attribute. Conclude the interface body
with an `END FUNCTION` or `END SUBROUTINE` statement. For
example:

```
MODULE PLOTLIB
   INTERFACE
     FUNCTION MYFUN(ARG1, ARG2)
       REAL MYFUN
       REAL, INTENT(IN) :: ARG1
       REAL, INTENT(IN), OPTIONAL :: ARG2
     END FUNCTION MYFUN
   END INTERFACE
END MODULE PLOTLIB
```

Include this module in the Coverity Fortran Syntax Analysis analysis by specifying it as
an input source file or place it in a Coverity Fortran Syntax Analysis library file.

When using Fortran 90 or up you include the procedure interface in the program-unit analysis by
referring the module which defines the interface. You do this with the
`USE` statement, for example:

```
USE PLOTLIB
```

Even if you are still restricted to use FORTRAN 77, you can apply the Fortran 90 way for the
Coverity Fortran Syntax Analysis analysis! Just enable Fortran 90 or up syntax in the
Coverity Fortran Syntax Analysis configuration file to analyze the interface modules and
enable extension 217, modules, for the analysis of the other program units. Place the
`USE` statement in an `INCLUDE` file which you
conditionally use for the Coverity Fortran Syntax Analysis analysis. For compilation you
replace this `INCLUDE` file by one with an `EXTERNAL`
statement specifying the procedure.

You can use the supplied utility `interf` to generate a module with interface
bodies from a Coverity Fortran Syntax Analysis library file. See the Operation chapter.
