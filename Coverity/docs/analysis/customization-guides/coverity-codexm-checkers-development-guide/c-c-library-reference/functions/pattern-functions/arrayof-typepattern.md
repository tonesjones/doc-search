---
title: "arrayOf( typePattern )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/arrayof-typepattern-.html"
content_id: "FmjMCui8ZtYGZnH4zWQg2Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:17.987706+00:00"
---

# arrayOf( typePattern )

Returns a pattern that matches an array of the type specified by `typePattern`.

The pattern returned will also match arrays of types that eventually resolve to `typePattern`.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `typePattern` | `pattern` | The type to match |
| ***return value*** | `pattern` | Pattern to match an array of `type` |

## Example

Given the following target code snippet:

  
 [image: C/C++ code follows]   

```
typedef int intAlias;

intAlias x[10];
x[0] = 1;
```

... the pattern returned by `arrayOf(intType)`
will match `x`,
because `x` is an array of elements of type `intAlias`,
and `intAlias` is in turn an alias for `int`.

Here is a sample CodeXM pattern to perform this match:

  
 [image: CXM code follows]   

```
    node matches expression as e
        && e.type matches arrayOf(intType);
```
