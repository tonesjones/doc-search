---
title: "ifStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/ifstatement.html"
content_id: "MWB17Pji_y02UCxR2WTPpQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:45.102153+00:00"
---

# ifStatement

Matches entire `if` statements, including their condition expressions
and their `true` and (optional) `false` branches.

This pattern only matches nodes of type `statement`.

## Properties

`ifStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `conditionExpression` | `expression` | The condition that determines whether the `trueStatement` or `falseStatement` is executed. |
| `falseStatement` | `statement`? | The `else` statement, which, if present, is only executed if `conditionExpression` is `false`. If there is no `else` statement in the source code, this property is `null`. |
| `trueStatement` | `statement` | The `then` statement, which is only executed if `conditionExpression` is `true` |

**Inherits properties from:**

- astnode
- statement

## Example

The `ifStatement` pattern matches the following two cases of JavaScript code:

[image: JavaScript code follows]

```
    if(cond) {        // Case 1
        // ...
    } else {
        // ...
    }
                
    if(cond) {        // Case 2
        // ...
    };
```

/

In the second case, the `.falseStatement` property is `null`.
