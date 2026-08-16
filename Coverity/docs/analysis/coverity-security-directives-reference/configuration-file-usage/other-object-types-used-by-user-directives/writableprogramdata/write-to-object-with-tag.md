---
title: "write_to_object_with_tag"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/write_to_object_with_tag.html"
content_id: "YGgULRVuj9ekUihKx4aS~Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:43.710654+00:00"
---

# write_to_object_with_tag

A `write_to_object_with_tag WritableProgramData` value identifies writable
values found along an access path relative to a value that has been tagged by a data_has_tag directive.

## Fields

The `write_to_object_with_tag WritableProgramData` object has the
following fields:

`write_to_object_with_tag`
:   A string value that names values tagged by any data_has_tag directive.

`path`
:   A non-empty array of AccessPathElement values. This
    specifies an access path to apply to the tagged values.

## Examples

```
{
     "data_has_tag" : { "read_off_any" : [ { "property" : "exampleTaggedValue" } ] },
     "tag" : "myTagName"
},
{
     sink_for_checker : "DOM_XSS",
     sink : {
          "write_to_object_with_tag" : "myTagName",
          "path" : [ { "property" : "f"}, { "property" : "g" } ]
     },
}
```

The `data_has_tag` directive marks `property` accesses
off any object (including the global object) with `myTagName`. The
`write_to_object_with_tag`
`WritableProgramData` matches property *writes*, such as
`exampleTaggedValue.f.g = x`.
