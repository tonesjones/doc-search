---
title: "labeledContinueStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/labeledcontinuestatement.html"
content_id: "p8HMuu25DXC_5cspE7MRWg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:43.462183+00:00"
---

# labeledContinueStatement

Matches `continue` statements that target a label.

This pattern only matches nodes of type `statement`.

## Properties

`labeledContinueStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `controlStatement` | `statement` | The flow-of-control statement within which the break occurs; for example, `while` or `switch` |
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
