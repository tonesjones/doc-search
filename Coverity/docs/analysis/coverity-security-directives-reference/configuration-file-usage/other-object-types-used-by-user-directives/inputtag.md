---
title: "InputTag"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/inputtag.html"
content_id: "Q5CN3hxlyeJSy0DN0fwJwQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:21.267947+00:00"
---

# InputTag

**Used by these directives:**
`async_method`, `local_callback`

An `InputTag` value assigns an arbitrary string-valued
`tag` to a specific parameter to a callback. Other structures, such
as read_from_object_with_tag and write_to_object_with_tag, can refer to these
parameters using this `tag` value. Tagging a callback parameter has no
other effect on the analysis; it simply enables the use of these other structures.

## Fields

This object uses the following fields:

`tag`
:   A JSON string that names the tag. Use this string to identify the tag in
    other directives.

`input`
:   A ParamIn value that indicates the parameter
    of the callback to which to assign the tag.
