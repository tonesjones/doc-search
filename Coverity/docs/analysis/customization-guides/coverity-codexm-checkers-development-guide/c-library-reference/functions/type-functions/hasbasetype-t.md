---
title: "hasBaseType( t )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/hasbasetype-t-.html"
content_id: "5PBOVG_MznCwOsrbVzGKKA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:37.173003+00:00"
---

# hasBaseType( t )

Returns the type that a `referenceType` points to, or the type of the elements in an array.

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `t` | `type` | The type to return the base type of |
| ***return value*** | `type` | The base type of the argument |

## Example

Using the function `hasBaseType()` on the target-code array `int[] a` gives you the result `integralType`.
