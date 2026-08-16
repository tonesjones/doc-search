---
title: "unaryOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/unaryoperator.html"
content_id: "UX3DDUC0QAPfmnpSmxHoAQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:53.880188+00:00"
---

# unaryOperator

Matches unary operators—those operators that have only one operand.

This pattern only matches nodes of type `expression`.

## Properties

`unaryOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `operator` | `enum` | Can be one of: `` `+` ``, `` `-` ``, `` `!` ``, or `` `~` ``. |
| `operandExpression` | `expression` | The expression being operated on |

**Inherits properties from:**

- astnode
- expression

## Example

The `unaryOperator` pattern matches source code such as this:

  
 [image: C/C++ code follows]   

```
n = -m;
isTrue = !false;
```

In the first instance, the `.operator` property is `` `-` ``
and in the second, the `.operator` is `` `!` ``.
