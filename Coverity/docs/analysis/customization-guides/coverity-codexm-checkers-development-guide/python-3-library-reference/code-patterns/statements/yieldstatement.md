---
title: "yieldStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/yieldstatement.html"
content_id: "VsFJ7BzHA0~r8XKwATks4Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:29.538339+00:00"
---

# yieldStatement

Matches `yield` statements.

This pattern only matches nodes of type `statement`.

## Properties

`yieldStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression being yielded |

**Inherits properties from:**

- astnode
- statement

## Example

The following CodeXM pattern matches statements that yield an integer:

[image: CXM code follows]

```
    pattern yieldInteger {
        yieldStatement {
            .expression == integerLiteral
        }
    };
```
