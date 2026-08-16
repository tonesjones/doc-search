---
title: "sendStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sendstatement.html"
content_id: "rKfm8uygvuMrqD9581oHpQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:19.570951+00:00"
---

# sendStatement

Matches `send` statements.

This pattern only matches nodes of type `statement`.

## Properties

`sendStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `lhsExpression` | `expression` | The left-hand side of the Send expression. |
| `rhsExpression` | `expression` | The right-hand side of the Send expression. |

**Inherits properties from:**

- astnode
- statement
