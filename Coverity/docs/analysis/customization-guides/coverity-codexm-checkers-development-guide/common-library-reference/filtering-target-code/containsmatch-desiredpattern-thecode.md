---
title: "containsMatch( desiredPattern, theCode )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/containsmatch-desiredpattern-thecode-.html"
content_id: "E8ZaCSTF7WDIBwpDn31qBQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:13.999351+00:00"
---

# containsMatch( desiredPattern, theCode )

Returns `true` if any code within the `theCode` argument matches the pattern. Return `false` otherwise.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `desiredPattern` | `pattern(astnode) -> T` | The desired pattern |
| `theCode` | `astnode` | The code to be checked |
| ***return value*** | `bool` | Whether there was any matching code |

## Example

[image: CXM code follows]

```
function hasThrow( n: astnode ) ->
    containsMatch( throwOperator, n );
```

This `hasThrow()` function checks whether `n` contains a `throw`.

## See also

contains
