---
title: "incrementOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/incrementoperator.html"
content_id: "UxuTNyTV74K0iSTiKfVZWA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:55.668321+00:00"
---

# incrementOperator

Matches the `++` operation, as either a prefix or postfix.

Important:
The unaryOperator pattern *does not match*
the increment ( `++` ) operator.

This pattern only matches nodes of type `expression`.

## Properties

`incrementOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum` | The operator kind: either `` `postfix` `` or `` `prefix` `` |
| `operandExpression` | `expression` | The operand |

**Inherits properties from:**

- astnode
- expression

## Example

The `incrementOperator` pattern matches the following expressions:

[image: JavaScript code follows]

```
    ++m
    m++
```

In the first instance, the `.kind` property is `` `prefix` ``.
In the second, it is `` `postfix` ``.
