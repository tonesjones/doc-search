---
title: "pointerTo( typePattern )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/pointerto-typepattern-.html"
content_id: "cXMZvEe8CYjO~sXxIQLwsA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:19.479309+00:00"
---

# pointerTo( typePattern )

Returns a pattern that matches a pointer to the type specified by `typePattern`.

The pattern returned will also match pointers to types that eventually resolve to `typePattern`.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `typePattern` | `pattern` | The type to match when it is pointed to |
| ***return value*** | `pattern` | Pattern to match a pointer to `type` |

## Example

Given the following target code snippet:

  
 [image: C++ code follows]   

```
typedef int intAlias;
intAlias *x = nullptr;
```

... the pattern returned by `pointerTo(intType)`
will match `x`,
because `x` points to the type `intAlias`,
and `intAlias` is an alias for `int`.

Here is a sample CodeXM pattern to perform this match:

  
 [image: CXM code follows]   

```
    node matches expression as e
        && e.type matches pointerTo(intType);
```
