---
title: "castOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/castoperator.html"
content_id: "khn5hxsiBNWm5qQBT670iA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:43.532228+00:00"
---

# castOperator

Matches all C and C++ type casts.
These includes C-style casts (explicit), implicit type conversions, and the C++ operations
`static_cast`, `dynamic_cast`, `reinterpret_cast`,
and `const_cast`.

This pattern only matches nodes of type `expression`.

## Properties

`castOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The expression being cast |
| `kind` | `enum castKind` | `` `explicit` ``, `` `implicit` ``, `` `static` ``, `` `dynamic` ``, `` `reinterpret` ``, or `` `const` ``; see castKind |

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

Consider the following target code:

  
 [image: C/C++ code follows]   

```
int i = 1;
float f = i;
```

The `castOperator` pattern matches the implicit cast on the second line,
where the integer `i` needs to be converted to floating point so it can be assigned to `f`.
In this example, the `.kind` property is `` `implicit` ``.

The following CodeXM pattern shows how to match any implicit cast from an integer type to a floating-point type:

  
 [image: CXM code follows]   

```
    pattern implicitCastIntToFloat {
        castOperator {
            .kind == `implicit`;
            .type == floatType;                  // The intended type
            .operandExpression.type == intType;  // the uncast type
        }
    };
```
