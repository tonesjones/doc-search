---
title: "usingType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/usingtype.html"
content_id: "jU08PrFyI36i4SN2OiOC3w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:25.772089+00:00"
---

# usingType

Matches types that have been defined with the `using` keyword.

This pattern only matches nodes of type `type`.

## Properties

`usingType` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `alias` | `string` | The (mangled) name of the type being defined |
| `id` | `symbol` | The identifier of the type being defined |
| `targetType` | `type` | The type being associated with the name |
