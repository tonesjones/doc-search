---
title: "listComprehension"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/listcomprehension.html"
content_id: "u2jf96L1GTnSRqibjM8k_A"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:50.990338+00:00"
---

# listComprehension

Matches list comprehensions.

Python comprehensions are represented by closures (lambda-expressions) and have function definitions of their own.

This pattern only matches nodes of type `expression`.

## Properties

`listComprehension` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `closure` | `expression` | The lambda expression that describes the comprehension |

**Inherits properties from:**

- astnode
- expression

## See also

mapComprehension,
setComprehension,
tupleComprehension
