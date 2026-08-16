---
title: "floatLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/floatliteral.html"
content_id: "1RL~BG50_M4~UlvtZ9IEmA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:44.483751+00:00"
---

# floatLiteral

Matches numeric values represented in the source code as floating-point numbers.

All JavaScript numeric values are stored and processed as floats, but this pattern matches only those that
appear as floats (that is, have a decimal point) in the source code.

This pattern only matches nodes of type `expression`.

## Properties

`floatLiteral` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `valueString` | `string` | The floating-point value in string form |

**Inherits properties from:**

- astnode
- expression
