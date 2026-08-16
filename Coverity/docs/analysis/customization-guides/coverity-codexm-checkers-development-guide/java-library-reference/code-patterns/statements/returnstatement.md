---
title: "returnStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/returnstatement.html"
content_id: "TzUMxp9q19Lp03yiIZLuXA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:44.768856+00:00"
---

# returnStatement

Matches both simple, void `return` statements,
and `return <expression>` returns.

This pattern only matches nodes of type `statement`.

## Properties

`returnStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isVoid` | `bool` | `true` if the `return` does not have an associated expression |
| `returnedExpression` | `expression>` | The expression returned, if one is specified; `null` otherwise |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches `return` statements that are void:

  
 [image: CXM code follows]   

```
    pattern voidReturn {
        returnStatement {
            .isVoid == true
        }
    };
```
