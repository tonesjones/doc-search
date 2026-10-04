---
title: "memberInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/memberinitializer.html"
content_id: "HIEzguFyJmdQNV467Em~fQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:30.543815+00:00"
---

# memberInitializer

Matches locations where a member is being initialized as part of a call to a constructor.

This pattern only matches nodes of type constructorInitializer.

## Properties

`memberInitializer` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `field` | `symbol` | The `fieldSymbol` of the member being initialized |

**Inherits properties from:**

- astnode
- initializer
