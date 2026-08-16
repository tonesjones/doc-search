---
title: "mapComprehension"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/mapcomprehension.html"
content_id: "9GNZmzI88AR9OmLjQ1875w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:44.073398+00:00"
---

# mapComprehension

Matches map comprehensions.

Python comprehensions are represented by closures (lambda-expressions) and have function definitions of their own.

This pattern only matches nodes of type `expression`.

## Properties

`mapComprehensionb` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `closure` | `expression` | The lambda expression that describes the comprehension |

**Inherits properties from:**

- astnode
- expression

## See also

listComprehension,
setComprehension,
tupleComprehension
