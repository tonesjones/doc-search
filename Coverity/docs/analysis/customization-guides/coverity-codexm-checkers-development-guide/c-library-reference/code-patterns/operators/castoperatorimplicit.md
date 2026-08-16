---
title: "castOperatorImplicit"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/castoperatorimplicit.html"
content_id: "TsIVqfHb1sRO6mKkicyW4g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:08.390378+00:00"
---

# castOperatorImplicit

Matches implicit casts; that is, casts that are not explicitly stated but are performed by the C# compiler.

This pattern only matches nodes of type `expression`.

## Properties

`castOperatorImplicit` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum castKind` | Always `` `implicit` ``. See castKind. |
| `operandExpression` | `expression` | The expression being cast |

**Inherits properties from:**

- astnode
- expression

## Example

In the following snippet of C#:

[image: C# code follows]

```
    int num = 2147483647;
    long bigNum = num;
```

... there is an implicit cast between the `int` and the `long`. To detect such a cast, you could use the following pattern:

[image: CXM code follows]

```
    pattern implicitCastFromString {
        castOperatorImplicit {
            .operandExpression == expression {
                .type == integralType {
                    .kind == `int`
                }
            }
        }
    };
```

## See also

castOperator,
castOperatorExplicit
