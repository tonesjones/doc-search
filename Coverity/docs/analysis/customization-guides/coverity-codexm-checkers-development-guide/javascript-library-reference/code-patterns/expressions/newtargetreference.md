---
title: "newTargetReference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/newtargetreference.html"
content_id: "HIYVDlCp3KA9yTTQAsg2gA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:34.867426+00:00"
---

# newTargetReference

Matches references to `new.target`.

This pattern only matches nodes of type `expression`.

## Properties

`newTargetReference` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `variable` | `symbol` | The `new.target` symbol |

**Inherits properties from:**

- astnode
- expression
