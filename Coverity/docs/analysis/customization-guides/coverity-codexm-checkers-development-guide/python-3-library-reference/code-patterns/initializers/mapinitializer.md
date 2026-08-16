---
title: "mapInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/mapinitializer.html"
content_id: "cy_qhSjZTn9YbQRcT4JCbA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:03.706246+00:00"
---

# mapInitializer

Matches map initializations (key/value mappings).

CAUTION:

This pattern does not appear in pattern decomposition:
Use assignmentStatement instead.
For more about decomposition, see Decomposing a pattern to match specific properties.

This pattern only matches nodes of type `initializer`.

## Properties

`mapInitializer` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression used to initialize the map |

**Inherits properties from:**

- astnode
- initializer
