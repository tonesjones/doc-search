---
title: "AccessPathElement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/accesspathelement.html"
content_id: "oAg2DWiUdMpvXLnel0Tbfg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:07.646425+00:00"
---

# AccessPathElement

**Used by these objects:**
`InputAndAccessPathSpecifier`,
`OutputAndAccessPathSpecifier`, `ReadableProgramData`,
`WritableProgramData`

An access path from a base value to another value is represented as a non-empty array of
`AccessPathElement` values. One `AccessPathElement`
describes a single step in the access path.

## Fields

This object uses a single field:

`property`
:   A JSON string value that names a property of the object at this point in
    the access path.

## Example

The following array of `AccessPathElement` values, if applied to the
object `baseObj`, would represent the value
`baseObj.x.y.z`.

```
[ { "property" : "x" }, { "property" : "y" }, { "property" : "z" }]
```
