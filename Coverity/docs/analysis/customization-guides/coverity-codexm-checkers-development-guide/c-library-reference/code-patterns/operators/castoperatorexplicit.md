---
title: "castOperatorExplicit"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/castoperatorexplicit.html"
content_id: "vgRhx9bm5BsNzR69e5MsUw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:07.191416+00:00"
---

# castOperatorExplicit

Matches explicit casts.

This pattern only matches nodes of type `expression`.

## Properties

`castOperatorExplicit` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum castKind` | Always `` `explicit`. `` See castKind. |
| `operandExpression` | `expression` | The expression being cast |

**Inherits properties from:**

- astnode
- expression

## Example

For the following snippet of C#:

[image: C# code follows]

```
    int i = 5;
    short a = (short) i;
```

... the following pattern matches casts to `short`, so it would match the preceding snippet:

[image: CXM code follows]

```
    pattern castToShort {
        castOperatorExplicit {
            .type == shortType
        }
    };
```

## See also

castOperatorImplicit,
castOperator
