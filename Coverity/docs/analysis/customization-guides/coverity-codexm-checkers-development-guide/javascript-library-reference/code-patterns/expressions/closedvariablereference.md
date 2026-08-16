---
title: "closedVariableReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/closedvariablereference.html"
content_id: "B9nnHkiw9487nnv~7CD1gA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:27.168448+00:00"
---

# closedVariableReference

Matches references to closed variables.

This pattern only matches nodes of type `expression`.

## Properties

`closedVariableReference` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `identifier` | `string?` | The identifier of the referenced variable; `null` if there is none |
| `mangledName` | `string` | The mangled name of the referenced variable |
| `variable` | `symbol` | The symbol referenced |

**Inherits properties from:**

- astnode
- expression

## See also

closedVariableSymbol
