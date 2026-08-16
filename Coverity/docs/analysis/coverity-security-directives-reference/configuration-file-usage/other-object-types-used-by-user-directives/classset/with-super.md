---
title: "with_super"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/with_super.html"
content_id: "pTUIdowQdtLG2K3fkDPdug"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:16.106186+00:00"
---

# with_super

A `with_super ClassSet` locates classes within the
`with_super` set that are categorized as a super-class or
super-interface.

## Fields

This kind of `ClassSet` object has a single field:

`with_super`
:   A ClassSet value. A `with_super ClassSet`
    matches all class types with a super-class or super-interface that are
    members of the `with_super` set.

## Examples

The following example matches all subclasses of `java.util.Collection`.

```
{ "with_super": { "named": "java.util.Collection" } }
```
