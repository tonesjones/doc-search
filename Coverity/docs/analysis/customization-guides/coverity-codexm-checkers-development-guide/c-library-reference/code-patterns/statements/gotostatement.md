---
title: "gotoStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/gotostatement.html"
content_id: "7YZklm2R8YFUVx_JM6cYEA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:58.901522+00:00"
---

# gotoStatement

Matches `goto` statements.

This pattern only matches nodes of type `statement`.

## Properties

`goToStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `labelStatement` | `statement` | The statement to go to |

**Inherits properties from:**

- astnode
- statement
