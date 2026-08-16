---
title: "unaryOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/unaryoperator.html"
content_id: "Zg_E7x6gwgpFBr_EP9RXcg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:01.104843+00:00"
---

# unaryOperator

Matches unary operators: those operators that have only one operand.

This pattern only matches nodes of type `expression`.

## Properties

`unaryOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The expression being operated upon |
| `operator` | `enum` | One of `` `**` ``, `` `-` ``, `` `+` ``, or `` `~` `` (tilde) |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches any use of the unary plus operator:

[image: CXM code follows]

```
    pattern unaryPlus {
        unaryOperator {
            .operator == `+`
        }
    };
```

## See also

binaryOperator
