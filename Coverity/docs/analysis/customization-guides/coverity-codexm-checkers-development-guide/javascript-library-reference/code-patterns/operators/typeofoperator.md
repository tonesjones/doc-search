---
title: "typeofOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/typeofoperator.html"
content_id: "YkIZT72KWnPbHpfoi2dCZw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:58.612608+00:00"
---

# typeofOperator

Matches instances of the `typeof` operator.

Important:
The unaryOperator pattern *does not match*
the `typeof` operator.

This pattern only matches nodes of type `expression`.

## Properties

`typeofOperator` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The operand |

**Inherits properties from:**

- astnode
- expression

## Example

The `typeofOperator` pattern matches the following expression:

[image: JavaScript code follows]

```
    typeof 'hello'
```

The `.operandExpression` property is `'string'`.
