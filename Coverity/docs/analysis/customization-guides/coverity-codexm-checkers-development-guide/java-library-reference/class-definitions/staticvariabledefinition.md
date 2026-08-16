---
title: "staticVariableDefinition"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/staticvariabledefinition.html"
content_id: "QLScgyNjob73ZCZZfXQsaA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:16.516191+00:00"
---

# staticVariableDefinition

Describes a variable declared as static within a class.

## Properties

`staticVariableDefinition` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `initializer` | `initializer>` | The initializer for this variable; `null` if one does not exist |
| `variable` | `symbol` | A `staticVariableSymbol` that represents this variable |

**Inherits properties from:**

- functionOrStaticVariableDefinition
