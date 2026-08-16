---
title: "declaration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/declaration.html"
content_id: "5LcK~uuRuBLdqGfw6Fyqfw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:40.009986+00:00"
---

# declaration

Represents a declaration.

## Properties

`declaration` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `initializer` | `initializer>` | An initializer; `null` if there is none |
| `kind` | `variableDeclarationKind` | The kind of declaration |
| `variable` | `symbol` | The symbol variable |

## Example

The following CodeXM pattern matches a try-with-resource statement, using a resource with the name `myResource`:

  
 [image: CXM code follows]   

```
    let myResourceDeclaration = pattern {
        declaration {
            .variable == localVariableSymbol {
                .simpleName == "myResource"
            }
        }
    }
    in
    patternResourceTry {
        tryStatement as t where
            exists r in t.resourcesList where
                r matches myResourceDeclaration
    };
```

## See also

tryStatement
