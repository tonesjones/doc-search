---
title: "propertyAccessBracket"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/propertyaccessbracket.html"
content_id: "EUXiumP5MChr6myx9wlEmg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:38.293045+00:00"
---

# propertyAccessBracket

Matches object property accesses that use array notation.

This pattern only matches nodes of type `expression`.

## Properties

`propertyAccessBracket` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `key` | `string` | The property accessed |
| `map` | `expression` | The object with the property |

**Inherits properties from:**

- astnode
- expression

## Example

Matches `obj[ "index" ]`.

## See also

propertyAccess
