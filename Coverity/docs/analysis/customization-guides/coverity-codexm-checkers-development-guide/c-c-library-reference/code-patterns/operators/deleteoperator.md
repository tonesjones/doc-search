---
title: "deleteOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/deleteoperator.html"
content_id: "C73gZ9I_l17rgLqD6aN1iA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:50.128425+00:00"
---

# deleteOperator

Matches the C++ `delete` operator.

This pattern only matches nodes of type `expression`.

## Properties

`deleteOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isArray` | `bool` | `true` if this instance represents the array `delete[]` rather than the scalar `delete` operator. |
| `operandExpression` | `expression` | The expression (typically a variable) being deleted |
| `hasGlobalScopeModifier` | `bool` | `true` if `::` precedes `delete` (specifying global scope) |
| `operatorDeleteFunction` | `functionSymbol` | The function operator `delete` |

**Inherits properties from:**

- astnode
- expression

## Example

The `deleteOperator` matches the following source code:

  
 [image: C++ code follows]   

```
    delete myPtr;
```

In this instance, `.isArray` is `false` because the scalar version of `delete`
was used.
The `.operandExpression` refers to `myPtr`.

The following CodeXM pattern matches any `delete` operator for an integer pointer:

  
 [image: CXM code follows]   

```
    pattern deleteIntPointer {
        deleteOperator {
            .operandExpression == variableReference {
                .type == pointerType {
                    .pointerToType == intType
                }
            }
        }
    };
```
