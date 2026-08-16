---
title: "memberInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/memberinitializer.html"
content_id: "szSpVD6jUxNhEc6X6ps6EA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:29.561952+00:00"
---

# memberInitializer

Matches locations where a member is being initialized as part of a call to a constructor.

## Properties

`memberInitializer` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `field` | `symbol` | The `fieldSymbol` of the member being initialized |

**Inherits properties from:**

- astnode
- initializer
