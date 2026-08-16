---
title: "castOperatorDynamicCast"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/castoperatordynamiccast.html"
content_id: "NjMRmLbNEcuBKPyT8og5jw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:44.997083+00:00"
---

# castOperatorDynamicCast

Matches only C++ dynamic casts (`dynamic_cast<A>( p )`).

This pattern is equivalent to using the `castOperator` pattern
with the `.kind` property set to `` `dynamic` ``.

This pattern only matches nodes of type `expression`.

## Properties

`castOperatorDynamicCast` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The expression being cast |
| `kind` | `enum castKind` | `` `dynamic` ``; see castKind |

The `.type` property, common to all expression nodes,
indicates the type the operand is being cast to.
The type of the expression being cast is determined by
`.operandExpression.type`.
In other words, this pattern represents a cast from `.operandExpression.type` to `.type`.

**Inherits properties from:**

- astnode
- expression

## Example

The `castOperatorDynamicCast` pattern matches the cast present in following source code:

  
 [image: C++ code follows]   

```
T1 *p1 = dynamic_cast<T2*>(p);
```

The following CodeXM pattern matches dynamic casts from the class named `A`:

  
 [image: CXM code follows]   

```
    pattern dynamicCastFromA {
        castOperatorDynamicCast {
            .operandExpression.type == classType {
                .identifier == "A"
            }
        }
    };
```
