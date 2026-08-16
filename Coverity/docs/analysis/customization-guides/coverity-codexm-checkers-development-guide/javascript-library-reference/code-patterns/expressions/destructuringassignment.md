---
title: "destructuringAssignment"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/destructuringassignment.html"
content_id: "o0ln_ZBW0CJPShyXa4Inxg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:28.564457+00:00"
---

# destructuringAssignment

Matches full destructuring assignment expressions.

A destructuring assignment has the form `[a, b] = c`. The pattern yields `[a, b]` as `targetExpressions`, and `c` as `sourceExpression`.

This pattern only matches nodes of type `expression`.

## Properties

`destructuringAssignment` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `sourceExpression` | `expression` | The source expression |
| `targetExpressions` | `expression` | The target expression |

**Inherits properties from:**

- astnode
- expression

## See also

destructuringDeclaration
