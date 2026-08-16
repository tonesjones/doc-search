---
title: "spreadOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/spreadoperator.html"
content_id: "h7O7KDN6Fcf5leaMW~IMnw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:57.874472+00:00"
---

# spreadOperator

Matches instances of the `...` (spread) operator.

The spread operator is specified in ECMAScript 2015, 12.2.5.

This pattern only matches nodes of type `expression`.

## Properties

`spreadOperator` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The operand |

**Inherits properties from:**

- astnode
- expression

## Example

The `spreadOperator` pattern matches the element with a
`...` prefix in the following array literal:

[image: JavaScript code follows]

```
    ["a", "b", ...otherList];
```

The `.operandExpression` property is the expression `otherList`.

## See also

arrayLiteral,
objectLiteral
