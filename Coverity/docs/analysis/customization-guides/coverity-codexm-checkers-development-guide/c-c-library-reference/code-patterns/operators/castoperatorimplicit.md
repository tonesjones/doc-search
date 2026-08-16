---
title: "castOperatorImplicit"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/castoperatorimplicit.html"
content_id: "05UcmD1MmosWOWOgbZjrEg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:46.385219+00:00"
---

# castOperatorImplicit

Matches only implicit type conversions.
That is, places where a type conversion occurs but is not explicitly specified in the source code.

This pattern is equivalent to using the `castOperator` pattern
with the `.kind` property set to `` `implicit` ``.

This pattern only matches nodes of type `expression`.

## Properties

`castOperatorImplicit` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The expression being cast |
| `kind` | `enum castKind` | `` `implicit` ``; see castKind |

The `.type` property, common to all expression nodes,
indicates the type the operand is being cast to.
The type of the expression being cast is determined by
`.operandExpression.type`.
In other words, this pattern represents a cast from `.operandExpression.type`
to `.type`.

**Inherits properties from:**

- astnode
- expression

## Example

To match an implicit cast from the `int` type, you could use the following CodeXM pattern:

  
 [image: CXM code follows]   

```
    pattern implicitCastFromInt {
        castOperatorImplicit {
            .operandExpression.type == intType;
        }
    };
```
