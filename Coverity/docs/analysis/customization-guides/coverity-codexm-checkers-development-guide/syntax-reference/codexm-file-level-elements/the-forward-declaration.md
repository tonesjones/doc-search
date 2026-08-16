---
title: "The forward-declaration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-forward-declaration.html"
content_id: "OFeS05mifRouICywkxw7lA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:15.074115+00:00"
---

# The forward-declaration

All identifiers must be declared before they are used.
With a `forward-declaration`, you can declare an identifier before you provide its detailed definition.

A forward declaration can be convenient, especially when you declare two or more entities whose definitions are interdependent.

## Syntax

The declaration is introduced by the keyword `declare`,
the identifier to declare, a colon ( `:` ),
and then the type the identifier will have when the declaration is completed.

  
 [image: Syntax diagram, forward-declaration]   

```
forward-declaration ::=
    'declare' identifier ':' type
```
