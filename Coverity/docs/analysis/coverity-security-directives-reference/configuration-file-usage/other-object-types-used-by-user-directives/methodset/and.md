---
title: "and"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/and.html"
content_id: "rjxXehH6Eknuz8m0umtbvQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:29.079005+00:00"
---

# and

An `and MethodSet` creates a new `MethodSet` by performing
a logical AND between methods in the source codes and methods in a specified array of
`MethodSet` values.

## Fields

The `and MethodSet` has a single field:

`and`
:   A JSON array of MethodSet values. The `and
    MethodSet` matches the intersection of the methods in the
    source and the methods matched by methods that are members of the
    `MethodSet` array.

## Examples

For example, the following `and MethodSet` matches methods in a
particular package that override a particular method.

```
{ "and": 
  [            
    { "overrides": { "named": "com.example.C.print(java.lang.String)void" } },
    { "matching": "com\\.example\\.package\\..*" } 
  ]
}
```

## See also

For additional details, see matching
and overrides.
