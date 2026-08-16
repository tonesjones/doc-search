---
title: "data_has_tag"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/data_has_tag.html"
content_id: "VJbwmz4I1DJyvtbW25AKhg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:39.221079+00:00"
---

# data_has_tag

**Languages: JavaScript**

The `data_has_tag` directive assigns an arbitrary string-valued
`tag` to a specified piece of data; for example, to the return value
of a specific function or to a specific global variable. Other structures, such as read_from_object_with_tag
and write_to_object_with_tag, can refer to this
piece of data using this `tag` value. Tagging this data has no other
effect on the analysis: It simply enables the use of these other structures.

## Fields

This directive uses the following fields:

`data_has_tag`
:   Specifies a ReadableProgramData
    value that specifies the data to which to apply the tag.

`tag`
:   Sets a JSON string that specifies the tag.

## Examples

See write_to_object_with_tag for an
example.
