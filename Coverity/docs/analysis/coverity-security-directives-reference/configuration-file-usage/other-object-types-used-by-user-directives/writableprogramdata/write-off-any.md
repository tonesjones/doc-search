---
title: "write_off_any"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/write_off_any.html"
content_id: "elqxatJ2jlRm3i~glxzzzQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:45.010963+00:00"
---

# write_off_any

**Languages: JavaScript**

A `write_off_any WritableProgramData` value identifies a writable value
found along a given access path.

## Fields

The `write_off_any WritableProgramData` object has the following
field:

`write_off_any`
:   A non-empty array of AccessPathElement values, specifying
    a path that is not necessarily based off of the global variable.

## Examples

See async_method for an example of the use of
`write_off_any WritableProgramData`.
