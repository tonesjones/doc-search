---
title: "unique( equal, s )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/unique-equal-s-.html"
content_id: "H32nMWQu_9sT51YUu85qvg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:19.576544+00:00"
---

# unique( equal, s )

Removes duplicates from a multi-set, based on a specified comparator.
In other words, returns a list that contains all elements in the input set, but no duplicates.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `equal` | `function(T, T)->bool` | The comparator |
| `s` | `set<T>` | The set to remove duplicates from |
| ***return value*** | `list<T>` | The list with all elements in the set, but no duplicates |

## Example

Executing the following function call:

[image: CXM code follows]

```
unique( function( x: int, y: int ) ->
    x == y, [1, 1, 2]
);
```

... results in the list `[1,2]`.
