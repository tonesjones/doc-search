---
title: "Display of the reference structure"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/display-of-the-reference-structure.html"
content_id: "oda9RitTUufCEXPSBmgDig"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:41.990045+00:00"
---

# Display of the reference structure

All referenced procedures are presented in a call tree. For each program unit or
procedure each referenced procedure is presented only once and in order of occurrence in
the source code. The reference structure is static only and does not show the actual
sequence of calls during program execution. Module procedures are ”qualified” with the
name of the module from which they are referred. Renamed procedures are presented by
their ”use” name.

The lines are being numbered and when a sub tree has already been presented, a reference
is made to the line at which the sub tree was presented, for example:

```
1 PROGRAM
2	SUBR1
3		SUB2
4			FUN1
5			FUN2
6				FUN21
7	SUBR2
8		SUB2 > 3
```

For the reference structure all entries of a procedure are equivalent, so if an entry
with its call tree has been presented, all next entries referenced will refer to this
sub tree. Unreferenced entries with their call tree are presented as separate sub trees
and are numbered in a hierarchical way, for example:

```
1 PROGRAM
2	SUBR1
3	SUBR2
```

```
1.1 MAIN2
1.2	SUBR3
1.3	SUBR4
```

When long names are being used and the nesting is too deep for the reference structure to
fit on the page, the tree is continued as a separate sub tree and a reference is made to
the line at which the continued tree starts, for example:

```
1 PROGRAM LONG NAME
2	SUBROUTINE1_LONG_NAME
3		SUBROUTINE11_LONG_NAME
4			SUBROUTINE111_LONG_NAME > 1.1
5	SUBROUTINE2_LONG_NAME
```

```
1.1 >
1.2    SUBROUTINE1111_LONG_NAME
```

When a procedure has more references than Coverity Fortran Syntax Analysis can store in
its tables a message will be printed and the remaining referenced procedures with its
references will be printed in separate sub trees.
