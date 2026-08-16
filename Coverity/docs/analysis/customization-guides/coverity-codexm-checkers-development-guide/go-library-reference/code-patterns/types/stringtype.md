---
title: "stringType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/stringtype.html"
content_id: "f1nq_4Ui9WPPj92Nm7Vs1A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:29.168074+00:00"
---

# stringType

Matches the `string` type.

This pattern only matches nodes of type `type`.

## Properties

`stringType` does not expose any new properties.

## Example

The following CodeXM pattern matches an expression whose result is a string type:

  
 [image: CXM code follows]   

```
   node matches expression as e
        where e.type matches stringType
```
