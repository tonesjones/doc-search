---
title: "incrementOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/incrementoperator.html"
content_id: "aHE0BNHrrgploGjR8KY6Vw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:42.127599+00:00"
---

# incrementOperator

Matches all increment operators, both prefix and postfix.

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
