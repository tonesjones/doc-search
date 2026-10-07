---
title: "globalAccess"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/globalaccess.html"
content_id: "BPOPGqzPaGOPob0e2eQKxw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:46.552315+00:00"
---

# globalAccess

Matches implicit accesses of properties of the global object.

This pattern only matches nodes of type `expression`.

## Properties

`globalAccess` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `key` | `string` | The property accessed |

**Inherits properties from:**

- astnode
- expression

## See also

theGlobalObjectSymbol
