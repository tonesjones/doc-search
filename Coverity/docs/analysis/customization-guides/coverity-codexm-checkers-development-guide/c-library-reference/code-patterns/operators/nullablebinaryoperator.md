---
title: "nullableBinaryOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/nullablebinaryoperator.html"
content_id: "~~nLWgyl59QBC~v4qml_vg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:11.753594+00:00"
---

# nullableBinaryOperator

Matches all possible C# binary operations with nullable values (all of these are comparisons).

This pattern only matches nodes of type `expression`.

## Properties

`nullableBinaryOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isImplicit` | `bool` | `true` if the operator is implicit |
| `lhsExpression` | `expression` | The expression on the left-hand side of the operator |
| `operator` | `enum` | The operator this pattern represents: one of `` `==` ``, `` `!=` ``, `` `&` ``, `` `^` ``, or `` `|` `` |
| `rhsExpression` | `expression` | The expression on the right-hand side of the operator |

**Inherits properties from:**

- astnode
- expression

## Example

The following CodeXM pattern matches only a comparison for equality:

  
 [image: CXM code follows]   

```
    pattern nullableEqaulityCheck {
        nullableBinaryOperator {
            .operator == `==`
        }
    };
```

## See also

binaryOperator
