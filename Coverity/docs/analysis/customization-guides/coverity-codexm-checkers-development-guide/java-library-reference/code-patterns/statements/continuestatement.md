---
title: "continueStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/continuestatement.html"
content_id: "U4SgeUQTTVqUp6KmbFxQCQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:36.971391+00:00"
---

# continueStatement

Matches `continue` statements.

This pattern only matches nodes of type `statement`.

## Properties

`continueStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `controlStatement` | `statement` | The loop statement within which the `continue` occurs; for example, `while` or `for` |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches `continue` statements from a `while` loop:

  
 [image: CXM code follows]   

```
    pattern continueFromWhile {
        continueStatement {
            .controlStatement == whileStatement
        }
    };
```

## See also

doWhileLoop,
forLoop,
forLoopEnhanced,
forLoopSimple,
labeledContinueStatement,
whileLoop
