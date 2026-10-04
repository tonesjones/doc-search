---
title: "ParamOut"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/paramout.html"
content_id: "6mqiGo8KkZvlRnuXfLT5aw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:01.442680+00:00"
---

# ParamOut

**Used by these directives:**
`method_with_servlet_sinks_on_output`,
`xss_sanitizer_method`

**Used by these objects:**
`CallsiteSet`, `MethodCallSpecifier`,
`OutputAndAccessPathSpecifier`,
`ReadableProgramData`

A `ParamOut` value describes an output of a function call.

## Fields

This object can use the following fields:

`return`
:   Indicates the function’s return value.

`this`
:   When present, indicates the receiver object on instance methods.

`arg1`, `arg2`, ...
:   These fields represent the parameters (arguments) to the function.

    The first non-`this` parameter field is
    `arg1`, and subsequent argument fields are numbered
    in sequence.
