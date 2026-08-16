---
title: "contains( predicate, theCode )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/contains-predicate-thecode-.html"
content_id: "3eV9wjXi_bCmf~oGWozZAQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:13.352083+00:00"
---

# contains( predicate, theCode )

Returns `true` if any code within the `theCode` argument satisfies the predicate. Returns `false` otherwise.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `predicate` | `function(astnode) -> bool` | The predicate function |
| `theCode` | `astnode` | The code to be checked |
| ***return value*** | `bool` | Whether there was any corresponding code |

## Example

[image: CXM code follows]

```
function hasThrow( n: astnode ) ->
    contains( function( t: astnode ) ->
        t matches throwOperator, n
    );
```

This `hasThrow()` function checks whether `n` contains a
`throw`.

## See also

containsMatch
