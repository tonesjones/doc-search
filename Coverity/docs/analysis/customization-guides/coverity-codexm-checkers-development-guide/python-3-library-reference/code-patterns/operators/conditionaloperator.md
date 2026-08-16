---
title: "conditionalOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/conditionaloperator.html"
content_id: "X~MiVZMXpW~IhLBokESH1A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:00.452580+00:00"
---

# conditionalOperator

Matches the ternary conditional operator:
`<trueExpression> if <conditionExpression> else <falseExpression>`.

This pattern only matches nodes of type `expression`.

## Properties

`conditionalOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `conditionExpression` | `expression` | The condition of the operator (the first argument) |
| `falseExpression` | `expression` | The expression to evaluate if the condition is false (the third argument) |
| `trueExpression` | `expression` | The expression to evaluate if the condition is true (the second argument) |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all conditional operators that use a `binaryOperator` as their condition:

[image: CXM code follows]

```
    pattern binaryOperatorCondition {
        conditionalOperator {
            .condtionExpression == binaryOperator
        }
    };
```
