---
title: "simpleStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/simplestatement.html"
content_id: "R3jRCcyAlz2pqYTk~s0Pzg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:12.202847+00:00"
---

# simpleStatement

Matches individual executable statements.

This pattern only matches nodes of type `statement`.

## Properties

`simpleStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression, such as a function call or an assignment |

**Inherits properties from:**

- astnode
- statement

## Example

The `simpleStatement` pattern matches the following case:

[image: JavaScript code follows]

```
    i++;
```

In this instance, the `.expression` property is the expression `i++`.
