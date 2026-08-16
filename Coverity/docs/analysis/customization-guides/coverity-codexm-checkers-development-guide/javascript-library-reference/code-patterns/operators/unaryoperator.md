---
title: "unaryOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/unaryoperator.html"
content_id: "hD7kgmPIP5o_bFhxTUwgyw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:59.361806+00:00"
---

# unaryOperator

Matches unary operators—those operators that have only one operand.

Important:
This pattern *does not match* certain unary operators that have their own specific JavaScript Library patterns:
See decrementOperator,
deleteOperator,
incrementOperator,
typeofOperator, and
voidOperator.

This pattern only matches nodes of type `expression`.

## Properties

`unaryOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isImplicit` | `bool` | Whether this expression is implicit |
| `operandExpression` | `expression` | The operand |
| `operator` | `enum` (see below) | The operator matched |

These are the possible values of the operator property:

| Name | Description |
| --- | --- |
| `` `+` `` | The unary plus/positive operator |
| `` `-` `` | The negation operator |
| `` `!` `` | The logical negation operator |
| `` `~` `` | The bitwise negation operator |

**Inherits properties from:**

- astnode
- expression

## Example

The `unaryOperator` pattern matches the source expression of the following assignments:

[image: JavaScript code follows]

```
    n = -m;
    isTrue = !false;
```

In the first instance, the `.operator` property is `` `-` ``. In the second, it is `` `!` ``.

## See also

binaryOperator
