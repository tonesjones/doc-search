---
title: "functionSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functionsymbol.html"
content_id: "u0nQatV7Lqstg~Dw99baKQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:28.320080+00:00"
---

# functionSymbol

Matches the symbols used to declare functions.

This pattern only matches nodes of type `symbol`.

## Properties

`functionSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `attributes` | `list<codeAttribute>` | A list of the code attributes applied to this function |
| `explicitParameterCount` | `int` | The number of explicit parameters this function has |
| `functionType` | `functionType` | The type of the function |
| `hasThis` | `bool` | `true` if the function has the implicit `this` argument |
| `isAbstract` | `bool` | `true` if the function is declared `abstract` |
| `isAnonymous` | `bool` | `true` if the function is a lambda or anonymous method |
| `isAsync` | `bool` | `true` if the function is `async` |
| `isClassInitializer` | `bool` | `true` if this function is a class initializer |
| `isCompilerGenerated` | `bool` | `true` if the function is compiler-generated |
| `isConstructor` | `bool` | `true` if the function is a constructor |
| `isDestructor` | `bool` | `true` if the function is a destructor |
| `isExtension` | `bool` | `true` if the function is an extension method |
| `isFinal` | `bool` | `true` if the function is declared `final` |
| `isGeneric` | `bool` | `true` if the function is generic |
| `isOverride` | `bool` | `true` if the function is overriding |
| `isStaticConstructor` | `bool` | `true` if the function is a static constructor |
| `isStaticMethod` | `bool` | `true` if the function is a static method |
| `isVirtual` | `bool` | `true` if the function is declared `virtual` |
| `qualifiedName` | `string` | The name of the function, including any scope information |
| `simpleName` | `string` | The name of the function, without scope information |

**Inherits properties from:**

- symbol

## Example

The following CodeXM pattern finds all calls to synchronized functions:

  
 [image: CXM code follows]   

```
    pattern callToSynchronized {
        functionCall {
            .calledFunction == functionSymbol { .isSynchronized == true }
        }
    };
```
