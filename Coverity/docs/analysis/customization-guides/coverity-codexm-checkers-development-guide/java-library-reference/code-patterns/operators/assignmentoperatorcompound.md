---
title: "assignmentOperatorCompound"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/assignmentoperatorcompound.html"
content_id: "8E5JL6vU5s7bRwbfDa7GIw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:16.077274+00:00"
---

# assignmentOperatorCompound

Matches only compound assignment operators: for example, `a += b`.

This pattern only matches nodes of type `expression`.

## Properties

`assignmentOperatorCompound` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum assignKind` | Always `` `compound` ``; see assignKind |
| `operator` | `enum` | The operator used: one of `` `+=` ``, `` `-=` ``, `` `*=` ``, `` `/=` ``, `` `|=` ``, `` `&=` ``, `` `%=` ``, `` `^=` ``, `` `>>=` ``, or `` `<<=` `` |
| `sourceExpression` | `expression` | The right-hand side of the assignment |
| `targetExpression` | `expression` | The left-hand side of the assignment |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches assignments that use the `` `+=` `` operator:

  
 [image: CXM code follows]   

```
    pattern addCompoundAssignment {
        assignmentOperatorCompound {
            .operator == `+=`
        }
    };
```

## See also

assignmentOperator,
assignmentOperatorSimple
