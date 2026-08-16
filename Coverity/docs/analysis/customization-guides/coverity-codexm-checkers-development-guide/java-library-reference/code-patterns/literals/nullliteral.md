---
title: "nullLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/nullliteral.html"
content_id: "~OclGpckCxnTOxyc0scuPw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:13.298026+00:00"
---

# nullLiteral

Matches all `null` literals.

This pattern only matches nodes of type `expression`.

## Properties

`nullLiteral` does not expose any new properties.

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern finds all assignments to `null` (for example, `a = null`):

  
 [image: CXM code follows]   

```
    pattern assignmentToNull {
        assignmentOperator {
            sourceExpression == nullLiteral
        }
    };
```
