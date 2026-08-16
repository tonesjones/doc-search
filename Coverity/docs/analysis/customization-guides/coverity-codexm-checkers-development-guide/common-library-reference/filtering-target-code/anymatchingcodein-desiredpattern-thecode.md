---
title: "anyMatchingCodeIn( desiredPattern, theCode )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/anymatchingcodein-desiredpattern-thecode-.html"
content_id: "lbii3FzMoD4WtOvYmfRc~w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:12.624266+00:00"
---

# anyMatchingCodeIn( desiredPattern, theCode )

If any code within the `theCode` argument matches the desired pattern, returns the value produced by the pattern match.
Otherwise, returns `null`. If there are multiple matches, returns a single, arbitrary match.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `desiredPattern` | `pattern(astnode) -> T` | The desired pattern |
| `theCode` | `astnode` | The code to be checked |
| ***return value*** | `T?` | Returns `null` if there is no code within the input that matches the desired pattern. |

## Example

[image: C++ code follows]

```
if ( x ) {       // "code" is the if statement.
    throw 1;
} else {
    throw 2;
};
```

In this case, `anyMatchingCodeIn(pattern { throwOperator as t -> t.operandExpression }, code)`
returns the target-language expression `1` or `2`.

## See also

allMatchingCodeIn
