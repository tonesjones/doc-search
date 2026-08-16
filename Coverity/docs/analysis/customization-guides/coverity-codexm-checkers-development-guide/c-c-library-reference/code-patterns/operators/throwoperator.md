---
title: "throwOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/throwoperator.html"
content_id: "Gm6che3t6Icv8zbj~qnpEg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:53.119107+00:00"
---

# throwOperator

Matches the C++ `throw` operation.

## Properties

`throwOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `operandexpression` | `expression?` | The expression to be thrown by this operator; `null` if an object is not specified |

**Inherits properties from:**

- astnode
- expression

## Example

The `throwOperator` pattern matches both of the following lines of target source:

  
 [image: C/C++ code follows]   

```
    throw e;
    throw;
```

In the former case, `.operandExpression` refers to `e`;
in the latter case, `.operandExpression` is `null`.

As part of memory ownership assignment, some development environments always require pointers to be thrown,
while others never do.
A CodeXM checker that enforces either of these conventions might use the following pattern:

  
 [image: CXM code follows]   

```
    pattern throwNewObject {
        throwOperator {
            .operandExpression == newOperator
        }
    };
```

Conversely, to find instances where `throw` doesn't use
`new`, the following CodeXM pattern would be useful:

  
 [image: CXM code follows]   

```
    pattern throwNonNewObject {
        throwOperator {
            .operandExpression != newOperator
        }
    };
```
