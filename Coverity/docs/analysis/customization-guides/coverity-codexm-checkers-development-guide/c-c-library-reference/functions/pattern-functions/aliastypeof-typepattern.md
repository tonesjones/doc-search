---
title: "aliasTypeOf( typePattern )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/aliastypeof-typepattern-.html"
content_id: "vSDfztW2oZMEqGhcBCIFBw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:16.481863+00:00"
---

# aliasTypeOf( typePattern )

Returns a pattern that matches the type specified by `typePattern`.
The pattern will also match declarations that eventually resolve to `typePattern`.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `typePattern` | `pattern` | The type to match |
| ***return value*** | `pattern` | Pattern to match `type` and its aliases |

## Example

Given the following target-code snippet:

  
 [image: C/C++ code follows]   

```
typedef int intAlias;
typedef intAlias intAliasAlias;

intAliasAlias x = 10;
```

... the pattern returned by `aliasTypeOf(intType)`
will match `x`,
because the type `intAliasAlias` is an alias for `int`.

Here is a sample CodeXM pattern to perform this match:

  
 [image: CXM code follows]   

```
    node matches expression as e
        && e.type matches aliasTypeOf(intType);
```
