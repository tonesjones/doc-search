---
title: "castOperatorConstCast"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/castoperatorconstcast.html"
content_id: "pXiUc498HeHkKRIXwnnzjw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:44.264193+00:00"
---

# castOperatorConstCast

Matches only C++ constant casts (`const_cast<A>( p )`).

This pattern is equivalent to using the `castOperator` pattern
with the `.kind` property set to `` `const` ``.

This pattern only matches nodes of type `expression`.

## Properties

`castOperatorConstCast` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The expression being cast |
| `kind` | `enum castKind` | `` `const` ``; see castKind |

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

The `castOperatorConstCast` matches the following source code:

  
 [image: C++ code follows]   

```
char* p1 = const_cast<char*>(p);
```

The following CodeXM pattern matches constant casts from the integer type:

  
 [image: CXM code follows]   

```
    pattern constCastFromInt {
        castOperatorStatic {
            .operandExpression.type == intType;
        }
    };
```
