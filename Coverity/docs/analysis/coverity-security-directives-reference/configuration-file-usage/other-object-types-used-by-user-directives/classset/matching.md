---
title: "matching"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/matching.html"
content_id: "JbT6~vSF26MiX2FzNvSPpg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:15.447814+00:00"
---

# matching

The `matching ClassSet` includes any class whose entire mangled name matches the
regular expression in the `matching` string (a substring match is
insufficient). See the ClassName section for a description
of the mangled name format.

## Fields

This kind of `ClassSet` object has a single field:

`matching`
:   A JSON string that contains a Perl-style regular
    expression that specifies the class name to match.

## Examples

The following example matches classes with names that end with
`"Writer"` in the `com.example` package.

```
{ "matching": "com\\.example\\..*Writer" }
```
