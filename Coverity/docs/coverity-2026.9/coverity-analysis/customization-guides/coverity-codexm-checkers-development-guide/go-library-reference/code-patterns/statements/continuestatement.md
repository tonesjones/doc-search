---
title: "continueStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/continuestatement.html"
content_id: "W86c4rqyBnvJNQxmxD~sbg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:33.612502+00:00"
---

# continueStatement

Matches `continue` statements.

This pattern only matches nodes of type `statement`.

## Properties

`continueStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `controlStatement` | `statement` | The flow-control statement within which the `continue` occurs. For example, `switch`. |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM example matches `continue` statements within a `switch`:

  
 [image: CXM code follows]   

```
    pattern continueFromSwitch {
        continueStatement {
            .controlStatement == switchStatement
        }
    };
```

## See also

allLoops,
forLoop,
forLoopSimple,
labeledContinueStatement,
switchStatement
