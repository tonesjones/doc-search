---
title: "incrementOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/incrementoperator.html"
content_id: "y8_tX_7JE6OkQ2K1NVUjKQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:10.359361+00:00"
---

# incrementOperator

Matches all increment operators, both prefix and postfix.

This pattern only matches nodes of type `expression`.

## Properties

`incrementOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum` | Either `` `prefix` `` or `` `postfix` `` |
| `operandExpression` | `expression` | The expression the increment operator is being applied to |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches when a prefix increment operator is used to update a `for` loop:

  
 [image: CXM code follows]   

```
    pattern forLoopPrefixIncrement {
        forLoop {
            .updateStatement == simpleStatement {
                .expression == incrementOperator {
                    .kind == `prefix`
                }
            }
        }
    };
```

## See also

decrementOperator
