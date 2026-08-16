---
title: "Global program analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/global-program-analysis.html"
content_id: "0wTyNa3rBhHZM3AXK4FppA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:14.905035+00:00"
---

# Global program analysis

`-ancmpl`
:   The complete program is analyzed and Coverity Fortran Syntax Analysis will
    flag unreferenced procedures, unreferenced and undefined common blocks,
    unreferenced and undefined common-block objects, unreferenced modules,
    unreferenced and undefined public module variables, unreferenced public
    module constants and unreferenced public module derived types. If the
    `-anref` option and the `-rigorous` are
    also in effect the call tree will be traversed to detect unsaved common
    blocks and modules with unsaved public data which are not specified in the
    root of referencing program units. See also Analysis of the reference structure, Verification of common blocks and Verification of modules. Default: `-nancmpl`.

`-anprg`
:   Verify the consistency of the global program. If this option is not in
    effect, only the individual

    program units are analyzed. See Global program analysis. Default:
    `-anprg`.

`-anref`
:   Analyze the reference structure. See also Reference structure (Call tree). Default: `-anref`.

    Global program analysis options are global only and must be specified before
    the filename of any source or library file.
