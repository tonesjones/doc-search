---
title: "spreadOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/spreadoperator.html"
content_id: "h7O7KDN6Fcf5leaMW~IMnw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:48.149824+00:00"
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
