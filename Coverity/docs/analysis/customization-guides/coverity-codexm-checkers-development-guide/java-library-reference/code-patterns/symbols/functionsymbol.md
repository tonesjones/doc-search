---
title: "functionSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functionsymbol.html"
content_id: "vdq34VpldI0SPu36o37VZg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:34.491761+00:00"
---

# functionSymbol

Matches symbols used to declare functions.

This pattern only matches nodes of type `symbol`.

## Properties

`functionSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `annotations` | `list<codeAnnotation>` | A list of the code annotations applied to this function |
| `explicitParameterCount` | `int` | The number of explicit parameters this function has |
| `functionType` | `functionType` | The type of the function |
| `hasThis` | `bool` | `true` if the function has the implicit `this` argument |
| `isAbstract` | `bool` | `true` if the function is declared `abstract` |
| `isClassInitializer` | `bool` | `true` if this function is a class initializer |
| `isCompilerGenerated` | `bool` | `true` if the function is compiler-generated |
| `isConstructor` | `bool` | `true` if the function is a constructor |
| `isFinal` | `bool` | `true` if the function is declared `final` |
| `isStaticMethod` | `bool` | `true` if the function is a static method |
| `isStrictfp` | `bool` | `true` if the function is declared with `strictfp` |
| `isSynchronized` | `bool` | `true` if the function is declared with `synchronized` |
| `isVirtual` | `bool` | `true` if the function is declared `virtual` |
| `qualifiedName` | `string` | The name of the function, including any scope information |
| `simpleName` | `string` | The name of the function, without scope information |

**Inherits properties from:**

- symbol

## Example

The following CodeXM pattern finds all function calls to synchronized functions:

  
 [image: CXM code follows]   

```
    pattern callToSynchronized {
        functionCall {
            .calledFunction == functionSymbol { .isSynchronized == true }
        }
    };
```
