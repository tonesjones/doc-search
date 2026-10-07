---
title: "fieldSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/fieldsymbol.html"
content_id: "5EwyG8KkTyOPHtL6UZQPhQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:30.956521+00:00"
---

# fieldSymbol

Matches field symbols in class declarations.

This pattern only matches nodes of type `symbol`.

## Properties

`fieldSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `access` | `enum` | The type of access to the field: `` `public` ``, `` `private` ``, or `` `protected` `` |
| `attributes` | `list<codeAttribute>` | A list of the code attributes applied to this field |
| `isFinal` | `bool` | `true` if the field is declared `final` |
| `isTransient` | `bool` | `true` if the field is declared `transient` |
| `isVolatile` | `bool` | `true` if the field is declared `volatile` |
| `ownerClass` | `classType` | The class that this field belongs to |
| `qualifiedName` | `string` | The name of the field, including any scope information |
| `simpleName` | `string` | The name of the field, excluding scope information |

## Example

The following CodeXM pattern finds all field accesses to private fields:

  
 [image: CXM code follows]   

```
    pattern privateFieldAccess {
        fieldAccess {
            .field == fieldSymbol { .access == `private` }
        }
    };
```
