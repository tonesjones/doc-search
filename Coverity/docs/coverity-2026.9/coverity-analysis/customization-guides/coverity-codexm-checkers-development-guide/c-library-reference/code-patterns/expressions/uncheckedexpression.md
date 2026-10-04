---
title: "uncheckedExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/uncheckedexpression.html"
content_id: "wzXWcK86_p1UWXr3JadZrg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:28.727827+00:00"
---

# uncheckedExpression

Matches `unchecked` expressions.

This pattern only matches nodes of type `expression`.

## Properties

`uncheckedExpression` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all `unchecked` expression on integer types:

  
 [image: CXM code follows]   

```
    pattern uncheckedExpressionOnInt {
        uncheckedExpression {
            .expression == expression {
                .type == integralType
            }
        }
    };
```

## See also

checkedBlock,
checkedExpression,
uncheckedBlock
