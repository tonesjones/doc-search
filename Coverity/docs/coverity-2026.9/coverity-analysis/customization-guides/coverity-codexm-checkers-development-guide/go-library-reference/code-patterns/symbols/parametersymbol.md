---
title: "parameterSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/parametersymbol.html"
content_id: "9LCM134Y_4MhK1~17TvSTw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:37.048852+00:00"
---

# parameterSymbol

Matches parameter symbols in function declarations.

This pattern only matches nodes of type `symbol`.

## Properties

`parameterSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `ownerClass` | `classType` | The owner class for the parameter symbol |
| `position` | `sourceloc` | The position of the parameter in the function |
| `qualifiedName` | `string` | The name of the class, including scope information |
| `scopeList` | `list<string>` | The scope of the parameter. This is the elements of the qualified name broken up into a list. |
| `simpleName` | `string` | The name of the parameter, without scope information |
| `type` | `type` | The parameter's type |

**Inherits properties from:**

- symbol

## Example

The following CodeXM pattern finds all uses of parameters whose type is referenceType:

  
 [image: CXM code follows]   

```
    pattern useOfReferenceType {
        variableReference {
            .variable == parameterSymbol { .type == referenceType }
        }
    }
```

## See also

variableSymbol
