---
title: "decrementOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/decrementoperator.html"
content_id: "ubLuY0hamBu2FI7Qc3EKig"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:52.448302+00:00"
---

# decrementOperator

Matches all decrement operators.

This pattern only matches nodes of type `expression`.

## Properties

`decrementOperator` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The expression the decrement operator is being applied to |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches when a decrement operator is used to update a `for` loop:

  
 [image: CXM code follows]   

```
    pattern forLoopPostfixDecrement {
        forLoop {
            .updateStatement == simpleStatement {
                .expression == decrementOperator
            }
        }
    };
```

## See also

incrementOperator
