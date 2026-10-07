---
title: "dynamicCastExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/dynamiccastexpression.html"
content_id: "X_kmJNTCcQS7AYLpKq178A"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:27.497949+00:00"
---

# dynamicCastExpression

Matches dynamic casts.

This pattern only matches nodes of type `expression`.

## Properties

`dynamicCastExpression` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression being cast |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches casts to `short`:

  
 [image: CXM code follows]   

```
    pattern dynamicCastToShort {
        dynamicCastExpression {
            .type == shortType
        }
    };
```

## See also

castOperator,
castOperatorImplicit
