---
title: "functionDefinition"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functiondefinition.html"
content_id: "GxvZvwL~wEGYbXhGiGqNkA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:48.755601+00:00"
---

# functionDefinition

Describes a function definition.

## Properties

`functionDefinition` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `body` | `statement` | A `blockStatement` that is the function's body. |
| `formalParameterList` | `list<symbol>` | A list of `parameterSymbol` objects, one for each parameter to the function |
| `functionSymbol` | `symbol` | The `functionSymbol` object that represents this function. |

**Inherits properties from:**

- functionOrStaticVariableDefinition
