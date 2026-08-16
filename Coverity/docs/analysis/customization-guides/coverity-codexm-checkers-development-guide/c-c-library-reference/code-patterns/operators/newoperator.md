---
title: "newOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/newoperator.html"
content_id: "MSt58SLGfRftD_Ugf8sX8w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:51.725094+00:00"
---

# newOperator

Matches the C++ `new` operator.

This pattern only matches nodes of type `expression`.

## Properties

`newOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `operandType` | `type` | The type being requested |
| `operatorDeleteFunction` | `functionSymbol?` | The function operator `delete` (if there is a chance the constructor might throw); `null` if there is no such operator |
| `operatorNewFunction` | `functionSymbol` | The function operator `new` |
| `placementArguments` | `list<expression>?` | Argument to placement `new`; size is not included; `null` if there are no arguments |
| `arraySizeExpression` | `expression?` | For array creation, the size of the array; `null` if the size is not specified |
| `hasGlobalScopeModifier` | `bool` | `true` if `::` precedes `new` (specifying global scope) |
| `initializer` | `initializer?` | The expression evaluated to determine the initial value; `null` if the array is not initialized. For an array `new`, repeat this argument for each element. |

**Inherits properties from:**

- astnode
- expression

## Example

The `newOperator` matches source code such as the following:

  
 [image: C++ code follows]   

```
int* myPtr = ::new int();
```

In this case, the `.operandType` is an `int`
(which can be matched by the `intType` pattern)
and the `.hasGlobalScopeModifier` is `true`.

The following CodeXM pattern matches uses of the `::new` operator
(that is, with the global scope modifier `::`):

  
 [image: CXM code follows]   

```
    pattern newIntPtrWithGlobalScope {
        newOperator {
            .hasGlobalScopeModifier == true;
        }
    };
```
