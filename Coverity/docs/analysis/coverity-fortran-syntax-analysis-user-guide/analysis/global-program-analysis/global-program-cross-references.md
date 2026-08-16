---
title: "Global program cross references"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/global-program-cross-references.html"
content_id: "IusTspH9SAm8cjF2mwdITA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:49.106754+00:00"
---

# Global program cross references

Global program cross references are generated if a listing file has been requested and
the `-shprg` option is in effect. If no global program cross references
are presented, all diagnostic messages are send to your screen or the log file. An ”...”
after a list of names in a cross-reference table indicates that there are more
references to that item than presented.

Module procedures are ”qualified” with the name of the module from which they are
referenced. Renamed procedures are presented by their ”use” name.

## Program units and procedures analyzed

In this table all program units and module procedures which have been analyzed are
listed with the page number of the listing and the filename in which the program
unit or module procedure resides. When you did not ask for a listing of a specific
program unit its page number will be left blank.

When you use Coverity Fortran Syntax Analysis’s library facility then a hierarchical
page number system will be applied. The library maintains a version number for each
program unit which has been stored and for which a listing has been made. This
program unit version number becomes the library version number at the moment you
insert or replace the program unit. The library version number will increase at each
Coverity Fortran Syntax Analysis run in which you update the library. In the table
of analyzed program units and procedures the version number and page number are
shown as ”version.page”.

## Referenced procedures not analyzed

All referenced procedure entries which were not analyzed are listed here. Because a
program often references external procedures of which no Fortran source is available
to include in the Coverity Fortran Syntax Analysis analysis (for example system
library routines), no separate messages will be presented for these ”undefined
references”. To make the analysis more complete, see Specification of procedure interfaces.

## Cross reference of program units and procedures

All names of the program, modules, block data program units, external and module
procedures are listed with their type and number of arguments. For functions the
type with non-default kind and length will also be presented. For each procedure all
program units and procedures which reference that procedure are shown.

Program unit and procedure types:
:   | B BLOCK DATA program unit |
    | E external, unknown whether subroutine or function |
    | F function |
    | M module |
    | P main program |
    | S subroutine |

Subcodes:
:   | E elemental |
    | M module |
    | N interface |
    | P pure |
    | R recursive |

Intrinsic types of functions and function entries:
:   | C complex |
    | CH character |
    | I integer |
    | L logical |
    | R real |
    | ? typeless |

The total size of the local data of all program units and procedures is presented.
Allocatable and automatic objects are not included.

## Cross reference of common blocks

All common blocks referenced in the program are listed with all subprograms in which
the common blocks have been specified. A ”#” in front of a subprogram name indicates
that the common block is modified directly in that program unit or procedure. Mind
that if a common-block object is used as an actual argument of a procedure
reference, a modification of the common block in that procedure will not be
indicated.

The type of the data in each common block and the common-block size in bytes are
presented. When the common block has been saved this will be indicated.

Common-block types:
:   | CH character |
    | N numeric |

When types have been mixed the common-block type will be left blank.

The size of the common block is presented in bytes. When the name table is full, or
the common block has too many objects to check, or when an array or record is too
long, the size cannot be determined and will be left blank. The largest size of all
occurrences of the common block is presented

The total size all common blocks will occupy is presented.

## Cross reference of external files

All external files used in the program are shown as a list of unit-identifiers with
all subprograms in which the external files are referenced. The types and operation
codes are presented.

The unit-identifier is the name or expression as specified in the I/O statement.
Because the value of the unit-identifier is not known to Coverity Fortran Syntax
Analysis I/O references may be placed incorrectly together or separately. By using
consistent names for all unit-identifiers throughout the program the I/O reference
tables will be valuable.

Type of I/O:
:   | D direct access |
    | F formatted |
    | S sequential access |
    | U unformatted |

When the access or format type is unknown to Coverity Fortran Syntax Analysis the
access or format type will be left blank.

I/O operation codes:
:   | A auxiliary: REWIND, BACKSPACE, ENDFILE, DELETE, UNLOCK, or LOCKING |
    | C CLOSE |
    | F FIND |
    | I INQUIRE |
    | O OPEN, or DEFINE FILE |
    | R READ, or ACCEPT |
    | W WRITE, REWRITE, PRINT, or TYPE |

## Cross reference of modules

For each module all subprograms which reference that module are presented.

Module type:
:   | I module nature is intrinsic |
    | N module nature is non-intrinsic |
    | S submodule |

## Cross reference of include files

For each include file all program units which contain that include file are
presented.
