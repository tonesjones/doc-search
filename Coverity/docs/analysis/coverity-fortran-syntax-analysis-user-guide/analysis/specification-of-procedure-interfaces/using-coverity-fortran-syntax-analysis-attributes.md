---
title: "Using Coverity Fortran Syntax Analysis attributes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-coverity-fortran-syntax-analysis-attributes.html"
content_id: "ApZWzsyvW5zhoMAUURWoog"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:53.655349+00:00"
---

# Using Coverity Fortran Syntax Analysis attributes

To define the interface for C, or system procedures, Coverity Fortran Syntax Analysis has
the possibility to specify additional attributes for the procedure and dummy arguments.
For the global program analysis they can be specified in an external template procedure.
For the program-unit analysis you can specify procedure attributes in an
`EXTERNAL` statement which could be placed in an
`INCLUDE` file which you conditionally use for the Coverity Fortran
Syntax Analysis analysis. For both the program-unit analysis and the global program
analysis you can specify the attributes in an interface body in a module.

These attributes have the form [attribute-list] in which attribute-list is a comma
separated list of attributes. You have to enable the [] type attribute extension, nr 69,
in your configuration file to use this facility.

The following attributes can be specified for dummy arguments:

- `OMITTABLE`

  By specifying the `OMITTABLE` attribute
  for a dummy argument of a procedure template you can tell Coverity Fortran
  Syntax Analysis to allow the actual argument to be left empty.
- `PLURI`

  By specifying the `PLURI` attribute for a dummy argument of a
  procedure template you can tell Coverity Fortran Syntax Analysis not to verify
  the argument.
- `PLURI KIND`

  By specifying the `PLURI KIND` attribute for a dummy argument of a
  procedure template you can tell Coverity Fortran Syntax Analysis to allow any
  kind of the argument.
- `POLY`

  You can specify the `POLY` attribute for a
  `TYPE(*)` argument of which the type must conform to the
  datatype as specified by the argument having the `POLY TYPE`
  attribute.
- `POLY TYPE`

  Specify the `POLY TYPE` attribute for the argument which specifies
  the datatype of the `TYPE(*)` argument(s). If one argument has
  the `POLY TYPE` attribute all the arguments having the POLY
  attribute are being verified for conformance with the datatype specified. If two
  arguments have the POLY TYPE attribute the first argument with a POLY attribute
  is verified for conformance with the datatype specified by the first argument
  having a POLY TYPE attribute and the second argument with a POLY attribute is
  verified for conformance with the datatype specified by the second argument
  having a POLY TYPE attribute. The types that can be specified are:

  - MPI INTEGER
  - MPI REAL
  - MPI COMPLEX
  - MPI LOGICAL
  - MPI CHARACTER
  - MPI DOUBLE PRECISION
  - MPI DOUBLE COMPLEX

  As defined in the MPI module MPI constants.
- %VAL

  By specifying the %VAL attribute for a dummy argument you specify that
  actual arguments have to be passed by value using the %VAL built-in function (VMS).
  An example of the specification of the %VAL attribute is: `SUBROUTINE
  SUB(ARG1[%VAL])`.

The following attributes can be specified for external procedure names:

- `INQUIRY`

  By specifying the `INQUIRY` attribute for a procedure template Coverity
  Fortran Syntax Analysis can indicate that the arguments do not have to be
  defined or associated. For example:

  ```
  REAL FUNCTION FUN[INQUIRY](Arg1)
  ```

  And within a subprogram: `EXTERNAL FUN[INQUIRY]`.
- `PLURI`

  By specifying the `PLURI` attribute for a procedure interface you can tell
  Coverity Fortran Syntax Analysis not to verify the number of arguments and the
  argument lists, for example:

  ```
  REAL FUNCTION FUN[PLURI](Arg1,Arg2)
  ```

  And within a subprogram: `EXTERNAL FUN[PLURI]`.
- `SUBREF`

  By specifying the `SUBREF` attribute for a procedure template you can allow a
  `CALL` to a function procedure, for example:

  ```
  REAL FUNCTION FUN[SUBREF](Arg1,Arg2)
  ```

  And within a subprogram: `EXTERNAL FUN[SUBREF]`.
- `VARYING`

  By specifying the `VARYING` attribute for a procedure template Coverity
  Fortran Syntax Analysis can allow a varying number of arguments. For
  example:

  ```
  REAL FUNCTION FUN[VARYING](Arg1,Arg2)
  ```

  And within a subprogram: `EXTERNAL FUN[VARYING]`.
