---
title: "parameterReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/parameterreference.html"
content_id: "htu5DU2GeCWTb1DkrZyhgg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:36.255968+00:00"
---

# parameterReference

Matches references to parameters.

This pattern only matches nodes of type `expression`.

## Properties

`parameterReference` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `identifier` | `string?` | The identifier of the referenced variable; `null` if there is none |
| `mangledName` | `string?` | The mangled name of the referenced variable; `null` if there is none |
| `variable` | `symbol` | The symbol referenced |

**Inherits properties from:**

- astnode
- expression

## See also

parameterSymbol
