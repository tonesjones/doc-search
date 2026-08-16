---
title: "getFunctionOverridees( f )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/getfunctionoverridees-f-.html"
content_id: "Km6UPJAT8fz9rbIOs~DKaw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:50.216760+00:00"
---

# getFunctionOverridees( f )

Returns all the overridees of a given `functionSymbol`.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `f` | `functionSymbol` | The `functionSymbol` to get the overridees of |
| ***return value*** | `set<functionSymbol>` | The overridees of the argument, as a set |

## Example

The following CodeXM function determines if a function overrides a function named `example()`:

  
 [image: CXM code follows]   

```
    function overridesExample( f : typeof(functionSymbol).producedType ) : bool ->
        let overridees = getFunctionOverridees(f) in
            for a in overridees accumulate b : bool = false :
                a matches functionSymbol { .simpleName == "example" } || b;
```
