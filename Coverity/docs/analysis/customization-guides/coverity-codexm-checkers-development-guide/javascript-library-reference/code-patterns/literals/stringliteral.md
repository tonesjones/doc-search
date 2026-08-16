---
title: "stringLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/stringliteral.html"
content_id: "nDwb8R1d9c059KonuTr6zw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:47.936312+00:00"
---

# stringLiteral

Matches string literals.

This pattern is independent of the type of quotation mark used (either single or double).

This pattern also matches individual string portions of template literals.

This pattern only matches nodes of type `expression`.

## Properties

`stringLiteral` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `value` | `string` | The contents of the string |

**Inherits properties from:**

- astnode
- expression
