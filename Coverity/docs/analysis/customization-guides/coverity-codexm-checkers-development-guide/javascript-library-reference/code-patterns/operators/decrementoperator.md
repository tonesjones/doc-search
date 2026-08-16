---
title: "decrementOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/decrementoperator.html"
content_id: "KPxwrIcNEXVJPWYtQ_2PsQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:54.274796+00:00"
---

# decrementOperator

Matches the `--` operation, as either a prefix or postfix.

Important:
The unaryOperator pattern *does not match*
the `decrement` ( `--` ) operator.

This pattern only matches nodes of type `expression`.

## Properties

`decrementOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum` | The operator kind: either `` `postfix` `` or `` `prefix` `` |
| `operandExpression` | `expression` | The operand |

**Inherits properties from:**

- astnode
- expression

## Example

The `decrementOperator` pattern matches the following JavaScript expressions:

[image: JavaScript code follows]

```
    --m
    m--
```

In the first instance, the `.kind` property is `` `prefix` ``.
In the second, it is `` `postfix` ``.
