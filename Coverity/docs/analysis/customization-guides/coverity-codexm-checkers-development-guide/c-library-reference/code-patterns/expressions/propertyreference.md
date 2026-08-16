---
title: "propertyReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/propertyreference.html"
content_id: "zAfVKt3a8k3idxzMxGJI6w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:45.173696+00:00"
---

# propertyReference

Matches expressions that reference a C# property.

This pattern only matches nodes of type `expression`.

## Properties

`propertyReference` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isFinal` | `bool` | `true` if this variable is declared as `final` |
| `qualifiedName` | `string` | The name of the variable, with scope information |
| `scope` | `enum variableDeclarationKind` | The scope of the variable: one of `` `static` ``, `` `local` ``, or `` `tryResource` ``; see variableDeclarationKind |
| `simpleName` | `string` | The name of the variable, without scope information. |
| `variable` | `symbol` | The symbol that represents this variable |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM code matches all variable references to final static variables:

  
 [image: CXM code follows]   

```
    pattern propertyReferenceFinal {
        propertyReference {
            .isFinal == true;
        }
    };
```
