---
title: "incrementOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/incrementoperator.html"
content_id: "nzYGtx2MXnZe~lnsyw3Slw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:36.457356+00:00"
---

# incrementOperator

Matches all increment operators.

This pattern only matches nodes of type `expression`.

## Properties

`incrementOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The expression the increment operator is being applied to |

**Inherits properties from:**

- astnode
- expression

## Example

The following example CodeXM matches when a prefix increment operator is used to update a `for` loop:

  
 [image: CXM code follows]   

```
    pattern forLoopPrefixIncrement {
        forLoop {
            .updateStatement == simpleStatement {
                .expression == incrementOperator
            }
        }
    };
```

## See also

decrementOperator
