---
title: "parameterSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/parametersymbol.html"
content_id: "z~~bjlCYXkjvf5Hg6LGRAw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:29.717947+00:00"
---

# parameterSymbol

Matches parameter symbols in function declarations.

This pattern only matches nodes of type `symbol`.

## Properties

`parameterSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `access` | `enum` | The type of access: `` `public` ``, `` `private` ``, or `` `protected` `` |
| `isFinal` | `bool` | `true` if the parameter is declared as `final`. |
| `isThis` | `bool` | `true` if the parameter is the implicit `this` parameter |
| `location` | `location` | The parameter's location information |
| `ownerClass` | `classType` | The owner class for the symbol |
| `position` | `sourceloc` | The position of the parameter in the function |
| `qualifiedName` | `string` | The name of the class, including scope information |
| `scopeList` | `list<string>` | The scope of the parameter. This is the elements of the qualified name broken up into a list. |
| `simpleName` | `string` | The name of the parameter, without scope information |
| `type` | `type` | The parameter's type |

**Inherits properties from:**

- symbol

## Example

The following CodeXM pattern finds all uses of parameters that are references:

  
 [image: CXM code follows]   

```
    pattern useOfReferenceType {
        variableReference {
            .variable == parameterSymbol { .type == referenceType }
        }
    };
```
