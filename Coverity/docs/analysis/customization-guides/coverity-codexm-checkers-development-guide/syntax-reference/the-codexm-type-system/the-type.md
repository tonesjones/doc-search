---
title: "The type"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-type.html"
content_id: "hjP7sNKaM9Elj_67VdhYXQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:58.788505+00:00"
---

# The type

The `type` is itself the root of the type system.

## Syntax

Declaring an object can be as simple as assigning a value to an identifier;
for example, assigning the identifier a literal numeric value or a string literal.
Other type declarations require more elaborate syntax;
for example, defining an `enum` or a `function-type`.

  
 [image: Syntax diagram, type]   

```
type ::=
      ( '(' type ')' )
    | builtin-type
    | collection-type
    | enum-type
    | function-type
    | globalset-type
    | named-type
    | node-type
    | nullable-type
    | pattern-type
    | record-type
```
