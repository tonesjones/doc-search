---
title: "yieldExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/yieldexpression.html"
content_id: "7TKLqP1zlmHKZUC2ZCoCGw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:51.292206+00:00"
---

# yieldExpression

Matches `yield` expressions.

This pattern only matches nodes of type `expression`.

## Properties

`yieldExpression` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The yielded expression |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches an expression that yields an integer:

[image: CXM code follows]

```
    pattern yieldInteger {
        yieldExpression {
            .expression == integerLiteral
        }
    };
```
