---
title: "assignmentOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/assignmentoperator.html"
content_id: "AJ_ois7tTFQfTtYGx9mipQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:58.298407+00:00"
---

# assignmentOperator

Matches all forms of assignment.

CAUTION:

This pattern does not appear in pattern decomposition:
Use assignmentStatement instead.
For more about decomposition, see Decomposing a Pattern to Match Specific Properties.

This pattern only matches nodes of type `expression`.

## Properties

`assignmentOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `operator` | `enum` | One of `` `=` ``, `` `+=` ``, `` `-=` ``, `` `*=` ``, `` `/=` ``, `` `|=` ``, `` `&=` ``, `` `%=` ``, `` `^=` ``, `` `>>=` ``, or `` `<<=` `` |
| `sourceExpression` | `expression` | The source of the new value (the right-hand side of the operator) |
| `targetExpression` | `expression` | The expression to which the new value is assigned (the left-hand side of the operator) |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches only assignments made using the `+=` operator:

[image: CXM code follows]

```
    pattern incrementAssignmentOperator {
        assignmentOperator {
            .operator == `+=`
        }
    };
```
