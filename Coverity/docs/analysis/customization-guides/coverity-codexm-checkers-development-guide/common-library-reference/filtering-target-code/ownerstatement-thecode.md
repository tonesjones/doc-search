---
title: "ownerStatement( theCode )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ownerstatement-thecode-.html"
content_id: "LrDXZ_iF5crfTgUdHZa40w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:17.600484+00:00"
---

# ownerStatement( theCode )

Returns the innermost statement that contains the `theCode` argument.
If `theCode` is a statement, returns `theCode` itself.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `theCode` | `astnode` | The code from which the search starts |
| ***return value*** | `astnode?` | Returns `null` if there is no such statement. |

## Example

[image: C/C++ code follows]

```
if( x ) {          // "code1" is expression "x"
    x++;           // "code2" is statement "x++;"
};
```

In this case, `ownerStatement(code1)` returns the target-code `if` statement,
and `ownerStatement(code2)` returns the target `x++;` statement itself.

## See also

innermostOwner
