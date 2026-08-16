---
title: "noneLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/noneliteral.html"
content_id: "z1AnlM9TxNGuvLYD5WsJJw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:54.251430+00:00"
---

# noneLiteral

Matches `None` literals.

This pattern only matches nodes of type `expression`.

## Properties

`noneLiteral` does not expose any new properties.

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern finds all assignments to `None`;
for example, `a = None;`:

[image: CXM code follows]

```
    pattern assignmentToNull {
        assignmentOperator {
            sourceExpression == noneLiteral
        }
    };
```
