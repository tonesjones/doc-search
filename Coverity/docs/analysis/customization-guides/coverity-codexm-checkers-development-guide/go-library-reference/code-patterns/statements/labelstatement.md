---
title: "labelStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/labelstatement.html"
content_id: "tdZH4J9yrZp5v48Sg3K8EA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:16.890015+00:00"
---

# labelStatement

Matches statements that have a label.

This pattern only matches nodes of type `statement`.

## Properties

`labelStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum labelScopeKind` | The scope of the label: `` `unscoped` `` if the label is inside a local scope; `` `scoped` `` if the label appears within a `struct` or an `interface`. See labelScopeKind. |
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
