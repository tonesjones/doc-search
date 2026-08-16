---
title: "filter( predicate, s )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/filter-predicate-s-.html"
content_id: "QYXsNfZFGRm07iNqzW6F9Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:14.660453+00:00"
---

# filter( predicate, s )

Returns a list of all the elements in the input set that satisfy the predicate.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `predicate` | `function(T) -> bool` | The predicate to be checked |
| `s` | `set<T>` | The set |
| ***return value*** | `list<T>` | A list that contains those elements in the input set that satisfy the predicate |

## Example

Executing the following function call:

[image: CXM code follows]

```
filter( function( x: int ) ->
    x == 1, [1, 2]
);
```

... results in the list `[1]`.
