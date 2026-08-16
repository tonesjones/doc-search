---
title: "The pattern-type"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-pattern-type.html"
content_id: "LqTlHPoh56_FWUTL4WhcRA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:07.686180+00:00"
---

# The pattern-type

Patterns differ in the type of code element the pattern can be applied to
(that is, what the pattern matches)
and in what the pattern returns when it successfully finds a match.

## Syntax

The keyword `pattern` introduces the `pattern-type`.
This is followed by the name of the type that the pattern can be applied to, then followed by an arrow
( `->` ) introducing the name of the type the pattern returns on finding a match.

  
 [image: Syntax diagram, pattern-type]   

```
pattern-type ::=
    'pattern' applicable-type '->' type
```

## Details

The `applicable-type` must not be nullable,
though it *can* be the nullable type's non-nullable counterpart.
You can convert a nullable type to non-nullable; for example,
by using `NonNull`.
See The nullable-type.
