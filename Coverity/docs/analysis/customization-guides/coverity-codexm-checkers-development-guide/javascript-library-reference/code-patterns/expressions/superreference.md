---
title: "superReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/superreference.html"
content_id: "cxt6ZLqwtSVE69b~ewjlXg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:39.687027+00:00"
---

# superReference

Matches references to `super`.

This pattern only matches nodes of type `expression`.

## Properties

`superReference` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `variable` | `symbol` | The `super` symbol |

**Inherits properties from:**

- astnode
- expression
