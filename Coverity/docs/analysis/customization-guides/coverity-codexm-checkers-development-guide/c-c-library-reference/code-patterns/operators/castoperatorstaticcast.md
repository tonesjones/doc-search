---
title: "castOperatorStaticCast"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/castoperatorstaticcast.html"
content_id: "p268A_Banx5DGfIfdgo_UA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:47.860517+00:00"
---

# castOperatorStaticCast

Matches only C++ static casts (`static_cast<A>( p )`).

This pattern is equivalent to using the `castOperator` pattern
with the `.kind` property set to `` `static` ``.

This pattern only matches nodes of type `expression`.

## Properties

`castOperatorStaticCast` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The expression being cast |
| `kind` | `enum castKind` | `` `static` ``; see castKind |

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

The `castOperatorStaticCast` matches the following source code:

  
 [image: C++ code follows]   

```
T1 *p1 = static_cast<T2*>(p);
```

To match static casts from integers, you could use the following CodeXM pattern:

  
 [image: CXM code follows]   

```
    pattern staticCastFromInt {
        castOperatorStatic {
            .operandExpression.type == intType;
        }
    };
```
