---
title: "aggregateInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/aggregateinitializer.html"
content_id: "qEwS9RexlDLUGGAd8ooVhA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:02.411621+00:00"
---

# aggregateInitializer

Matches aggregate initializers for lists or expression.

CAUTION:

This pattern does not appear in pattern decomposition:
Use assignmentStatement instead.
For more about decomposition, see Decomposing a pattern to match specific properties.

This pattern only matches nodes of type `initializer`.

## Properties

`aggregateInitializer` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression that initializes the list or expression |

**Inherits properties from:**

- astnode
- initializer
