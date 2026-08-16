---
title: "propertyUpdate"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/propertyupdate.html"
content_id: "Rcu3EqXDm2Vu0FbyUBrf_w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:45.823442+00:00"
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
