---
title: "allCodeIn( theCode )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/allcodein-thecode-.html"
content_id: "M3Ne8HBP0f419C8LdlxZ4A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:11.186598+00:00"
---

# allCodeIn( theCode )

Returns all code within the `theCode` argument.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `theCode` | `astnode` | The input code |
| ***return value*** | `set<astnode>` | A set whose elements are the code elements |

## Example

[image: C/C++ code follows]

```
    x + 1;          // "code" is this statement.
```

In this case, `allCodeIn(code)` returns a set of code that includes
the statement `x + 1;`, the expression `x + 1`,
the expression `x`, and the expression `1`.

## See also

contains
