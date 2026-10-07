---
title: "throwOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/throwoperator.html"
content_id: "M7_nW8n_MGA_UqGImN4oEw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:42.213684+00:00"
---

# throwOperator

Matches instances of the `throw` operator.

This pattern only matches nodes of type `expression`.

## Properties

`throwOperator` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The expression being thrown by the operator |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern will find all throws of the type `Exception`:

  
 [image: CXM code follows]   

```
    pattern throwException {
        throwOperator {
            .operandExpression == expression {
                .type == classType { .simpleName == "Exception" }
            }
        }
    };
```
