---
title: "anyQualifiedTypeOf( typePattern )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/anyqualifiedtypeof-typepattern-.html"
content_id: "GEztsl5YCAZ06k0V9d_B9Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:17.229041+00:00"
---

# anyQualifiedTypeOf( typePattern )

Returns a pattern that matches a type (specified by `typePattern`) provided the type is qualified by
`const`, `restrict` (C++), or `volatile`.

The pattern returned will also match qualified declarations that eventually resolve to `typePattern`.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `typePattern` | `pattern` | The type to match |
| ***return value*** | `pattern` | Pattern to match `type` when it is qualified |

## Example

Given the following C/C++ target code:

  
 [image: C/C++ code follows]   

```
const int a = 5;        // (1)
const int *b = NULL;    // (2)
```

... the pattern that
`anyQualifiedTypeOf(intType)`
returns will match line (1),
because this line declares an integer qualified by `const`.
The pattern will *not* match line (2),
because this line declares a pointer, not an integer.

Here is a sample CodeXM pattern to perform this match:

  
 [image: CXM code follows]   

```
    node matches expression as e
        && e.type matches anyQualifiedTypeOf(intType);
```
