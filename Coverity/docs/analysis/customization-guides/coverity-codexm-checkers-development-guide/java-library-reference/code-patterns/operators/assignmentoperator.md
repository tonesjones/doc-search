---
title: "assignmentOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/assignmentoperator.html"
content_id: "xAtqsJDhN6qAMCYNrKqSNw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:15.337453+00:00"
---

# assignmentOperator

Matches all forms of the assignment-operator expression.

Even though variable declarations look similar to assignment operators, this pattern does not match variable declarations where the variable is
initialized with a value (see variableDeclaration).

This general pattern matches both simple (`a = b`)
and compound (`a += b`) forms of assignments.

This pattern only matches nodes of type `expression`.

## Properties

`assignmentOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum assignKind` | The kind of assignment, either `` `simple` `` or `` `compound` ``; see assignKind |
| `operator` | `enum` | The operator used: one of `` `=` ``, `` `+=` ``, `` `-=` ``, `` `*=` ``, `` `/=` ``, `` `|=` ``, `` `&=` ``, `` `%=` ``, `` `^=` ``, `` `>>=` ``, or `` `<<=` `` |
| `sourceExpression` | `expression` | The right-hand side of the assignment |
| `targetExpression` | `expression` | The left-hand side of the assignment |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches any assignment where the source of the assignment is a cast:

  
 [image: CXM code follows]   

```
    pattern assignedFromCast {
        assignmentOperator {
            .sourceExpression == castOperator
        }
    };
```

## See also

assignmentOperatorCompound,
assignmentOperatorSimple
