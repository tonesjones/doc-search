---
title: "binaryOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/binaryoperator.html"
content_id: "T7N4U4a3NYwvOH2IJPwNFw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:52.130814+00:00"
---

# binaryOperator

Matches JavaScript binary operators.

Important:
This pattern *does not match* assignment operators, as these have their own specific JavaScript Library patterns:
See assignmentOperator,
assignmentOperatorCompound, and
assignmentOperatorSimple.

This pattern only matches nodes of type `expression`.

## Properties

`binaryOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isImplicit` | `bool` | Whether this expression is implicit |
| `lhsExpression` | `expression` | The operand on the left-hand side of the operator |
| `operator` | `enum` (see below) | The operator matched |
| `rhsExpression` | `expression` | The operand on the right-hand side of the operator |

These are the possible values for the `operator` property:

| Name | Description |
| --- | --- |
| `` `=` `` | The simple assignment operator |
| `` `+=` `` | The addition assignment operator |
| `` `-=` `` | The subtraction assignment operator |
| `` `*=` `` | The multiplication assignment operator |
| `` `/=` `` | The division assignment operator |
| `` `%=` `` | The modulo assignment operator |
| `` `**=` `` | The exponentiation assignment operator |
| `` `&=` `` | The bitwise assignment operator |
| `` `|=` `` | The bitwise OR assignment operator |
| `` `^=` `` | The bitwise codexmspan AND assignment operator |
| `` `<<=` `` | The left-shift assignment operator |
| `` `>>=` `` | The sign-preserving right-shift operator |
| `` `>>>=` `` | The unsigned right-shift operator |

**Inherits properties from:**

- astnode
- expression

## Nested Expressions

Complex binary operations are specifically represented with the correct order of operations,
regardless of operator precedence (the compiler has already evaluated the precedence in order to build
the expression’s tree structure). When pattern matching, be aware that either operand of a
binary operator, or *both,* can also act as a binary operator representing operations that are completed before the
match operation is performed.

For example, `a + b * c` is understood as `a + (b * c)` due to operator precedence. It is encoded as a binary addition that has a right-hand operand of `b * c`: this must be computed before the addition is performed. On the other hand, `(a + b) * c` is a multiplication where the left-hand
operand, `a + b`, must be computed before it is multiplied by `c`.

The following illustration shows this situation:

[image: Differing syntax trees based on differing operator precedence]

In both cases, a `` binaryOperator{.operand == `*`} `` pattern matches some part of the expression.
In the left-hand case, it matches `b * c`.
In the right-hand case, it matches the entire expression.

## Example

This pattern would match `a + b`, and yield `"a"` as
`lhsExpressions`, `"b"` as `rhsExpression`,
and `` `+` `` as `operator`.

The following pattern matches only multiplication:

[image: CXM code follows]

```
    pattern multiplicationOperation {
        binaryOperator {
            .operator == `*`
        }
    };
```

Sometimes there will be implicit binary operators, such as in the following example:

[image: JavaScript code follows]

```
    let strTemplate = `text1 ${expression} test2`;
```

... where the initializer is actually an implicit string concatenation.

## See also

unaryOperator
