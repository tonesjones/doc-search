---
title: "emptyStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/emptystatement.html"
content_id: "dgbxcCX8CRxh3X94u6mEJA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:05.219680+00:00"
---

# emptyStatement

Matches empty, placeholder statements.

This pattern only matches nodes of type `statement`.

## Properties

`emptyStatement` does not expose any new properties.

**Inherits properties from:**

- astnode
- statement

## Example

The `emptyStatement` pattern matches each of the two lines that follow:

[image: JavaScript code follows]

```
    ;
    ;
```
