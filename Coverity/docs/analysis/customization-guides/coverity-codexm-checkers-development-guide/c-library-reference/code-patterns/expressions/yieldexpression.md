---
title: "yieldExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/yieldexpression.html"
content_id: "xbuYtyRhw3UTl0VPerPQag"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:54.398651+00:00"
---

# yieldExpression

Matches `yield return` expressions.

This pattern only matches nodes of type `expression`.

## Properties

`yieldExpression` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression being yielded |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all `yield return` expressions that return integral types:

  
 [image: CXM code follows]   

```
    pattern yieldingIntExpression {
        yieldExpression {
            .expression == expression {
                .type == integralType
            }
        }
    };
```
