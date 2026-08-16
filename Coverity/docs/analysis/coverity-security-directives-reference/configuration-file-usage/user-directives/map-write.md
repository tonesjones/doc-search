---
title: "map_write"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/map_write.html"
content_id: "I4iLIoL7e7W3w2XlmogW1Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:45.811227+00:00"
---

# map_write

**Languages: JavaScript**

The `map_write` directive indicates that a function call acts like a
property write where one of its arguments is the object whose property is written,
another is the name of the property, and a third is the value to write to that
property.

## Fields

This directive uses the following fields.

`map_write`
:   Specifies a CallsiteSet that identifies function call
    sites to which this directive applies.

`map`
:   Specifies a ParamIn value that indicates which argument
    is the object whose property is being written.

`key`
:   Specifies a ParamIn value that indicates which argument
    is the property of `map` that is being overwritten.

    This directive only applies if the argument indicated by
    `key` is a string literal.

`value`
:   Specifies a ParamIn value that indicates which argument
    is the value being written.

## Examples

The following directive indicates that `localStorage.setItem(obj, "prop",
value)` writes `value` to property
`"prop"` of `localStorage` just as
`localStorage.prop = value` would.

```
{
    "map_write" : {
        "call_on" : {
            "read_path_off_global" : [
                { "property" : "localStorage" },
                { "property" : "setItem" }
            ]
        }
    },
    "map" : "this",
    "key" : "arg1",
    "value" : "arg2"
},
```
