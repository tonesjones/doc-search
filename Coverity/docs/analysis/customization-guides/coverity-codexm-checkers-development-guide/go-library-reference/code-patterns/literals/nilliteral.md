---
title: "nilLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/nilliteral.html"
content_id: "ejAWP8E8529AxkzVq~CC0Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:46.183404+00:00"
---

# nilLiteral

Matches all `nil` literals.

This pattern only matches nodes of type `expression`.

## Properties

`nilLiteral` does not expose any new properties.

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern finds all assignments to `nil`; for example, `a = nil`:

  
 [image: CXM code follows]   

```
    pattern assignmentToNil {
        assignmentOperator {
            sourceExpression == nilLiteral
        }
    };
```
