---
title: "functionDefinition"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/functiondefinition.html"
content_id: "7JcdiZYmsjKNU9dphjGodg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:44.094352+00:00"
---

# functionDefinition

This class represents a function definition.

The `functionDefinition` class appears in the following hierarchy:

- **functionDefinition**

## Properties

`functionDefinition` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `allCode` | `set<astnode>` | All source code in this function |
| `body` | `statement` | A `blockStatement` of the function body |
| `formalParameterList` | `list<symbol>` | A list of `parameterSymbol` objects, one for each parameter to the function |
| `functionSymbol` | `symbol` | The `functionSymbol` that represents this function |
| `location` | `sourceloc` | The location of the definition |
| `paths` | `executionPaths` | All execution paths in this function |
