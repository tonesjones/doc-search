---
title: "globalVariableSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/globalvariablesymbol.html"
content_id: "6QUTSMmLlHYEW8afjH4Gyw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:03.134352+00:00"
---

# globalVariableSymbol

Matches uses of global variables.

## Properties

`globalVariableSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `hasImplicitSize` | `bool` | `true` if the variable is an array with an implicit size; for example, `int a[] = {1, 2, 3}` |
| `isFunctionStatic` | `bool` | `true` if the variable is a static variable in a function |
| `isVolatile` | `bool` | `true` if the variable was declared with the `volatile` specifier |
| `isClassStatic` | `bool` | `true` if the variable is a static class member |
| `isConstexpr` | `bool` | (C++) `true` if the variable was declared as a `constexpr` |
| `isCUDAConstant` | `bool` | `true` if the variable is declared as a CUDA `__constant__` |
| `isCUDAManaged` | `bool` | `true` if the variable is declared as a CUDA `__managed__` variable |
| `isCUDAShared` | `bool` | `true` if the variable is declared as a CUDA `__shared__` variable |
| `isAlignmentAssigned` | `bool` | `true` if the variable is aligned |
| `alignmentInBytes` | `int?` | The alignment of the type, in bytes; `null` if the type is not aligned |

**Inherits properties from:**

- symbol

## Example

The `globalVariableSymbol` CodeXM pattern matches variable
`a` in the following source-code snippet,
provided the property `.identifier` specifies `"a"`:

  
 [image: C/C++ code follows]   

```
int a;
void test() {
    a++;
};
```

The following CodeXM expression matches `a` in the preceding source code:

  
 [image: CXM code follows]   

```
    node matches variableReference as v
        && v.variable matches globalVariableSymbol;
```

The following CodeXM code, relying on pattern decomposition, accomplishes the same thing:

  
 [image: CXM code follows]   

```
    node matches variableReference {
        .variable matches globalVariableSymbol
    };
```
