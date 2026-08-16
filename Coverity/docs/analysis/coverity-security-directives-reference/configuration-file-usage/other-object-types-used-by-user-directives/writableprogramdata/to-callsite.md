---
title: "to_callsite"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/to_callsite.html"
content_id: "ALKmNEpVR1~m6nQu4dpW0w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:43.058085+00:00"
---

# to_callsite

A `to_callsite WritableProgramData` value identifies writable values
consumed by call sites.

## Fields

The `to_call_site WritableProgramData` object has the following
fields:

`to_callsite`
:   A CallsiteSet that identifies call sites
    of interest.

`input`
:   A ParamIn value that identifies a base value
    passed into the call site.

`path`
:   (Optional) An array of AccessPathElement values that
    specify an access path to apply to the base value.

    The `path` field is only allowed for JavaScript uses of
    `to_callsite WritableProgramData`.

    If no `path` field is specified, the writable value is the
    base value indicated by the `input` field. Adding a
    `path` field indicates a writable value along the
    access path off of the base value.

## Examples:

**JavaScript example:**

```
{
    "to_callsite" : { 
        "call_on" : {
            "read_off_any" : [ { "property" : "exampleCall" } ]
        }
    },
    "input" : "arg1",
    "path" : [ { "property" : "f"}, { "property" : "g" } ]
}
```

The `to_callsite WritableProgramData` value above will match the
writable value `passedInValue.f.g` when
`passedInValue` is passed into this call site:

```
exampleCall(passedInValue);
```
