---
title: "innermostOwner( ownerPattern, theCode )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/innermostowner-ownerpattern-thecode-.html"
content_id: "c191RVmtajbcXQI_0~tvPw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:15.402150+00:00"
---

# innermostOwner( ownerPattern, theCode )

Returns the innermost code that owns the `theCode` argument that matches the pattern.
If the `theCode` argument matches the pattern, returns `theCode` itself.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `ownerPattern` | `pattern(astmonode) -> T` | The pattern that matches the owner |
| `theCode` | `astnode` | The code from which the search starts |
| ***return value*** | `astnode?` | Returns `null` if there is no such owner. |

## Example

[image: C/C++ code follows]

```
while( 1 ) {
    if( x ) {        // "code1" is the expression "x"
        x++;         // "code2" is the statement "x++;"
    }
}
```

In this case, `innermostOwner(statement, code1)` returns the target code's `if` statement,
and `innermostOwner(statement, code2)` returns the target `x++;` statement itself.

## See also

outermostOwner
