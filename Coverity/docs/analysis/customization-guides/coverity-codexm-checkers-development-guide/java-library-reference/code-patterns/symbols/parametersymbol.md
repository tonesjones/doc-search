---
title: "parameterSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/parametersymbol.html"
content_id: "kj9JTx4Mxn4O2iLGoCSbng"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:35.880699+00:00"
---

# parameterSymbol

Matches parameter symbols used in function definitions.

This pattern only matches nodes of type `symbol`.

## Properties

`parameterSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `access` | `enum` | The type of access: `` `public` ``, `` `private` ``, or `` `protected` `` |
| `isFinal` | `bool` | `true` if the parameter is declared as `final` |
| `isThis` | `bool` | `true` if the parameter is the implicit `this` parameter |
| `ownerClass` | `classType` | The owner class for the symbol |
| `position` | `string` | The position of the parameter in the function |
| `qualifiedName` | `string` | The name of the class, including scope information |
| `scopeList` | `list<string>` | The scope of the parameter. This is the elements of the qualified name, broken up into a list. |
| `simpleName` | `string` | The name of the parameter, without scope information |
| `type` | `type` | The type of the parameter |

**Inherits properties from:**

- symbol

## Example

The following CodeXM pattern finds all uses of parameters with a `referenceType` type:

  
 [image: CXM code follows]   

```
    pattern useOfReferenceType {
        variableReference {
            .variable == parameterSymbol { .type == referenceType }
        }
    };
```
