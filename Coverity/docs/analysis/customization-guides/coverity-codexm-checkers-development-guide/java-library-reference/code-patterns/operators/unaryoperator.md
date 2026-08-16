---
title: "unaryOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/unaryoperator.html"
content_id: "vaQC8oA2vo_LyJdZHtyIjA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:24.517432+00:00"
---

# unaryOperator

Matches all possible unary operators in Java.

This pattern only matches nodes of type `expression`.

## Properties

`unaryOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `operandExpression` | `expression` | The expression the operation is performed on |
| `operator` | `enum` | The unary operator this pattern represents: One of `` `+` ``, `` `-` ``, `` `!` ``, or `` `~` `` |

**Inherits properties from:**

- astnode
- expression

## Example

The folowing CodeXM pattern matches any use of the unary plus operator:

  
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
