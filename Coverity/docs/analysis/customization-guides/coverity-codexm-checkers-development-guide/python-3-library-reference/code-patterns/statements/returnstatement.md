---
title: "returnStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/returnstatement.html"
content_id: "BVDmpOpteYFTyc20XRqShA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:26.745509+00:00"
---

# returnStatement

Matches either simple `return` statements or
`return <expression>`.

This pattern only matches nodes of type `statement`.

## Properties

`returnStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isVoid` | `bool` | `true` if the function does not return an expression |
| `returnedExpression` | `expression?` | The expression that the function returns; `null` if there is none |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches `return` statements that do not return a value:

[image: CXM code follows]

```
    pattern voidReturn {
        returnStatement {
            .isVoid == true
        }
    };
```
