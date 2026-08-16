---
title: "breakStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/breakstatement.html"
content_id: "GtJF43tLAJ4HHKQmiAAFXg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:20.677252+00:00"
---

# breakStatement

Matches `break` statements.

This pattern only matches nodes of type `statement`.

## Properties

`breakStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `controlStatement` | `statement` | The flow-of-control statement, such as `while`, within which the `break` occurs |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches `break` statements
within `while` loops:

[image: CXM code follows]

```
    pattern breakFromSwitch {
        breakStatement {
            .controlStatement == whileLoop
        }
    };
```

## See also

continueStatement,
forEachLoop,
whileLoop
