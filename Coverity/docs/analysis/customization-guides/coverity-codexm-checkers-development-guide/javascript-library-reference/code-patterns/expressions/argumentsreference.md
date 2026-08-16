---
title: "argumentsReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/argumentsreference.html"
content_id: "_KDlbBpfTYJUBXE_gIHc8g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:25.035660+00:00"
---

# argumentsReference

Matches references to the implicitly declared `arguments` variable.

This pattern only matches nodes of type `expression`.

## Properties

`argumentsReference` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `variable` | `symbol` | The `arguments` symbol |

**Inherits properties from:**

- astnode
- expression
