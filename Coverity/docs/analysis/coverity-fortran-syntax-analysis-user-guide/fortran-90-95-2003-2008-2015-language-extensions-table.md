---
title: "Fortran 90/95/2003/2008/2015 language extensions table"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/fortran-90/95/2003/2008/2015-language-extensions-table.html"
content_id: "5Sg2HuuVdZYUF2CWqBplKg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:31.583088+00:00"
---

# Fortran 90/95/2003/2008/2015 language extensions table

| no. |  | F2003 | F2008 | F2015 | Cray | NAG | XLF | Dec-95 | FTN95 | LF95 | MSF | FUJ | SG95 | SF95 | OF95 | HP95 | INT | CVF | AB95 | gfort | g95 | PATH | PGI03 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **maxima in lay-out:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | max. number of characters per line | 132 | 132 | 132 | 132 | 132 | 132 | 132 | 132 | 132 | 132 | 255 | 132 | 132 | 132 | 254 | 132 | 132 | 132 | 132 | 132 | 132 | 132 |
|  | max. number of cont. lines (fixed) | 255 | 255 | 255 | @ | 255 | 255 | 99 | 19 | 19 | 99 | @ | 99 | 99 | 999 | 255 | 511 | 511 | 99 | @ | @ | 255 | @ |
|  | max. number of cont. lines (free) | 255 | 255 | 255 | @ | 255 | 255 | 99 | 39 | 39 | 99 | @ | 99 | 99 | 999 | 255 | 511 | 511 | 99 | @ | @ | 255 | @ |
|  | max. length of names | 63 | 63 | 63 | 63 |  | 250 | 31 | 63 | 240 | 31 | 31 | 32 | 31 | 127 | 255 | 255 | 63 | 31 |  |  | 63 | 63 |
|  | max. length of subprogram names | 63 | 63 | 63 | 63 |  | 250 | 31 | 63 | 240 | 31 | 31 | 32 | 31 | 127 | 255 | 255 | 63 | 31 |  |  | 63 | 63 |
|  | max. length of common-block names | 63 | 63 | 63 | 63 |  | 250 | 31 | 63 | 240 | 31 | 31 | 32 | 31 | 127 | 255 | 255 | 63 | 31 |  |  | 63 | 63 |
|  | **type length modifiers:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | INTEGER *1 |  |  |  | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
|  | INTEGER *2 |  |  |  | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
|  | INTEGER *4 |  |  |  | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
|  | INTEGER *8 |  |  |  | + | + | + | + | + | + |  | + | + |  |  | + | + | + |  | + | + | + | + |
|  | REAL *4 |  |  |  | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
|  | REAL *8 |  |  |  | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
|  | REAL *10 |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  | + |  |  | + | + | + |  |
|  | REAL *16 |  |  |  | + | + | + | + |  | + | + | + | + | + | + | + | + |  |  |  |  |  |  |
|  | COMPLEX *8 |  |  |  | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
|  | COMPLEX *16 |  |  |  | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
|  | COMPLEX *20 |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  | + |  |  | + | + | + |  |
|  | COMPLEX *32 |  |  |  | + | + | + | + |  | + |  | + | + | + | + |  | + |  |  |  |  |  |  |
|  | LOGICAL *1 |  |  |  | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
|  | LOGICAL *2 |  |  |  | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
|  | LOGICAL *4 |  |  |  | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
|  | LOGICAL *8 |  |  |  | + | + | + | + |  | + |  | + | + |  |  | + | + | + |  |  | + | + | + |
|  | **maximum length of type CHARACTER:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | CHARACTER *255 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | CHARACTER *511 |  |  |  |  |  | @ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | CHARACTER *16384 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | CHARACTER *32767 |  |  |  |  | + | @ |  | + |  | + | + |  | + | + | + | + | + |  |  |  |  |  |
|  | CHARACTER *65280 |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | CHARACTER *65535 |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |
|  | CHARACTER *2147483647 |  |  |  | + |  |  |  |  | + |  |  |  |  |  |  |  |  | + | + | + | + | + |
|  | default source file name extension |  |  |  | f |  | f |  |  |  | FOR | f | f | f | f | f |  |  |  | f | f | f | f |
|  | default include file name extension |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | include list option delimiter |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | compiler directive string |  |  |  |  |  |  |  |  |  | $ |  |  |  |  | $ | !DIR$ | $ | $ | # | # | # | # |
|  | free form continuation character |  |  |  |  |  |  |  |  |  |  | - |  |  |  |  |  |  |  |  |  |  |  |
|  | free form 1st column comment char. |  |  |  |  |  |  |  |  |  |  | " |  |  |  |  |  |  |  |  |  |  |  |
|  | **lay-out:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 | debug lines (D) |  |  |  |  |  | + | + |  |  |  |  |  |  |  | + | + | + | + |  | + |  | + |
| 3 | debug lines (A-Z) |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | tabs |  |  |  | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + | + |
| 5 | formfeeds |  |  |  |  |  |  | + |  | + | + |  | + | + | + | + | + | + | + |  | + | + | + |
| 7 | cpp preprocessing |  |  |  |  |  | + |  | + |  |  |  |  | + | + |  | + |  |  | + | + | + | + |
| 8 | in-line comment after @ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 | in-line comment {...} |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 | any character allowed as continuation charac- ter |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  | + | + |  |  |  |  |  |
| 12 | line may start with; |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  | + |  |
|  | **names:** |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 13 | names with $ |  |  |  | + |  | + | + |  | + | + | + |  |  |  | + | + | + | + | + | + |  | + |
| 15 | names beginning with $ |  |  |  |  |  | + |  |  |  | + | + |  |  |  |  | + | + | + |  |  |  |  |
| 16 | built-in functions beginning with % |  |  |  | + |  | + | + |  |  | + |  | + |  |  | + | + | + | + |  | + | + | + |
| 17 | names with @ |  |  |  |  |  |  |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 18 | names beginning with _ |  |  |  |  |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | **constants:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 21 | REAL*16 with Q-exponent |  |  |  |  |  | + |  |  |  |  |  | + |  |  |  | + |  |  | + | + | + |  |
| 22 | named constants in complex constants | + | + | + | + | + | + | + | + | + |  |  |  |  | + | + | + |  |  | + | + | + | + |
| 23 | Hollerith |  |  |  | + |  | + | + |  |  | + | + | + | + | + | + | + | + | + | + | + | + | + |
| 26 | X’xxx’, X”xxx” hex |  |  |  | + |  | + | + |  |  |  | + |  | + | + |  |  |  |  | + | + |  |  |
| 28 | ’xxx’B, ”xxx”B binary |  |  |  |  |  | + | + |  |  |  |  |  |  |  |  | + |  |  | + |  |  |  |
| 29 | ’xxx’O, ”xxx”O octal |  |  |  | + |  | + | + |  |  |  | + |  |  |  | + | + |  |  | + |  |  | + |
| 30 | ’xxx’X, ”xxx”X hex |  |  |  | + |  | + | + |  |  |  | + |  |  |  | + | + | + |  | + |  |  | + |
| 31 | ’xxx’Z, ”xxx”Z hex |  |  |  |  |  | + | + |  |  |  |  |  |  |  |  |  | + |  | + |  |  |  |
| 32 | Oxxx octal |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 33 | Zxxx hex |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 34 | xxxB octal |  |  |  | + |  |  |  |  |  |  |  |  | + | + |  |  |  |  |  |  |  |  |
| 35 | [-]:xxx hex |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 36 | "xxx octal |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 37 | $xxx hex |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 38 | [radix]#value |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  | + | + |  |  |  |  |  |
| 39 | nRxxx radix 50 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 40 | C-string: ’xxx’C* |  |  |  |  |  |  |  |  |  |  |  |  | o | o | + | + | + |  |  |  |  |  |
| 41 | Length modifier suffix: B,S,I (FTN77) |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |
| 42 | C-string: \ editing* |  |  |  |  |  | + |  |  |  |  | + |  |  |  | o | + | + | + | + | + |  | + |
|  | **specification statements:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 44 | STATIC |  |  |  |  |  | + | + |  |  | + |  |  |  |  | + | + | + | + |  |  |  |  |
| 46 | AUTOMATIC |  |  |  |  |  | + | + |  |  | + |  |  |  |  | + | + | + | + |  |  |  |  |
| 47 | BOOLEAN |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |
| 48 | BYTE |  |  |  |  |  | + | + |  | + |  |  |  |  |  | + | + | + | + |  | + |  | + |
| 49 | C EXTERNAL |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |
| 50 | DOUBLE COMPLEX |  |  |  | + | + | + | + | + | + |  |  |  |  |  | + | + | + | + | + | + |  | + |
| 52 | IMPLICIT UNDEFINED |  |  |  |  |  | + |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |
| 53 | IMPLICIT AUTOMATIC/STATIC |  |  |  |  |  | + |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |
| 331 | IMPLICIT(EXTERNAL,TYPE) |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 55 | integer (Cray) POINTER |  |  |  | + |  | + | + |  |  |  |  | + | + | + | + | + | + | + | + |  | + | + |
| 56 | LC, BC, HC, MS, MSC EXTERNAL |  |  |  |  |  |  |  |  |  | + | + |  |  |  |  |  |  |  |  |  |  |  |
| 61 | VIRTUAL |  |  |  |  |  | o | o |  |  |  |  |  |  |  | o | o |  |  |  |  |  |  |
| 62 | VOLATILE | + | + | + | + | + | + | + |  | + |  |  |  |  | + | + | + | + | + | + | + | + | + |
| 64 | DEFINE |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 66 | DLL IMPORT, DLL EXPORT |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 67 | C EXTERNAL, Salford STDCALL |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 68 | specif.functions in specif.expressions | + | + | + |  |  |  |  |  |  |  | + | + | + | + | + | + |  | + | + | + | + | + |
| 69 | [..] type attributes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 70 | init. of var. in type spec.stmnt /../ |  |  |  |  |  | + | + |  | + |  |  |  |  |  | + | + | + | + | + |  |  | + |
| 71 | length modifier after dimension |  |  |  |  |  |  |  |  |  | + | + |  |  |  |  |  |  |  |  |  |  |  |
| 72 | PARAMETER symbol=constant |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  | + | + | + |  |  |  | + |
| 77 | IMPLICIT mixed with specification stmnts. |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |
| 81 | Record fields and records in DATA |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 82 | Subobjects of constants in DATA | + | + | + |  |  | + |  |  |  |  | + | + | + | + | + | + |  | + | + | + | + | + |
| 83 | intrinsic functions in DATA | + | + | + |  |  | + |  |  |  |  | + | + | + | + | + | + |  | + | + | + | + | + |
| 84 | pointers can be initialized in a DATA stmnt. | + | + | + |  |  | + |  |  |  |  | + | + | + | + | + | + |  | + | + | + | + | + |
| 239 | PROTECTED | + | + | + | + | + | + |  |  |  |  |  |  |  | + |  | + |  | + | + |  |  | + |
| 240 | C-binding and enumerators | + | + | + | + | + | + |  |  |  |  |  |  |  | + | + | + |  |  | + | + | + | + |
| 241 | VALUE for scalars | + | + | + | + | + | + |  |  |  |  |  |  |  | + |  | + |  |  | + | + | + | + |
| 242 | VALUE for arrays |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 243 | type parameter enquiry | + | + | + | + | + | + |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |
| 244 | TS 29113, further interop of Fortran with C |  |  | + | + | + | + |  |  |  |  |  |  |  |  |  | + |  |  | + |  |  |  |
| 251 | IMPORT statement | + | + | + | + | + | + |  |  |  |  |  |  |  | + | + | + |  |  | + | + | + |  |
| 333 | IMPORT,ONLY/NONE/ALL statement |  |  | + | + | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 252 | pointer INTENT attribute | + | + | + | + | + | + |  |  |  |  |  |  |  | + |  | + |  |  | + | + | + |  |
| 257 | renaming of operators in USE statement | + | + | + | + | + | + |  |  |  |  |  |  |  |  |  | + |  |  | + | + |  |  |
| 259 | allocatable scalars | + | + | + | + | + | + |  |  |  |  |  |  |  | + |  | + |  |  | + |  |  |  |
| 260 | deferred character length | + | + | + | + | + | + |  |  |  |  |  |  |  | + |  | + |  |  | + |  |  |  |
| 261 | F2003 specification and initialization expressions | + | + | + | + | + | + |  |  |  |  |  |  |  |  |  |  |  |  | + | + |  |  |
| 262 | PROCEDURE | + | + | + | + | + | + |  |  |  |  |  |  |  |  |  | + |  |  | + |  |  |  |
| 263 | mixing of subroutines and functions in generic |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + | + |  |  |  |  |  |
| 264 | allocatable dummy arguments (TR 15581) | + | + | + | + | + | + |  |  |  |  |  |  |  |  |  | + |  |  | + | + |  | + |
| 265 | CONTIGUOUS attribute |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
| 266 | implied-shape array |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
| 267 | initialization of pointer with target |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
| 268 | maximum rank 15 |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
| 269 | :: after PROCEDURE allowed |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  | + |  |  |  |
| 313 | F2003 extended NAMELIST | + | + | + | + | + | + |  |  |  |  |  |  |  |  |  | + |  |  | + |  |  | + |
|  | **derived types:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 59 | STRUCTURE, RECORD |  |  |  |  |  |  | + |  |  | + |  |  |  | + | + | + | + | + |  |  |  | + |
| 270 | type extension | + | + | + | + | + | + |  |  |  |  |  |  |  |  |  | + |  |  | + |  |  |  |
| 271 | parameterized derived type | + | + | + | + | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 272 | deferred binding and abstract type | + | + | + | + | + | + |  |  |  |  |  |  |  |  |  | + |  |  | + | + |  |  |
| 273 | polymorphic entities, CLASS statement | + | + | + | + | + | + |  |  |  |  |  |  |  | + |  | + |  |  | + |  |  |  |
| 274 | TYPE statement for intrinsic type |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
|  | **derived-type components:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 73 | /../ initialization of structure components |  |  |  |  |  |  | + |  |  |  |  |  |  |  | + | + | + |  |  |  |  | + |
| 108 | F95 initialization of structure components | + | + | + |  | + | + |  | + | + |  |  | + | + | + |  | + |  | + | + | + |  | + |
| 245 | allocatable structure components (TR 15581) | + | + | + | + | + | + |  |  |  |  |  |  |  | + |  | + |  |  | + | + | + | + |
| 247 | access spec. of components | + | + | + | + | + | + |  |  |  |  |  |  |  | + |  | + |  |  | + |  |  |  |
| 249 | procedure components | + | + | + | + | + | + |  |  |  |  |  |  |  |  |  | + |  |  | + |  |  |  |
| 250 | type bound procedures | + | + | + | + | + | + |  |  |  |  |  |  |  | + |  | + |  |  | + |  |  |  |
| 275 | empty type-bound-procedure-part |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 276 | list of type-bound-procedures |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
| 277 | omitting an all. comp. in a structure constructor |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 324 | public entities of private type | + | + | + |  |  |  |  |  |  |  |  |  |  | + |  | + |  |  | + |  |  | + |
| 328 | GENERIC statement (outside derived-type spec.) |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | **program units, subprograms, interfaces:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 214 | IMPURE |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
| 215 | INTERFACE TO |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  | + |  |  |  |  |  |
| 218 | PURE | + | + | + |  |  |  |  |  |  |  | + | + | + | + | + | + |  | + | + | + | + | + |
| 219 | ELEMENTAL | + | + | + |  |  |  |  |  |  |  | + | + | + | + | + | + |  | + | + | + | + | + |
| 334 | NON RECURSIVE |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 220 | argument list in PROGRAM statement |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 221 | [type[*len]] FUNCTION name |  |  |  | + |  | + | + |  |  | + | + | + |  |  | + | + | + | + | + | + |  | + |
| 222 | [type] FUNCTION name [*len] |  |  |  |  |  | 0 | 0 |  |  |  |  |  |  |  | o |  |  |  |  |  |  | + |
| 225 | Unisys internal subprograms |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 227 | END INTERFACE name |  |  |  |  | + | + |  |  |  |  | + | + | + | + | + | + |  | + | + | + | + | + |
| 228 | STDCALL |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  |
| 229 | recursive reference of all procedures allowed |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 230 | intrinsic modules: USE, [NON ]INTRINSIC :: | + | + | + | + | + | + |  |  |  |  |  |  |  | + | + | + |  |  | + | + |  | + |
| 231 | procedure pointers | + | + | + | + | + | + |  |  |  |  |  |  |  | + | + | + |  |  | + | + |  | + |
| 232 | SUBMODULE |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 233 | ABSTRACT INTERFACE | + | + | + | + | + | + |  |  |  |  |  |  |  |  |  | + |  |  | + |  |  |  |
| 234 | Data in main or module are saved implicitly |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 235 | allocatable function result (TR 15581) | + | + | + | + | + | + |  |  |  |  |  |  |  |  | + | + |  |  | + | + |  | + |
| 236 | defining interface of containing procedure | + | + | + | + | + | + |  |  |  |  |  |  |  |  |  | + | + |  | + | + |  |  |
| 237 | empty contains section |  | + | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
| 238 | END statement for internal and module procedure |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
|  | **arguments:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 112 | alternate return label &label |  |  |  |  |  |  | o |  |  |  |  |  |  |  | o |  |  |  |  |  |  |  |
| 113 | alternate return label $label |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 115 | null-arguments |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 320 | internal procedure as actual argument |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  | + |  |  |  |
| 321 | unall. actual arg. allowed for optional dummy |  | + | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
| 322 | target actual arg. assoc. with dummy pointer |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | **commons:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 85 | initialization of blank COMMON |  |  |  |  |  |  | o |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 86 | differing lengths for a named COMMON | + | + | + | o |  | o | o |  |  |  |  |  |  |  |  |  |  |  |  | o |  |  |
| 87 | initialization of COMMON not in BLOCK DATA |  |  |  | o |  |  | o |  |  |  |  |  |  |  | o |  |  |  |  |  |  |  |
|  | **executable statements:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 94 | FORALL |  |  |  |  | + | + | + | + | + |  | + | + | + | + | + | + | + | + | + | + | + | + |
| 98 | debug packet statements |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 99 | SELECT TYPE construct | + | + | + |  | + | + |  |  |  |  |  |  |  | + |  | + |  |  | + |  |  |  |
| 101 | Watcom constructs |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 102 | REMOTE BLOCK, EXECUTE |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 105 | ASSOCIATE | + | + | + | + | + | + |  |  |  |  |  |  |  |  |  | + |  |  | + |  |  |  |
| 106 | ERRMSG= in (DE)ALLOCATE | + | + | + | + | + | + |  |  |  |  |  |  |  | + |  | + |  |  | + |  |  |  |
| 299 | EXEC |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 300 | bounds/remapping in pointer assignment | + | + | + | + | + | + |  |  |  |  |  |  |  | + |  |  |  |  | + | + |  |  |
| 301 | transfering an allocation; typed allocation | + | + | + | + | + | + |  |  |  |  |  |  |  | + |  | + |  |  | + |  |  |  |
| 302 | SOURCE= specifier on ALLOCATE | + | + | + | + | + | + |  |  |  |  |  |  |  | + |  | + |  |  | + |  |  |  |
| 303 | MOLD= on ALLOCATE |  | + | + |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  | + |  |  |  |
| 304 | copy bounds and values from SOURCE and |  | + | + |  |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |
| 314 | MOLD | + | + | + | + |  | + |  |  |  |  |  |  |  | + |  | + |  |  | + |  |  | + |
|  | **allocation at assignment to an allocatable** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 305 | DO [label][,] [CONCURRENT].. ENDDO |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
| 306 | FORALL index kind specification |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 307 | BLOCK construct |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
| 308 | EXIT any construct |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
| 309 | STOP and ERROR STOP with constant expression |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
| 327 | SELECT RANK construct |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 329 | STOP and ERROR STOP with QUIET option |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 330 | STOP and ERROR STOP with variable stop code |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 332 | TS18508, Additional parallel features (TEAM) |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | **general syntax:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 310 | F2003 array constructor enhancements | + | + | + | + | + | + |  |  |  |  |  |  |  | + |  | + |  |  | + | + |  |  |
| 311 | co-array |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
| 312 | real and imag part-ref |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 315 | intrinsic assignment of def., ascii and iso char | + | + | + | + |  | + |  |  |  |  |  |  |  |  |  | + |  |  | + |  |  | + |
| 323 | reference of pointer function |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 109 | F2003 array constructor syntax: [..] | + | + | + | + | + | + |  | + |  |  |  |  |  | + | + | + |  |  | + | + | + |  |
| 110 | .XOR. exclusive or as .NEQV. |  |  |  | o |  | o | o |  |  | o |  |  |  |  | o | o | o |  |  |  |  |  |
| 114 | RETURN in main as STOP |  |  |  |  |  | o |  |  |  | o |  |  |  |  |  |  |  |  |  |  |  |  |
| 124 | F2003 structure constructors: comp. keywords | + | + | + | + | + | + |  |  |  |  |  |  |  | + |  | + |  |  | + | + |  |  |
|  | **type checking:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 126 | string argument compatible with Hollerith |  |  |  | o |  |  | o |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 127 | strings can be assigned to INT/REAL/LOG |  |  |  | o |  |  | o |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 128 | strings can be ass. to BYTE and LOGICAL*1 |  |  |  |  |  |  | o |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 129 | typeless (BOZ) can be used in expressions |  |  |  | + | + | + | + | + |  |  |  |  |  | + | + | + | + |  | + | + |  | + |
| 131 | equivalence of numeric and character |  |  |  | o |  | o | o |  |  | o |  |  |  |  | o | o | o |  |  |  |  |  |
| 132 | real array indices and substring expressions |  |  |  |  |  | o | o |  |  | o |  |  |  |  |  |  |  |  |  |  |  |  |
| 133 | i and l const. comp. with shorter dummy |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |
| 134 | passing character scalar actual to dummy array | + | + | + | + | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 135 | BOZ constants as arg. in some intr. procedures | + | + | + | + | + | + |  |  |  |  |  | + | + | + |  |  | + | + |  |  |  |  |
| 136 | intr. assignment of characters of different kinds | + | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
|  | **I/O statements:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 140 | ACCEPT, TYPE statement |  |  |  |  |  |  | + |  |  |  |  |  |  |  | + | + | + | + |  |  |  | + |
| 141 | INPUT statement |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 142 | ENCODE, DECODE statement |  |  |  | o |  |  | o |  |  |  |  |  |  |  | o | o | o |  |  |  |  |  |
| 143 | FIND, DEFINE FILE statement |  |  |  |  |  |  | o |  |  |  | o |  |  |  | o |  |  |  |  |  |  |  |
| 144 | direct access (lun’record) |  |  |  |  |  |  |  |  |  |  | o |  |  |  |  |  |  |  |  |  |  |  |
| 145 | READ, PRINT, INPUT without format |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 146 | READ(KEY=) REWRITE, DELETE |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  | + | + |  |  |  |  |  |
| 147 | LOCKING statement |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 148 | UNLOCK statement |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  | + | + |  |  |  |  |  |
| 149 | FLUSH statement | + | + | + | + | + | + |  |  |  |  |  |  |  | + |  | + |  |  | + | + | + |  |
| 155 | NUM= in READ |  |  |  |  |  | + |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |
| 156 | list directed on internal file |  |  |  |  | + | + |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |
| 157 | non-advancing i/o |  |  |  |  | + | + |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |
| 158 | formatted derived type i/o |  |  |  |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 159 | asynchronous i/o | + | + | + | + | + | + |  |  |  |  |  |  |  | + |  | + |  |  | + | + |  |  |
| 160 | stream access i/o | + | + | + | + | + | + |  |  |  |  |  |  |  | + |  | + |  |  | + | + |  |  |
| 161 | temporary i/o mode | + | + | + | + | + | + |  |  |  |  |  |  |  |  |  | + |  |  | + | + |  |  |
| 162 | IOMSG= specifier in all i/o statements | + | + | + | + | + | + |  |  |  |  |  |  |  |  | + | + |  |  | + | + |  |  |
| 163 | namelist i/o on internal file | + | + | + | + | + | + |  |  |  |  |  |  |  |  |  | + |  |  | + |  |  |  |
| 164 | recursive i/o | + | + | + | + | + | + |  |  |  |  |  |  |  |  |  | + |  |  | + | + | + |  |
|  | **OPEN/CLOSE/INQUIRE specifiers:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 165 | RECL= for sequential files |  |  |  |  | + | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 166 | RECL= not required if STATUS=’OLD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | **format specifiers and edit descriptors:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 175 | noncharacter array name allowed |  |  |  | o |  |  | o |  |  | o |  |  |  |  | o |  |  |  |  |  |  |  |
| 176 | variable length fields <...> |  |  |  |  |  | + | + |  |  | + |  |  |  | + |  | + | + |  |  |  |  |  |
| 177 | aEw.dDe double precision exponent |  |  |  |  |  | + |  |  |  |  |  |  |  |  | + |  | + |  |  |  |  |  |
| 178 | aQw[.d] quadruple precision mantissa |  |  |  |  |  | + |  |  |  |  | + |  |  |  | + |  |  |  |  |  |  |  |
| 182 | aR[w] char edit descriptor |  |  |  | + |  |  |  |  |  |  |  |  |  |  | + | + |  |  |  |  |  |  |
| 183 | \ edit descriptor |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  | + | + |  |  | + |  |  |
| 184 | Q edit descriptor |  |  |  |  |  | + | + |  | + | + |  |  |  |  | + | + | + | + |  |  |  | + |
| 185 | $ edit descriptor |  |  |  | + |  | + | + |  | + | + | + |  |  |  | + | + | + | + | + | + |  | + |
| 189 | zero field width in edit descriptors |  |  |  |  | + | + |  |  |  |  | + | + | + | + | + | + |  | + | + | + | + | + |
| 190 | derived type (DT) edit descriptor | + | + | + | + | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 191 | RU .. round edit descriptors | + | + | + | + | + | + |  |  |  |  |  |  |  | + | + | + |  |  | + |  |  |  |
| 192 | DC, DP decimal edit descriptors | + | + | + | + | + | + |  |  |  |  |  |  |  | + | + | + |  |  | + | + |  |  |
| 193 | comma after P optiona, if followed by repeat | + | + | + | + | + | + |  |  |  |  |  |  |  |  | + | + |  |  | + | + | + |  |
| 194 | g0 edit descriptor |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
| 195 | unlimited repeat of format list |  | + | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | + |  |  |  |
| 196 | EXw.d, EXw.dEe edit descriptor |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | **compiler directives:** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 201 | OPTIONS statement |  |  |  |  |  |  | + |  |  |  |  |  |  |  | + | + | + |  |  |  |  | + |
| 203 | OPTION BREAK statement |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 204 | EJECT statement |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 205 | [NO]LIST compiler directive |  |  |  |  |  |  |  |  |  | + |  |  |  |  |  |  |  |  |  |  |  |  |
| 206 | COMPILER(... |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
