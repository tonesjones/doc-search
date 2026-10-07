---
title: "booleanLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/booleanliteral.html"
content_id: "OLl5cxD35w2Pyp9DuSZWhQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:47.248606+00:00"
---

# booleanLiteral

Matches Boolean literals: that is, either `true` or `false`.

This pattern only matches nodes of type `expression`.

## Properties

`booleanLiteral` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `value` | `bool` | Either `true` or `false` |

**Inherits properties from:**

- astnode
- expression
