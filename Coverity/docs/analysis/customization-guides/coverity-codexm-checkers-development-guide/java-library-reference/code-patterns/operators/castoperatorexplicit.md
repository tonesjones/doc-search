---
title: "castOperatorExplicit"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/castoperatorexplicit.html"
content_id: "_ygQ8iuW6HL47kMgZ1~LPQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:19.830167+00:00"
---

# castOperatorExplicit

Matches explicit casts.

This pattern only matches nodes of type `expression`.

## Properties

`castOperatorExplicit` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum castKind` | Always `` `explicit` ``; see castKind |
| `operandExpression` | `expression` | The expression being cast |

**Inherits properties from:**

- astnode
- expression

## Example

The following snippet of Java casts `i` to `short`:

  
 [image: Java code follows]   

```
int i = 5;
short a = (short) i;
```

... you could use the following CodeXM pattern to match it:

  
 [image: CXM code follows]   

```
    pattern castToShort {
        castOperatorExplicit {
            .type == shortType
        }
    };
```

## See also

castOperator,
castOperatorChecked,
castOperatorImplicit
