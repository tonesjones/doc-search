---
title: "localVariableSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/localvariablesymbol.html"
content_id: "ohVwChcRRTMQwF0GqaOF~A"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:31.055380+00:00"
---

# localVariableSymbol

Matches the variable symbols used in variable declarations.

This pattern only matches nodes of type `symbol`.

## Properties

`localVariableSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isFinal` | `bool` | `true` if they symbol is declared as `final` |
| `qualifiedName` | `string` | The name of the variable, including any scope information |
| `simpleName` | `string` | The name of the variable, without scope information |

**Inherits properties from:**

- symbol

## Example

The following CodeXM pattern finds all uses of local variables:

  
 [image: CXM code follows]   

```
    pattern localVariableUse {
        variableReference {
            .variable == localVariableSymbol
        }
    };
```
