---
title: "ifStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ifstatement.html"
content_id: "~9jj8jD4lfDy0LcuT9FaBg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:42.065940+00:00"
---

# ifStatement

Matches entire `if` statements, including their condition expressions
and their `true` and `false` branches.

This pattern only matches nodes of type `statement`.

## Properties

`ifStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `conditionDeclaration` | `variableDeclaration?` | The variable declared in the condition, if one exists; `null` otherwise |
| `conditionExpression` | `expression` | The condition of the `if` statement |
| `falseStatement` | `statement>` | The false branch of the if statement; `null` if no false branch exists |
| `trueStatement` | `statement` | The true branch of the `if` statement |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches `if` statements that have no `else` clause:

  
 [image: CXM code follows]   

```
    pattern ifNoElse {
        ifStatement {
            .falseStatement == null
        }
    };
```
