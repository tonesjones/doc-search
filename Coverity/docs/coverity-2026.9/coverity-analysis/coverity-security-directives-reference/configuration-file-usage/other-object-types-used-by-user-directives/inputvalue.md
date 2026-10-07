---
title: "InputValue"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/inputvalue.html"
content_id: "YQ2O2JNf9JFsq9R6ZDp24Q"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:00.833796+00:00"
---

# InputValue

**Used by these directives:**
`async_method`, `local_callback`

An `InputValue` indicates that some argument at a call site flows into
some parameter of a callback.

## Fields

This object uses the following fields:

`value`
:   A ParamIn value that indicates the call site
    argument that flows to the callback's `input`
    parameter.

`input`
:   A ParamIn value that indicates the parameter
    of the callback to which `value` flows.
