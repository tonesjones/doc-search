---
title: "staticVariableSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/staticvariablesymbol.html"
content_id: "r1esFzP_7ktvPJyN5ipPtw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:03.138995+00:00"
---

# staticVariableSymbol

Matches symbols for variables declared as `const`.

This pattern only matches nodes of type `symbol`.

## Properties

`staticVariableSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `ownerClass` | `classType` | The owner class for the static variable symbol |
| `qualifiedName` | `string` | The name of the variable, including any scope information |
| `simpleName` | `string` | The name of the variable, without scope information |

**Inherits properties from:**

- symbol

## Example

The following CodeXM pattern finds all uses of statically defined variables:

  
 [image: CXM code follows]   

```
    pattern staticVariableUse {
        variableReference {
            .variable == staticVariableSymbol
        }
    };
```

## See also

variableSymbol
