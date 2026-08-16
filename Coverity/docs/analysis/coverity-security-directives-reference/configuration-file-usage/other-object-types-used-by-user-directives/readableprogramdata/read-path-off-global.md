---
title: "read_path_off_global"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/read_path_off_global.html"
content_id: "0_L3DpL91azw2~8RkPwKag"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:34.226403+00:00"
---

# read_path_off_global

**Languages: JavaScript**

A `read_path_off_global ReadableProgramData` value identifies a readable
value that is found along a given access path off of the global variable.

## Fields

The `read_path_off_global ReadableProgramData` object has the
following field:

`read_path_off_global`
:   A non-empty array of AccessPathElement values that specify paths where
    readable values can be found.

## Examples

For examples that use `read_path_off_global ReadableProgramData`, see
tainted_data, async_method, local_callback, and map_write.
