---
title: "labelStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/labelstatement.html"
content_id: "61uZMP3_fyejFVncThVWjQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:01.669216+00:00"
---

# labelStatement

Matches statements that have a label.

This pattern only matches nodes of type `statement`.

## Properties

`labelStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `nameString` | `string` | The name of the label |
| `targetStatement` | `statement` | The statement to which this label is assigned |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern finds all `continue` statements that target the label `outer`:

  
 [image: CXM code follows]   

```
    pattern continueOuter {
        labeledContinueStatement  {
            .target == labelStatement { .nameString == "outer" }
        }
    };
```

## See also

labeledBreakStatement,
labeledContinueStatement
