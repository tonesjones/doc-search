---
title: "blockStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/blockstatement.html"
content_id: "p7gdzVNSiKzq~5q0DKooLg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:00.132278+00:00"
---

# blockStatement

Matches block statements.

This pattern only matches nodes of type `statement`.

## Properties

`blockStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `containedStatements` | `statement` | The statements contained in the block |

**Inherits properties from:**

- astnode
- statement

## Example

The `blockStatement` pattern matches the body of the following function:

[image: JavaScript code follows]

```
    function f(x, y, z) {
        return x + y + z;
    };
```

In this instance, the `.containedStatement` property is a list that contains the `return` statement.
