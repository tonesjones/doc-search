---
title: "referenceDereference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/referencedereference.html"
content_id: "i4fDHmJr_dCWMXI0uJdJew"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:40.053443+00:00"
---

# referenceDereference

Matches locations where a reference-type expression has been dereferenced.

This pattern only matches nodes of type `expression`.

## Properties

`referenceDereference` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `referencedExpression` | `expression` | The expression being dereferenced |

**Inherits properties from:**

- astnode
- expression

## See also

referenceType
