---
title: "assignmentOperatorCompound"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/assignmentoperatorcompound.html"
content_id: "eELbln7Ste60M5u~v_Ri0Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:03.207791+00:00"
---

# assignmentOperatorCompound

Matches only compound assignment operators such as `a += b`.

This pattern only matches nodes of type `expression`.

## Properties

`assignmentOperatorCompound` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum assignKind` | Always `` `compound` ``; see assignKind |
| `operator` | `enum` | The operator used: one of `` `+=` ``, `` `-=` ``, `` `*=` ``, `` `/=` ``, `` `|=` ``, `` `&=` ``, `` `%=` ``, `` `^=` ``, `` `>>=` ``, or `` `<<=` `` |
| `sourceExpression` | `expression` | The expression on the right-hand side of the assignment operator |
| `targetExpression` | `expression` | The expression on the left-hand side of the assignment operator |

**Inherits properties from:**

- astnode
- expression

## Example

The following pattern matches the `+=` operator:

```
    pattern addCompoundAssignment {
        assignmentOperatorCompound {
            .operator == `+=`
        }
    };
```

## See also

assignmentOperatorSimple,
assignmentOperator
