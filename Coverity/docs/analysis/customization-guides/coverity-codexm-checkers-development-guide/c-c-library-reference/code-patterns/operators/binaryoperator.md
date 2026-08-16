---
title: "binaryOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/binaryoperator.html"
content_id: "WnnFk2tEuHWnuG4btJyVgQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:42.799587+00:00"
---

# binaryOperator

Matches the many binary operators—operators that take an operand on either side,
such as `+`, `*`, `==`, and so on.

This pattern only matches nodes of type `expression`.

## Properties

`binaryOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `operator` | `enum` | Can be one of: `` `==` ``, `` `!=` ``, `` `<` ``, `` `>` ``, `` `<=` ``, `` `>=` ``, `` `<=>` ``, `` `*` ``, `` `/` ``, `` `%` ``, `` `+` ``, `` `-` ``, `` `<<` ``, `` `>>` ``, `` `&` ``, `` `^` ``, `` `|` ``, `` `&&` ``, `` `||` ``, `` `,` ``, or `` `=` `` |
| `lhsExpression` | `expression` | The operand on the left-hand side of the operator |
| `rhsExpression` | `expression` | The operand on the right-hand side of the operator |
| `isImplicit` | `bool` | `true` if the operator is implicit |

**Inherits properties from:**

- astnode
- expression

## Nested Expressions

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

[image: Parsing binary operations]

In both these cases, a `` binaryOperator { .operand == `*` } ``
pattern matches some part of the expression.
In the left-hand case, it matches `b * c`.
In the right-hand case, it matches the entire expression.

## Example

In the following snippet, an unconstrained `binaryOperator` matches all binary operations,
including `2*a + 3` (the addition operation, where the left-hand side is a binary operation),
`2*a` (multiplication),
and `a & c` (logical AND).

  
 [image: C/C++ code follows]   

```
int a = 1;
int b, c, d;

b = 2*a + 3;
c = 2;
d = a & c;
```

You can refine the `binaryOperator` pattern to match only specific operations.
For example, the following CodeXM pattern:

  
 [image: CXM code follows]   

```
    binaryOperator {
        .operator == `*`
    };
```

... matches only multiplication (the instance `2*a` in the example above), and the following CodeXM pattern:

  
 [image: CXM code follows]   

```
    binaryOperator {
        .operator == `+`
    };
```

... matches only addition.

Patterns can be compositions of separate sub-patterns, in order to match a more complicated expression;
for example, to match the addition of a product of two terms with another term, you could use a pattern such as
the following:

  
 [image: CXM code follows]   

```
    pattern multiplyThenAdd {
        binaryOperator {
            .operator == `+`;
            .lhsExpression == binaryOperator {
                .operator == `*`
            };
        }
    };
```

The previous pattern only detects when the multiplication happens on the left-hand side of the addition:
`2*a + 3` matches, but `3 + 2*a` does not.
To generalize the pattern so it matches either variation, use the following CodeXM code:

  
 [image: CXM code follows]   

```
    pattern multiplyThenAdd {
        | binaryOperator {
              .operator == `+`;
              .lhsExpression == binaryOperator {
                  .operator == `*`
              };
          }
        | binaryOperator {
              .operator == `+`;
              .rhsExpression == binaryOperator {
                  .operator == `*`
              };
          }
    };
```

This uses the alternative ( `|` ) operator to say the pattern can match either
multiplication on the left-hand side or the right-hand side.

However, this new pattern matches multiplication on one side, the other, or both;
for example, it would also match this code:

  
 [image: C/C++ code follows]   

```
2*a + 3*b
```

... where multiplication occurs on both sides of the addition.
If you want to match multiplication on one side only, revise the pattern to impose that constraint.
