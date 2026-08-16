---
title: "functionDefinition"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functiondefinition.html"
content_id: "qpqIkT~I8whHBEHPKR1rTw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:13.413531+00:00"
---

# functionDefinition

Describes a function definition.

## Properties

`functionDefinition` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `allCode` | `set<astnode>` | All nodes within the function. If the object is a variable, this list contains only the variable's initializer. |
| `body` | `statement` | The function body. This is a `blockStatement`. |
| `formalParameterList` | `list<symbol>` | A list of `parameterSymbol` objects, one for each parameter to the function |
| `functionSymbol` | `symbol` | The symbol that represents this function |
| `isScriptFunction` | `bool` | `true` if this function definition defines the body of the Python script |
| `location` | `sourceloc` | The location in the code: can be used for defect reporting |
| `paths` | `executionPaths` | The executable paths that can be used for path-sensitive analysis |
| `qualifiedName` | `string?` | The name of the function, including scope information; `null` if the name is not available |
| `simpleName` | `string?` | The name of the function, excluding scope information; `null` if the name is not available |
