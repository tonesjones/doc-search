---
title: "expressionInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/expressioninitializer.html"
content_id: "~KtVRt9Py2z1pvZylbtvUg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:03.057887+00:00"
---

# expressionInitializer

Matches expressions used as initializers.

CAUTION:

This pattern does not appear in pattern decomposition:
Use assignmentStatement instead.
For more about decomposition, see Decomposing a pattern to match specific properties.

This pattern only matches nodes of type `initializer`.

## Properties

`expressionInitializer` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression used to initialize an object |

**Inherits properties from:**

- astnode
- initializer
