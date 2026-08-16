---
title: "read_off_any"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/read_off_any.html"
content_id: "qwX8Ea8hFab~ldtv4tMaDA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:34.865352+00:00"
---

# read_off_any

**Languages: JavaScript**

A `read_off_any ReadableProgramData` value identifies a readable value
found along a given access path.

## Fields

A `read_off_any ReadableProgramData` object has the following
field:

`read_off_any`
:   A non-empty array of AccessPathElement values that
    specify paths where readable values can be found. Paths in
    `read_off_any` do not have to be relative to the
    global variable.

## Examples

For examples that use `read_off_any ReadableProgramData`, see dataflow_through_callsite,
to_callsite, from_callsite, and write_to_object_with_tag.
