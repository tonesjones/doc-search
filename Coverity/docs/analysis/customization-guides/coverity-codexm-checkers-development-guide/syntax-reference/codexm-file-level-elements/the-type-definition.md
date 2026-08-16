---
title: "The type-definition"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-type-definition.html"
content_id: "Pq6LrhgyVV8k0h1__Sizsw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:19.389505+00:00"
---

# The type-definition

With a `type-definition` you can define a name for a new type based on one of the standard CodeXM types.

You might want to use a `type-definition` to define a special-purpose type; for example, a specialized
`enum` or `record` type.

## Syntax

The type definition is introduced by the `typedef` keyword.
This is followed by an identifier that gives the new type its name.
Following that is an equals sign ( `=` ), and then the name of the base type.

  
 [image: Syntax diagram, type-definition]   

```
type-definition ::=
    'typedef' identifier '=' type
```
