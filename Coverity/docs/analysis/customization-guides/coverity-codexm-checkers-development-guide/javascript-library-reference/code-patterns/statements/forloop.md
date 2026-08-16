---
title: "forLoop"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/forloop.html"
content_id: "YN082dTupZlwWPTL11ehwQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:05.873014+00:00"
---

# forLoop

Matches any of the `for` loop constructs.

## Properties

`forLoop` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The statement that the loop repeatedly executes. Frequently, this is a blockStatement. |
| `kind` | `enum` | The kind of `for` loop: `` `in` ``, `` `of` ``, or `` `simple` `` |

**Inherits properties from:**

- astnode
- statement

## See also

forLoopIn,
forLoopOf,
forLoopSimple
