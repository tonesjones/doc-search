---
title: "labeledBreakStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/labeledbreakstatement.html"
content_id: "~7NIT1nZxG3URS88rJgEeQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:42.807526+00:00"
---

# labeledBreakStatement

Matches `break` statements that target a label.

This pattern only matches nodes of type `statement`.

## Properties

`labeledBreakStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `controlStatement` | `statement` | The flow-of-control statement within which the break occurs; for example, `while` or `switch`. |
| `target` | `statement` | The label to break to. |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches a `break` statement that targets the label `outer`:

  
 [image: CXM code follows]   

```
    pattern outerBreak {
        labeledBreakStatement {
            .target == labelStatement { .nameString == "outer" }
        }
    };
```

## See also

breakStatement,
doWhileLoop,
forLoop,
forLoopEnhanced,
forLoopSimple,
labelStatement,
switchStatement,
whileLoop
