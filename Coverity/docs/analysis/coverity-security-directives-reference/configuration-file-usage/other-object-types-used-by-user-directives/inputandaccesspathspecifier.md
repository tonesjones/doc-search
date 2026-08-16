---
title: "InputAndAccessPathSpecifier"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/inputandaccesspathspecifier.html"
content_id: "Djc5Ussa41z55V7_sKfHxw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:19.980547+00:00"
---

# InputAndAccessPathSpecifier

**Used by the following directives:**
`dataflow_through_call_site`

An `InputAndAccessPathSpecifier` object uses a path to locate an input
value.

## Fields

This object uses the following fields:

`input`
:   A ParamIn value. This specifies a base value that is input to
    the call site. Without a `path` entry, this value is the
    input value.

`path`
:   (Optional) A non-empty array of AccessPathElement
    values. When present, the input value is found on this access path,
    using the base value.
