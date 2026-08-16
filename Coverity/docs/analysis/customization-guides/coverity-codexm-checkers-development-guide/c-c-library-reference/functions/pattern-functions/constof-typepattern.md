---
title: "constOf( typePattern )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/constof-typepattern-.html"
content_id: "5G2JLGWBS3dYowTtntpi_Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:18.736987+00:00"
---

# constOf( typePattern )

Returns a pattern that matches a type (specified by `typePattern)`,
provided the type is declared to be `const`.

The pattern returned will also match declarations that eventually resolve to `typePattern`.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `typePattern` | `pattern` | The type to match |
| ***return value*** | `pattern` | Pattern to match constants of `type` |

## Example

Given the following target code snippet:

  
 [image: C/C++ code follows]   

```
typedef const int intAlias;
intAlias x = 10;
```

... the pattern returned by `constOf(intType)`
will match `x`,
because `x` is of type `intAlias`,
and `intAlias` is an alias for `const int`.

Here is a sample CodeXM pattern to perform this match:

  
 [image: CXM code follows]   

```
    node matches expression as e
        && e.type matches constOf( intType );
```
