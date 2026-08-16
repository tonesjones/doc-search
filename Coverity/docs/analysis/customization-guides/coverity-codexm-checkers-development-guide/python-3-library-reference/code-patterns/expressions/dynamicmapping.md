---
title: "dynamicMapping"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/dynamicmapping.html"
content_id: "BR0EbSa6_nwgTmXjm_ycew"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:40.741986+00:00"
---

# dynamicMapping

Matches key/value mappings used in Python `map` and `set` data structures.

This pattern only matches nodes of type `expression`.

## Properties

`dynamicMapping` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `key` | `expression` | The key |
| `value` | `expression` | The value |

**Inherits properties from:**

- astnode
- expression

## See also

mapLiteral,
setLiteral
