---
title: "write_path_off_global"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/write_path_off_global.html"
content_id: "GbM7LHxRIDc5TFsoA8f40A"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:02.228456+00:00"
---

# write_path_off_global

**Languages: JavaScript**

A `write_path_off_global WritableProgramData` value identifies a writable
value found along a given access path off of the global variable.

## Fields

The `write_path_off_global WritableProgramData` object has the
following field:

`write_path_off_global`
:   A non-empty array of AccessPathElement values, specifying
    the path off the global variable.

## Examples

See sink_for_checker for an example of the use
of `write_path_off_global WritableProgramData`.
