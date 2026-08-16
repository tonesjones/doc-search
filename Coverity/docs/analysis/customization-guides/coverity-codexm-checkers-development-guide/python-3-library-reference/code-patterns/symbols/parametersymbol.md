---
title: "parameterSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/parametersymbol.html"
content_id: "1RsGoJ4dhmewvKmARk80gQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:08.342913+00:00"
---

# parameterSymbol

Matches parameter symbols used in function declarations.

This pattern only matches nodes of type `symbol`.

## Properties

`parameterSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `location` | `sourceloc` | The location of the parameter in the source code |
| `position` | `int` | The position of the parameter in the function declaration |
| `qualifiedName` | `string` | The name of the parameter, with scope information |
| `scopeList` | `list<string>` | The elements of the `qualifiedNsame`, broken up into a list |
| `simpleName` | `string` | The name of the parameter, without scope information |
| `type` | `type` | The parameter's type |

**Inherits properties from:**

- symbol

## Example

The following CodeXM pattern finds all uses of parameters whose type is composite:

[image: CXM code follows]

```
    pattern useOfCompositeTypeParameter {
        variableReference {
            .variable == parameterSymbol {
                .type == compositeType
            }
        }
    };
```

## See also

functionSymbol
globalVariableSymbol
localVariableSymbol
