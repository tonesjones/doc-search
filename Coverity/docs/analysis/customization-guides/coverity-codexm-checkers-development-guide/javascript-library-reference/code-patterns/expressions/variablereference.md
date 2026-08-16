---
title: "variableReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/variablereference.html"
content_id: "dYPgjp1V7~IkIIYWHX5HPg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:41.017583+00:00"
---

# variableReference

Matches references to variables.

This pattern only matches nodes of type `expression`.

## Properties

`variableReference` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `identifier` | `string?` | The identifier of the referenced variable; `null` if there is none |
| `mangledName` | `string?` | The mangled name of the referenced variable; `null` if there is none |
| `variable` | `symbol` | The symbol referenced |

**Inherits properties from:**

- astnode
- expression
