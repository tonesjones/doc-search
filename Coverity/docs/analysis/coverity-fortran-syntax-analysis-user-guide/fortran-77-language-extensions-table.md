---
title: "Fortran 77 language extensions table"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/fortran-77-language-extensions-table.html"
content_id: "1zXzpatR6uAOEA88gAiG8Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:19.145971+00:00"
---

# Fortran 77 language extensions table

| no. |  | PDP | VAX | VS2 | UNI | CBR | PR | CF77 | CVX | SGI | SUN | HP9 | DEC | CD4 | RM | RM2 | MS5 | LH | PF | NDP | FTN | WAT | AB | F2C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **maxima in lay-out:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | max. number of characters per line | 88 | 132 | 80 | 80 | 80 | 80 | 96 |  | 132 | 132 | 80 | 132 | 132 | 80 | 80 | 80 | 80 | 80 | @ | 80 |  | 132 | @ |
|  | max. number of continuation lines | 99 | @ | 99 | @ | 19 | @ | 99 | 19 | 99 | @ | 99 | 19 | 19 | @ | @ | @ | @ | 19 | 99 | 19 | 61 | 99 | @ |
|  | max. length of names | 6 | 31 | 31 | 6 | 7 | 32 | 31 | @ | 32 | 32 | @ | 31 | 32 | 31 | 31 | 31 | 31 | 31 | 31 | 32 | 32 | 31 | @ |
|  | max. length of subprogram names | 6 | 31 | 7 | 6 | 7 | 32 | 31 | @ | 32 | 32 | @ | 31 | 32 | 8 | 8 | 31 | 31 | 31 | 31 | 32 | 32 | 31 | @ |
|  | max. length of common-block names | 6 | 31 | 7 | 6 | 7 | 32 | 31 | @ | 32 | 32 | @ | 31 | 32 | 8 | 8 | 31 | 31 | 31 | 31 | 32 | 32 | 31 | @ |
|  | **type length modifiers:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | INTEGER *1 |  |  |  |  |  |  |  | + | + |  |  | + | + |  |  | + | + | + | + | + | + | + | + |
|  | INTEGER *2 | + | + | + |  | + | + | @ | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
|  | INTEGER *4 | + | + | + | + | + | + | @ | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
|  | INTEGER *8 |  |  |  |  | + |  | @ | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |
|  | REAL *4 | + | + | + | + |  | + | @ | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
|  | REAL *8 | + | + | + | + | + | + | @ | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
|  | REAL *16 |  | + | + |  | + | + | @ |  | @ | + | + |  | @ |  |  |  |  |  |  |  |  |  |  |
|  | COMPLEX *8 | + | + | + | + |  | + | @ | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
|  | COMPLEX *16 |  | + | + | + | + | + | @ | + | + | + | + | + | + | + | + | + | + |  | + | + | + | + | + |
|  | COMPLEX *32 |  |  | + |  |  |  | @ |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | LOGICAL *1 | + | + | + |  |  | + |  | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
|  | LOGICAL *2 | + | + |  |  |  | + | @ | + | + | + | + | + | + |  |  | + |  | + | + | + |  | + | + |
|  | LOGICAL *4 | + | + | + | + |  | + | @ | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
|  | LOGICAL *8 |  |  |  |  |  |  | @ | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | **maximum length of type CHARACTER:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | CHARACTER *255 | + |  |  |  |  |  |  |  |  |  |  |  |  | + | + |  |  |  |  |  |  |  |  |
|  | CHARACTER *511 |  |  | @ | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | CHARACTER *16384 |  |  |  |  |  |  | + |  |  | + | + |  |  |  |  | + | + | + |  | + |  |  |  |
|  | CHARACTER *32767 |  |  | @ |  |  | + |  |  | + |  |  | + | + |  |  |  |  |  | + |  | + |  |  |
|  | CHARACTER *65280 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + | + |
|  | CHARACTER *65535 |  | + |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | CHARACTER *2147483647 |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | default source file name extension | FTN | FOR |  |  |  | F77 | f | f | f | f | f | f | f | FOR | FOR | FOR | FOR | FOR | f | FOR | FOR |  | f |
|  | default include file name extension | FTN | FOR |  |  |  |  |  |  |  |  |  |  |  |  |  |  | FOR |  |  |  | FOR |  |  |
|  | include list option delimiter | / | / |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | compiler directive string |  |  | @ | # |  | $ |  | # | $ | # | $ |  | $ |  |  | $ | % |  |  |  |  | $ |  |
|  | free form continuation character |  |  | - |  |  |  |  |  |  |  |  |  |  |  |  | - |  |  |  |  |  | & | & |
|  | free form 1st column comment char. |  |  | " |  |  |  |  |  |  |  |  |  |  |  |  | " | * |  |  |  |  | ! | ! |
|  | **lay-out:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1 | lower case characters | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
| 2 | debug lines (D) | + | + |  |  |  |  |  | + | + |  | + | + | + |  | + |  |  |  | + |  | + | + |  |
| 3 | debug lines (A-Z) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |
| 4 | tabs | + | + |  |  |  |  | + | + | + | + | + | + | + |  | + | + | + | + | + | + | + | + | + |
| 5 | formfeeds | + | + |  |  |  |  |  | + | + | + | + | + | + |  |  | + | + |  | + |  | + | + | + |
| 6 | in-line comment after! | + | + | + |  | + |  | + | + | + | + | + | + | + |  |  | + | + | + | + | + | + | + | + |
| 7 | cpp preprocessing |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 | in-line comment after @ |  |  |  | + |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |
| 10 | statement separator; |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |
| 11 | any character allowed as continuation character |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | **names:** |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |
| 13 | names with $ |  | + | + | + |  | + | + | + | + | + | + | + | + | + | + | + | + |  | + | + | + | + |  |
| 14 | names with_ |  | + | + |  |  | + | + | + | + | + | + | + | + |  | + | + | + | + | + | + | + | + | + |
| 15 | names beginning with $ |  |  | + |  |  |  |  |  |  |  |  |  |  |  | + | + |  |  | + |  | + |  |  |
| 16 | built-in functions beginning with % |  | + |  |  |  |  |  | + | + |  | + | + | + |  |  |  |  |  |  |  |  | + |  |
| 17 | names with @ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
| 18 | names beginning with _ |  |  |  |  |  |  |  |  | + |  |  |  | + |  |  |  |  |  |  |  | + |  | + |
|  | **constants:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 20 | character constants between "" |  |  |  |  | + |  | + |  | + | + | + | + | + |  |  | + | + |  | + |  |  | + | + |
| 21 | REAL*16 with Q-exponent |  | + | + |  |  | + |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 22 | named constants in complex constants | + | + |  |  | + |  |  | + | + |  | + | + |  |  |  |  |  |  |  |  |  |  | + |
| 23 | Hollerith | + | + | + |  | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
| 24 | B’xxx’, B”xxx” binary |  |  |  |  |  |  |  |  | + | + |  | + | + |  |  |  |  |  | + | + |  | + | + |
| 25 | O’xxx’, O”xxx” octal |  |  |  |  | + | + | + |  | + | + | + | + | + |  |  |  |  |  | + | + |  | + | + |
| 26 | X’xxx’, X”xxx” hexadecimal |  |  |  |  |  |  | + |  | + | + |  | + | + |  |  |  |  |  |  |  |  |  | + |
| 27 | Z’xxx’, Z”xxx” hexadecimal |  |  |  |  | + | + | + |  | + | + | + | + | + |  | + |  | + |  | + | + |  | + | + |
| 28 | ’xxx’B, ”xxx”B binary |  |  |  |  |  |  |  |  | + |  |  | + | + |  |  |  |  |  |  |  |  |  | + |
| 29 | ’xxx’O, ”xxx”O octal | + | + |  |  |  |  |  | + | + |  | + | + | + |  |  |  |  |  |  |  | + | + | + |
| 30 | ’xxx’X, ”xxx”X hexadecimal | + | + |  |  |  |  |  | + | + |  | + | + | + |  |  |  |  |  |  |  | + | + | + |
| 31 | ’xxx’Z, ”xxx”Z hexadecimal |  |  |  |  |  |  |  |  | + |  |  | + | + |  |  |  |  |  |  |  |  |  | + |
| 32 | Oxxx octal | o | o |  | + |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |
| 33 | Zxxx hexadecimal | o | o | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |
| 34 | xxxB octal |  |  |  |  |  |  | + |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |
| 35 | [-]:xxx hexadecimal |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 36 | "xxx octal | + | + |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 37 | $ xxx hexadecimal |  |  |  |  |  |  |  |  | + |  |  |  | + |  |  |  |  | + |  |  |  |  |  |
| 38 | [radix]#value |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  | + |
| 39 | nRxxx radix 50 | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  |
| 40 | C-string: ’xxx’C* |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  | + |  |  |
| 41 | Length modifier suffix: B,S,L (FTN77) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
| 42 | C-string: \ editing* |  |  |  |  |  |  |  |  | + | @ |  | + | + |  |  | + |  |  | @ |  |  |  | + |
|  | **specification statements:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 43 | ALLOCATABLE |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  | + |  |  |  |  |  |  |
| 44 | STATIC |  |  |  |  |  |  |  |  | + | + | + | + | + |  |  |  |  |  | + |  |  |  | + |
| 45 | [DE]ALLOCATE, deferred dimension spec. |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  | + | + |  |  |  | + |  |  |
| 46 | AUTOMATIC |  |  |  |  |  |  |  |  | + | + | + | + | + |  |  | + |  |  | + |  |  |  | + |
| 47 | BOOLEAN |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 48 | BYTE | + | + |  |  | + |  |  |  | + | + | + | + | + |  |  | + |  |  | + |  |  |  | + |
| 49 | C EXTERNAL |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  | + |  |  |  |  |
| 50 | DOUBLE COMPLEX |  |  |  |  |  |  |  |  | + | + | + | + | + |  |  | + | + |  | + |  | + | + | + |
| 51 | IMPLICIT NONE |  | + | + |  | + |  | + | + | + | + | + | + | + |  | + | + | + | + | + | + | + | + | + |
| 52 | IMPLICIT UNDEFINED |  |  |  |  |  |  |  |  | + | + |  |  | + |  |  |  |  |  | + |  |  |  | + |
| 53 | IMPLICIT AUTOMATIC/STATIC |  |  |  |  |  |  |  |  | + | + |  |  | + |  |  |  |  |  | + |  |  |  |  |
| 54 | OPTIONAL, INTENT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 55 | integer (Cray) POINTER |  |  |  |  |  |  | + |  | + | + |  | + | + |  |  |  |  |  |  |  |  | + |  |
| 56 | LC, BC, HC, MS, MSC EXTERNAL |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |
| 57 | NAMELIST |  | + | + |  | + | + | + | + | + | + | + | + | + | + | + | + | + |  | + | + | + | + | + |
| 58 | F90 extended NAMELIST features |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 59 | STRUCTURE, RECORD |  | + |  |  |  |  |  | + | + | + | + | + | + |  |  | + |  |  | + |  | + | + |  |
| 60 | F90 derived type |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 61 | VIRTUAL | + | o |  |  |  |  |  |  | o |  | o | o | o |  |  |  |  |  | o |  |  | o |  |
| 62 | VOLATILE |  | + |  |  |  |  |  |  | + |  | + | + | + |  |  |  |  |  | + |  |  | + |  |
| 63 | F90 POINTER, TARGET |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 64 | DEFINE |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 65 | automatic arrays |  |  |  |  |  |  | + |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |
| 66 | DLL IMPORT, DLL EXPORT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 67 | C EXTERNAL, Salford STDCALL |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
| 68 | specif. functions in specif. expressions |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 69 | [..] type attributes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |
| 70 | /../ init. of var. in type specif.stmnt. |  | + | + | + |  | + |  | + | + | + | + | + | + | + | + | + | + |  |  | + | + | + |  |
| 107 | F90 init. of var. in type specif.stmnt. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 71 | length modifier after dimension |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | o |  |  |  |  |  |  |
| 72 | PARAMETER symbol=constant | + | + |  | + |  | + |  | + | + |  | + | + | + | + |  |  |  |  |  | + |  |  |  |
| 73 | /../ initialization of structure components |  | + |  |  |  |  |  | + | + | + |  | + | + |  |  |  |  |  | + |  |  |  |  |
| 74 | intrinsic functions in PARAMETER |  | + |  | + | + |  |  |  | + | + | + | + | + | + |  |  |  |  |  |  |  |  | + |
| 75 | intrinsic functions in dimension spec. |  |  |  |  | + |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 76 | DATA statements mixed with spec. stmnts. | o | o | o |  |  |  | o | o | o |  | o | o | o | o |  |  |  |  |  |  |  |  |  |
| 77 | IMPLICIT mixed with specification stmnts. |  |  | o |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 78 | F90 KIND and Character selectors |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 79 | F90 attributes and entity oriented decl. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 80 | F90 specification expressions |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 81 | Record fields and records in DATA |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |
| 82 | Subobject of constant in DATA |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 83 | intrinsic functions in DATA |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 84 | pointers can be initialized in a DATA stmnt |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | **subprograms:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 119 | END program unit [name] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 215 | INTERFACE TO |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |
| 216 | RECURSIVE |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |
| 217 | MODULE |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 220 | argument list in PROGRAM statement |  |  |  |  |  |  | + |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  | @ |
| 221 | [type[*len]] FUNCTION name | + | + |  |  |  | + |  | + | + | + | + | + |  |  | + | + | + | + | + | + | + | + | + |
| 222 | [type] FUNCTION name [*len] | o | o | + | + | + |  |  | o | o | o | o | o |  | + |  |  |  |  |  |  | o | o |  |
| 223 | F90 interface block |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 224 | F90 internal subprograms |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 225 | Unisys internal subprograms |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 226 | array valued functions |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 227 | END INTERFACE name |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 228 | STDCALL** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 229 | recursive subprograms |  |  |  |  |  |  | o |  | + | + | + | + | + |  |  |  |  |  |  |  |  |  |  |
|  | **commons:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 85 | initialization of blank COMMON | o | o |  |  |  | o | o | o |  |  | o | o |  | o | o |  |  |  |  |  |  |  | o |
| 86 | differing lengths for a named COMMON | o | o |  | o |  | o | o |  | o |  |  | o | o | o | o |  |  |  |  |  |  |  |  |
| 87 | initialization of COMMON not in BLOCK DATA | o | o |  |  | o | o | o | o |  | o | o | o |  | o |  |  |  |  |  | o | o |  | o |
| 88 | mixing of numeric and character in COMMON |  | o | o |  | o | o | o |  | o | o | o | o | o | o | o | o |  | o | o | o | o | o | o |
|  | **executable statements:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 93 | WHERE |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 94 | FORALL |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 95 | EXIT, CYCLE |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  | + | + |  |  |  | + | + |  |
| 96 | DO [label] [WHILE] .. ENDDO |  | + | + |  |  | + | @ | + | + | + | + | + | + |  |  | + | + |  | + | + | + | + | + |
| 97 | SELECT CASE |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  | + | + |  |  |  | + | + |  |
| 98 | debug packet statements |  |  | + | + |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |
| 100 | named constructs |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  | + |  |  |  |  |  |  |
| 101 | Watcom constructs |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |
| 102 | REMOTE BLOCK, EXECUTE |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |
|  | **general syntax:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 109 | [...] array constructor |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 110 | .XOR. exclusive or as .NEQV. | o | o |  |  | o | o | o | o | o |  | o | o | o |  |  | o |  | o | o |  | o | o |  |
| 111 | alternate relational operators <, ==, etc. |  |  | + |  |  |  |  |  |  |  |  |  |  |  | + |  | + |  |  |  |  | + | + |
| 112 | alternate return label &label |  | o |  |  |  |  |  | o | o | o | o | o | o | o |  |  |  |  |  |  |  |  |  |
| 113 | alternate return label $label |  |  |  |  |  | o |  |  |  |  |  |  |  | o |  |  |  |  |  |  |  |  |  |
| 114 | RETURN in main as STOP |  |  | o |  |  |  |  |  |  |  | o |  |  | o | o | o |  |  |  |  |  |  |  |
| 115 | null-arguments | + | + |  |  |  |  |  |  |  | + | + | + |  |  |  |  |  |  |  |  |  |  |  |
| 116 | array expressions, but no dummy or alloc. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |
| 117 | F90 array expressions and sections |  |  |  |  |  |  | + |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |
| 118 | constant arrays,constructors and substr. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 120 | keyword actual arguments |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 121 | zero sized data objects |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | type checking: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 125 | mixing of DP and COMPLEX in expressions | + | + | + | + | + |  | + | + | + |  | + | + |  | + | + | + |  |  | + | + | + | + | + |
| 126 | string argument compatible with Hollerith | o | o |  | o | o |  |  |  |  |  | o | o |  |  | o |  |  |  | o | o |  | o | o |
| 127 | strings can be assigned to INT/REAL/LOG | o | o |  |  |  |  |  |  | o |  | o | o | o |  |  |  |  |  |  | o |  | o | o |
| 128 | strings can be ass. to BYTE and LOGICAL*1 | o | o |  |  |  |  |  |  | o |  | o | o | o |  |  |  |  |  |  |  |  | o |  |
| 129 | boz constants can be used in expressions | + | + |  |  | + | + | + |  | + |  | + | + | + | + | + |  |  |  |  | + |  |  | + |
| 130 | boz constants in PARAMETER statement | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + | + |
| 131 | equivalence of numeric and character | o | o | o |  | o | o | o |  |  | o | o | o |  | o | o | o |  | o | o | o | o | o | o |
| 132 | real array indices and substring expressions | o | o | o |  | o |  |  |  | o |  | o | o | o | o |  | o |  |  |  |  |  |  |  |
| 133 | i and l const. comp. with shorter dummy | + | + |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  | o |
|  | **I/O statements:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 140 | ACCEPT, TYPE | + | + |  |  |  |  |  | + | + | + | + | + | + |  |  |  |  |  | + |  |  | + |  |
| 141 | INPUT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |
| 142 | ENCODE, DECODE | o | o |  |  |  |  | o | o | o | o | o | o | o | o |  |  |  |  | o |  |  | o |  |
| 143 | FIND, DEFINE FILE | o | o |  |  |  |  |  |  | o |  |  | o | o | o |  |  |  |  |  |  |  |  |  |
| 144 | direct access (lun’record) | o | o |  |  |  | o |  |  |  | o |  |  |  | o |  |  |  |  |  |  |  |  |  |
| 145 | READ, PRINT, INPUT without format |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | o |  |  |  |  |  |  |
| 146 | READ(KEY=) REWRITE, DELETE |  | + | + |  |  |  |  |  | + |  |  | + | + |  |  |  |  |  |  |  |  |  |  |
| 147 | LOCKING |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |
| 148 | UNLOCK |  | + |  |  |  |  |  |  | + |  |  | + | + |  |  |  |  |  |  |  |  |  |  |
|  | **I/O:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 155 | NUM= in READ |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 156 | list directed on internal file | + | + | + |  |  |  |  |  | + | + | + | + | + |  |  |  |  |  | + | + | + |  | + |
| 157 | F90 nonadvancing I/O |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 158 | Formatted derived type I/O |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | **OPEN/CLOSE/INQUIRE specifiers:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 165 | RECL= for sequential files | + | + |  | + | + | + |  | + |  |  |  | + |  |  | + |  | + |  |  | + | + |  |  |
| 166 | RECL= not required if STATUS=’OLD | + | + |  | + |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  | + |  |  |  |
|  | **format specifiers and edit descriptors:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 175 | noncharacter array name allowed | o | o | o | o | o |  |  | o |  | o | o | o |  | o | o | o |  |  |  | o | o |  |  |
| 176 | variable length fields <...> | + | + |  |  |  |  |  |  | + |  | + | + | + |  |  |  |  |  |  | + |  |  |  |
| 177 | aEw.dDe double precision exponent |  |  | + |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  | + |  |  |
| 178 | aQw[.d] quadruple precision mantissa |  |  | + |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 179 | aOw[.m] octal edit descriptor | + | + |  |  | + | + | + | + | + | + | + | + | + | + |  |  | + |  | + | + |  | + | + |
| 180 | aZw hex edit descriptor |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  | + | + |  | + |  | + |  |  |
| 181 | aZw[.m] hexadecimal edit descriptor | + | + |  | + | + | + | + | + | + | + | + | + | + | + | + |  |  | + |  | + |  | + | + |
| 182 | aR[w] char edit descriptor |  |  |  |  |  |  | o |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |
| 183 | \ edit descriptor |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + | + | + | + |  | + | + | + |  |
| 184 | Q edit descriptor | + | + |  |  |  |  |  | + | + | + | + | + | + |  |  |  | + |  | + |  |  | + |  |
| 185 | $ edit descriptor | + | + |  |  |  |  | + | + | + | + | + | + | + |  |  | + | + |  | + | + | + | + | + |
| 186 | aBw[.m] binary edit descriptor |  |  |  |  |  |  | + |  |  |  |  |  | + |  |  |  |  |  |  | + |  | + |  |
| 189 | Zero field width in edit descriptor |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | **compiler directives:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 200 | INCLUDE | + | + | + | + |  | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
| 201 | OPTIONS |  | + |  |  |  |  |  | + | + | + |  | + | + |  |  |  |  |  | + | + |  |  |  |
| 203 | OPTION [N]BREAK |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |
| 204 | EJECT |  | + |  | + |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |
| 205 | [NO]LIST |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 206 | COMPILER(... |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

*If extensions 40 and 42 are both enabled backslash editing is only applied
for ’xxx’C-strings.

**When extension 67 is enabled, the Salford variant of STDCALL is accepted.
