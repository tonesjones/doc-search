---
title: "yieldBreakStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/yieldbreakstatement.html"
content_id: "DXn9q_lUy1fb72AiGr_0sA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:28.877971+00:00"
---

# yieldBreakStatement

Matches the end of yield-generators.

Note:
Python does not actually have a statement to mark the end of a `yield`, but
the Python library places a node in the abstract syntax tree to enable you to match this situation.

This pattern only matches nodes of type `statement`.

## Properties

`yieldBreakStatement` does not expose any new properties.

**Inherits properties from:**

- astnode
- statement
