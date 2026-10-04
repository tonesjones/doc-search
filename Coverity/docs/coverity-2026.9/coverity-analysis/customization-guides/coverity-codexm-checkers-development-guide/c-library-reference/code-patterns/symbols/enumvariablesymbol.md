---
title: "enumVariableSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/enumvariablesymbol.html"
content_id: "moqmAz1IkfdIUkVCqCKeiA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:30.907676+00:00"
---

# enumVariableSymbol

Matches symbols used in `enum` declarations.

This pattern only matches nodes of type `symbol`.

## Properties

`enumVariableSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `parentEnum` | `classType` | The parent `enum` class of this enum value |
| `qualifiedName` | `string` | The name of the `enum` value, including any scope information |
| `simpleName` | `string` | The name of the `enum` value, without scope information |

**Inherits properties from:**

- symbol

## Example

The following CodeXM pattern finds *all* uses of enum variables:

  
 [image: CXM code follows]   

```
    pattern enumVariableUse {
        variableReference {
            .variable == enumVariableSymbol
        }
    };
```
