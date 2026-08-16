---
title: "Verification of common blocks"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/verification-of-common-blocks.html"
content_id: "2SAzZIkVEYcrM7DCMUjU8Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:47.779591+00:00"
---

# Verification of common blocks

The type, size and list of objects of common blocks are compared with the occurrence in
the main program, if present, or with the first occurrence otherwise. The size of the
largest occurrence of the common block is presented in the cross-reference table. An
occurrence of a common block with a different list of objects will be flagged with the
message ”inconsistent list of objects”. If the `-rigorous` option has
been enabled each inconsistent object will be flagged separately. An object could differ
in type, type parameters, array length, array rank, or shape.

When the `-ancmpl` option is in effect and all occurrences of a common
block are identical, common-block objects which are not referenced, not defined, not
associated, or not defined before referenced will be listed. If the
`-rigorous` option has been enabled each common-block object which is
only conditionally defined before referenced is listed also.

When a common block has been specified in an include file, it should be included from the
same include file at all instances. If that is not the case an informational message
will be presented.

If the `-anref` option is also in effect the call tree will traversed to
detect unsaved common blocks which are not specified in the root of referencing program
units. See also Analysis of the reference structure.
