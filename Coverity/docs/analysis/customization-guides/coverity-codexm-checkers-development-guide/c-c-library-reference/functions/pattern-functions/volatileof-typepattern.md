---
title: "volatileOf( typePattern )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/volatileof-typepattern-.html"
content_id: "WnKkZnABCiYVMr_EgU1NXw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:20.216928+00:00"
---

# volatileOf( typePattern )

Returns a pattern that matches a type (specified by `typePattern`),
provided the type is declared to be `volatile`.

The pattern returned will also match declarations that eventually resolve to `typePattern`.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `typePattern` | `pattern` | The type to match |
| ***return value*** | `pattern` | Pattern to match volatile instances of `type` |

## Example

Given the following target code snippet:

  
 [image: C/C++ code follows]   

```
typedef volatile int foo;
foo x = 10;
```

... the pattern returned by `volatileOf(intType)`
will match `x`,
because `x` is of type `foo`,
and `foo` is an alias for `volatile int`.

Here is a sample CodeXM pattern to perform this match:

  
 [image: CXM code follows]   

```
    node matches expression as e
        && e.type matches volatileOf( intType );
```
