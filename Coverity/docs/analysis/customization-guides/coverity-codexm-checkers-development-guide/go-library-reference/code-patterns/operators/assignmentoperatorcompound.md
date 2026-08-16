---
title: "assignmentOperatorCompound"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/assignmentoperatorcompound.html"
content_id: "cOwTZJH0UbIU0Rdp8x9ZAA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:49.629278+00:00"
---

# assignmentOperatorCompound

Matches only compound assignment operators such as `a += b`.

Even though variable declarations look similar to assignment operators, this pattern does not match
variable declarations. See variableDeclaration.

This pattern only matches nodes of type `expression`.

## Properties

`assignmentOperatorCompound` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum assignmentOperatorCompound` | Always `` `compound` ``. See assignKind. |
| `operator` | `enum` | The operator used: one of `` `+=` ``, `` `-=` ``, `` `*=` ``, `` `/=` ``, `` `|=` ``, `` `&=` ``, `` `%=` ``, `` `^=` ``, `` `>>=` ``, or `` `<<=` `` |
| `sourceExpression` | `expression` | The expression on the right-hand side of the assignment operator |
| `targetExpression` | `expression` | The expression on the left-hand side of the assignment operator |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches the `+=` operator:

  
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
