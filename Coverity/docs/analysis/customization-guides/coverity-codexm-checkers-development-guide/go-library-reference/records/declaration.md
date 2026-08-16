---
title: "declaration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/declaration.html"
content_id: "Mn5YbbnEiV7rhtL93aVnxg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:05.115297+00:00"
---

# declaration

Represents a declaration.

## Properties

`declaration` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `initializer` | `initializer?` | An initializer; `null` if there is none |
| `kind` | `enum variableDeclarationKind` | The kind of declaration: `` `local` `` if the scope of the variable is local; `` `static` `` if the variable is declared within a `struct` or an `interface`. See variableDeclarationKind. |
| `variable` | `symbol` | The symbol variable |

## Example

The following CodeXM pattern matches the declaration of an array whose name is `perYear`:

  
 [image: CXM code follows]   

```
   let myTableDeclaration = pattern {
        declaration {
            .variable == localVariableSymbol {
                .simpleName == "perYear"
            }
        }
    }
```
