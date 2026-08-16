---
title: "matching"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/matching.html"
content_id: "oHWN67664w9ViZwxcbD6Wg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:09.594989+00:00"
---

# matching

A `matching AnnotationSet` includes all uses of any Java annotation or C#
attribute whose entire mangled class name matches the regular expression in the
`matching` string (a substring match is insufficient). See ClassName for a description of the mangled name format.

## Fields

A `matching AnnotationSet` has a single field called
`matching`:

`matching`
:   A JSON string that contains a Perl-style regular
    expression that specifies an analysis annotation class name
    to match.

## Examples

The following `matching AnnotationSet` example matches uses of
annotation classes named `EntryPoint` in any package.

```
{ "matching": ".*EntryPoint" }
```
