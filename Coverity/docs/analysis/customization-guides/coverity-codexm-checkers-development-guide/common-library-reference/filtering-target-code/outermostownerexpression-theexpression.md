---
title: "outermostOwnerExpression( theExpression )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/outermostownerexpression-theexpression-.html"
content_id: "wHhBqyp_q4xUTg_IUkAwOg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:16.871205+00:00"
---

# outermostOwnerExpression( theExpression )

Returns the outermost expression that owns the `theExpression` argument.
If the `theExpression` argument is already the outermost expression, returns `theExpression` itself.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `theExpression` | `expression` | The expression from which the search starts |
| ***return value*** | `expression` | The outermost owner expression |

## Example

[image: C/C++ code follows]

```
if( x + y == 10 ) {      // "expr1" is the expression "x"
    x++;                 // "expr2" is the expression "x++""
};
```

In this case, `outermostOwnerExpression(expr1)` returns the target-code binary expression
`x + y == 10`, and `outermostOwnerExpression(expr2)` returns the target post-increment
expression `x++` itself.

## See also

outermostOwner
