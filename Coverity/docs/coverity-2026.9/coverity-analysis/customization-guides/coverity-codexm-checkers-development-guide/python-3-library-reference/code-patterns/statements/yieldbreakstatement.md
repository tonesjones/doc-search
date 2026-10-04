---
title: "yieldBreakStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/yieldbreakstatement.html"
content_id: "DXn9q_lUy1fb72AiGr_0sA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:50.024527+00:00"
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
