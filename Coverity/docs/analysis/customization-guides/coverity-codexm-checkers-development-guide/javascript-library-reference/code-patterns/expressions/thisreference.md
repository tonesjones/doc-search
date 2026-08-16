---
title: "thisReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/thisreference.html"
content_id: "_zhT1soWlnyXo0D2A_NhzA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:40.361555+00:00"
---

# thisReference

Matches references to the implicit parameter `this`.

This pattern only matches nodes of type `expression`.

## Properties

`thisReference` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `variable` | `symbol` | The `this` symbol |

**Inherits properties from:**

- astnode
- expression
