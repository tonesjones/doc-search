---
title: "returnStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/returnstatement.html"
content_id: "BMCmciLaqRmSIqtBs5WSWQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:11.463686+00:00"
---

# returnStatement

Matches `return` statements.

This pattern only matches nodes of type `statement`.

## Properties

`returnStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isVoid` | `bool` | Indicates that this is a simple `return` statement as used in a void function |
| `returnedExpression` | `expression?` | The expression that returns when the return type is is not `void`; `null` if the return type is `void` |

**Inherits properties from:**

- astnode
- statement

## Example

The `returnStatement` pattern matches the following two cases:

[image: JavaScript code follows]

```
    return 1;       // Case 1
    return;         // Case 2
```

In the first case, the `.returnedExpression` property is the literal `1`.

In the second case, the `.isVoid` property is `true`.
