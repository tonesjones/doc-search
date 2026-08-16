---
title: "Limitations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/limitations.html"
content_id: "XTlcJAKDrfZ0zCOquGW5UA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:32.245094+00:00"
---

# Limitations

Coverity Fortran Syntax Analysis is a static analyzer, therefore it cannot detect any
errors which manifest themselves at run time only. For example, a variable array index,
or variable character substring expression which is out of bounds, cannot be detected.
Likewise, the detection of operations on external files can hardly be checked without
executing the program. For example a file which has not been opened before usage, or a
variable logical unit not being used consistently, cannot be detected.

Coverity Fortran Syntax Analysis warns you, if possible, when a variable has not been defined
in a program unit, when a common-block object has not been defined in the program (use
the `-ancmpl` option to enable this feature), when an allocatable
variable has never been allocated, or when a pointer has never been associated to a
target or procedure. However, if an object is used as an input/output actual argument
Coverity Fortran Syntax Analysis cannot verify this. In a limited number of cases
Coverity Fortran Syntax Analysis reports when an item has been referenced, before it was
defined, allocated, or associated. However the path flow analysis to detect this is
limited. As soon as a labeled executable statement has been encountered and either a
forward reference to a label has been made, or we are in a construct, Coverity Fortran
Syntax Analysis cannot signal this kind of errors any more. So avoid labels and
`GOTO`s. This is another good reason to use `IF` and
`SELECT CASE` constructs as much as possible! By specifying the
`-rigorous` option Coverity Fortran Syntax Analysis will detect more
occurrences of ”referenced before defined” at the cost of more false alarms

Arrays, character variables and variables of derived type are treated as a single entity. The
individual array elements, substring elements or structure components are not checked
for unreferenced, undefined, or not allocated. This is not only to reduce the storage
and processing time requirements, but also because most array and substring elements are
referenced using variable array indices or substring values which cannot be verified
statically.

Recursive I/O attempts will only be detected in a limited number of cases. Coverity
Fortran Syntax Analysis does not compare the consistency of format strings with the
actual I/O list. This is because many I/O lists have implied `DO` loops
which generate a variable number of elements. Future versions of Coverity Fortran Syntax
Analysis may check format strings as far as possible.
