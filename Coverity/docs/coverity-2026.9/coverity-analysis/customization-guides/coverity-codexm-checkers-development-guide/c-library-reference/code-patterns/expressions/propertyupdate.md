---
title: "propertyUpdate"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/propertyupdate.html"
content_id: "Rcu3EqXDm2Vu0FbyUBrf_w"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:28.285305+00:00"
---

# propertyUpdate

Matches all property updates.

This pattern only matches nodes of type `expression`.

## Properties

`propertyUpdate` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `setterCall` | `functionSymbol` | The setter to be called |

**Inherits properties from:**

- astnode
- expression
