---
title: "globalVariableSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/globalvariablesymbol.html"
content_id: "~tUxT7m3r~F6p1~bFsS_aQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:52.496502+00:00"
---

# globalVariableSymbol

Matches global variable symbols.

This pattern only matches nodes of type `symbol`.

## Properties

`globalVariableSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `qualifiedName` | `string` | The name of the variable, with scope information |
| `simpleName` | `string` | The name of the variable, without scope information |

**Inherits properties from:**

- symbol

## Example

The following CodeXM pattern finds all uses of global variables whose type is composite:

[image: CXM code follows]

```
    pattern useOfCompositeTypeGlobalVariable {
        variableReference {
            .variable == globalVariableSymbol {
                .type == compositeType
            }
        }
    };
```

## See also

functionSymbol,
localVariableSymbol,
parameterSymbol
