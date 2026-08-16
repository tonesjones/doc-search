---
title: "from_callsite"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/from_callsite.html"
content_id: "hZ7KSxoMX17E73Orl5Oqkg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:32.947259+00:00"
---

# from_callsite

**Languages: JavaScript**

A `from_callsite ReadableProgramData` value identifies readable values
produced by call sites.

## Fields

The `from_call_site ReadableProgramData` object has the following
fields:

`from_call_site`
:   A CallsiteSet value that identifies call sites of
    interest.

`output`
:   A ParamOut value that identifies a base value passed in
    or returned from a call site.

`path`
:   (Optional) a non-empty array of AccessPathElement
    values. This is an access path to apply to the base value.

    If no `path` field is specified, then the readable value
    is the base value indicated by the `output` field. Adding
    a `path` field indicates a readable value along the
    access path that is off of the base value.

## Examples

```
{
   "from_callsite" : { 
      "call_on" : { 
         "read_off_any" : [ { "property" : "exampleCall" } ] 
      } 
   },
   "output" : "return",
   "path" : [ { "property" : "f"}, { "property" : "g" } ]
}
```

The `from_callsite`
`ReadableProgramData` value above will match the readable value
`exampleCall().f.g` based off of the return value of this call
site:

```
 exampleCall();
```
