---
title: "castOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/castoperator.html"
content_id: "QYldgDyEcER62mApollRfA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:18.361396+00:00"
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

| Name | Type |
| --- | --- |
| `` `checkedExplicit` `` | An explicit checked cast |
| `` `checkedImplicit` `` | An implicit checked cast |
| `` `explicit` `` | An explicit cast; for example, `(int) a` |
| `` `implicit` `` | An implicit cast |
| `` `uncheckedFromGenerics` `` | An unchecked cast from generics |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches all casts (implicit, explicit, checked) to type `int`:

  
 [image: CXM code follows]   

```
    pattern castToInt {
        castOperator {
            .type == integerType { .kind == `int` }
        }
    };
```

## See also

castOperatorChecked,
castOperatorExplicit,
castOperatorImplicit
