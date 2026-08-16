---
title: "Cross references of public module derived types"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cross-references-of-public-module-derived-types.html"
content_id: "GTRg~nHQQfE7nhAA~iiU9Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:50.402830+00:00"
---

# Cross references of public module derived types

Cross references of public module derived types are presented if a listing file has been
requested and the `-shmodtyp` is in effect.

All public derived types of each module for which a cross-reference table is requested
are listed with all subprograms in which the derived type is used. If a derived type is
used in one or more module procedures of the module in which the derived type is used,
the module name is listed instead of the these individual module procedures.

Because the amount of information can be huge if you have many modules with many public
derived types, Coverity Fortran Syntax Analysis’s internal tables can easily become
full. In that case you have to split up the process in several runs in which you request
the cross references of the derived types of a limited number of modules at a time. The
optimal procedure is to compose a Coverity Fortran Syntax Analysis library file first
and to analyze this library file repeatedly.
