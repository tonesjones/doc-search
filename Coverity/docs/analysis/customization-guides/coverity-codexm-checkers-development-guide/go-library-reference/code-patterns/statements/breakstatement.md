---
title: "breakStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/breakstatement.html"
content_id: "eDsLve0M0O7obbInCIRW6w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:06.817342+00:00"
---

# breakStatement

Matches `break` statements.

This does not match a break that has a label.
See labeledBreakStatement.

This pattern only matches nodes of type `statement`.

## Properties

`breakStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `controlStatement` | `statement` | The flow control statement within which the break occurs; for example, `while` or `switch` |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM example matches `break` statements within a `switch`:

  
 [image: CXM code follows]   

```
    pattern breakFromSwitch {
        breakStatement {
            .controlStatement == switchStatement
        }
    };
```

## See also

forLoop,
forLoopSimple,
switchStatement
