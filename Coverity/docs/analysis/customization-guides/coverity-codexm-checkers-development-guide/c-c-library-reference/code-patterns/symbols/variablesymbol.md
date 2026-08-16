---
title: "variableSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/variablesymbol.html"
content_id: "MOGuWud4b6FVDYcrS_dKIQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:05.299120+00:00"
---

# variableSymbol

Matches uses of variables, including both global and local variables.

This pattern only matches nodes of type `symbol`.

## Properties

`variableSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `scope` | `enum variableScopeEnum` | The scope of the variable: either `` `local` `` or `` `global` ``; see variableScopeEnum |
| `hasImplicitSize` | `bool` | `true` if the variable is an array with an implicit size; for example, `int a[] = {1, 2, 3}` |
| `isFunctionStatic` | `bool` | `true` if the variable is a static variable in a function |
| `isVolatile` | `bool` | `true` if the variable was declared with the `volatile` specifier |
| `isClassStatic` | `bool` | `true` if the variable is a static class member |
| `isConstexpr` | `bool` | (C++ since C++11) `true` if the variable was declared as a `constexpr` |
| `isCUDAConstant` | `bool` | `true` if the variable is declared as a CUDA `__constant__` |
| `isCUDAManaged` | `bool` | `true` if the variable is declared as a CUDA `__managed__` variable |
| `isCUDAShared` | `bool` | `true` if the variable is declared as a CUDA `__shared__` variable |
| `isAlignmentAssigned` | `bool` | `true` if the variable is aligned |
| `alignmentInBytes` | `int?` | The alignment of the type, in bytes; `null` if the type is not aligned |

**Inherits properties from:**

- symbol

## See also

globalVariableSymbol, localVariableSymbol
