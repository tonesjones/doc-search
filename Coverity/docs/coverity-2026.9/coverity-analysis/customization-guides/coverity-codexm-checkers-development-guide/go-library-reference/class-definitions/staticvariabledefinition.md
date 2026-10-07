---
title: "staticVariableDefinition"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/staticvariabledefinition.html"
content_id: "bI6v7hJVMRkpmxRWKYbZ4A"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:32.533595+00:00"
---

# staticVariableDefinition

Matches symbols for variables that are declared as `const`.

## Properties

`staticVariableDefinition` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `initializer` | `initializer?` | The initializer for this variable; `null` if no initializer exists. |
| `variable` | `symbol` | A `staticVariableSymbol` that represents this variable. |

**Inherits properties from:**

- functionOrStaticVariableDefinition
