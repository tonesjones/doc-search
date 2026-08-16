---
title: "variableDeclaration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/variabledeclaration.html"
content_id: "cAvRF9DN0zBOeP03e44vcQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:50.421245+00:00"
---

# variableDeclaration

Matches all kinds of variable declarations.

## Properties

`variableDeclaration` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `initializer` | `initializer>` | The initialization of the variable, if it exists |
| `kind` | `enum variableDeclarationKind` | Either `` `local` `` or `` `static` ``; see variableDeclarationKind |
| `variable` | `symbol` | The symbol of the defined variable |

**Inherits properties from:**

- astnode
- declaration

## Example

The following CodeXM pattern matches all variables declared with type `char`:

  
 [image: CXM code follows]   

```
    pattern charVariableDeclaration {
        variableDeclaration {
            .variable  == symbol {
                .type == charType
            }
        }
    };
```
