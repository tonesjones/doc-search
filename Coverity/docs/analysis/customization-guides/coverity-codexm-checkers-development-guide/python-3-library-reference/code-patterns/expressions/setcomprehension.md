---
title: "setComprehension"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setcomprehension.html"
content_id: "SBr06kxY1gBMVJSFe_tHPQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:44.728772+00:00"
---

# setComprehension

Matches set comprehensions.

Python comprehensions are represented by closures (lambda-expressions) and have function definitions of their own.

This pattern only matches nodes of type `expression`.

## Properties

`setComprehension` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `closure` | `expression` | The lambda expression that describes the comprehension |

**Inherits properties from:**

- astnode
- expression

## See also

listComprehension,
mapComprehension,
tupleComprehension
