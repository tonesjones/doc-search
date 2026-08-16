---
title: "conditionalOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/conditionaloperator.html"
content_id: "jq62rLr33P6k4XeoIuJqTg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:48.628240+00:00"
---

# conditionalOperator

Matches the conditional operator (sometimes called the "ternary" operator) `?:`.

This pattern only matches nodes of type `expression`.

## Properties

`conditionalOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `conditionExpression` | `expression` | The condition: the expression before the question mark |
| `trueExpression` | `expression` | The expression to evaluate if the condition is `true`: the expression between the question mark and the colon |
| `falseExpression` | `expression` | The expression to evaluate if the condition is `false`: the expression after the colon |

**Inherits properties from:**

- astnode
- expression

## Example

The `conditionalOperator` matches the following source code:

  
 [image: C/C++ code follows]   

```
x > 0 ? x : -x;
```

In the preceding code, the property `.conditionExpression` is set to the condition `x > 0`.
The `x` and `-x` outcomes correspond to
the `trueExpression` and `falseExpression`, respectively.

The following CodeXM pattern matches any operator that uses a binary operator as its condition:

  
 [image: CXM code follows]   

```
    pattern binaryOpInCond {
        conditionalOperator {
            .conditionExpression == binaryOperator
        }
    };
```
