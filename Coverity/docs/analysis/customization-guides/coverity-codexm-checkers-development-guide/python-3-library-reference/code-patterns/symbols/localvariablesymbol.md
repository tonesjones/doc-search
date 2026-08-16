---
title: "localVariableSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/localvariablesymbol.html"
content_id: "8Aa7XpLkVvNL9FXwS_jS_g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:07.282559+00:00"
---

# localVariableSymbol

Matches local variable symbols.

This pattern only matches nodes of type `symbol`.

## Properties

`localVariableSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `qualifiedName` | `string` | The name of the variable, with scope information |
| `simpleName` | `string` | The name of the variable, without scope information |

**Inherits properties from:**

- symbol

## Example

The following CodeXM pattern finds all uses of local variables whose type is composite:

[image: CXM code follows]

```
    pattern useOfCompositeTypeLocalVariable {
        variableReference {
            .variable == localVariableSymbol {
                .type == compositeType
            }
        }
    };
```

## See also

functionSymbol,
globalVariableSymbol,
parameterSymbol
