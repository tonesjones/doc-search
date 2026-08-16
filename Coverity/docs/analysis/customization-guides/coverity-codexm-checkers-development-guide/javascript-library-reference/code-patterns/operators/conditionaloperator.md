---
title: "conditionalOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/conditionaloperator.html"
content_id: "AGVa6GSKXex_m1oNkTPWtg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:53.537226+00:00"
---

# conditionalOperator

Matches the conditional operator `? :`, sometimes called the “ternary” operator.

This pattern only matches nodes of type `expression`.

## Properties

`conditionalOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `conditionExpression` | `expression` | The condition (the operand before the `?` symbol) |
| `falseExpression` | `expression` | The expression to evaluate if the condition is false (that is, the operand to the right of the `:` symbol) |
| `trueExpression` | `expression` | The expression to evaluate if the condition is true (that is, the operand between the `?` and `:` symbols) |

**Inherits properties from:**

- astnode
- expression

## Example

The `conditionalOperator` pattern matches the following expression:

[image: JavaScript code follows]

```
    isA ? "A" : "B"
```

The `.conditionalExpression` property is the expression `"isA"`,
the `.trueExpression` property is the literal `"A"`, and
the `.falseExpression` property is the literal `"B"`
