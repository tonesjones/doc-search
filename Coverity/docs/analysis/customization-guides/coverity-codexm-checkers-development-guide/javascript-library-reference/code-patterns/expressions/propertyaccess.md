---
title: "propertyAccess"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/propertyaccess.html"
content_id: "geWc3ieZ3HEie3Xtl6A2pQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:37.657134+00:00"
---

# propertyAccess

Matches accesses to an object property that are not implicit accesses to a property of the global object.

This pattern only matches nodes of type `expression`.

## Properties

`propertyAccess` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `key` | `string` | The property accessed |
| `map` | `expression` | The object with the property |
| `notation` | `enum` (see below) | The notation used in the access |

These are the possible values of the `notation` property:

| Name | Description |
| --- | --- |
| `` `bracket` `` | Array notation access as in `obj[ "index" ]` |
| `` `dot` `` | Dot notation access as in `obj.index` |

**Inherits properties from:**

- astnode
- expression

## Example

Matches `obj[ "index" ]` or `obj.index`,
where the property `.map` is `obj` and the
property `.key` is `"index"`.
