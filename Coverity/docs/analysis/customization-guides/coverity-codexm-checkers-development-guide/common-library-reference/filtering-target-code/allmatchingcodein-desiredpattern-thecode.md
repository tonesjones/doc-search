---
title: "allMatchingCodeIn( desiredPattern, theCode )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/allmatchingcodein-desiredpattern-thecode-.html"
content_id: "bj9Ps7ZnlbKTVAaZaLtncw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:11.919010+00:00"
---

# allMatchingCodeIn( desiredPattern, theCode )

Finds all the code within the `theCode` argument that matches the desired pattern.
Returns a list of values produced by the pattern matches.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `desiredPattern` | `pattern(astnode) -> T` | The predicate pattern |
| `theCode` | `astnode` | The input code |
| ***return value*** | `list<T>` | A list of values produced by the pattern matches |

## Example

[image: C++ code follows]

```
if ( x ) {       // "code" is the if statement.
    throw 1;
} else {
    throw 2;
};
```

In this case, `allMatchingCodeIn(pattern { throwOperator as t -> t.operandExpression }, code)`
returns a list that contains the target expressions `1` and `2`.

## See also

anyMatchingCodeIn
