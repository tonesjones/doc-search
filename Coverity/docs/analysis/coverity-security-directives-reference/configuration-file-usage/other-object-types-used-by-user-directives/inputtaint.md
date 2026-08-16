---
title: "InputTaint"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/inputtaint.html"
content_id: "TKB4jhcaCsg4ei71t9rT2w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:20.618504+00:00"
---

# InputTaint

**Used by the following directives:**
`async_method`

An `InputTaint` value marks the parameter of a callback as tainted with a
specific taint kind.

## Fields

This object uses the following fields:

`input`
:   A ParamIn value that indicates the parameter
    to the callback that is tainted.

`taint_kind`
:   A TaintKind string value that
    specifies the kind of taint that `input` has.

`is_deep_taint`
:   (Optional) Specifies a JSON Boolean value.

    Setting this field to `true` indicates that properties of
    `input` are also tainted, along with the parameter
    itself.

    Not specifying this field is equivalent to setting it to
    `false`.

An `InputTaint` value is used together with identifying a callback.
The analysis considers the callback parameter given by `input` to be
tainted with taint of kind `taint_kind`. If
`is_deep_taint` is `true`, the analysis also
considers properties of that parameter object (including array elements, properties
of those properties, and so on) to be similarly tainted.
