---
title: "decrementOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/decrementoperator.html"
content_id: "z3O6xkXNy_UBfaBFhBhgUg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:29.770733+00:00"
---

# decrementOperator

Matches all decrement operators, both prefix and postfix.

This pattern only matches nodes of type `expression`.

## Properties

`decrementOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum` | Either `` `prefix` `` or `` `postfix` `` |
| `operandExpression` | `expression` | The expression the decrement operator is being applied to |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches when a postfix decrement operator is used to update a `for` loop:

  
 [image: CXM code follows]   

```
    pattern forLoopPostfixDecrement {
        forLoop {
            .updateStatement == simpleStatement {
                .expression == decrementOperator {
                    .kind == `postfix`
                }
            }
        }
    };
```

## See also

incrementOperator
