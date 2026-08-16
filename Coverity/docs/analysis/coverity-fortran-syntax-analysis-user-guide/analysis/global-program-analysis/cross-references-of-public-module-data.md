---
title: "Cross references of public module data"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cross-references-of-public-module-data.html"
content_id: "0z~EFCaX1tqfjkVKTlZJjg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:51.052902+00:00"
---

# Cross references of public module data

Cross references of public module data are presented if a listing file has been
requested and the `-shmodvar` is in effect.

All public
constants and variables of each module for which a cross-reference table is
requested are listed with all subprograms in which the module constant or
variable is used. If a module constant or variable is used in one or more module
procedures of the module in which the constant or variable is specified, the
module name is listed instead of the these individual module procedures.

A
”#” in front of a subprogram name indicates that the variable is modified
directly in that subprogram. Mind that if a variable is used as an actual
argument in a subprogram, the variable may be modified indirectly.

Because
the amount of information can be huge if you have many modules with many public
variables, Coverity Fortran Syntax Analysis’s internal tables can easily become
full. In that case you have to split up the process in several runs in which you
request the cross references of the variables of a limited number of modules at a
time. The optimal procedure is to compose a Coverity Fortran Syntax Analysis library
file first and to analyze this library file repeatedly.
