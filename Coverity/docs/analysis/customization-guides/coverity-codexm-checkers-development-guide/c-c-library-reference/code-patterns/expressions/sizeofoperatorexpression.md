---
title: "sizeofOperatorExpression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sizeofoperatorexpression.html"
content_id: "xyaEmWOzFxPK5McK3OBeUg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:30.621378+00:00"
---

# sizeofOperatorExpression

Matches instances of the `sizeof()` operator applied to expressions;
for example, `sizeof( y[0] )`.

## Properties

`sizeofOperatorExpression` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The expression being evaluated for size information |

**Inherits properties from:**

- astnode
- expression

## Example

The `sizeofOperatorExpression` pattern matches target C/C++ code such as the following:

  
 [image: C/C++ code follows]   

```
    int num = 1;
    int size = sizeof(num)
```

In this instance, `.operandExpression` property refers to `num`.

The following CodeXM pattern matches a `sizeof()` operator invoked using a variable reference expression:

  
 [image: CXM code follows]   

```
    pattern sizeofVar {
        sizeofOperatorExpression {
            .operandExpression == variableReference;
        }
    };
```

## See also

sizeofOperatorType
