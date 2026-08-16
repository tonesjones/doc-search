---
title: "variableSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/variablesymbol.html"
content_id: "codhfehrP0wGqHAfuT8nqg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:31.131251+00:00"
---

# variableSymbol

Matches the symbols of all declared variables.

This pattern only matches nodes of type `symbol`.

## Properties

`variableSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isFinal` | `bool` | `true` if the variable is declared `final` |
| `qualifiedName` | `string` | The name of the variable, including any scope information |
| `variableScopeKind` | `enum` | Either `` `local` `` for local variables, or `` `static` `` for statically defined variables; see variableScopeKind |
| `simpleName` | `string` | The name of the variable, without scope information |

**Inherits properties from:**

- symbol

## See also

enumVariableSymbol,
localVariableSymbol,
parameterSymbol,
staticVariableSymbol
