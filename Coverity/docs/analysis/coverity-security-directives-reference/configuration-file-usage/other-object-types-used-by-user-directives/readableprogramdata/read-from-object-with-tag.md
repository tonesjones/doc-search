---
title: "read_from_object_with_tag"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/read_from_object_with_tag.html"
content_id: "Rp3KA9MrRp4NRqqhRQtkeA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:33.580943+00:00"
---

# read_from_object_with_tag

**Languages: JavaScript**

A `read_from_object_with_tag ReadableProgramData` value identifies
readable values found along an access path relative to a value that has been tagged by a
`data_has_tag` directive. See data_has_tag.

## Fields

The `read_from_object_with_tag ReadableProgramData` object has the
following fields:

`read_from_object_with_tag`
:   A string value to identify values tagged by any data_has_tag directive that has the specified name.

`path`
:   A non-empty array of AccessPathElement values. This
    field specifies an access path to apply to the tagged values.

## Examples

```
{
    "read_from_object_with_tag" : "myTagName",
    "path" : [ { "property" : "f"}, { "property" : "g" } ]
},
```

The `read_from_object_with_tag`
`ReadableProgramData` value above with the following
`data_has_tag` will match the readable value at location
`exampleTaggedValue.f.g` because it tags the property
`exampleTaggedValue` with the tag `myTagName`.

```
{
    "data_has_tag" : { "read_off_any" : [ { "property" : "exampleTaggedValue" } ] },
    "tag" : "myTagName"
}
```
