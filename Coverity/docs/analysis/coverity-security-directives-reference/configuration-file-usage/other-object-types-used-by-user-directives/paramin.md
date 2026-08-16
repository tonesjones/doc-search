---
title: "ParamIn"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/paramin.html"
content_id: "Az6F0UwUTxVgrxZ7WsVfvQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:31.020005+00:00"
---

# ParamIn

**Used by these directives:**
`map_read`, `map_write`,
`method_returns_param`,
`method_with_servlet_sinks_on_input`,
`xss_sanitizer_method`

**Used by these objects:**
`HtmlOutputContext`, `InputAndAccessPathSpecifier`,
`InputTaint`, `InputTag`, `InputValue`,
`MethodCallSpecifier`, `WritableProgramData`

A `ParamIn` value describes an input to a function call.

## Fields

This object can use the following fields:

`this`
:   When present, indicates the receiver object on instance methods.

`arg1`, `arg2`, ...
:   These fields represent the parameters (arguments) to the function.

    The first non-`this` parameter field is
    `arg1`, and subsequent argument fields are numbered
    in sequence.
