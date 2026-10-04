---
title: "nilLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/nilliteral.html"
content_id: "ejAWP8E8529AxkzVq~CC0Q"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:36.015026+00:00"
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
