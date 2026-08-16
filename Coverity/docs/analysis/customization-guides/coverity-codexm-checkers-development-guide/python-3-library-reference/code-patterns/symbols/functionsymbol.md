---
title: "functionSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functionsymbol.html"
content_id: "l1134ziNcAc7WcTP5mt0bw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:05.660061+00:00"
---

# functionSymbol

Matches function variable symbols.

This pattern only matches nodes of type `symbol`.

## Properties

`functionSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `explicitParameterCount` | `int` | The number of explicit parameters this function has |
| `functionType` | `functionType` | The type of the function |
| `isClassInitializer` | `bool` | `true` if the function is a class initializer |
| `isCompilerGenerated` | `bool` | `true` if the function is compiler-generated |
| `qualifiedName` | `string` | The name of the function, with scope informaton |
| `simpleName` | `string` | The name of the function, without scope information |

**Inherits properties from:**

- symbol

## See also

globalVariableSymbol,
localVariableSymbol,
parameterSymbol
