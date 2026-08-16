---
title: "variableReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/variablereference.html"
content_id: "_Qz3hxdSyI__YCi5y2zQcQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:32.114815+00:00"
---

# variableReference

Matches variable references within expressions.

## Properties

`variableReference` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `identifier` | `string` | The name of the identifier (shorthand for `.variable.identifier`) |
| `mangledName` | `string` | The internal "mangled" name used for the variable (the mangled name includes type and scope information, to disambiguate this instance of the identifier); `null` if the mangled name is not available |
| `variable` | `variableType` | The variable being referenced |
| `scope` | `enum variableScopeEnum` | The scope of the variable: either `` `local` `` or `` `global` ``. Static variables are classified as `` `global` ``; see variableScopeEnum |
| `isVolatile` | `bool` | `true` if this variable is `volatile` |
| `isFunctionStatic` | `bool` | `true` if this variable was declared within a function and modified by the keyword `static` |
| `isClassStatic` | `bool` | `true` if this variable is a `static` member variable of a class (C++ only) |

**Inherits properties from:**

- astnode
- expression

## Example

Imagine the following target code:

  
 [image: C/C++ code follows]   

```
int x = 123;        // "x" is a global variable.

void func() {
    int y;
    y = x;
};
```

The `variableReference` pattern matches `x`
in the function `func()`
(specifically in respect to the assignment `y = x`).

The following CodeXM pattern detects all references of global variables within expressions:

  
 [image: CXM code follows]   

```
    pattern globalVariableSymbolReference {
        variableReference {
            .scope == `global`;
        }
    }
```
