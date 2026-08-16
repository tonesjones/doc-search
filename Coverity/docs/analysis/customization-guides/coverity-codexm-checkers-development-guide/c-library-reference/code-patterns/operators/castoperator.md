---
title: "castOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/castoperator.html"
content_id: "0G2GfmYVfH3cPVhd7gyV2A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:06.362276+00:00"
---

# castOperator

Matches all kinds of casts.

This pattern only matches nodes of type `expression`.

## Properties

`castOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum castKind` (see below) | The kind of cast represented |
| `operandExpression` | `expression` | The expression being cast |

These are the possible values of the `kind` property
(see also castKind):

| Name | Description |
| --- | --- |
| `` `checkedExplicit` `` | An explicit checked cast |
| `` `checkedImplicit` `` | An implicit checked cast |
| `` `dynamic` `` | A dynamic cast |
| `` `explicit` `` | An explicit cast; for example, `(int) a` |
| `` `implicit` `` | An implicit cast |
| `` `uncheckedFromGenerics` `` | An unchecked cast from generics |

**Inherits properties from:**

- astnode
- expression

## Example

[image: CXM code follows]

```
    pattern castToInt {
        castOperator {
            .type == integralType { .kind == `int` }
            .type == integralType { .kind == `int` }
        }
    };
```

## See also

castOperatorExplicit,
castOperatorImplicit
