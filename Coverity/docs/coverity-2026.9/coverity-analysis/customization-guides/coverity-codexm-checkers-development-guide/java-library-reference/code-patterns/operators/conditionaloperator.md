---
title: "conditionalOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/conditionaloperator.html"
content_id: "OLCo1j1Ti5ACOc7gCAnK5A"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:42.033227+00:00"
---

# conditionalOperator

Matches the conditional operator (sometimes called the "ternary" operator), `?:`.

This pattern only matches nodes of type `expression`.

## Properties

`conditionalOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `conditionExpression` | `expression` | The expression that is the condition of the operator (first argument) |
| `falseExpression` | `expression` | The expression on the `false` side of the operator (third argument) |
| `trueExpression` | `expression` | The expression on the `true` side of the operator (second argument) |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all conditional operators that use the `?:` operator:

  
 [image: CXM code follows]   

```
    pattern binaryOperatorCondition {
        conditionalOperator {
            .condtionExpression == binaryOperator
        }
    };
```
