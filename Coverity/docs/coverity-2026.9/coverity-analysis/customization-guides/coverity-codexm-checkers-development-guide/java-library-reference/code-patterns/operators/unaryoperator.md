---
title: "unaryOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/unaryoperator.html"
content_id: "vaQC8oA2vo_LyJdZHtyIjA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:42.258417+00:00"
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
