---
title: "continueStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/continuestatement.html"
content_id: "0hs88QsrksxO~yU~tsdH2Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:21.341123+00:00"
---

# continueStatement

Matches `continue` statements.

This pattern only matches nodes of type `statement`.

## Properties

`continueStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `controlStatement` | `statement` | The flow-of-control statement, such as `while`, within which the `continue` occurs |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches `continue` statements
within `while` loops:

[image: CXM code follows]

```
    pattern continueFromWhile {
        continueStatement {
            .controlStatement == whileLoop
        }
    };
```

## See also

breakStatement,
forEachLoop,
whileLoop
