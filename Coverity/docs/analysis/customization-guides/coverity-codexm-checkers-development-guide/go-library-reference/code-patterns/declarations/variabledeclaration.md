---
title: "variableDeclaration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/variabledeclaration.html"
content_id: "7V5Hz22qWFJ1I_FTMJnbNA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:22.318512+00:00"
---

# variableDeclaration

Matches all kinds of variable declarations.

## Properties

`variableDeclaration` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `initializer` | `initializer?` | The initializer of the variable, if it exists |
| `variableDeclarationKind` | `enum` | Either `` `unscoped` `` or `` `scoped` `` |
| `variable` | `symbol` | The identifier of the variable being declared |

**Inherits properties from:**

- astnode
- declaration

## Example

The following CodeXM pattern matches all Go variables declared with the type `int`:

  
 [image: CXM code follows]   

```
    pattern intVariableDeclaration {
        variableDeclaration {
            .variable  == symbol {
                .type == integerType
            }
        }
    }
```
