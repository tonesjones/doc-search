---
title: "castOperatorExplicit"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/castoperatorexplicit.html"
content_id: "5o63WazjHTCnIYY4SCHREQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:45.650392+00:00"
---

# castOperatorExplicit

Matches only explicit C-style casts.

This pattern is equivalent to using the `castOperator` pattern
with the `.kind` property set to `` `explicit` ``.

This pattern only matches nodes of type `expression`.

## Properties

`castOperatorExplicit` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The expression being cast |
| `kind` | `enum castKind` | `` `explicit` ``; see castKind |

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

To match an explicit cast from the `int` type, you could use the following CodeXM pattern:

  
 [image: CXM code follows]   

```
    pattern explicitCastFromInt {
        castOperatorExplicit {
            .operandExpression.type == intType;
        }
    };
```
