---
title: "ifStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ifstatement.html"
content_id: "Kj_10YxJio~tctDuo2LU4A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:24.116845+00:00"
---

# ifStatement

Matches entire `if` statements, including their condition expressions
and their `true` and `false` branches.

This pattern only matches nodes of type `statement`.

## Properties

`ifStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `conditionExpression` | `expression` | The condition of the `if` |
| `falseStatement` | `statement?` | The statement to execute if the condition is false; `null` if there is none |
| `trueStatement` | `statement` | The statement to execute if the condition is true |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches `if` statements
that have no `else` clause:

[image: CXM code follows]

```
    pattern ifNoElse {
        ifStatement {
            .falseStatement == null
        }
    };
```
