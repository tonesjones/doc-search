---
title: "binaryOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/binaryoperator.html"
content_id: "HiFsOPtdI5x78bjEOF2OVQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:59.120867+00:00"
---

# binaryOperator

Matches all possible Python binary operators.

Binary operators include
the power operator `**`;
the arithmetic operators
`*`,
`//`,
`/`,
`%`,
`+`,
and `-`;
the shifting operators
`>>`
and `<<`;
the bitwise operattors
`&`,
`^`,
and `|`;
and the comparisons
`>`,
`<`,
`==`,
`>=`,
`<=`,
`!=`,
`is`,
and `in`.

This pattern only matches nodes of type `expression`.

## Properties

`binaryOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `lhsExpression` | `expression` | The left-hand side of the binary expression |
| `operator` | `enum` | One of `` `**` ``, `` `*` ``, `` `//` ``, `` `/` ``, `` `%` ``, `` `+` ``, `` `-` ``, `` `>>` ``, `` `<<` ``, `` `&` ``, `` `^` ``, `` `|` ``, `` `<` ``, `` `>` ``, `` `==` ``, `` `>=` ``, `` `<=` ``, `` `!=` ``, `` `is` ``, or `` `in` `` |
| `rhsExpression` | `expression` | The right-hand side of the binary expression |

**Inherits properties from:**

- astnode
- expression

## Nested Expression

When pattern matching, be aware that either or both operands of a binary operator can themselves be binary operators
that represent operations to be completed before the matched operation is performed.

For example, `a + b * c` is understood as
`a + (b * c)` due to operator precedence.
This is matched as a binary addition that has a right-hand operand of `b * c`.
The value of the subexpression must be computed before the addition is performed.

On the other hand, `(a + b) * c` is matched as a binary multiplication.
The left-hand operand, `a + b`, must be computed before it is
multiplied by `c`.

The following illustration shows these two situations:

[image: image]

In both these cases, a `` binaryOperator { .operand == `*` } ``
pattern matches some part of the expression.
In the left-hand case, it matches `b * c`.
In the right-hand case, it matches the entire expression.

## Example

The following CodeXM pattern matches only multiplication:

[image: CXM code follows]

```
    pattern multiplicationOperation {
        binaryOperator {
            .operator == `*`
        }
    };
```

## See also

unaryOperator
