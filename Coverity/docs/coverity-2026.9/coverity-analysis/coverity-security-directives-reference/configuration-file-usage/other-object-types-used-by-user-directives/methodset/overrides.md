---
title: "overrides"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/overrides.html"
content_id: "QjayiXpfxFZMP0I93YmE0w"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:01.197835+00:00"
---

# overrides

An `overrides MethodSet` specifies a `MethodSet` to match
any method that overrides a method in `overrides`. This includes methods
in `overrides` itself.

## Fields

The `overrides MethodSet` has a single field:

`overrides`
:   A MethodSet. If a method in this set overrides a method in
    `overrides`, the overridden method is matched.

## Examples

For example, the following `overrides MethodSet` matches methods such
as `java.util.ArrayList.add(java.lang.Object)boolean`:

```
{ "overrides": 
  { "named": "java.util.Collection.add(java.lang.Object)boolean" } }
```
