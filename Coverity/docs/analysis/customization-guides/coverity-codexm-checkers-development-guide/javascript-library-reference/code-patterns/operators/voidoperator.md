---
title: "voidOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/voidoperator.html"
content_id: "c68gMsxKNtMFkxT7bk94ZQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:00.117346+00:00"
---

# voidOperator

Matches instances of the `void` operator.

Important:
The unaryOperator pattern *does not match*
the `void` operator.

This pattern only matches nodes of type `expression`.

## Properties

`voidOperator` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The operand |

**Inherits properties from:**

- astnode
- expression

## Example

The `voidOperator` pattern matches the following expression:

[image: JavaScript code follows]

```
    void 0
```

The `.operandExpression` property is `0`.
