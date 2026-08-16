---
title: "localVariableSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/localvariablesymbol.html"
content_id: "aw0vV4QadaG7scXAGtKRgg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:03.878753+00:00"
---

# localVariableSymbol

Matches uses of local variables.

## Properties

`localVariableSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `hasImplicitSize` | `bool` | `true` if the variable is an array with an implicit size; for example, `int a[] = {1, 2, 3}` |
| `isVolatile` | `bool` | `true` if the variable was declared with the `volatile` specifier |
| `isRegister` | `bool` | `true` if the variable was declared with the `register` specifier |
| `isCUDAConstant` | `bool` | `true` if the variable is declared as a CUDA `__constant__` |
| `isCUDAManaged` | `bool` | `true` if the variable is declared as a CUDA `__managed__` variable |
| `isCUDAShared` | `bool` | `true` if the variable is declared as a CUDA `__shared__` variable |
| `isAlignmentAssigned` | `bool` | `true` if the variable is aligned |
| `alignmentInBytes` | `int?` | The alignment of the type, in bytes; `null` if the type is not aligned |

**Inherits properties from:**

- symbol

## Example

The `localVariableSymbol` pattern matches variable
`a` in the following source code snippet, provided
the property `.identifier` specifies `"a"`:

  
 [image: C/C++ code follows]   

```
void test() {
    int a = 1;
    a++;
};
```

The following CodeXM pattern limits the more general `variableReference` to match only local variables:

  
 [image: CXM code follows]   

```
    pattern variableReferenceLocal {
        variableReference {
            .variable == localVariableSymbol
        }
    };
```
