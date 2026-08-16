---
title: "castOperatorReinterpretCast"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/castoperatorreinterpretcast.html"
content_id: "pHzzyk6ipiYQtUbgojHTsw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:47.118337+00:00"
---

# castOperatorReinterpretCast

Matches only C++ reinterpret casts (`reinterpret_cast<A>( p )`).

This pattern is equivalent to using the `castOperator` pattern
with the `.kind` property set to `` `reinterpret` ``.

This pattern only matches nodes of type `expression`.

## Properties

`castOperatorReinterpretCast` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The expression being cast |
| `kind` | `enum castKind` | `` `reinterpret` ``; see castKind |

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

The `castOperatorReinterpretCast` pattern matches the following source code:

  
 [image: C++ code follows]   

```
char* p1 = reinterpret_cast<char*>(p);
```

The following CodeXM pattern matches reinterpret casts from the class named `A`:

  
 [image: CXM code follows]   

```
    pattern reinterpretCastFromA {
        castOperatorReinterpretCast {
            .operandExpression.type == classType {
                .identifier == "A"
            }
        }
    };
```
