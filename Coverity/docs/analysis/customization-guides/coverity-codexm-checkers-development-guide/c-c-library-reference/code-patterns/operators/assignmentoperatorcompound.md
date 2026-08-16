---
title: "assignmentOperatorCompound"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/assignmentoperatorcompound.html"
content_id: "jcm~RtunlJKjhps3tTs5rg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:41.037375+00:00"
---

# assignmentOperatorCompound

Matches only compound assignments such as `x += y` or `z *= 3.14`.

This pattern is shorthand for the pattern `` assignmentOperator { .kind == `compound` } ``.

This pattern only matches nodes of type `expression`.

## Properties

`assignmentOperatorCompound` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `enum assignKind` | Always `` `compound` ``; see assignKind |
| `targetExpression` | `expression` | The target of the assignment; typically, a variable receiving a new value, such as what C/C++ refers to as an *lvalue* |
| `sourceExpression` | `expression` | The expression which, when evaluated, is assigned to the target |
| `operator` | `enum` | The assignment operator: one of the many compound forms, such as `` `+=` `` or `` `*=` `` |

**Inherits properties from:**

- astnode
- expression

## Example

The `assignmentOperatorCompound` pattern can match source code
that uses the `+=` operator:

  
 [image: C/C++ code follows]   

```
int count = 0;

count += 1;
```

In this match, the property `.kind` is `` `compound` `` and
`.targetExpression` refers to `count`.
The `.sourceExpression` refers to the `intLiteral`
with the value of `1`, and `.operator` is `` `+` ``.

Combining these properties, we can construct the following pattern.
It detects compound addition assignments to a variable named `count`.
Pattern decomposition defines two constraints on the assignment operator's properties—that is,
both must be `true` for the overall pattern to match.

  
 [image: CXM code follows]   

```
    pattern compoundAdditionToCount {
        assignmentOperatorCompound {
            .operator == `+=`;
            .targetExpression == variableReference {
                .identifier == "count"
            };
        }
    };
```
