---
title: "Cross references of common-block objects"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cross-references-of-common-block-objects.html"
content_id: "LtcqQC9HqCAqarJpGU95tA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:49.752552+00:00"
---

# Cross references of common-block objects

Cross references of common-block objects are presented if a listing file has been requested and
the `-shcom` option is in effect.

All objects of each common block for which a cross-reference table is requested are
listed with all subprograms in which the common-block object is used. A ”#” in front of
a subprogram name indicates that the common-block object is modified in that subprogram
directly or indirectly by an equivalenced object. Mind that if a common-block object is
used as an actual argument in a referenced subprogram and Coverity Fortran Syntax
Analysis has no knowledge of the usage, the common-block object may be modified even if
no ”#” is presented.

A cross-reference of common-block objects is only meaningful if the lists of objects at
the various occurrences of that common block have identical characteristics. The names
of the objects may not be the same in the various occurrences. The name of the object in
main or the first occurrence is presented.

Variables that are equivalenced with objects in common are also listed. They are
associated by their offset in the common block. A ”#” in front of a subprogram name
indicates in this part of the list that the common-block object is modified in that
subprogram directly.

If a common-block object is defined and referenced in a single subprogram only, the
object could be replaced by a local variable, or record.

Because the amount of information can be huge if you have many common blocks with many
objects, Coverity Fortran Syntax Analysis’s internal tables can easily become full. In
that case you have to split up the process in several runs in which you request the
cross references of the objects of a limited number of common blocks at a time. The
optimal procedure is to compose a Coverity Fortran Syntax Analysis library file first
and to analyze this library file repeatedly.
