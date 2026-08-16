---
title: "The reference structure or call tree"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-reference-structure-or-call-tree.html"
content_id: "GgPXavrwCPboJCodw3nFZA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:51.080216+00:00"
---

# The reference structure or call tree

Coverity Fortran Syntax Analysis can present the call tree in the listing file, or store
it in xml format so you can browse and use it for further analysis or documentation. In
producing the call tree, Coverity Fortran Syntax Analysis expands only one copy of each
subtree for the sake of brevity. This behavior can be overridden by specifying multiple
root nodes; the tree will be expanded at each such root node.

-shref
:   Show the reference structure.

-shref *root list*
:   Show the reference structure for the roots specified. The specified roots
    must be separated by a ”;”.

If the `-anref` option is in effect Coverity Fortran Syntax Analysis also
analyses the tree. In that case, procedures that are referenced recursively but are not
declared as such, or declared to be recursive but not referenced recursively are
spotted.

Unsaved common blocks and module variables which are not specified in the root of the
referencing program units are reported. From Fortran 2008 on, saving is the default
behavior and most compilers will store those objects statically. However, in earlier
levels of the standard, failing to save such objects is not standard conforming and a
potential risk when porting the program to another platform.
