---
title: "INTRINSICS"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/intrinsics.html"
content_id: "9MBczZvnrKOptBHlI_6D_Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:15.177932+00:00"
---

# INTRINSICS

Coverity Fortran Syntax Analysis recognizes all standard Fortran intrinsic procedures.
More­over the additional intrinsic procedures as specified in the configuration file
will be recognized. You can modify the configuration file and remove, add, or change the
nonstandard intrinsic procedures to be recognized. Not all *specific* names of each
generic procedure are specified in the various configuration files, because in general
there is no need to use these names.

Coverity Fortran Syntax Analysis can accept added intrinsic functions which are
standardized in a higher Fortran standard level than the Fortran conformance level as
specified in this configuration file without reporting. You can group the added
intrinsic functions for each language level. Each group must have one of the following
headers:

```
!Fortran 90 additions
!Fortran 95 additions
!Fortran 2003 additions
!Fortran 2008 additions
!Fortran 2015 additions
```

The nonstandard compiler specific additions must be in a group with the following
header:

```
!Nonstandard additions
```

If you specify e.g. `-f03` only the intrinsic functions which are not in
the Fortran 2003 standard are reported.

In the next paragraphs we describe the way intrinsic procedures can be specified in the
configuration file. The properties of intrinsic procedures are very divers and hard to
specify in a general way, covering all implementations. Moreover the various Fortran
language reference manuals describe the intrinsic functions each in their own way from
which it is often hard to discover the system behind the generation of specific
functions from generic functions. Therefore it is not an easy task to specify additional
intrinsic procedures in the configuration file. However, if you follow the rules
described below and use the configuration files supplied as examples you will be able to
fulfill the job.

In the record ”allowed type lengths for generic procedures” of the configuration file you
can specify which argument type lengths will be accepted by a generic function to
generate a specific function. To allow the `BYTE` type as argument,
specify it as `INTEGER*1`.

Each specific intrinsic procedure is specified by a header record and a record for each
of its arguments.

The header record is composed of the following fields:

1. Generic procedure name, string.

   If blank, the procedure is specific only. If
   non-blank, and if the procedure does not exist already, it is added to the list
   of generic procedures.
2. Specific procedure name, string.

   If the specific procedure name already exists, the specific procedure specified
   over­rules the existing one. Otherwise, the specific procedure name is added to
   the list of specific procedures.

   If the generic procedure name is non-blank, the procedure is added to the chain
   of specific procedures which can be generated from the generic procedure.

   If the specific name is left blank the generic name is used as the specific
   name.

   Specific procedures must have different names if they can be generated from a
   single generic procedure and have different resulting types or type lengths.

   If the intrinsic procedure is a subroutine, the procedure type must be specified
   as ’S’, the type length and rank are not relevant and can be set to zero.
3. Procedure type, character.

   ’ ’ same as the type of the argument(s)

   ’?’ typeless

   ’C’ complex

   ’CH’ character

   ’I’ integer

   ’L’ logical

   ’R’ real

   ’X’ result of MATMUL or DOT PRODUCT

   ’S’ subroutine
4. Procedure type kind/length, integer. Special codes:

   ¿0 type length

   0 same as the type kind/length of the argument(s)

   -1 default type kind/length of the function type

   -2 default type kind/length of type double precision

   -3 same as the type kind of the argument(s); half the type length of the type
   length of the arguments

   -4 unknown

   -5 type kind of an address (or integer POINTER)
5. Procedure rank and shape code, integer. Special codes:

   0 scalar

   1 rank 1

   2 rank 2

   -1 take shape of argument with largest rank

   -2 rank N+1

   -3 scalar or rank 1

   -4 scalar or rank N-1

   -5 rank 1 or N-1

   -6 shape of second array argument

   -7 follow the rules of matrix multiplication

   In which N is the highest rank of all arguments.
6. Number of arguments, integer. Special codes:

   -1 one or two arguments allowed, one argument line must follow

   -2 two or more arguments allowed, one argument line must follow

   -3 one or none arguments allowed, three argument lines must follow

   -4 two or three arguments allowed, two if first argument is complex; three
   argument lines must follow

   -5 any number of arguments allowed, no argument lines must follow
7. Procedure name allowed as actual argument, logical.
8. Intrinsic procedure class, string:

   ’A’ atomic subroutine

   ’C’ collective
   subroutine

   ’E’ elemental function

   ’I’ inquiry function

   ’P’
   procedure (can be referenced as function or subroutine)

   ’S’ subroutine

   ’T’ transformational function
9. Compile-time inquiry, or transformational function, logical.
10. Optional comment, string.

Each record for an argument is composed of the following fields:

1. Argument name, character.
2. Argument type, character.

   ’ ’ any type allowed (but all arguments must have the
   same type)

   ’?’ typeless

   ’C’ complex

   ’CH’ character

   ’I’
   integer

   ’L’ logical

   ’N’ numeric: integer, real, complex

   ’B’
   real’

   ’T’ derived type

   ’U’ intrinsic type

   ’X’ any type allowed, don’t
   check
3. Argument type kind/length, integer.

   ¿0 type length

   0 any kind/length allowed
   which is allowed for the generic procedure

   -1 default kind/length of the argument
   type

   -2 double precision
4. Argument rank, integer. Special codes:

   0 argument must be scalar

   1
   argument must be array of rank 1

   2 argument must be array of rank 2

   -1 array argument required

   -2 argument can be scalar or array,
   even in Fortran 77

   -3 argument can be scalar or array

   -4 argument
   can be scalar or rank N-1

   -5 argument can be rank 1 or 2

   -6
   argument must be a dummy argument

   -7 argument must be the name of a
   variable or external procedure

   -8 argument must be a pointer or pointer
   procedure

   In which N is the highest rank of all arguments.
5. Argument must have the same type and type parameters as the previous ones (if
   any) of which this flag has been set, logical. If the resulting type kind of the
   intrinsic procedure depends on the type kind of this argument, this flag must be
   set true.
6. Argument is optional, logical.
7. Argument must be defined on entry, logical.
8. Argument will be defined, logical.
9. Optional comment, string.
