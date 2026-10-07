---
title: "named"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/named.html"
content_id: "koWWiolQvXh9UyafAMsxqw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:00.386188+00:00"
---

# named

A `named ClassSet` locates a class by name.

## Fields

This kind of `ClassSet` object has a single field:

`named`
:   Specifies a `ClassName` value. The `named
    ClassSet` matches this class with the mangled name in
    `named`. See the ClassName section for a description of the
    mangled name format.

## Examples

The following example matches the Java `String` class:

```
{ "named": "java.lang.String" }
```
