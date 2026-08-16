---
title: "variableDeclaration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/variabledeclaration.html"
content_id: "ZgPXxZzJOrs2cFE7e9D0Bw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:12.587944+00:00"
---

# variableDeclaration

Matches all kinds of variable declarations.

## Properties

`variableDeclaration` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `initializer` | `initializer?` | The initializer of the variable, if it exists |
| `kind` | `enum variableDeclarationKind` | Either `` `local` `` or `` `static` ``; see variableDeclarationKind |
| `variable` | `symbol` | The identifier of the variable being declared |

**Inherits properties from:**

- astnode
- declaration

## Example

The following CodeXM pattern matches all variables declared with the type `char`:

  
 [image: CXM code follows]   

```
    pattern charVariableDeclaration {
        variableDeclaration {
            .variable == symbol {
                .type == charType
            }
        }
    };
```
