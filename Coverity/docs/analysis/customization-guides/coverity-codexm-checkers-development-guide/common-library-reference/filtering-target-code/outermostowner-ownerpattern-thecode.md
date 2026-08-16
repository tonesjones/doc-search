---
title: "outermostOwner( ownerPattern, theCode )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/outermostowner-ownerpattern-thecode-.html"
content_id: "mtf0Yx5ijGvId_msuuOj2g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:16.134522+00:00"
---

# outermostOwner( ownerPattern, theCode )

Returns the outermost code that owns the `theCode` argument that matches the pattern.
If the theCode argument matches the pattern, returns `theCode` itself.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `ownerPattern` | `pattern(astnode) -> T` | The pattern |
| `theCode` | `astnode` | The code from which the search starts |
| ***return value*** | `astnode?` | Returns `null` if there is no such owner. |

## Example

[image: C/C++ code follows]

```
if( x + y == 10 ) {      // "code1" is the expression "x"
    x++;                 // "code2" is the expression "x++"
};
```

In this case, `outermostOwner(expression, code1)` returns the target code's binary expression
`x + y == 10`, and `outermostOwner(expression, code2)` returns the
target expression `x++` itself.

## See also

innermostOwner,
outermostOwnerExpression
