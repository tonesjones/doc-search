---
title: "Program-unit cross references"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/program-unit-cross-references.html"
content_id: "ku6M83DFjxwNb9U2UMtr0w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:40.046542+00:00"
---

# Program-unit cross references

Program-unit and procedure cross references are generated if a listing file has been
re­quested and the `-shsub` option is in effect. If no program-unit cross
references are being generated, all diagnostic messages are sent the report file and log
file. An ”...” after a list of line or statement numbers in a cross-reference table
indicates that there are more references to that item than are presented.

The cross-reference table of each module- and internal procedure is presented straight
after its source code listing. The cross-reference tables of the program unit are
presented after all module- and internal procedures.

Variables in a statement context (data-implied-do-variables, ac-implied-do-variables,
forall-indices, and statement-function-dummy-arguments) are not included in the
cross-reference lists. The cross-reference tables of module- and internal procedures
contain locally declared objects and use-associated objects from locally referenced
modules only. Host-associated objects are listed in the host program unit
cross-reference tables.

## Subprogram entries

The cross-reference table of entries displays the following information:

- The name of the program unit or procedure entry.
- The program unit or procedure entry type.
- The type of the result.
- The non-default type kind and length of the result.
- The rank of an array valued result.
- The number of dummy arguments.
- The line or statement numbers of all occurrences of the name of the entry. The
  line or statement number at which the entry is defined is flagged with a
  ”#”.

Program unit and procedure types:
:   | B BLOCK DATA program unit |
    | F function |
    | M module |
    | P main program |
    | S subroutine |

Subcodes:
:   | M module |
    | N interface |
    | R recursive |
    | T internal |

Intrinsic types of function entries, named constants, variables, and referenced functions:
:   | C complex |
    | CH character |
    | R real |
    | I integer |
    | N numeric (integer, real, or complex) |
    | ? typeless |

## Labels

The cross-reference table of labels displays all labels,the
label type, and the line or statement number of all occurrences. The line or
statement number at which the label is de­fined is flagged with a ”#”.

**Label types:**
:   | F format |
    | L DO loop |

For labels, other than DO loop or FORMAT statements, the label type field is left
blank.

## Derived types

The cross-reference table of derived types displays the following information:

- the name of the derived type.
- the type length: the number of bytes a scalar instance of this type will
  occupy.
- the line or statement numbers of all occurrences of the name of the derived
  type. The line or statement number at which the type is defined is flagged with
  a ”#”.

Unreferenced derived types, which are not specified in an include file or a
referenced module, are listed. These derived types are not used and can therefore be
removed from the program unit without affecting the operation of the
program.

## Constants

The cross-reference table of named constants displays
the following information:

- The name of the constant.
- The type: see entries.
- The non-default type kind and length.
- The rank of array valued constants.
- The size the constant occupies.
- The line or statement numbers of all occurrences of the name of the constant.
  The line or statement number at which the constant is defined is flagged with a
  ”#”.

Only when the `-shsngl` option is in effect, all unreferenced
constants which have been specified in an include file or module, are
listed.

For types of named constants see the section on
entries.

Unreferenced constants are listed, except those which are defined in
an include file or referenced module. These constants are not used and can therefore
be removed from the program unit without affecting the operation of the
program.

To get an idea of its size Coverity Fortran Syntax Analysis presents
the total size of the referenced named constants.

## Variables

The cross-reference table of variables displays the following information:

- The name of the variable.
- The type: see entries.
- The non-default type kind and length.
- The rank of arrays.
- The size the variable occupies.
- The operation codes.
- The line or statement numbers of all occurrences of the name of the variable.
  The line or statement numbers at which the variable is modified are flagged with
  a ”#”.

The kind of usage of variables and procedures is presented as a set of operation
codes with the listed meaning. Only one set of operation codes is presented for each
variable. The set of operation codes presented is the or-ed set of operation codes
on all array elements, structure components, or character positions of a variable.
The operation codes of the various array elements, components, or character elements
cannot be viewed separately.

Operation codes:
:   | A ”defined” by means of  - an assignment statement - an actual argument associated with an INTENT(OUT) dummy   argument - a statement function definition statement - an ASSIGN statement - ”associated variable” in DEFINE FILE or OPEN - ”IOSTAT=” in an IO statement - an INQUIRE statement |
    | C in COMMON |
    | D initialized in a DATA or explicit type statement |
    | I input by means of  - READ, or ACCEPT - list in DECODE - conversion buffer in ENCODE - internal file in a READ |
    | L DO variable, or FORALL index |
    | O output by means of  - WRITE, TYPE, PRINT - list in ENCODE - buffer in DECODE - internal file in a WRITE |
    | P dummy argument |
    | Q in EQUIVALENCE |
    | R referenced, for example by means of:  - an expression - an argument of an intrinsic procedure - an argument of a statement function - an actual argument associated with an INTENT(IN) dummy   argument |
    | S actual argument associated with a dummy argument with unknown intent or INTENT(INOUT) |

An ”*” after C, or Q denotes that the name is not referenced (used) and therefore is
dummy. When variables are specified in an EQUIVALENCE statement, the operation codes
are presented for each variable name separately. However, when a variable is in a
common block, all objects specified in the equivalence lists concerned, are in
common and a ”C” will be presented for all these objects. An ”*” after this C
indicates that none of the objects in the equivalence lists, containing this
variable, are being used.

Only when the `-shsngl` is in effect, common-block objects, and module
data that are not referenced, are included in the cross-reference listing.
Referenced but undefined variables are flagged. Unreferenced variables are flagged,
except those which are in common or in a module. They are not used and can therefore
be removed from the subprogram without affecting the operation of the
program.

To get an idea of its size, Coverity Fortran Syntax Analysis presents
the total size of the used local variables. Use associated, allocatable and
automatic objects are not included. Variables with the POINTER attribute account for
the size of a pointer only.

## Structures and records

Structures and records are a Fortran language extension as offered by some compiler
vendors. The cross-reference table of records displays the following
information:

- The name of the record.
- The name of its structure.
- The length of the structure: the number of bytes a record occupies.
- The rank for arrays of records.
- The operation codes.
- The line or statement numbers of all occurrences of the name of the record. The
  line or statement numbers at which the record is modified are flagged with a
  ”#”.

The kind of usage of records is presented as an operation code as described for
variables. As for arrays, only one operation code is presented for each record or
array of records. This is the or-ed operation code of all the operations on the
various fields of the record and the various array elements of an array of
records.

Only when the `-shsngl` option is in effect,
common-block objects, and module records that are not referenced, are included in
the cross-reference listing. Unreferenced records, which are not in common or in a
module, are listed. Unreferenced structures, which are not specified in an include
file or module, are also listed. They are not used and can therefore be removed from
the subprogram without affecting the operation of the program.

## Namelist groups

The cross-reference table of namelist groups
displays the following information:

- The name of the namelist group.
- The line or statement numbers of all occurrences of the name of the namelist
  group. The line or statement number at which the namelist group is defined is
  flagged with a ”#”.

Only when the `-shsngl` option is in effect, unreferenced
namelist groups, which have been specified in an include file or module, are
listed.

**Referenced procedures**

The cross-reference table of
referenced procedures displays the following information:

- The name of the procedure.
- The type: see entries.
- The non-default type kind and length of a function.
- The rank of array valued functions.
- The operation codes.
- The line or statement numbers of all occurrences of the name of the procedure.

Procedure types:
:   | E external procedure, unknown whether subroutine or function |
    | F function |
    | S subroutine |
    | P procedure |

Subcodes:
:   | D dummy |
    | E elemental |
    | G generic |
    | I intrinsic |
    | M module |
    | N interface |
    | n abstract interface |
    | P pure |
    | p pointer |
    | R recursive |
    | S statement |
    | T internal |

For the type of functions see the section on entries. Only when the
`-shsngl` option is in effect, unreferenced procedures which have
been specified in an include file or module, are listed.

When flagged as
unreferenced the external declaration can be removed from the subprogram, except
when it declares a block data subprogram to be included by the linker.

## Operators

The cross-reference table of operators displays the
following information:

- The name of the operator.
- The line or statement numbers of all occurrences of the operator.

When flagged as unreferenced the definition of the operator can be removed from
the subprogram.

## Common blocks

The cross-reference table of common blocks displays
the following information:

- The name of the common block.
- The type.
- The size of the common block.
- The operation codes. The OR-ed operation code of all objects in each common
  block is presented.
- The line or statement numbers of all occurrences of the name of the common
  block.

Common-block types:
:   | CH character |
    | N numeric |

If both character and numeric variables are stored in a common block the type
will be left blank.

The size of the common block is presented in bytes. If the
name table is full, or if the common block has too many objects to check, or if an
array is too long, the size cannot be determined and will be left blank.

When
none of the objects of a common block have been used, the common block will be
flagged as unreferenced unless is has been specified in an include file or a
referenced module. When flagged as unreferenced the common block declaration can

be removed from the subprogram, except when this subprogram is the root of
those sub­programs which use this common block and the common-block does not have
the SAVE attribute in each of the occurrences. In that case the declaration may be
necessary to save the data and the linker may need it to build correct overlay
structures.

## External files

The usage of external files is shown as a list of unit-identifiers with access types
and operation codes. The unit-identifier is the name or expression as specified in
the I/O statement.

The value of the unit-identifier is not known to Coverity
Fortran Syntax Analysis. Therefore, I/O references may be placed incorrectly
together or separately. By using consistent names for all unit-identifiers
throughout the program, the I/O reference tables will be concise and valuable.

Type of I/O:
:   | D direct access |
    | Q sequential access |
    | S stream access |
    | F formatted |
    | U unformatted |

When the access type or format type is unknown to Coverity Fortran Syntax
Analysis, the access type field or format type field will be left blank.

I/O operation codes:
:   | A auxiliary: REWIND, BACKSPACE, ENDFILE, DELETE, UNLOCK, or LOCKING |
    | F FIND |
    | I INQUIRE |
    | O OPEN, or DEFINE FILE |
    | R READ, or ACCEPT |
    | W WRITE, REWRITE, PRINT, or TYPE |

## Include files

Include files which contain only definitions of
constants, variables, and common blocks which are not referenced outside the include
file are marked as unreferenced except in the specification part of a module. Then
the INCLUDE line can be removed from this program unit, except when common blocks,
which are in the root of those subprograms which use these common blocks and do not
have the SAVE attribute, have been declared in the include file concerned. In that
case the declaration may be necessary to save the data and for your linker to build
correct overlay structures.
