---
title: "staticVariableSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/staticvariablesymbol.html"
content_id: "AXSaABNEnq9OK8pzorQoHg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:30.479195+00:00"
---

# staticVariableSymbol

Matches symbols for variables declared as `static` within a class.

This pattern only matches nodes of type `symbol`.

## Properties

`staticVariableSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `attributes` | `list<codeAttribute>` | A list of the code attributes applied to this variable |
| `isFinal` | `bool` | `true` if the variable is declared `final` |
| `ownerClass` | `classType` | The class this variable is located in |
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
