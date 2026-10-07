---
title: "locallyDeclaredTypeStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/locallydeclaredtypestatement.html"
content_id: "u7kutAGlYhGZB6wLkC2WNg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:34.170976+00:00"
---

# locallyDeclaredTypeStatement

Matches statements that use a locally declared type.

This pattern only matches nodes of type `statement`.

## Properties

`locallyDeclaredTypeStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `declaredClass` | `expression` | The expression, such as a function call or an assignment. |

**Inherits properties from:**

- astnode
- statement
