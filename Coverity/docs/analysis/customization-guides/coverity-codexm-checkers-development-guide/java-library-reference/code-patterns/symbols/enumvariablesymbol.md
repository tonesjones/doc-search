---
title: "enumVariableSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enumvariablesymbol.html"
content_id: "WmxoSHCWx2N7cJqyLh5~3g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:33.001001+00:00"
---

# enumVariableSymbol

Matches symbols used in `enum` declarations.

This pattern only matches nodes of type `symbol`.

## Properties

`enumVariableSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `parentenum` | `classType` | The parent `enum` class of this `enum` value |
| `qualifiedName` | `string` | The name of the `enum` value, including any scope information |
| `simpleName` | `string` | The name of the `enum` value, without scope information |

**Inherits properties from:**

- symbol

## Example

The following CodeXM pattern finds all uses of `enum` variables:

  
 [image: CXM code follows]   

```
    pattern enumVariableUse {
        variableReference {
            .variable == enumVariableSymbol
        }
    };
```
