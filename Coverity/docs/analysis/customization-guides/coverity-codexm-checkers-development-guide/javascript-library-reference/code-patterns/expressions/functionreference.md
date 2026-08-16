---
title: "functionReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functionreference.html"
content_id: "v_SfCnRAzSaaoLLPTB4BbQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:31.393524+00:00"
---

# functionReference

Matches references to functions.

This pattern only matches nodes of type `expression`.

## Properties

`functionReference` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `identifier` | `string`? | The identifier of the referenced function |
| `mangledName` | `string` | The mangled name of the referenced function |
| `variable` | `symbol` | The function referenced |

**Inherits properties from:**

- astnode
- expression

## See also

functionSymbol
