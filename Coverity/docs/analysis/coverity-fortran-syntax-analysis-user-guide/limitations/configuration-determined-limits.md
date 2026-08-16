---
title: "Configuration determined limits"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuration-determined-limits.html"
content_id: "OhKsTwImXWIdPFnQsVysQQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:32.920559+00:00"
---

# Configuration determined limits

The tables used in Coverity Fortran Syntax Analysis to store all information have limited
sizes. The sizes of all internal tables will be specified in the following table.

These limits cannot be changed by the user. When a limit has been exceeded a system
message will be given. Analysis will proceed, but will no longer be complete.

|  |  |
| --- | --- |
| value | description |
| 255 | max. length of a file specification |
| 255 | max. length of an include filename |
| 512 | max. number of characters in an input record |
| 512 | max. number of characters in an output record |
| 25 | max. nesting of include files |
| 100 | max. nesting of modules |
| 50 | max. nesting of references in call-tree |
| 200 | max. number of library files |
| 1000 | max. number of (non-comment) lines in a statement |
| 25000 | max. number of characters in a statement |
| 8000000 | length of name table |
| 20000 | max. number of contexts in a program unit |
| 100 | max. nesting of structures + unions + maps |
| 16 | max. number of parameters of a derived type |
| 10000 | max. nesting of `DO` + `IF` + `ELSEIF` + `ELSE` + `SELECTCASE` + `CASE` |
| 7 | max. nesting of implied `DO` loops in `DATA` statement |
| 50 | max. nesting level in an expression |
| 2000 | max. number of objects being checked in an argument list, or equivalence list |
| 4000 | max. number of shape, bound, or vector values in an argument list, equivalence list, or common-block list |
| 16 | max. number of derived-type parameters for a derived type |
| 20000 | length of argument key list |
| 4000 | max. number of objects in a common-block list, or data list |
| 200000 | max. number of entries in the symbol table |
| 1000 | max. number of references in a cross-reference table presented |
| 1000000 | max. total number of references in the cross-reference tables |
| 1000 | max. number of non-analyzed procedures presented |
| 100 | max. number of messages that can be redefined |
| 25 | max. number of common blocks specified with the `-shcom` *com list* option |
| 25 | max. number of modules specified with the `-shmodtyp` *mod list* option |
| 25 | max. number of modules specified with the `-shmodvar` *mod list* option |
| 25 | max. number of roots specified with the `-shref` *root list* option |
| 25 | max. number of roots specified with the `-shmoddep` *root list* option |
| 25 | max. number of program units specified with the `-include` option |
| 50 | max. number of include directories specified with the `-I` option |
| 500 | max. maximum number of intrinsic procedures |
| 100 | max. maximum number of `OPEN`/`CLOSE`/`INQUIRE` keywords |
| 100 | max. maximum number of `OPEN`/`CLOSE`/`INQUIRE` value keywords |
