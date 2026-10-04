---
title: "tupleComprehension"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/tuplecomprehension.html"
content_id: "9aMAK8h046SzQpdK1BySrg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:51.205259+00:00"
---

# tupleComprehension

Matches tuple comprehensions.

Python comprehensions are represented by closures (lambda-expressions) and have function definitions of their own.

This pattern only matches nodes of type `expression`.

## Properties

`tupleComprehension` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `closure` | `expression` | The lambda expression that describes the comprehension |

**Inherits properties from:**

- astnode
- expression

## See also

listComprehension,
mapComprehension,
setComprehension
