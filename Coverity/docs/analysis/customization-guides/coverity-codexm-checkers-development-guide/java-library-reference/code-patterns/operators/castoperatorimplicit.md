---
title: "castOperatorImplicit"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/castoperatorimplicit.html"
content_id: "pMFQ~PeKCK_l6A6vOPkueA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:20.574690+00:00"
---

# castOperatorImplicit

Matches casts that are implicit to the code; that is, not explicitly stated.

This pattern only matches nodes of type `expression`.

## Properties

`castOperatorImplicit` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum castKind` | Always `` `implicit` ``; see castKind |
| `operandExpression` | `expression` | The expression being cast |

**Inherits properties from:**

- astnode
- expression

## Example

For the following snippet of Java:

  
 [image: Java code follows]   

```
Object o = "Example";
```

... there is an implicit cast between the string literal and the class `Object`. To detect such
a cast, you could use the following CodeXM pattern:

  
 [image: CXM code follows]   

```
    pattern implicitCastFromString {
        castOperatorImplicit {
            .operandExpression == expression {
                .type == classType { .simpleName == "String"}
            }
        }
    };
```

## See also

castOperator,
castOperatorChecked,
castOperatorExplicit
