---
title: "functionReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/functionreference.html"
content_id: "vgf8ERRsLKxGn2MNv4fu6w"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:50.894363+00:00"
---

# functionReference

Matches references to function definitions.

This pattern only matches nodes of type `expression`.

## Properties

`functionReference` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `functionSymbol` | `symbol` | The symbol of the referenced function |

**Inherits properties from:**

- astnode
- expression
