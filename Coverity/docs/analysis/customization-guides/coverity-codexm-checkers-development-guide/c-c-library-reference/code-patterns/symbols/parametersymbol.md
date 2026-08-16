---
title: "parameterSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/parametersymbol.html"
content_id: "eMMo~sZRwJpFcOkV0TioAw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:04.636311+00:00"
---

# parameterSymbol

Matches uses of named parameters in function definitions.

## Properties

`parameterSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `position` | `int` | The position in the parameter list |
| `isThis` | `bool` | `true` if the symbol is the `this` pointer (applies only to C++ source) |
| `isArray` | `bool` | `true` if this parameter was declared as an array with brackets and a minimum size |
| `arrayType` | `arrayType?` | If the parameter was declared as an array, this property names the associated array type; `null` if the parameter is not an array |
| `isStaticSizeArray` | `bool` | `true` if the keyword `static` was used when specifying the array size (does not apply if the parameter is not an array) |
| `declaredType` | `type` | The parameter type as it appears in the function declaration, before dereferencing. In particular, this property can include array types. |

**Inherits properties from:**

- symbol

## Example

The `parameterSymbol` pattern matches variable
`a` in the following snippet, provided the `.identifier` property
specifies `"a"`:

  
 [image: C/C++ code follows]   

```
void test( int a, int b[100] ) {
    a++;
};
```

The following CodeXM pattern limits the more general `variableReference` to match only parameters:

  
 [image: CXM code follows]   

```
    pattern variableReferenceParameter {
        variableReference {
            .variable == parameterSymbol
        }
    };
```
