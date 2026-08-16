---
title: "map_read"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/map_read.html"
content_id: "f9GEKRgMUFt~lqcWhhOhMg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:45.140394+00:00"
---

# map_read

**Languages: JavaScript**

The `map_read` directive indicates that a function call acts like a
property *read* where one of its arguments is the object whose property is read and
another is the name of the property. The return value of the function is the result of
the property *read*.

## Fields

This directive uses the following fields:

`map_read`
:   Specifies a CallsiteSet that identifies function call
    sites to which this directive applies.

`map`
:   Specifies a ParamIn value that indicates which argument
    is the object whose property is being read.

`key`
:   Specifies a ParamIn value that indicates which argument
    is the name of the property that is read from `map`.

    This directive only applies if the argument indicated by
    `key` is a string literal.

## Examples

**JavaScript example:**

The following directive indicates that `localStorage.getItem(obj,
"prop")` reads property `"prop"` from
`localStorage`, just as `localStorage.prop`
would.

```
{
    "map_read" : {
        "call_on" : {
            "read_path_off_global" : [
                { "property" : "localStorage" },
                { "property" : "getItem" }
            ]
        }
    },
    "map" : "this",
    "key" : "arg1"
}
```
