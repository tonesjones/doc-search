---
title: "assignmentStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/assignmentstatement.html"
content_id: "kpEWcB7mMjfYvEHNVU7O8A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:19.296981+00:00"
---

# assignmentStatement

Matches assignment statements.

This pattern only matches nodes of type `statement`.

## Properties

`assignmentStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum assignmentKind` | Either `` `simple` `` or `` `augmented` ``; see assignmentKind |
| `assignmentOperator` | `expression` | The expression that describes this assignment statement |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches simple assignment statements
(that is, assignments that use the `=` operator):

[image: CXM code follows]

```
    pattern simpleAssignment {
        assignmentStatement {
            .assignmentKind == `simple`
        }
    };
```
