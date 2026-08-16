---
title: "integerLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/integerliteral.html"
content_id: "ohfEXs3LRZ3sRvgkIxmgHg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:45.127566+00:00"
---

# integerLiteral

Matches numeric values represented in the source code as integers.

All JavaScript numeric values are stored and processed as floats, but this pattern matches only those that appear as integers
(that is, have no decimal point) in the source code.

This pattern only matches nodes of type `expression`.

## Properties

`integerLiteral` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `value` | `int` | The integer value |

**Inherits properties from:**

- astnode
- expression
