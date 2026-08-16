---
title: "fieldSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/fieldsymbol.html"
content_id: "Qu12NYeonZWyXwaI_IAvIQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:00.258686+00:00"
---

# fieldSymbol

Matches field symbols in class declarations.

This pattern only matches nodes of type `symbol`.

## Properties

`fieldSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isTransient` | `bool` | `true` if the field is declared `transient` |
| `isVolatile` | `bool` | `true` if the field is declared `volatile` |
| `ownerClass` | `classType` | The owner class for the field symbol |
| `qualifiedName` | `string` | The name of the field, including any scope information |
| `simpleName` | `string` | The name of the field, excluding scope information |

**Inherits properties from:**

- symbol

## Example

The following CodeXM pattern finds the field name `Unleaded`:

  
 [image: CXM code follows]   

```
    pattern privateFieldAccess {
        fieldAccess {
            .field == fieldSymbol { .simpleName == `Unleaded` }
        }
    }
```
