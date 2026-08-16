---
title: "castOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/castoperator.html"
content_id: "l9jSayfhTOBhzTDUuNPj_Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:51.785009+00:00"
---

# castOperator

Matches all kinds of casts.

This pattern only matches nodes of type `expression`.

## Properties

`castOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `castKind` | `enum` | The kind of cast represented: `` `explicit` ``, `` `implicit` ``, or `` `dynamic` ``. See castKind. |
| `operandExpression` | `expression` | The expression being cast |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all kinds of casts (implicit, explicit, dynamic) to type `int`:

  
 [image: CXM code follows]   

```
    pattern castToInt {
        castOperator {
            .type == integerType { .kind == `int` }
        }
    };
```
