---
title: "labeledContinueStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/labeledcontinuestatement.html"
content_id: "QixBvFj3_gSCODqMleTEww"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:25.625602+00:00"
---

# labeledContinueStatement

Matches `continue` statements that target a label.

This pattern only matches nodes of type `statement`.

## Properties

`labeledContinueStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `controlStatement` | `statement` | The flow-of-control statement within which the `continue` occurs; for example, `while` or `switch` |
| `target` | `statement` | The label to target |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches a `continue` statement that targets the label `outer`:

  
 [image: CXM code follows]   

```
    pattern outerBreak {
        labeledContinueStatement {
            .target == labelStatement { .nameString == "outer" }
        }
    };
```
